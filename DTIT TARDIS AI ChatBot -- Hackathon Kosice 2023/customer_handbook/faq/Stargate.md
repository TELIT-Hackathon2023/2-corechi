# Stargate FAQ

## Do I need to provide certificates towards StarGate?

No, the communication is secured with OIDC. The communication channel is secure via TLS (HTTPS).
There is no certificate-based security supported on T‧AR‧D‧I‧S Please refer [API Security](/docs/src/tardis_customer_handbook/APISecurity/) section for more details.

## Is TLS supported on the StarGate?

Yes, TLS (HTTPS) is supported. Please note there is no support for mTLS on StarGate.
Application connecting to StarGate needs to implement OIDC protocol at their end.

## Which ZONE should I expose my APIs to?

Select the nearest StarGate available to your application.
Which means, if your application runs on AppAgile, OTC, Hitnet, Baremetal in Bierre, then you need to use **CAAS** as their nearest zone.
Otherwise, if you are running on AWS, then use **AWS** as zone in `Rover.yaml`.

## How to connect from internet?

For this scenario we offer the Spacegate which supports both directions. Either the inbound connection offering a DT API for an external consumer or consuming an externally provided API as a DT consumer.
For more information take a look into the [Spacegate documentation](/docs/src/tardis_customer_handbook/StarGate/Spacegate/).

## Where do I find the SST Templates?

!!! info "Not here."

For the purpose of consuming and providing an API on T‧AR‧D‧I‧S there is no interface agreement/ "Schnittstellenvereinbarung" (SST) mandated by us.
Any and all such agreements are bilateral between providers and consumers, this is also why providers always have to approve Consumers.

Whether the Consumer chooses to require a mandatory SST document in parallel is a decision left to the provider alone.

## I still have a Question

!!! Note
    Please use our [Support channel](/docs/src/tardis_customer_handbook/support/) to address your Question - we will do our best to help you.
