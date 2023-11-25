# Environment Overview

On T‧AR‧D‧I‧S, we are offering different types of environments:

* **Runtime** environments:  
  These are environments that each run in their own, dedicated clusters.  
* **Virtual** environments:  
  These environments all **share** one physical cluster which we call **QA**,  
  they were created and named to facilitate the historic, well-established release container testing stages.  
  There is also an [entry in our FAQ](https://developer.telekom.de/docs/src/tardis_faqs/#which-environment-should-i-use) on which environment to use. 

The **hierarchy** of these environments is as follows, 
with respect to e. g. stability or maturity of features and deployments. 

`playground` → `QA` → `preprod` → `prod` 

I. e. this means we **recommend** to move from playground onto a more mature environment 
whenever you are done experimenting and playing around. 
This is also because we will deploy new features and fixes according to the hierarchy, 
which in turn means that **on playground things may break**. 

=== "Runtime"

    | Environment | Status | Purpose |
    |:------------|:------:|:--------|
    | playground  | :white_check_mark: Available | SandBox, great for experiments |
    | preprod     | :white_check_mark: Available | Integration/Testing with partner system |
    | prod        | :white_check_mark: Available | Production |

=== "Virtual envrionments"

    | Environment | Status | Purpose |
    |:------------|:------:|:--------|
    | av          | :white_check_mark: Available | Release Testing OSS |
    | bond        | :white_check_mark: Available | Testing Environment |
    | frv         | :white_check_mark: Available | Production Reference OSS |
    | cit2        | :white_check_mark: Available | Release Testing BSS |
    | cit4        | :white_check_mark: Available | Production Reference BSS |
    | rv          | :white_check_mark: Available | Last & Performance OSS |
    | sit         | :white_check_mark: Available | System Integration Test |

Customers can use any of these Environments. Although, it is advised to always use Preprod env before going to Prod.

## StarGate and Iris

Applications should always communicate with the nearest StarGate available next to their runtime Applications.

If your application runs on HITNET or CNDTAG or OTC & AppAgile or CaaS then please use CaaS as Zone in `Rover.yml`

If your application runs on AWS then select use AWS as Zone in `Rover.yml`

### StarGate ZONE: AWS

=== "Runtime"

    | Environment | Stargate                          | IRIS M2M|
    |-------------|-----------------------------------|--------------------|
    | playground  | https://stargate-playground.live.dhei.telekom.de |  https://iris-playground.live.dhei.telekom.de/auth/realms/default |
    | preprod     | https://stargate-preprod.live.dhei.telekom.de | https://iris-preprod.live.dhei.telekom.de/auth/realms/default |
    | prod        | https://stargate.prod.dhei.telekom.de |  https://iris.prod.dhei.telekom.de/auth/realms/default |

=== "Virtual envrionments"

    | Environment | Stargate                          | IRIS M2M|
    |-------------|-----------------------------------|--------------------|
    | av          | https://stargate.qa.dhei.telekom.de/av |  https://iris.qa.dhei.telekom.de/auth/realms/av |
    | bond        | https://stargate.qa.dhei.telekom.de/bond |  https://iris.qa.dhei.telekom.de/auth/realms/bond |
    | frv         | https://stargate.qa.dhei.telekom.de/frv |  https://iris.qa.dhei.telekom.de/auth/realms/frv |
    | cit2        | https://stargate.qa.dhei.telekom.de/cit2 |  https://iris.qa.dhei.telekom.de/auth/realms/cit2 |
    | cit4        | https://stargate.qa.dhei.telekom.de/cit4 |  https://iris.qa.dhei.telekom.de/auth/realms/cit4 |
    | rv          | https://stargate.qa.dhei.telekom.de/rv |  https://iris.qa.dhei.telekom.de/auth/realms/rv |
    | sit         | https://stargate.qa.dhei.telekom.de/sit |  https://iris.qa.dhei.telekom.de/auth/realms/sit |

### StarGate ZONE: CaaS

=== "Runtime"

    | Environment | Stargate                          | IRIS M2M|
    |-------------|-----------------------------------|--------------------|
    | playground  | https://stargate-playground.caas-t01.telekom.de | https://iris-playground.caas-t01.telekom.de/auth/realms/default |
    | preprod     | https://stargate-preprod.caas-t01.telekom.de | https://iris-preprod.caas-t01.telekom.de/auth/realms/default |
    | prod        | https://stargate.caas-p01.telekom.de | https://iris.caas-p01.telekom.de/auth/realms/default |

=== "Virtual envrionments"

    | Environment | Stargate                          | IRIS M2M|
    |-------------|-----------------------------------|--------------------|
    | av          | https://stargate-qa.caas-t01.telekom.de/av |  https://iris-qa.caas-t01.telekom.de/auth/realms/av |
    | bond        | https://stargate-qa.caas-t01.telekom.de/bond |  https://iris-qa.caas-t01.telekom.de/auth/realms/bond |
    | frv         | https://stargate-qa.caas-t01.telekom.de/frv |  https://iris-qa.caas-t01.telekom.de/auth/realms/frv |
    | cit2        | https://stargate-qa.caas-t01.telekom.de/cit2 |  https://iris-qa.caas-t01.telekom.de/auth/realms/cit2 |
    | cit4        | https://stargate-qa.caas-t01.telekom.de/cit4 |  https://iris-qa.caas-t01.telekom.de/auth/realms/cit4 |
    | rv          | https://stargate-qa.caas-t01.telekom.de/rv |  https://iris-qa.caas-t01.telekom.de/auth/realms/rv |
    | sit         | https://stargate-qa.caas-t01.telekom.de/sit |  https://iris-qa.caas-t01.telekom.de/auth/realms/sit |

### StarGate ZONE: Cetus (CaaS T21, P21 - TPC)

=== "Runtime"

    | Environment | Stargate                                            | IRIS M2M           |
    |-------------|-----------------------------------------------------|--------------------|
    | playground  | https://stargate-cetus.playground.tardis.telekom.de | https://iris-cetus.playground.tardis.telekom.de/auth/realms/default |
    | preprod     | https://stargate-cetus.preprod.tardis.telekom.de    | https://iris-cetus.preprod.tardis.telekom.de/auth/realms/default    |
    | prod        | https://stargate-cetus.prod.tardis.telekom.de    | https://iris-cetus.prod.tardis.telekom.de/auth/realms/default    |


=== "Virtual envrionments"

    | Environment | Stargate                          | IRIS M2M|
    |-------------|-----------------------------------|--------------------|
    | av          | https://stargate-cetus.qa.tardis.telekom.de/av   |  https://iris-cetus.qa.tardis.telekom.de/auth/realms/av |
    | bond        | https://stargate-cetus.qa.tardis.telekom.de/bond |  https://iris-cetus.qa.tardis.telekom.de/auth/realms/bond |
    | frv         | https://stargate-cetus.qa.tardis.telekom.de/frv  |  https://iris-cetus.qa.tardis.telekom.de/auth/realms/frv |
    | cit2        | https://stargate-cetus.qa.tardis.telekom.de/cit2 |  https://iris-cetus.qa.tardis.telekom.de/auth/realms/cit2 |
    | cit4        | https://stargate-cetus.qa.tardis.telekom.de/cit4 |  https://iris-cetus.qa.tardis.telekom.de/auth/realms/cit4 |
    | rv          | https://stargate-cetus.qa.tardis.telekom.de/rv   |  https://iris-cetus.qa.tardis.telekom.de/auth/realms/rv |
    | sit         | https://stargate-cetus.qa.tardis.telekom.de/sit  |  https://iris-cetus.qa.tardis.telekom.de/auth/realms/sit |

### Spacegate ZONE: Space

=== "Runtime"

    | Environment | Spacegate                          | IRIX M2M|
    |-------------|-----------------------------------|--------------------|
    | playground  | https://playground.spacegate.telekom.de |  https://playground.spacegate.telekom.de/auth/realms/default |
    | preprod     | https://preprod.spacegate.telekom.de | https://preprod.spacegate.telekom.de/auth/realms/default |
    | prod        | https://api.telekom.de |  https://api.telekom.de/auth/realms/default |

=== "Virtual envrionments"

    | Environment | Stargate                          | IRIX M2M|
    |-------------|-----------------------------------|--------------------|
    | av          | https://qa.spacegate.telekom.de/av |  https://qa.spacegate.telekom.de/auth/realms/av |
    | bond        | https://qa.spacegate.telekom.de/bond |  https://qa.spacegate.telekom.de/auth/realms/bond |
    | frv         | https://qa.spacegate.telekom.de/frv |  https://qa.spacegate.telekom.de/auth/realms/frv |
    | cit2        | https://qa.spacegate.telekom.de/cit2 |  https://qa.spacegate.telekom.de/auth/realms/cit2 |
    | cit4        | https://qa.spacegate.telekom.de/cit4 |  https://qa.spacegate.telekom.de/auth/realms/cit4 |
    | rv          | https://qa.spacegate.telekom.de/rv |  https://qa.spacegate.telekom.de/auth/realms/rv |
    | sit         | https://qa.spacegate.telekom.de/sit |  https://qa.spacegate.telekom.de/auth/realms/sit |

### Spacegate ZONE: Canis (CaaS T21, P21 - TPC)

=== "Runtime"

    | Environment | Spacegate                          | IRIX M2M|
    |-------------|-----------------------------------|--------------------|
    | playground  | https://spacegate-canis.playground.tardis.telekom.de | https://spacegate-canis.playground.tardis.telekom.de/auth/realms/default |
    | preprod     | https://spacegate-canis.preprod.tardis.telekom.de    | https://spacegate-canis.preprod.tardis.telekom.de/auth/realms/default    |
    | prod        | https://sg-api.telekom.de    | https://sg-api.telekom.de/auth/realms/default    |

=== "Virtual envrionments"

    | Environment | Stargate                                          | IRIX M2M           |
    |-------------|---------------------------------------------------|--------------------|
    | av          | https://spacegate-canis.qa.tardis.telekom.de/av   |  https://spacegate-canis.qa.tardis.telekom.de/auth/realms/av   |
    | bond        | https://spacegate-canis.qa.tardis.telekom.de/bond |  https://spacegate-canis.qa.tardis.telekom.de/auth/realms/bond |
    | frv         | https://spacegate-canis.qa.tardis.telekom.de/frv  |  https://spacegate-canis.qa.tardis.telekom.de/auth/realms/frv  |
    | cit2        | https://spacegate-canis.qa.tardis.telekom.de/cit2 |  https://spacegate-canis.qa.tardis.telekom.de/auth/realms/cit2 |
    | cit4        | https://spacegate-canis.qa.tardis.telekom.de/cit4 |  https://spacegate-canis.qa.tardis.telekom.de/auth/realms/cit4 |
    | rv          | https://spacegate-canis.qa.tardis.telekom.de/rv   |  https://spacegate-canis.qa.tardis.telekom.de/auth/realms/rv   |
    | sit         | https://spacegate-canis.qa.tardis.telekom.de/sit  |  https://spacegate-canis.qa.tardis.telekom.de/auth/realms/sit  |

## Mission Control UI

=== "Runtime"

    | Environment | Mission Control                   | Purpose|
    |-------------|-----------------------------------|--------------------|
    | playground  | https://missioncontrol-playground.live.dhei.telekom.de | APIs overview in Playground |
    | preprod     | https://missioncontrol-preprod.live.dhei.telekom.de | APIs overview  in Preprod |
    | prod        | https://missioncontrol.prod.dhei.telekom.de | APIs overview in Production |

=== "Virtual envrionments"

    | Environment | Mission Control                   | Purpose|
    |-------------|-----------------------------------|--------------------|
    | av          | https://missioncontrol.qa.dhei.telekom.de/?env=av | APIs overview in AV |
    | bond        | https://missioncontrol.qa.dhei.telekom.de/?env=bond | APIs overview in BOND |
    | frv         | https://missioncontrol.qa.dhei.telekom.de/?env=frv | APIs overview in FRV |
    | cit2        | https://missioncontrol.qa.dhei.telekom.de/?env=cit2 | APIs overview in CIT2 |
    | cit4        | https://missioncontrol.qa.dhei.telekom.de/?env=cit4 | APIs overview in CIT4 |
    | rv          | https://missioncontrol.qa.dhei.telekom.de/?env=rv | APIs overview in RV |
    | sit         | https://missioncontrol.qa.dhei.telekom.de/?env=sit | APIs overview in SIT |


## Raccoon Grafana UI

| Environment | Raccoon/Grafana         | Purpose|
|-------------|-----------------------------------|--------------------|
| playground, preprod and qa  | <https://grafana-rocket-raccoon-guardians.live.dhei.telekom.de> | Query T‧AR‧D‧I‧S metrics for playground, preprod and virtual test envs |
| prod        | <https://grafana-rocket-raccoon-guardians.prod.dhei.telekom.de> | Query T‧AR‧D‧I‧S metrics for production |

## Drax Jaeger UI

| Environment | Drax/JaegerUI         | Purpose|
|-------------|-----------------------------------|--------------------|
| playground and preprod  | <https://drax-guardians.live.dhei.telekom.de> | Query T‧AR‧D‧I‧S traces for playground and preprod |
| qa  | <https://drax-guardians.qa.dhei.telekom.de> | Query T‧AR‧D‧I‧S traces for virtual test environments |
| prod        | <https://drax-guardians.prod.dhei.telekom.de> | Query T‧AR‧D‧I‧S traces for production |

## Quill Kibana UI

| Environment | Quill/Kibana           | Purpose|
|-------------|-----------------------------------|--------------------|
| prod | <https://7ca5edff9d1f46f59c863f3c93aa3eea.otc-ece.telekom.de> | Query T‧AR‧D‧I‧S log messages for production  (CIAM role "tardis.maintainer" needed). Respective indices are `log-prod-*`, the originating cluster can be gathered from attribute `clusterID` |
| playground, preprod, qa | <https://9a5aa1833ffa419ea660e38b2822e085.otc-ece.telekom.de> | Query T‧AR‧D‧I‧S log messages for all non prod customer facing environments (CIAM role "tardis.maintainer" needed). Respective indices are `log-live-*`, the originating cluster can be gathered from attribute `clusterID`  |

## Drax Collector

### Protocols:

| Name        | Protocol | Description                                                                                                   |
|-------------|----------|---------------------------------------------------------------------------------------------------------------|
| `grpc`      | gRPC     | Accepts spans in jaeger model.proto format                                                                    |
| `http`      | HTTP     | Accepts spans directly from clients in jaeger.thrift format with binary thrift protocol (POST to /api/traces) |
| `zipkin`    | HTTP     | Accepts Zipkin spans in Thrift, JSON and Proto (/api/v1/spans or /api/v2/spans)                               |
| `otlp-grpc` | gRPC     | Accepts traces in [OpenTelemetry OTLP gRPC](https://opentelemetry.io/docs/specs/otlp/#otlpgrpc) format        |
| `otlp-http` | HTTP     | Accepts traces in [OpenTelemetry OTLP HTTP](https://opentelemetry.io/docs/specs/otlp/#otlphttp) format        |

### Endpoints for zone: AWS

| Environment        | Protocol-Name | Endpoint                                                                     | 
|--------------------|---------------|------------------------------------------------------------------------------|
| playground/preprod | `grpc`        | ```grpc://collector-grpc-drax-guardians.live.dhei.telekom.de:443```          | 
| playground/preprod | `http`        | ```https://collector-http-drax-guardians.live.dhei.telekom.de:443```         | 
| playground/preprod | `zipkin`      | ```https://collector-zipkin-http-drax-guardians.live.dhei.telekom.de:443 ``` |
| playground/preprod | `otlp-grpc`   | ```grpc://collector-otlp-grpc-drax-guardians.live.dhei.telekom.de:443```     |
| playground/preprod | `otlp-http`   | ```https://collector-otlp-http-drax-guardians.live.dhei.telekom.de:443```    |
| qa (virtual envs)  | `grpc`        | ```grpc://collector-grpc-drax-guardians.qa.dhei.telekom.de:443```            |
| qa (virtual envs)  | `http`        | ```https://collector-http-drax-guardians.qa.dhei.telekom.de:443```           |
| qa (virtual envs)  | `zipkin`      | ```https://collector-zipkin-http-drax-guardians.qa.dhei.telekom.de:443```    |
| qa (virtual envs)  | `otlp-grpc`   | ```grpc://collector-otlp-grpc-drax-guardians.qa.dhei.telekom.de:443```       |
| qa (virtual envs)  | `otlp-http`   | ```https://collector-otlp-http-drax-guardians.qa.dhei.telekom.de:443```      |
| prod               | `grpc`        | ```grpc://collector-grpc-drax-guardians.prod.dhei.telekom.de:443```          |
| prod               | `http`        | ```https://collector-http-drax-guardians.prod.dhei.telekom.de:443```         |
| prod               | `zipkin`      | ```https://collector-zipkin-http-drax-guardians.prod.dhei.telekom.de:443```  |  
| prod               | `otlp-grpc`   | ```grpc://collector-otlp-grpc-drax-guardians.prod.dhei.telekom.de:443```     |   
| prod               | `otlp-http`   | ```https://collector-otlp-http-drax-guardians.prod.dhei.telekom.de:443```    |

### Endpoints for zone: CaaS

| Environment       | Protocol-Name | Endpoint                                                                              | 
|-------------------|---------------|---------------------------------------------------------------------------------------|
| playground        | `grpc`        | ```grpc://collector-grpc-drax-guardians-playground.caas-t01.telekom.de:443```         | 
| playground        | `http`        | ```https://collector-http-drax-guardians-playground.caas-t01.telekom.de:443```        | 
| playground        | `zipkin`      | ```https://collector-zipkin-http-drax-guardians-playground.caas-t01.telekom.de:443``` |
| playground        | `otlp-grpc`   | ```grpc://collector-otlp-grpc-drax-guardians-playground.caas-t01.telekom.de:443```    |
| playground        | `otlp-http`   | ```https://collector-otlp-http-drax-guardians-playground.caas-t01.telekom.de:443```   |
| preprod           | `grpc`        | ```grpc://collector-grpc-drax-guardians-preprod.caas-t01.telekom.de:443```            | 
| preprod           | `http`        | ```https://collector-http-drax-guardians-preprod.caas-t01.telekom.de:443```           | 
| preprod           | `zipkin`      | ```https://collector-zipkin-http-drax-guardians-preprod.caas-t01.telekom.de:443```    |
| preprod           | `otlp-grpc`   | ```grpc://collector-otlp-grpc-drax-guardians-preprod.caas-t01.telekom.de:443```       |
| preprod           | `otlp-http`   | ```https://collector-otlp-http-drax-guardians-preprod.caas-t01.telekom.de:443```      |
| qa (virtual envs) | `grpc`        | ```grpc://collector-grpc-drax-guardians-qa.caas-t01.telekom.de:443```                 |
| qa (virtual envs) | `http`        | ```https://collector-http-drax-guardians-qa.caas-t01.telekom.de:443```                |
| qa (virtual envs) | `zipkin`      | ```https://collector-zipkin-http-drax-guardians-qa.caas-t01.telekom.de:443```         |
| qa (virtual envs) | `otlp-grpc`   | ```grpc://collector-otlp-grpc-drax-guardians-qa.caas-t01.telekom.de:443```            |
| qa (virtual envs) | `otlp-http`   | ```https://collector-otlp-http-drax-guardians-qa.caas-t01.telekom.de:443```           |
| prod              | `grpc`        | ```grpc://collector-grpc-drax-guardians-prod.caas-p01.telekom.de:443```               |
| prod              | `http`        | ```https://collector-http-drax-guardians-prod.caas-p01.telekom.de:443```              |
| prod              | `zipkin`      | ```https://collector-zipkin-http-drax-guardians-prod.caas-p01.telekom.de:443```       |  
| prod              | `otlp-grpc`   | ```grpc://collector-otlp-grpc-drax-guardians-prod.caas-p01.telekom.de:443```          |   
| prod              | `otlp-http`   | ```https://collector-otlp-http-drax-guardians-prod.caas-p01.telekom.de:443```         |

### Endpoints for zone: Cetus 

| Environment        | Protocol-Name | Endpoint                                                                        |
|--------------------|---------------|---------------------------------------------------------------------------------|
| playground         | `grpc`        | ```grpc://collector-grpc-drax-cetus.playground.tardis.telekom.de:443```         |
| playground         | `http`        | ```https://collector-http-drax-cetus.playground.tardis.telekom.de:443```        |
| playground         | `zipkin`      | ```https://collector-zipkin-http-drax-cetus.playground.tardis.telekom.de:443``` |
| playground         | `otlp-grpc`   | ```grpc://collector-otlp-grpc-drax-cetus.playground.tardis.telekom.de:443```    |
| playground         | `otlp-http`   | ```https://collector-otlp-http-drax-cetus.playground.tardis.telekom.de:443```   |
| preprod            | `grpc`        | ```grpc://collector-grpc-drax-cetus.preprod.tardis.telekom.de:443```            |
| preprod            | `http`        | ```https://collector-http-drax-cetus.preprod.tardis.telekom.de:443```           |
| preprod            | `zipkin`      | ```https://collector-zipkin-http-drax-cetus.preprod.tardis.telekom.de:443```    |
| preprod            | `otlp-grpc`   | ```grpc://collector-otlp-grpc-drax-cetus.preprod.tardis.telekom.de:443```       |
| preprod            | `otlp-http`   | ```https://collector-otlp-http-drax-cetus.preprod.tardis.telekom.de:443```      |
| qa                 | `grpc`        | ```grpc://collector-grpc-drax-cetus.qa.tardis.telekom.de:443```                 |
| qa                 | `http`        | ```https://collector-http-drax-cetus.qa.tardis.telekom.de:443```                |
| qa                 | `zipkin`      | ```https://collector-zipkin-http-drax-cetus.qa.tardis.telekom.de:443```         |
| qa                 | `otlp-grpc`   | ```grpc://collector-otlp-grpc-drax-cetus.qa.tardis.telekom.de:443```            |
| qa                 | `otlp-http`   | ```https://collector-otlp-http-drax-cetus.qa.tardis.telekom.de:443```           |
| prod               | `grpc`        | ```grpc://collector-grpc-drax-cetus.prod.tardis.telekom.de:443```               |
| prod               | `http`        | ```https://collector-http-drax-cetus.prod.tardis.telekom.de:443```              |
| prod               | `zipkin`      | ```https://collector-zipkin-http-drax-cetus.prod.tardis.telekom.de:443```       |
| prod               | `otlp-grpc`   | ```grpc://collector-otlp-grpc-drax-cetus.prod.tardis.telekom.de:443```          |
| prod               | `otlp-http`   | ```https://collector-otlp-http-drax-cetus.prod.tardis.telekom.de:443```         |


<!-- SDDHEI-3364
| Schiff | playground         | ```grpc://collector-grpc-drax-guardians.tardis-1.reftmdc.bn.das-schiff.telekom.de:443```         | Collector grpc endpoint for traces (used by jaeger agent, TLS enabled)   |
| Schiff | playground         | ```https://collector-http-drax-guardians.tardis-1.reftmdc.bn.das-schiff.telekom.de:443```        | Collector http endpoint for traces: /api/traces                          |
| Schiff | playground         | ```https://collector-zipkin-http-drax-guardians.tardis-1.reftmdc.bn.das-schiff.telekom.de:443``` | Collector zipkin endpoint for traces: /api/v1/spans or /api/v2/spans     |
-->

## Trusted Issuers

For more informations regarding  Last Mile Security, you can find the documentation [here](https://developer.telekom.de/docs/src/tardis_customer_handbook/StarGate/#last-mile-security-gateway-token)

For more informations regarding Legacy Last Mile Security, you can find the documentation [here](https://developer.telekom.de/docs/src/tardis_customer_handbook/StarGate/#legacy-last-mile-security) 

### StarGate ZONE: AWS

=== "Runtime"

    | Environment | Last Mile Security (recommended)   | Legacy Last Mile Security |
    |-------------|-----------------------------------|--------------------|
    | playground  | https://stargate-playground.live.dhei.telekom.de/auth/realms/default |  https://iris-playground.live.dhei.telekom.de/auth/realms/default |
    | preprod     | https://stargate-preprod.live.dhei.telekom.de/auth/realms/default | https://iris-preprod.live.dhei.telekom.de/auth/realms/default |
    | prod        | https://stargate.prod.dhei.telekom.de/auth/realms/default |  https://iris.prod.dhei.telekom.de/auth/realms/default |

=== "Virtual envrionments"

    | Environment | Last Mile Security (recommended) | Legacy Last Mile Security |
    |-------------|-----------------------------------|--------------------|
    | av          | https://stargate.qa.dhei.telekom.de/auth/realms/av |  https://iris.qa.dhei.telekom.de/auth/realms/av |
    | bond        | https://stargate.qa.dhei.telekom.de/auth/realms/bond|  https://iris.qa.dhei.telekom.de/auth/realms/bond |
    | frv         | https://stargate.qa.dhei.telekom.de/auth/realms/frv  |  https://iris.qa.dhei.telekom.de/auth/realms/frv |
    | cit2        | https://stargate.qa.dhei.telekom.de/auth/realms/cit2 |  https://iris.qa.dhei.telekom.de/auth/realms/cit2 |
    | cit4        | https://stargate.qa.dhei.telekom.de/auth/realms/cit4 |  https://iris.qa.dhei.telekom.de/auth/realms/cit4 |
    | rv          | https://stargate.qa.dhei.telekom.de/auth/realms/rv |  https://iris.qa.dhei.telekom.de/auth/realms/rv |
    | sit         | https://stargate.qa.dhei.telekom.de/auth/realms/sit |  https://iris.qa.dhei.telekom.de/auth/realms/sit |

### StarGate ZONE: CaaS

=== "Runtime"

    | Environment | Last Mile Security (recommended) | Legacy Last Mile Security |
    |-------------|-----------------------------------|--------------------|
    | playground  | https://stargate-playground.caas-t01.telekom.de/auth/realms/default | https://iris-playground.caas-t01.telekom.de/auth/realms/default |
    | preprod     | https://stargate-preprod.caas-t01.telekom.de/auth/realms/default | https://iris-preprod.caas-t01.telekom.de/auth/realms/default |
    | prod        | https://stargate.caas-p01.telekom.de/auth/realms/default | https://iris.caas-p01.telekom.de/auth/realms/default |

=== "Virtual envrionments"

    | Environment | Last Mile Security (recommended)  | Legacy Last Mile Security |
    |-------------|-----------------------------------|--------------------|
    | av          | https://stargate-qa.caas-t01.telekom.de/auth/realms/av |  https://iris-qa.caas-t01.telekom.de/auth/realms/av |
    | bond        | https://stargate-qa.caas-t01.telekom.de/auth/realms/bond |  https://iris-qa.caas-t01.telekom.de/auth/realms/bond |
    | frv         | https://stargate-qa.caas-t01.telekom.de/auth/realms/frv |  https://iris-qa.caas-t01.telekom.de/auth/realms/frv |
    | cit2        | https://stargate-qa.caas-t01.telekom.de/auth/realms/cit2 |  https://iris-qa.caas-t01.telekom.de/auth/realms/cit2 |
    | cit4        | https://stargate-qa.caas-t01.telekom.de/auth/realms/cit4 |  https://iris-qa.caas-t01.telekom.de/auth/realms/cit4 |
    | rv          | https://stargate-qa.caas-t01.telekom.de/auth/realms/rv |  https://iris-qa.caas-t01.telekom.de/auth/realms/rv |
    | sit         | https://stargate-qa.caas-t01.telekom.de/auth/realms/sit |  https://iris-qa.caas-t01.telekom.de/auth/realms/sit |

### StarGate ZONE: Cetus (CaaS T21 - TPC)

=== "Runtime"

    | Environment | Last Mile Security (recommended) |
    |-------------|-----------------------------------|
    | playground  | https://stargate-cetus.playground.tardis.telekom.de/auth/realms/default |
    | preprod     | https://stargate-cetus.preprod.tardis.telekom.de/auth/realms/default |
    | prod        | https://stargate-cetus.prod.tardis.telekom.de/auth/realms/default |

=== "Virtual envrionments"

    | Environment | Last Mile Security (recommended)  |
    |-------------|-----------------------------------|
    | av          | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/av |
    | bond        | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/bond |
    | frv         | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/frv |
    | cit2        | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/cit2 |
    | cit4        | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/cit4 |
    | rv          | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/rv |
    | sit         | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/sit |

### Spacegate

=== "Runtime"

    | Environment | Last Mile Security (recommended)    | Legacy Last Mile Security |
    |-------------|-----------------------------------|--------------------|
    | playground  | https://playground.spacegate.telekom.de/spacegate/auth/realms/default |  https://playground.spacegate.telekom.de/auth/realms/default |
    | preprod     | https://preprod.spacegate.telekom.de/spacegate/auth/realms/default | https://preprod.spacegate.telekom.de/auth/realms/default |
    | prod        | https://api.telekom.de/spacegate/auth/realms/default |  https://api.telekom.de/auth/realms/default |

=== "Virtual envrionments"

    | Environment | Last Mile Security (recommended)   | Legacy Last Mile Security |
    |-------------|-----------------------------------|--------------------|
    | av          | https://qa.spacegate.telekom.de/spacegate/auth/realms/av |  https://qa.spacegate.telekom.de/auth/realms/av |
    | bond        | https://qa.spacegate.telekom.de/spacegate/auth/realms/bond |  https://qa.spacegate.telekom.de/auth/realms/bond |
    | frv         | https://qa.spacegate.telekom.de/spacegate/auth/realms/frv |  https://qa.spacegate.telekom.de/auth/realms/frv |
    | cit2        | https://qa.spacegate.telekom.de/spacegate/auth/realms/cit2 |  https://qa.spacegate.telekom.de/auth/realms/cit2 |
    | cit4        | https://qa.spacegate.telekom.de/spacegate/auth/realms/cit4 |  https://qa.spacegate.telekom.de/auth/realms/cit4 |
    | rv          | https://qa.spacegate.telekom.de/spacegate/auth/realms/rv |  https://qa.spacegate.telekom.de/auth/realms/rv |
    | sit         | https://qa.spacegate.telekom.de/spacegate/auth/realms/sit |  https://qa.spacegate.telekom.de/auth/realms/sit |

### Spacegate ZONE: Canis (CaaS T21 - TPC)

=== "Runtime"

    | Environment | Last Mile Security (recommended)    |
    |-------------|-----------------------------------|
    | playground  | https://spacegate-canis.playground.tardis.telekom.de/spacegate/auth/realms/default |
    | preprod     | https://spacegate-canis.preprod.tardis.telekom.de/spacegate/auth/realms/default|
    | prod        | https://sg-api.telekom.de/spacegate/auth/realms/default |

=== "Virtual envrionments"

    | Environment | Last Mile Security (recommended)   |
    |-------------|-----------------------------------|
    | av          | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/av |
    | bond        | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/bond |
    | frv         | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/frv |
    | cit2        | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/cit2 |
    | cit4        | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/cit4 |
    | rv          | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/rv |
    | sit         | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/sit |


## JSON Web Key Set URLs

For more informations regarding  JSON Web Key set, please see the official [RFC7517](https://www.ietf.org/rfc/rfc7517.txt)

### StarGate ZONE: AWS

=== "Runtime"

    | Environment | JSON Web Key Set URL  |
    |-------------|-----------------------------------|
    | playground  | https://stargate-playground.live.dhei.telekom.de/auth/realms/default/protocol/openid-connect/certs |
    | preprod     | https://stargate-preprod.live.dhei.telekom.de/auth/realms/default/protocol/openid-connect/certs |
    | prod        | https://stargate.prod.dhei.telekom.de/auth/realms/default/protocol/openid-connect/certs |

=== "Virtual envrionments"

    | Environment | JSON Web Key Set URL  |
    |-------------|-----------------------------------|
    | av          | https://stargate.qa.dhei.telekom.de/auth/realms/av/protocol/openid-connect/certs  | 
    | bond        | https://stargate.qa.dhei.telekom.de/auth/realms/bond/protocol/openid-connect/certs  |
    | frv         | https://stargate.qa.dhei.telekom.de/auth/realms/frv/protocol/openid-connect/certs   | 
    | cit2        | https://stargate.qa.dhei.telekom.de/auth/realms/cit2/protocol/openid-connect/certs  |
    | cit4        | https://stargate.qa.dhei.telekom.de/auth/realms/cit4/protocol/openid-connect/certs  | 
    | rv          | https://stargate.qa.dhei.telekom.de/auth/realms/rv/protocol/openid-connect/certs  |
    | sit         | https://stargate.qa.dhei.telekom.de/auth/realms/sit/protocol/openid-connect/certs  |

### StarGate ZONE: CaaS

=== "Runtime"

    | Environment | JSON Web Key Set URL  |
    |-------------|-----------------------------------|
    | playground  | https://stargate-playground.caas-t01.telekom.de/auth/realms/default/protocol/openid-connect/certs | 
    | preprod     | https://stargate-preprod.caas-t01.telekom.de/auth/realms/default/protocol/openid-connect/certs |
    | prod        | https://stargate.caas-p01.telekom.de/auth/realms/default/protocol/openid-connect/certs |

=== "Virtual envrionments"

    | Environment | JSON Web Key Set URL  |
    |-------------|-----------------------------------|
    | av          | https://stargate-qa.caas-t01.telekom.de/auth/realms/av/protocol/openid-connect/certs | 
    | bond        | https://stargate-qa.caas-t01.telekom.de/auth/realms/bond/protocol/openid-connect/certs | 
    | frv         | https://stargate-qa.caas-t01.telekom.de/auth/realms/frv/protocol/openid-connect/certs | 
    | cit2        | https://stargate-qa.caas-t01.telekom.de/auth/realms/cit2/protocol/openid-connect/certs | 
    | cit4        | https://stargate-qa.caas-t01.telekom.de/auth/realms/cit4/protocol/openid-connect/certs | 
    | rv          | https://stargate-qa.caas-t01.telekom.de/auth/realms/rv/protocol/openid-connect/certs | 
    | sit         | https://stargate-qa.caas-t01.telekom.de/auth/realms/sit/protocol/openid-connect/certs | 

### StarGate ZONE: Cetus (CaaS T21 - TPC)

=== "Runtime"

    | Environment | JSON Web Key Set URL  |
    |-------------|-----------------------------------|
    | playground  | https://stargate-cetus.playground.tardis.telekom.de/auth/realms/default/protocol/openid-connect/certs | 
    | preprod     | https://stargate-cetus.preprod.tardis.telekom.de/auth/realms/default/protocol/openid-connect/certs |
    | prod        | https://stargate-cetus.prod.tardis.telekom.de/auth/realms/default/protocol/openid-connect/certs |

=== "Virtual envrionments"

    | Environment | JSON Web Key Set URL  |
    |-------------|-----------------------------------|
    | av          | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/av/protocol/openid-connect/certs | 
    | bond        | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/bond/protocol/openid-connect/certs | 
    | frv         | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/frv/protocol/openid-connect/certs | 
    | cit2        | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/cit2/protocol/openid-connect/certs | 
    | cit4        | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/cit4/protocol/openid-connect/certs | 
    | rv          | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/rv/protocol/openid-connect/certs | 
    | sit         | https://stargate-cetus.qa.tardis.telekom.de/auth/realms/sit/protocol/openid-connect/certs | 

### Spacegate ZONE: AWS

=== "Runtime"

    | Environment | JSON Web Key Set URL  |
    |-------------|-----------------------------------|
    | playground  | https://playground.spacegate.telekom.de/spacegate/auth/realms/default/protocol/openid-connect/certs |
    | preprod     | https://preprod.spacegate.telekom.de/spacegate/auth/realms/default/protocol/openid-connect/certs |
    | prod        | https://api.telekom.de/spacegate/auth/realms/default/protocol/openid-connect/certs |

=== "Virtual envrionments"

    | Environment | JSON Web Key Set URL  |
    |-------------|-----------------------------------|
    | av          | https://qa.spacegate.telekom.de/spacegate/auth/realms/av/protocol/openid-connect/certs | 
    | bond        | https://qa.spacegate.telekom.de/spacegate/auth/realms/bond/protocol/openid-connect/certs |
    | frv         | https://qa.spacegate.telekom.de/spacegate/auth/realms/frv/protocol/openid-connect/certs | 
    | cit2        | https://qa.spacegate.telekom.de/spacegate/auth/realms/cit2/protocol/openid-connect/certs |
    | cit4        | https://qa.spacegate.telekom.de/spacegate/auth/realms/cit4/protocol/openid-connect/certs |
    | rv          | https://qa.spacegate.telekom.de/spacegate/auth/realms/rv/protocol/openid-connect/certs |
    | sit         | https://qa.spacegate.telekom.de/spacegate/auth/realms/sit/protocol/openid-connect/certs |

### Spacegate ZONE: Canis (CaaS T21 - TPC)

=== "Runtime"

    | Environment | JSON Web Key Set URL  |
    |-------------|-----------------------------------|
    | playground  | https://spacegate-canis.playground.tardis.telekom.de/spacegate/auth/realms/default/protocol/openid-connect/certs |
    | preprod     | https://spacegate-canis.preprod.tardis.telekom.de/spacegate/auth/realms/default/protocol/openid-connect/certs |
    | prod        | https://sg-api.telekom.de/spacegate/auth/realms/default/protocol/openid-connect/certs |

=== "Virtual envrionments"

    | Environment | JSON Web Key Set URL  |
    |-------------|-----------------------------------|
    | av          | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/av/protocol/openid-connect/certs | 
    | bond        | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/bond/protocol/openid-connect/certs |
    | frv         | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/frv/protocol/openid-connect/certs | 
    | cit2        | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/cit2/protocol/openid-connect/certs |
    | cit4        | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/cit4/protocol/openid-connect/certs |
    | rv          | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/rv/protocol/openid-connect/certs |
    | sit         | https://spacegate-canis.qa.tardis.telekom.de/spacegate/auth/realms/sit/protocol/openid-connect/certs |
