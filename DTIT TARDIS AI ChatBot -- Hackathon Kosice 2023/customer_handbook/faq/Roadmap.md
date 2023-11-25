# T‧AR‧D‧I‧S Roadmap

The below is information about the T‧AR‧D‧I‧S roadmap process, as well as current backlog and further backlog ideas.

## Where is the T‧AR‧D‧I‧S roadmap?

Not here.  
At least not in a traditional sense.

It is **important** to understand that there is no fixed / preplanned roadmap.

We prepare our PI backlog based on two criteria:

1. We have a **Pilot Customer** that wants to develop a feature jointly with us.
2. We pick things from the IDEA backlog if there is capacity left.

And at regular intervals we also put **Refactoring** into our backlog so we do not aquire lint or technical debt.

## Current PI 16: Important Business Value committed by our teams

While in this PI the teams are mainly **focusing on handing over stuff due to the EWC cut**, there are still a few items in our current PI backlog, which are requested by our stakeholders.
Items marked as a _Stretch objective_ are those that the teams will work on,
but could not fully committed due to external dependencies and risks.  

| Topic | Description | Pilot(s) |
|-------|-------------|----------|
basicAuth on Spacegate | enable additional authentication method for internet communicaiton | 
Handover due to EWC cut | various tasks and knowledge transfer to remaining teams |
Grafana and Drax-UI integration | seamlessly integrate dashboards and tracing UI into developer portal |
API documentation access control | provide possibility to limit access to API specs | DTT
Enhance Search on Catalog | enable filtering of APIs on additional attributes | GAPI
Rover Online POC | create a way of applying rover yamls in the developer portal |
Horizon 3.0 (cntd.) | further improving performance and stability | 
Horizon redelivery POC | ensure at least once delivery in case of consumer errors |



