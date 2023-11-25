# Maverick FAQ

## Who is creating Developer Portal?

### Who are you and how can I contact you?

We are the Atlas Team from the T‧AR‧D‧I‧S Please contact us via E-Mail or GARD Link [you can find in here](/docs/src/tardis_customer_handbook/support/).

### I have cool Idea or feedback, where to put it?

Simply give us feedback.

### I found a bug, how to report it?

Please open a GARD ticket via E-Mail: [fmb_tardis_support@telekom.de](mailto:fmb_tardis_support@telekom.de?subject=DevPortal%20-%20it%20seems%20I%20found%20a%20bug), or you can use [Support Section](/docs/src/tardis_customer_handbook/support/).

----

## How to use Developer Portal

### Who can use Developer Portal?

All internal employees + external colleagues with ZAM account can use Developer Portal from the **intranet** and **internet**.

### Can I open Developer Portal from the internet?

YES! For some functionalities you have to login yourself, but common parts are open for you.

### I use Edge or Internet Explorer and cannot see anything?

We are small teams and focused on limited Browser’s portfolio to support. We do not support IE and Edge, but Firefox and Chrome instead. You can order in [myIT](https://myit.telekom.de/MyIT/).

### It is not easy to use your portal from the Mobile Phone

We know, sorry for that. As mentioned before, we do support mostly Desktops with Firefox or Chrome Browsers. We are working on update here.

### What is Maverick?

Maverick is our Developer Portal, you are visiting it now.

### How to use permanent link to an API?

If you share the link with colleagues that contains exact version, and this version will be updated. Do not worry about we will do our best and find actual API version for you, so shared links are never get broken again.

### How frequently are you syncing data? My API still not in Catalog.

On a **Production** do we have webhooks solution, that enable us with a few seconds react time.
Due to the Security Restrictions (calling from Test Prod ENVs) this Solution is currently does not work for Preprod and PlayGround environments. Here we do have only 1 sync per day at the nighttime, but we are working on a better solution now.

## How to remove my old API or OAS only from the Portal

We are fully synchronized with a Rover, so you must use it to manage your APIs.

Depends on if you have registered API with `rover.yaml`, or only did [OAS upload](/docs/src/tardis_customer_handbook/rover/#step-1-upload-open-api-specification) 2 command could help you:

```shell
roverctl delete -f <absolute-path to rover.yaml/>
```

OR

```shell
roverctl delete -f <absolute-path to api specification file/>
```

Read more in [T‧AR‧D‧I‧S Customer Handbook](/docs/src/tardis_customer_handbook/rover/#clearing).

## If I upload different OAS, what you will show?

We will synchronize all Environments and parse latest one OAS for API Name and API Description. In this case LIFO method been used, API name and API description will be taken from the latest uploaded OAS regardless of the Environment.
This gives your opportunity to quickly make corrections to description, or even rename API without uploading all the Specifications.

Of course, if your latest upload was with the wrong API Name or API description it will be taken too. This can’t be predicted by us.

## I still have a Question

!!! Note
    Please use our [Support channel](/docs/src/tardis_customer_handbook/support/) to address your Question - we will do our best to help you.

## Can I add Diagram or Markdown to the swagger file

Yes you can! Use [PlantUML](https://plantuml.devops.telekom.de/) from the Magenta CICD to add it as an image, we do support basic markdown there. Try following code in our [Swagger editor](https://developer.telekom.de/swagger-editor) or click on
 [![](https://shields.devops.telekom.de/badge/-TRY%20ME-blue)](https://developer.telekom.de/swagger-editor/?url=https://developer.telekom.de/docs/src/tardis_faqs/markdown-oas-example.yml):

```yaml
openapi: "3.0.0"
info:
  title: "My Cool API"
  version: "1.0.0"
  x-api-category: "SYSTEM"
  description: "# This is header 1
  
  ## This is Header 2
  
  ![My cool Diagram](https://plantuml.devops.telekom.de/svg/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000)
  
  
  Some description to my cool diagram.
  
  ## Some Header 3
  
  - Of course some list
  
  - With 2 options
  
  
  My Links to [the git](https://gitlab.devops.telekom.de/)
  
  My **Bold** or any *other fomrated* _text_.
  
  ### Lets make diagram clickable
  
  Read more under [Markdown examples](https://developer.telekom.de/docs/src/developer_portal_howtos/examples/examples/#zoomable-images). Now use can zoom in by clicking on diagram.
  
  [![My cool Diagram](https://plantuml.devops.telekom.de/svg/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000)](https://plantuml.devops.telekom.de/svg/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000)"
```
