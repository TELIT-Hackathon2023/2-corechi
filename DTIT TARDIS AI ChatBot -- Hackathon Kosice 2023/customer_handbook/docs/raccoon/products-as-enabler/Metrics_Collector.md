# Metrics Collector

Below you find some information about the metrics collector we use in T‧AR‧D‧I‧S and is as well usable by every team outside of T‧AR‧D‧I‧S 

The [VMAgent](https://docs.victoriametrics.com/vmagent.html) works similar to Prometheus at the topic collecting metrics.
The VMAgent actively and iteratively pulls metrics from configured endpoints and sends them to configured remote destinations.

The Scrape-Config-Generator (SCG) is used to manage the scrape configurations of VMAgent. 
With watching serviceMonitors the SCG keeps the configurations up-to-date.  

## Helm Chart

You´ll find our helm chart [here](https://gitlab.devops.telekom.de/dhei/teams/skoll/dev/charts/raccoon/victoria-metrics-agent).

Or just run these commands:
```
helm repo add --username PUBLIC_CHART_PACKAGE_REGISTRY_READ_DEPLOY_TOKEN --password ***** tardis-skoll-public https://gitlab.devops.telekom.de/api/v4/projects/196065/packages/helm/stable
helm repo update
```

Now you´re able to install and customize packages from our public helm repository
```
helm install tardis-skoll-public/victoria-metrics-agent -f my-additional-values.yaml 
```

### Deploy outside T‧AR‧D‧I‧S

It´s necessary to be able to pull the used images from the Magenta-Trusted-Registry. 
That´s why it´s necessary to set/change the following configurations.

#### Provide credentials for pulling the image
To pull from the 'tardis-customer' organization in the MTR create a secret and use the DOCKER_AUTH_CONFIG / pull-secret like for [Rover](../../rover/README.md#pull-rover-docker-image).
```
kubectl create secret docker-registry mtr-tardis-customer --docker-server=${MTR_MCICD_HOST} --docker-username=$MTR_PULL_USER --docker-password=$MTR_PULL_PASSWORD --namespace=$MY_NAMESPACE
```

Bind the secret in the helm chart at the global section:
```yaml
global:
  imageRegistryOrganisation: "tardis-customer"
  imagePullSecrets:
    - mtr-tardis-customer
```
 
### Deploy on restricted kubernetes clusters

Restricted Kubernetes clusters like from CaaS prevent deploying ClusterRoles to for example watching serviceMonitors.

VMAgent and SCG are able to run in namespaced mode. For this add these configurations (set your own namespaces in the namespaces array):
```yaml
kubeApiServer: # disable scraping from kubernetes api server because it isn´t reachable 
  enabled: false
rbac:
  pspEnabled: false

namespaces:
  - my-namespace-1
  - my-namespace-2

scrapeConfigGenerator:
  kubeletService:
    enabled: false # disable service because host apis aren´t reachable
```


### Scrape Configuration

In the scrape configuration are all jobs for endpoints to collect metrics from.
VMAgent requests the kubernetes api for details of services and filters based on configured relabeling configurations in each job for relevant endpoints.

Example configuration:

```yaml
global:
  scrape_interval: 30s
  scrape_timeout: 30s
  external_labels:
    platform: aws
    prometheus: skoll/guardians-raccoon
scrape_configs:
  - job_name: scraped-by-service-annotation
    follow_redirects: null
    relabel_configs:
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scrape]
        regex: "true"
        action: keep
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scheme]
        target_label: __scheme__
        regex: (https?)
        action: replace
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_path]
        target_label: __metrics_path__
        regex: (.+)
        action: replace
      - source_labels: [__address__, __meta_kubernetes_service_annotation_prometheus_io_port]
        target_label: __address__
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
        action: replace
      - source_labels: [__meta_kubernetes_namespace]
        target_label: namespace
        action: replace
      - source_labels: [__meta_kubernetes_service_name]
        target_label: service
        action: replace
      - source_labels: [__meta_kubernetes_pod_name]
        target_label: pod
      - source_labels: [__meta_kubernetes_pod_container_name]
        target_label: container
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_port]
        target_label: endpoint
      - action: labelmap
        regex: __meta_kubernetes_service_label_(tardis_telekom_de_.+)
    kubernetes_sd_configs:
      - role: endpoints
        namespaces:
          names: [] # set your namespaces here to run in namespaced mode
```

In the example above there is a static scrape job to scrape metrics from every service which has specific annotations configured like in this service:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: sample-service
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/path: /metrics
    prometheus.io/port: "8080"
spec:
  selector:
    app: sample
  ports:
    - protocol: TCP
      name: http
      port: 80
      targetPort: 8080
```

With the annotation 'prometheus.io/scrape: true' you activate the scraping from the configured path and port from the key `prometheus.io/path` and `prometheus.io/port`.

### Send collected metrics to an endpoint

The VMAgent supports sending metrics to multiple endpoints differently secured and is able to filter before sending.

Configurations will be done in the **remoteWrite** - section of the helm chart:
```yaml
remoteWrite:
  - url: https://stargate-playground.live.dhei.telekom.de/raccoon/metrics/v1/eni/eni-example-metrics-tenant/insert
    queues: 4
    show_url: "true"
    relabel_config:
      - action: keep
        source_labels:
          - kubernetes_io_app
        regex: "my-app"
    oauth:
      client_id: "eni--skoll--my-example-metricsTenant"
      client_secret: "*****"
      scopes: "openid"
      token_url: "https://iris-playground.live.dhei.telekom.de/auth/realms/default/protocol/openid-connect/token"
```

Every array entry consists of an url and can be extended with [relabeling-configurations](https://docs.victoriametrics.com/vmagent.html#relabeling) for filtering, 
with authentication details like above with oauth2 for stargate to write to a metricsTenant and more.


### Watching ServiceMonitors

Like the Prometheus-Operator the SCG watches the custom resources ServiceMonitor, reads from their configured details and generates additional custom scrape jobs.

Example ServiceMonitor:
```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: sample-servicemonitor
spec:
  endpoints:
  - port: service
    scheme: http
    path: /metrics
    relabelings:
      - action: labelmap
        regex: __meta_kubernetes_service_label_(tardis_telekom_de_.+)
  selector:
    matchLabels:
      key.of.service.label: "value-of-service-label"
  namespaceSelector:
    matchNames:
      - default
```

#### Advantages of using ServiceMonitors

A very simple solution for creating scrape jobs is simply add the prometheus.io - labels to your service which points to the metrics endpoint and then VMAgent knows where to scrape.

Using ServiceMonitors gives the advantage to dynamically add more lables to your metrics if wanted.
The static "scrape-by-service-annotation" - job above just provides a fix number of specific labels. 

|                | serviceMonitor                                                                 | scrape-by-service-annotation                                                                           |
|----------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| default labels | * pod<br>* service<br>* namespace<br>* container<br>* endpoint<br>* instance   | * pod<br>* service<br>* namespace<br>* container<br>* endpoint<br>* instance<br>* tardis_telekom_de_.+ |
| global labels  | * platform<br>* clusterID<br>* cluster_type<br>* prometheus                    | * platform<br>* clusterID<br>* cluster_type<br>* prometheus                                            |
| custom labels  | every label can be added with relabeling configurations in the serviceMonitor  | **not possible**                                                                                       |

We in T‧AR‧D‧I‧S are adding global lables pending on the cluster to all metrics to be able to separate the metrics if needed.

### Managing kubelet metrics endpoints

The SCG is able to manage scraping from the kubelet metrics endpoints. For this the SCG keeps an Endpoints definition up-to-date of IP-addresses from every kubernetes node.
This is necessary that a related service can point to all available metric endpoints.

Together with the kubelet-serviceMonitor the VMAgent scrape kubelet metrics endpoints too. 

### Deprecation of versions

Maybe later on some helm versions will be deprecated. To prevent issues after removing old deprecated version, please keep an eye on our docu.
We will inform you on these pages about versions who are deprecated and when they will be removed from the helm repository.
