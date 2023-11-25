# Horizon FAQ

## General questions

??? faq "What are the limitations of Horizon? How many events can be published per second/minute/day?"

    How many events can be published currently depends on the zone and traffic there. For example, currently we scaled Horizon differently on CaaS zone than on AWS, since on CaaS we have more customers than on AWS but on the other hand on AWS we sees that events are published more frequently.  
    So we cannot give a general figure for the limitations here. Currently we try to scale our instances need-based.  

    Publishing thousands of events spread over the day should be no problem at all for Horizon. However, sending thousands of events per minute could be a problem in some cases.  
    For example on AWS more than **100 events per seconds** will most likely lead to events piling up on T‧AR‧D‧I‧S side causing bigger delays in event consumption. *It's important to note that this figure is the total of all events not just per provider.*  
    This is why we worked on Horizon 3.0 with improved architecture in the past which should handle these peaks much better. We plan to rollout Horizon 3.0 on production end of August 23/beginnging of September 23.  

    However, keep in mind that publishing high volumes of events will most likely also overwhelm consumer services as we currently do not support any throttling on consumer side. This is planned for the future.  
    In order to send a large amount of data via Horizon, we highly recommend combining business events into one Horizon event to reduce traffic on Horizon (event envelope).  

    Please understand that Horizon is primarily a solution to send events to consumers to realize asynchronous business processes. Originally Horizon was not intended to simply transfer mass data (like million events per minute) from one data lake to another in real time.  

    If you are still unsure whether your use case might exceed the current limits, please contact us directly (see contact at the bottom). We are always interested in your use case and are happy to find a solution.

??? faq "Is there any limit regarding payload size?"

    Yes. Currently 1 mb is the limit but we highly advise you to not send events of that size. In fact we might decrease the maximum payload size in the future even more.  
    According to general best practices we recommend to reduce payloads to the essentials and to send only fields that are really relevant for the possible consumer. You can store a lot of data in a few kilobytes!

