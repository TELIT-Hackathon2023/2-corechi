# Quill

<img src="../img/quill.svg" width="250"/>

**Table of Contents**

[[_TOC_]]

## What it is

Quill is an infrastructure for the management of application logging data. It will take care of reading log messages from stdout, buffering them and eventually feeding them into a document-oriented database for further processing. Underlying the current implementation is the "EFK"-stack (Elasticsearch database, fluentd for data collecting and forwarding, Kibana for data analysis).

Other than originally intended, the access to Quill is currently limited to T‧AR‧D‧I‧S components. This is because Quill's Elasticsearch / Kibana units are in turn rented as managed service from the PSPC Hub and fluentd agents need to run and be operated on the application's site anyway. This given, there is obvioulsy no added value using Quill by external applications over setting up their own EFK stack. The point of interest remains to be the proper configuration, which Guardians are happy to support with.




