# Introduction and Overview

## Context
In May 2022, an audit activity into the implementation quality of all services published on T‧AR‧D‧I‧S was started.

This actitivity has yielded a number of useful tools which were subsequently made available to all teams implementing services published on T‧AR‧D‧I‧S

The tools materialize in the form of a report which is generated through a gitlab pipeline include and as dashboards in Racoon (Grafana), showing a live view of some the historical information presented in the report.

## Report
Reports can be generated for services which are published on T‧AR‧D‧I‧S They will not work for other services, because they rely on configuration information and metrics for and from T‧AR‧D‧I‧S

Reports are generated on the basis of Rover configuration files, not actually on the basis of individual repositories. From the Rover file, the tools find the involved repositories and include them in the report. Therefore, if a service is distributed across multiple repositories, it is sufficient to generate the report in only one of them.

The reports rely on data from gitlab static code scans (SAST) which are triggered automatically in the background, and on metrics from T‧AR‧D‧I‧S on the performance of the service over the last 30 days, which is also collected automatically.

All report input data is provided through pre-fabricated docker images used during report generation.

In case a service is not part of any of the top level gitlab groups for which pre-fabricated images have been created, it will be necessary to additionally generate these images. This step is included in the documentation.

## Racoon
The graphics which are shown in the reports have also been implemented as Dashboards for Racoon. They can be used in both Racoon for ENI and Racoon as a Service.

## Used Images
The images of Service Audit Team are signed by Cosign. You can verify the signature with following public key:
```yaml
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEMh6hmulioU+IHN80DIx96hWUlj5q
D40Yt4FxYR8uAKjqJ4MeBMlshEOZXN+wljQjjCHDg99DiC8H/N8ZK9zxiw==
-----END PUBLIC KEY-----
```

You can find more information about cosign in Magenta CICD documentation [Documentation Magenta CICD - Cosign](https://docs.devops.telekom.de/documentation/mcicd/userdocumentation-magentacicd/tools/mtr/cosign/) 

