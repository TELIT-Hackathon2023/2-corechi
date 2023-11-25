# Geheimschutz

[YaM Link](https://yam-united.telekom.com/pages/eni-hub/apps/blog/tardis-blog/view/51e59178-b0ab-4bf3-8c15-1e7aee413375)

## Information for API-Provider (English)

### Precondition

Precondition to bring an API to production: IRON-Demand, classification by Geheimschutz

### Requirements

Basic requirements of Geheimschutz for **DE4 K3** and **DE4 K1b**:

- [X] End-to-end Encryption:

!!! attention "Attention"
    :heavy_check_mark: Transfer-encryption is done by default by T‧AR‧D‧I‧S

    :grey_exclamation: Payload-encryption is in responsibility of the API-providers.

- [X] Encryption method:
  see Requirements Document 3.50, cryptographical algorithms and security protocols in PSA.

#### Header and URLs

!!! important
    It’s in responsibility of the API-Provider, that in header / URL no data with classification “confidential” are published!

#### Information to Approval process

IAM Requirements:

!!! info
    The IAM Requirements are also valid for machine-user.

- [X] It‘s in responsibility of each API-provider, to participate the functional data owner or his substitute in the decision if a consumer will be allowed to use the API provided!
- [X] It must be checked regularly, that the consumers still need access to the API.

----

## Informationen für API-Provider (Deutsch)

### Voraussetzung

um eine API in Produktion anzubieten: IRON-Demand, Einstufung durch Geheimschutz

### Rahmenanforderungen

Rahmenanforderungen Geheimschutz für **DE4 K3** und **DE4 K1b**:

- [X] Ende-zu-Ende-Verschlüsselung:

!!! attention "Hinweis"
    :heavy_check_mark: Die Transfer-Verschlüsselung erfolgt standardisiert über T‧AR‧D‧I‧S

    :grey_exclamation: Die Payloadverschlüsselung liegt in Verantwortung des API-Providers.

- [X] Verschlüsselungsverfahren:
  Requirementpapier 3.50, Kryptographische Algorithmen und Sicherheitsprotokolle, vgl. PSA.

#### Header und URLs

!!! important
    Es liegt in Verantwortung des API-Providers, dass über diesen Weg KEINE vertraulichen Informationen veröffentlicht werden!

#### Informationen zum Freigabeprozess

IAM Requirements:

!!! info
    Die IAM Requirements, gelten grundsätzlich auch für Machinen-User.

- [X] Es liegt in Verantwortung des API-Providers, den fachlichen Datenverantwortlichen in den Genehmigungsworkflow einzubinden!
- [X] Es ist regelmäßig zu überprüfen ob eine vergebene Berechtigung weiterhin benötigt wird.

## Cloud Security

### Wer braucht eine BIA. Wer braucht eine TIA? Und Warun?

Under following link you can find information about BIA and TIA: https://yam-united.telekom.com/pages/src-dt-it/apps/content/src-bia-tia

!!! Note
    Please use our [Support channel](/docs/src/tardis_customer_handbook/support/) to address your Question - we will do our best to help you.

## What Data can be stored in Cloud?

The is a "tool" (German only) that will help you to understand if your data could be stored in Cloud or not. Please visit [YAM - GEO oder VS-NfD-Daten & Cloud…geht das?](https://yam-united.telekom.com/pages/src-dt-it/apps/blog/blog/view/2f1db1a2-11fd-45df-b091-a6cf6b5226b7)

!!! Note
    Please use our [Support channel](/docs/src/tardis_customer_handbook/support/) to address your Question - we will do our best to help you.