??? faq "Are external partners able to consume events (from the internet)?"

    Yes, this is possible. However the eventType exposure must be flagged with `visibility: world` in the Rover yaml and the consumer service must use the "space"-zone. In general this works exactly like with API-exposures and API-subscriptions. For mor information on this particular topic, also have a look at: [Spacegate](https://developer.telekom.de/docs/src/tardis_customer_handbook/StarGate/Spacegate/).

??? faq "Are external partners able to publish events (from the internet)?"

    Yes, this is also possible. However make sure to set zone to "space" for the provider service. In general this works exactly like with API-exposures and API-subscriptions. For mor information on this particular topic, also have a look at: [Spacegate](https://developer.telekom.de/docs/src/tardis_customer_handbook/StarGate/Spacegate/).

??? faq "Is it possible for external event publishers to use an DE4 environment?"

    Yes, for this we introduced the "spacex" zone (located at CaaS p01 cluster). But keep in mind that due to the CaaS cluster migration (p01 -> p21) you will need to use the zone "canis" (located at CaaS p21 cluster) instead.

??? faq "Will Horizon deliver events in the same order as they were sent?"

    No. Horizon does not guarantee to deliver events in the order they were sent. However, it is likely that events arrive in the order they were sent, but e.g. due to error-handling this cannot be guaranteed. That said in-sequence delivery is a topic we want to address in the future without making any promises at this point.

## Troubleshooting

??? faq "I do not receive any events. Is there a way to test the connectivity?"

    Yes, we created a tool to check whether Horizon is able to reach your consumer's callback endpoint. You can try it here: [Connectivity Check](https://developer.telekom.de/eventhorizon/playground/connectivity-check/)

??? faq "All events are in `WAITING` status, what does this mean?"
    
    This indicates, that there is an open circuit for the consumer service. You can verify whether your subscription has an open circuit here: [Health status](https://developer.telekom.de/eventhorizon/playground/health/)  
    Also see [Erro-Handling/Callback](#callback) to learn more about the circuit-breaker functionality of Horizon.

??? faq "I got a lot of duplicate events. Why is that?"

    This is a known problem and is being investigated by us. Please note that with Horizon's current architecture, we cannot guarantee that an event will arrive exactly once. This means that the consumer systems may have to perform a uniqueness check themselves based on the event ID. However, duplicates should not occur frequently, an excess of duplicates is clearly an error on our side that we are analyzing.

??? faq "Some events took >3000ms. Why is that?"
    
    This can have multiple causes, for example and new release rollout of Horizon can cause delays for serveal minutes. Same applies when any of our components crash and come up again. Fortunately, this does not happen often, but it cannot be ruled out in a cloud environment. Another issue could be, that the consumer service temporarily could not be reached by Horizon - in this case multiple retries can cause a delay in the overall delivery of an event. If the bad performance persists for a longer period of time do not hesitate and [contact us](https://developer.telekom.de/docs/src/tardis_customer_handbook/horizon/#contact).

??? faq "I cannot access the events UI and connectivity check from the portal. Why is that?"

    Unfortunately the Horizon UIs are currently only accesible by EMEA1/EMEA2 accounts. ZAM account integration is planned and will come soon.

??? faq "Our event consumer cannot handle the mass of events. Is it possible to enable throttling for our subscription?"

    Currently Horizon doesn't support throttling but it's a planned feature. Unfortunately we cannot share a release date yet but we understand that this is an important feature for some of you.  
    If you are not interested in every event that reaches the consumer service you can also enable filters to reduce the mass of events.  
    See details about the filtering feature here: [Consumer side filtering](https://developer.telekom.de/docs/src/tardis_customer_handbook/horizon/#consumer-side-filtering)

??? faq "Is it possible to re-deliver certain events?"

    Currently this is not possible but this feature is something we want to address in the future, without naming a time schedule for this feature at this point. In case of emergency we can try to re-publish certain events manually, please [contact us](https://developer.telekom.de/docs/src/tardis_customer_handbook/horizon/#contact) in this case and we might help you.

??? faq "Is it possible to use an endpoint exposed on Stargate as callback URL?"

    No, this is not possible. When Horizon delivers events, the events will always pass through Stargate by using one central route configured on the gateway. Horizon always authenticates at the Gateway with its own clientId ("eventstore"). But endpoints exposed on Stargate usually check against specific consumer clientIds and not against "eventstore". Changing this would require additional security mechanisms that are not planned at this moment.

??? faq "Why does not Horizon send any `x-gateway-token` Header with the callback request?"
    By default Horizon uses "Enhanced Last Mile Security". This means you will receive only one token places in the `Authorization` header. For more information, visit: [Last Mile Security](https://developer.telekom.de/docs/src/tardis_customer_handbook/StarGate/#last-mile-security-gateway-token)

??? faq "On production the clientId claim of the Gateway token sent with the Horizon callback is 'gateway', on other environments it's 'eventstore'?"

    We are sorry, that we have this inconsistency right now. In the future we will switch to "eventstore" also on Production but we will announce this change properly when the times come so that you can change the token check logic accordingly.

??? faq "As a publisher I get a 202 response code instead of 201. Why is that?"

    Horizon responds with 202 in case the event type does not exist or there is no subscription for it. In this case Horizon ignores the event and won't keep it. Horizon's principle is to fully decouple event providers from all possible event consumers, therefore we decided to not respond with an error code in case there is noone listening.  
    However, event providers are easily able to differentiate between HTTP code 201 (event will be processed and forwarded to all consumer) and HTTP code 202 (Horizon ignores it) if they are really interested into that information.  

## Other questions

??? faq "Does gateway token validation work differently for event consumers (callback) than for API providers?"

    Yes, it's slightly different. In general you would also check expiration, signature and the issuer of the gateway token. But to ensure the maximum of security you would also need to check additional claims like publisherId, subscriberId and client ID.  
    You can read about the details here: [Receiving events via callback](https://developer.telekom.de/docs/src/tardis_customer_handbook/horizon/#via-callback)

??? faq "Are headers forwarded via Horizon?"

    Yes, in general all headers are forwarded and appended to the callback-request. However, headers that e.g. carry authentication-information are not forwarded. Below you can find a list of headers that are not forwarded:
    
    `x-spacegate-token, authorization, content-length, host, accept.*, x-forwarded.*, Cookie`
    
    Naturally, delivery via SSE does not support the propagation of headers.

??? faq "Can I integrate an external IDP for issuing a token that will be sent with th Horizon callback?"

    No, currently Horizon does not support external IDPs.

??? faq "Is there an API that can be used to retrieve the same information as the UI (EventHorizon) provides?"

    No, currently we do not provide such an API. Feel free to [contact us](https://developer.telekom.de/docs/src/tardis_customer_handbook/horizon/#contact) if you really need such an API, we would like to hear about your use-case.

??? faq "Where can I find Traces and TraceIds?"

    There are three ways to locate your Traces and TraceIds:

    1. Whenever you publish an event to Horizon, the HTTP-Response contains a header named `X-B3-TraceId`. This is the ID for the trace of your published event.
    2. After the event was published, you can find the TraceIds for specific events by looking up EventHorizon. Either click on the location/marker icon or press Details and navigate to Headers → x-b3-traceid.
    3. You can find all your traces for a specific EventType by going to MissionControl → Select your Application → EventTypes → Exposed/Subscribed and click on the location/marker icon. This will open DRAX and filter for your EventType.