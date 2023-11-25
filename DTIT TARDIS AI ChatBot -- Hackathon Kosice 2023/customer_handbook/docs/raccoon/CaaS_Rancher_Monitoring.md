# CaaS Rancher Monitoring

!!! Attention
    This documentation is for users working on CaaS Rancher platforms who want to send metrics to Raccoon.
    Monitoring of Rancher is managed by the [CaaS-Team](https://mywiki.confluence.telekom.de/pages/viewpage.action?pageId=1227591792).

## Monitoring V3

Because of several issues with V2 a quick update to V3 was started. We found a way to prevent using the helm chart for V3.
(Solution in helm chart version 1.1.2)

### Using VMAgent and SCG

Using VMAgent and SCG is described [here](products-as-enabler/Metrics_Collector.md).
Configure it for your CaaS project.

Add this part to your values.yaml: 
```yaml
cattle_enabler:
    enabled: true
```
A serviceAccount with rights bound by role will be added to the namespace and enables scraping project related metrics from the master Prometheus.

Now add a scrape_config job in the following array to scrape from this master Prometheus:
```yaml
scrapeConfigGenerator:
  defaultScrapeConfig:
    scrape_configs:
      - job_name: federate-system-prometheus
        bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
        honor_labels: true
        metrics_path: /federate
        params:
          match[]:
            - '{__name__=~".+"}'
        static_configs:
          - targets:
              - rancher-monitoring-prometheus.cattle-monitoring-system.svc:9091
```

!!! Note
    No ProjectHelmChart resource or kube-prometheus-stack - helm chart deployment is necessary  
