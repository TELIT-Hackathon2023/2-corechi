# Postman Collection for Chevron-API on *playground* environment

This folder contains a Postman collection showing how to use the Chevron API.

Download: [ChevronDemo.postman_collection.json](ChevronDemo.postman_collection.json)

To use this collection in the *playground* environment following environment variables should be configured in Postman:

| variable        | value                                                           | comment                                               | 
|-----------------|-----------------------------------------------------------------|-------------------------------------------------------| 
| irisBrokerHost  | https://iris-broker-playground.live.dhei.telekom.de             | *used for issuing an id-token*                        |
| irisBrokerRealm | user-idp                                                        |                                                       |
| irisHost        | https://iris-playground.live.dhei.telekom.de                    | *used for authentication with subscribed Chevron API* |
| clientId        | eni--io--chevron-demo                                                             | *see MissionControl->Application details*             |
| clientSecret    | *****                                                             | *see MissionControl->Application details*             |
| chevronApiUrl   | https://stargate-playground.live.dhei.telekom.de/eni/chevron/v2 |                                                       | 
| application     | eni--io--chevron-demo                                           | *your unique application identifier (can be found in MissionControl->Application details)*                                                                                                                                   |

You can view and change the collection-scoped variables by clicking the button with the three dots at your collection and chosing "Edit".  
Note, that these variables will overwrite environment variables.

