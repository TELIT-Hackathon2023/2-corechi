# Horizon PoC zone

!!! attention "PoC zone currently is only available on demand"
   
      In order to save ressources we decided to shutdown the PoC zone and only make it available to customers either on demand or when we can offer a new experimental Horizon release and need early feedback. Please contact Horizon's PO [Mike Herwig](mailto:mike.herwig@telekom.de) if you wish to evaluate new ideas in form of a prototype together with us within a dedicated environment.

## What is the PoC zone?

We created a new T‧AR‧D‧I‧S zone "poc" for customers who are willing to participate in Horizon friendly user tests where they can try out early builds of new Horizon releases in a non-productive manner.  
We created a complete new and separated zone so that we are able to experiment with major changes changes to the architecture or the general behavior of Horizon components without disrupting the daily business.
Your participation helps us to shape the future of Horizon.

## Why does it exist?

Event publishers and consumers configured in the PoC zone will be able to try new prototype features or whole experimental releases of Horizon and give early feedback.  
Your feedback is valuable to us and will help us heading in the right direction - sooner or later Horizon versions tested in the PoC zone will also be rolled out to your familiar TARDIS zones and environments.

## Limitations

**Production-like availability and operability**  
In the PoC zone Horizon might be temporarily unavailable or things might break. It's not production-ready.  
We will frequently update Horizon in this zone and might experiment with things that we will revert later again.

**Retention**  
We plan to experiment with data retention in this zone and might change the current default configuration of keeping events for 7 days. We even consider to do wipes of the whole data if necessary.

**Extensive support**  
The PoC zone is considered as experimental, therefore solving customer problems in this zone has a lower priority. Please reach out to us directly instead of creating a ticket if you face issues while using the PoC zone.

**Feature completeness**  
Horizon in the PoC zone currently comes with some limitations. See below.

## Feature limitations

- PoC zone is only available on PreProduction environment
- PoC Horizon is located in AWS only
- No Horizon user interface (EventHorizon) support
- No Horizon Grafana dashboard support
- No ticket support

## How to use the PoC zone?

Just change the zone in your rover configuration to "poc". It's as simple as that. But be aware that this is only possible in a preproduction environment.

Example event provider configuration:

```yaml
apiVersion: tcp.ei.telekom.de/v1
kind: Rover
metadata:
  name: foo
spec:
  zone: poc
  exposures:
    - eventType: example.event.v1
```

And for the consumer:

```yaml
apiVersion: tcp.ei.telekom.de/v1
kind: Rover
metadata:
  name: bar
spec:
  zone: poc
  subscriptions:
    - eventType: example.event.v1
      deliveryType: callback
      payloadType: data
      callback: https://example-consumer.telekom.de/example-event-callback
```

When you successfully applied the configuration you will find the new connection details in MissionControl as usual.


*Note:  
Even if the consumer is not located in the poc zone, it still would automatically participate in the friendly user test when the event publisher is located in the poc zone.  
Therefore the consumer could also be in the caas zone and is still able to try the new Horizon. This is because events are always processed and handled on the publisher side and will be delivered through gateway mesh routing of T‧AR‧D‧I‧S*

## Contact

Please contact Horizon's PO [Mike Herwig](mailto:mike.herwig@telekom.de) for further questions or if you want to share some ideas!