The progress of these topics is reported upon bi-weekly in the [T‧AR‧D‧I‧S Open Hour](https://yam-united.telekom.com/pages/eni-hub/apps/events/tardis-events) and we are looking forward to your feedback about the implementation of our PI-Objectives in our [System Demo sessions](https://yam-united.telekom.com/pages/eni-hub/apps/events/tardis-events).

## Our IDEA backlog

The below topics are in our IDEA backlog — topics that wait for a convenient time to implement them.

<!--

### Requested for PI 16

This is a list of topics with either high customer value and/or acute stakeholder demand. Being on this list **does not guarantee implementation** in the next PI. The actual selection will be done in the PI planning in accordance with the teams capacity and priority agreed upon by all stakeholders.

| Topic | Description | Pilot(s) |
|-------|-------------|----------|
E2E encryption concept | Provide means to encrypt API calls end-to-end | T-SEC
Central team management | Unify team management across all environments | 

### Further ideas

-->

IDEAs with pilot customers have a higher likelihood to be planned in an upcoming PI.
If you would like to pilot for one of these topics, just [talk to us](mailto:christopher.braun@telekom.de) and make your case, i. e. tell us which problems you face and how a feature helps solving it.
We are always happy to help solve concrete problems with a pilot customer on our side.

| Topic | Description | Pilot(s) |
|-------|-------------|----------|
Rate limiting per API consumer | Enhance rate limiting to allow quotas also for consumers |
Secret rotation without downtime | Allow for a more comfortable secret rotation without service interruption |
(Almost) synchronous file transfer | Allow simultaneous file up- and download without storage in between |
Policy based authorization with OPA | Provide tailored roles and permissions in access tokens with Open Policy Agent |
T‧AR‧D‧I‧S goes open-source | Effort to open-source T‧AR‧D‧I‧S to benefit from the dev community |
Request caching | Possibility to cache API responses on the StarGate to increase speed and reduce load on upstream |
Connection to SAM3 & ICU | Broker customer user IDs from these legacy IDPs. | B2B DT
Enhanced Resource Permissions on Portal and Documentation | Differentiating _Private_, _Internal_, _External_ and _Public_ (or similar) for API documentation and other tools / resources |
Rover API for every team | Offer complete functionality of roverctl via REST API |
Support for Webhooks | Especially for Amazon and Apple webhooks |
Keyless T‧AR‧D‧I‧S | Exact definition tbd. | 
Different endpoints per operation | Add possibility to contact different upstream URLs based on HTTP operation (Siebel specialty) | CRM FN
Comments in Mission Control | Feature to add comments to exposures and subscriptions (w/o changing approval status) | 
Automated interface agreements | Feature to automatically generate interface agreements between API consumers and providers | 
Export subscriber contacts | Feature to export contact details of subscribers to inform them regarding deprecation etc. | 


## Missing a feature?

As reiterated time and time again, our backlog is driven by actual customer demands and their willingness to work jointly on an implementation.

If you feel you need a feature from us that is not listed above — please contact our [PM Christopher Braun](mailto:christopher.braun@telekom.de).

## Changelog

Here you can find a list of previously developed T‧AR‧D‧I‧S features:

??? note "PI 15 (Mar - May 23)"
    - [X] API for PSI
    - [X] Replace ADFS with Azure AD (ongoing)
    - [X] Automatic WAF config
    - [X] Grafana SMTP support
    - [X] API deprecation
    - [X] OAS changelogs
    - [X] Cloudwalker SSE support
    - [X] Horizon 3.0 (ongoing)
    - [X] Connectivity check
    - [X] PIM updates
    - [X] Sirius ZAM support

??? note "PI 14 (Dec 22 - Feb 23)"
    - [X] Rover API and API keys improvements
    - [X] SpaceGate on CaaS
    - [X] MetricsTenants in Mission Control
    - [X] ZAM login in Iris Broker
    - [X] Update to Grafana 9
    - [X] Integration of Linting Scores for APIs
    - [X] Multifiletypes clients in CloudWalker
    - [X] Bulk update for Orion
    - [X] Sirius performance tests

??? note "PI 13 (Sep - Nov 22)"
    - [X] Rover API for managing subscriptions on behalf of Hub:raum
    - [X] Support for API keys
    - [X] Event type subscription scopes
    - [X] Include audience claim in Gateway token
    - [X] Integration with CAPE API
    - [X] Security logs improvements
    - [X] Rate limiting on provider side

??? note "PI 12 (Jun - Sep 22)"
    - [X] API Scopes
    - [X] Horizon support UI "Event Horizon"
    - [X] Automatic Raccoon-as-a-Service onboarding
    - [X] Long term metrics
    - [X] Declarative CloudWalker onboarding
    - [X] POC "real no trust" for H2M
    - [X] Admin panel on developer portal
    - [X] New tools in developer portal

??? note "PI 11 (Mar - May 22)"
    - [X] Rate limiting for APIs
    - [X] Declarative Racoon-as-a-Service
    - [X] API health check status on portal
    - [X] T‧AR‧D‧I‧S universe POC
    - [X] Advanced selection filters for events
    - [X] Support multiple file subscriptions for recipients
    - [X] POC for M2M communication with token exchange

??? note "PI 10 (Nov 21 - Mar 22)"
    - [X] POC new zone on "Das Schiff" cluster
    - [X] Mission Control availability from internet
    - [X] Public management dashboards
    - [X] User account on Developer Portal
    - [X] Metadata support for file uploads
    - [X] Orion MVP

??? note "PI 9 (Aug - Nov 21)"
    - [X] Implementation of 4-eyes-principle and recertification
    - [X] Introducing a circuit breaker on dead or problematic APIs
    - [X] Design and Functionality overhaul of Maverick, the Developer Portal
    - [X] Integration of external user IDP
    - [X] Introduction of request copies for business monitoring
    - [X] Transparent file compression on CloudWalker
    - [X] Full self service integration between CloudWalker and Rover
    - [X] Pilot Racoon as a DINA-Dashboard replacement
    - [X] Further integration of Rover and Maverick

## I still have a Question

!!! Note
    Please use our [Support channel](/docs/src/tardis_customer_handbook/support/) to address your Question - we will do our best to help you.
