# Legacy Alerting

Legacy alerting is based on Grafana 8 with alerts and notification channels as configuration objects.

## Alert definition

The alert-definition is based on queries and can be configured in the following way:

<img src="../../img/Grafana_Alert.png" width="700px"/>

* every query returns a value for each timestamp, usually by scraping metric-endpoints every 15s (the green dots)
* the query is evaluated every 1 minute (14:39 until 14:47)
* an alert is triggered, if the condition matches for 3 consecutive minutes (pending state from 14:44 until 14:47)
* the Condition is based on the 5 minutes average of the query, reaching a level above 90 (the red and green areas)

So for 14:44 - 14:47, the average of the last 5min (14:39-14:44 to 14:42-14:47) needs to be above 90 to trigger the alert.

You can simplify the time-ranges, by e.g. using `For 0m` or using the `last` value instead of a ranged average.


#### Resulting Alert

To send alerts to external components, you have to create a notification channel in Grafana.
For [CEIS](https://ceis.telekom.de/) as well as Webex, you need to configure a matching notification channel of type **webhook** with http method **POST**.


The following parameters are pre-defined by a Grafana-alert:

| attribute     | description                   |
|---------------|-------------------------------|
| `title`       | title of alert                |
| `ruleId`      | id of alert-rule              |
| `ruleName`    | name of alert-rule            |
| `state`       | state of alert: `alerting/ok` |
| `orgId`       | orgId of the alert            |
| `dashboardId` | dashboardId of the alert      |
| `panelId`     | panelId of the alert          |
| `ruleUrl`     | url to the alert in grafana   |


On a firing alert, Grafana sends webhook alerts in a json format - here is an example:

```
{
  "title": "[Alerting] Test notification",
  "ruleId": 12345678901234567890,
  "ruleName": "Test notification",
  "state": "alerting",
  "evalMatches": [
    {
      "value": 100,
      "metric": "High value",
      "tags": null
    },
    {
      "value": 200,
      "metric": "Higher Value",
      "tags": null
    }
  ],
  "orgId": 0,
  "dashboardId": 1,
  "panelId": 1,
  "tags": {},
  "ruleUrl": "https://grafana.local.de/",
  "message": "Someone is testing the alert notification within Grafana."
}
```

#### Test Alerts

You can test your alerts via pause and resume in the Alert rules overview.

<img src="../../img/Grafana_PauseResumeAlert.png" width="400px"/>


### Use CEIS for alerting

The CEIS description you´ll find [here](https://ceis.telekom.de/).

CEIS connects all events to a specific application which has to be managed in [Darwin](https://darwin.telekom.de/).
The Darwin application name is required in the `ApplName` parameter.
For authentication you´ll need the `AuthenticationKey`.
This key you´ll get at [Pacman](https://pacman.telekom.de/asap/public/#/ceis) if you have the 'Technical Approver' role in your application in Darwin at the section 'Contacts'.

In the alert column of a time series panel you´re only able to fill the message and tags which will be transferred to the corresponding fields in the json.
<img src="../../img/Grafana_alert_column.png" width="700px"/>

CEIS expects all parameters in the top level of that json event or is able to read from the http parameters.
Additionally you can tell CEIS to use a key in lower levels of the json event.

So to handle all the fields which CEIS accepts you need to set everything except the message in the http parameters. Here an example:
```
https://ceis.telekom.de/ceis.php?
eventtype=EMAIL
&ApplName=myDarwinApplication
&AuthenticationKey=123456789012345678901234567890
&SystemName=%40SysName%40
&SendTo=%40MailTo%40
&InstName=%40InstanceName%40%23%40state%40
&Subject=%5BTEST%5D%20%40title%40
```

In the example above we tell CEIS to send an e-mail. We´ve set `ApplName` and `AuthenticationKey` directly in the http parameters and related further parameter to tag key names.
We tell CEIS to search for a key `SysName` in the event and use the value of that key in the parameter `SystemName`.
The same we do for

* `SendTo` -> `MailTo`,
* `InstName` -> `InstanceName` + `state`
* `Subject`-> `'[TEST]'` + `title`.

All relations need to be bracketed with '@' signs and the whole url needs to be encoded.
Now I´m able to set the related keys as tags in the alert column of a time series panel.
<img src="../../img/Grafana_alert_column_filled.png" width="700px"/>


### Use Webex for alerting

On a firing alert, Grafana sends the json-alert + Webex-parameter to a webex-alert-pod, which runs next to each Grafana.
The webex-alert-pod then parses the message and uses the webex-api to send a markdown message to the given Webex-Room.

<img src="../../img/Webex_AlertArch.png" width="700px"/>

You can find a more detailed description and it's implementation in [gitlab](https://gitlab.devops.telekom.de/dhei/teams/skoll/images/webex-alert).

#### Prepare Webex bot and room

Currently, you need to create a personalized webex-bot, based on your ADFS login:


1) login via telekom.de-ADFS at [developer.webex.com](https://developer.webex.com/)

2) [create a new bot](https://developer.webex.com/my-apps/new/bot)

3) note it's username and token


Invite the bot via it's username to the webex-room, where the bot should send alerts to.

Get the Webex RoomId for this room via the [webex-room-api](https://developer.webex.com/docs/api/v1/rooms/list-rooms):


1) run the query with the pre-filled Bearer token

2) search in the response for your room-name and note the id of the room


#### Prepare Grafana notification channel

In your Grafana organization, create a new Notification channel below Alerting - Notification channels:

<img src="../../img/GrafanaWebexNotificationChannel.png" width="600px"/>

You need to configure a Notification channel of type webhook:

* the Url consists of multiple parts:

    1) `http://guardians-raccoon-webex-alert:8080/alert` - local service of the webex-alert-api next to Raccoon-Grafana, which creates an webex-alert out of an grafana-alert

    2) `?Stage=Prod&webexroomid=A123...` - url parameter, which will be set in the webex-alert, e.g. Stage and default-WebexRoomId

* insert the Webex-Bot-Token as Password in the Optional Webhook settings, together with an not-empty Username


#### Create Webex Alert

The Webex-alert needs different parameters to send a message to Webex:

* WebexRoomId - the room where a message is sent to
* ParserMode - currently `Debug` or `Markdown` or `Default` are supported
* WebexToken - only supported via Webhook-Password


##### Parameters
The static parameters can be used in the alert message via `@ruleName@`.

Dynamic parameters can be defined via 3 different ways

* as url-Query-parameter at the NotificationChannel, e.g. Stage value: `http://guardians-raccoon-webex-alert:8080/alert?Stage=Prod`
* as Tags in the Alert, e.g. a Tag `WebexRoomId` with its correct value
* as inline-values in the alert-Message, e.g. `@WebexRoomId := ABC123@`

The dynamic parameters can be used via `@Key@` (e.g. Stage) in the message of the alert, similar to static parameters
  ```
  ## @state@ on @Stage@: [@ruleName@](@ruleUrl@)
  ```

You can also define default-values for dynamic parameters in the notification channel url via a key in lowercase.
This default-value will be used, when the case-sensitive key is not present,

e.g. `webexroomid=123` in the Url as default, which can be overridden in each alert via the Tag `WebexRoomId`.

##### Modes

###### Debug Mode
You can analyse the result of your alert-query via the Debug mode, which contains:


* the query-parameter given by the NotificationChannel-configuration
* the json-alert from grafana

<img src="../../img/Webex_DebugAlert.png" width="700px"/>

###### Default Mode
The default mode ignores your configured alert message (so it can be added to any existing alert).
It contains:

```
## @state@ on @Stage@: [@ruleName@](@ruleUrl@)
@{evalMatches}[*]@
```

<img src="../../img/Webex_DefaultAlert.png" width="700px"/>

###### Markdown Mode
The Markdown mode uses your configured alert message and replaces the placeholders within the message.
Following are 2 examples for its usage.
If you want to know more [contact us](mailto:dtit_eni_hub_team_skoll@telekom.de?subject=RaaS%3A%20Question%20regarding%20alerting)
or have a look at it's [implementation](https://gitlab.devops.telekom.de/dhei/teams/skoll/images/webex-alert).


#### Simple Example

##### Query and graph

<img src="../../img/Webex_SimpleQuery.png" width="700px"/>

##### Alert

<img src="../../img/Webex_SimpleAlert.png" width="700px"/>

The alert is evaluated every 1 minute and it's condition needs to be fulfilled for 5 minutes.
The alert fires, if the query average through 5 minutes is below 11 (so if less than 11 kong-containers are up).


If the alert fires, it notifies the Webex notification channel, with the message:

```
## @state@ on @Stage@: [@ruleName@](@ruleUrl@)
On the following clusters less than 11 kong-container are running:
@{evalMatches}[*]@
```

The 2 Tags on the alert provide the `WebexRoomId` for this alert and the `ParserMode`,
so the message is used and line-breaks are interpreted as seen.


##### Resulting Alert

<img src="../../img/Webex_SimpleResult.png" width="700px"/>

#### Example for advanced formatting

The T‧AR‧D‧I‧S Blame Bot channel is filled via 2 periodical alerts.
To send period alerts, you have to enable `Send reminders` in the Notification channel and set a duration.
Be careful with this setting, or you will be spammed.


Here is the alert message for the `Stargate Failure rate alert` based on 3 queries.

The Alert is configured with the following message:

```
## @state@ on @Stage@: [@ruleName@](@ruleUrl@)
The following routes had a failure rate above 10% within the last hour:
@{evalMatches}[*{consumer, route}]  - `{consumer}` using `{route}`: {value[0]#%.f}% = {value[1]#%.f} / {value[2]#%.f}@
```

It produces this markdown-message in the Webex T‧AR‧D‧I‧S Blame Bot room:

<img src="../../img/Webex_TardisBlameBot.png" width="700px"/>