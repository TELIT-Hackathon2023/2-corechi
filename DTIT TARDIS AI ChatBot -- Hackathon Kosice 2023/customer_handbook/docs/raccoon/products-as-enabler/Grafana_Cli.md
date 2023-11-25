# Grafana-Cli

Team Skoll created a golang cli tool for managing dashboards and more in Grafana via console or CI/CD Pipeline. 

Documentation describes current version:   **v1.3.0**

In case of issues or feature requests don´t hesitate to [contact us](../../support/README.md#tardis-monitoring-support-channel).

## Usage

The cli tools has the following configuration options

| Option        | Description                                                           | Default |
|---------------|-----------------------------------------------------------------------|---------|
| `--log-level` | Logging level (0=Panic, 1=Error, 2=Warning, 3=Info, 4=Debug, 5=Trace) | `3`     |
| `--action`    | Action (`apply`, `delete`)                                            | `apply` |
| `--overwrite` | Overwrite existing configurations in Grafana                          | `false` |
| `--config`    | Path and file name of the configuration file                          |         |

## Configuration file

The configuration file has to be in YAML format and consists of these sections:

* Destinations
* Dashboards
* AlertRules
* Users
* Teams
* Folders

### Destinations

The destinations section gets configurations of the Grafana instances. 
The following parameters are necessary for every array element:

```yaml
- name: my-target-grafana-instance
  url: https://my-target-grafana-instance.telekom.de
  authToken: <my-grafana-auth-token>
  folderUid: K2yLFroVk    # optional, overwrite target folder
```

The target folder and auth token need to be created in the target grafana instance first. 
Permissions as organization admin are necessary for the auth token.

The name is used to refer from the other sections. 

### Dashboards

In the dashboards section you can configure sources of type 'file' or type 'grafana' 

#### Type: file

Load a dashboard from a local file. 

Mandatory fields:

* path

example: 
```yaml
dashboards:
  - type: file
    path: ./my-dashboard.json
    destinations:
      - my-target-grafana-instance
```

#### Type: grafana

Migrate a dashboard from a grafana instance

Mandatory fields:

* endpoint
* uid

example: 
```yaml
dashboards:
  - type: grafana
    endpoint: my-source-grafana-instance
    uid: <uid-of-source-dashboard>
    destinations:
      - my-target-grafana-instance
```

Multipe array entries with mixed types are possible.

Like the destinations the endpoint refers to a configured destination in the [destinations section](#destinations).

### AlertRules

In the alertRules section you can configure source files to load alert rules from.

#### Type: file

Load an alertRule from a local file

Mandatory fields:

* path

example: 
```yaml
alertRules:
  - type: file
    path: ./my-alertRule.json
    destinations:
      - my-target-grafana-instance
```

Multipe array entries are possible.

The destinations refer to a configured destination in the [destinations section](#destinations).

### Users

In the users section you can manage users with their roles in the organization. 
Prerequisite is the user is initialized in Grafana (initial login). 
After Grafana knows the user, the user can be invited to Grafana.

example:
```yaml
users:
  - destination: my-target-grafana-instance
    list:
      - email: max-muster@telekom.de
        role: Viewer
```

#### Roles

Allowed roles are `Viewer`, `Editor` and `Admin`.
To change existing roles, you´ll have to set `--overwrite=true`.

### Teams

If a user is managed in your organization, you´ll be able to add that user to a team.
In the teams section you´ll be able to create a team and add users to it.

example:
```yaml
teams:
  - destination: my-target-grafana-instance
    list:
      - name: my-new-team
        email: my-team-email@telekom.de
        members:
          - email: max-muster@telekom.de
          - email: jane-doe@telekom.de 
```

### Folders

Folders are the place where you store your dashboards and folders can be used to enable teams for private workspaces.
Users, teams and roles are entities how can get permissions to folders. The permissions are equal to the roles on the organization level
(`Viewer`, `Editor` and `Admin`). To manage permissions you´ll have to configure the entity as `type`, 
related to the type the user name, team name oder role name as `for` and role you want to give as `role`.

example:
```yaml
folders:
  - destination: my-target-grafana-instance
    list:
      - name: my-folder-name
        permissions:
          - type: user
            for: max-muster@telekom.de
            role: Admin
          - type: team
            for: my-new-team
            role: Editor
          - type: role
            for: Editor # All editors in the organization get only Viewer rights for that folder
            role: Viewer
          - type: role
            for: Viewer
            role: None # this is no official role in Grafana but will be used to remove the rights of an entity
```


## Use the Grafana-Cli in the CI/CD pipeline

The grafana-cli can be used in a CI/CD pipeline. The images are published in the MTR.

Use the same DOCKER_AUTH_CONFIG like for [Rover](../../rover/README.md#pull-rover-docker-image).

### Example

#### .gitlab-ci.yml

```yaml
variables:
  DOCKER_AUTH_CONFIG: $DOCKER_AUTH_CONFIG_TARDIS_CUSTOMER
  GRAFANA_CLI_IMAGE: $MTR_DEVOPS_REGISTRY/tardis-customer/grafana-cli:v1.1.0
  LOG_LEVEL: 3
 
stages:
  - apply
  - delete
 
.base:
  image: $GRAFANA_CLI_IMAGE
  tags:
    - run01_docker
  when: manual
 
.translateVarsInCfgFile: &translateVarsInCfgFile |
  echo 'cat << EOF' > ${CFG_FILE}.tmp
  cat $CFG_FILE >> ${CFG_FILE}.tmp
  echo '' >> ${CFG_FILE}.tmp
  echo 'EOF' >> ${CFG_FILE}.tmp
  . ${CFG_FILE}.tmp > tr_${CFG_FILE}
  rm ${CFG_FILE}.tmp
 
ApplyDashboards:
  extends: .base
  stage: apply
  variables:
    CFG_FILE: cfg.yaml
  script:
    - *translateVarsInCfgFile
    - grafana-cli --log-level=$LOG_LEVEL --config=tr_${CFG_FILE}
 
DeleteDashboards:
  extends: .base
  stage: delete
  variables:
    CFG_FILE: cfg.yaml
  script:
    - *translateVarsInCfgFile
    - grafana-cli --action=delete --log-level=$LOG_LEVEL --config=tr_${CFG_FILE}
```

#### cfg.yaml

````yaml
destinations
  - name: my-target-grafana-instance
    url: https://my-target-grafana-instance.telekom.de
    authToken: $AUTH_TOKEN_FROM_CI_CD_VARIABLE
    folderUid: K2yLFroVk    # optional, overwrite target folder 
dashboards:
  - type: file
    path: ./my-first-dashboard.json
    destinations:
      - my-target-grafana-instance
````

#### my-first-dashboard.json

```yaml
{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "grafana",
          "uid": "-- Grafana --"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "target": {
          "limit": 100,
          "matchAny": false,
          "tags": [],
          "type": "dashboard"
        },
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": 1,
  "links": [],
  "liveNow": false,
  "panels": [],
  "schemaVersion": 37,
  "style": "dark",
  "tags": [],
  "templating": {
    "list": []
  },
  "time": {
    "from": "now-6h",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "",
  "title": "my-first-dashboard",
  "uid": "ABCdefGHI",
  "version": 1,
  "weekStart": ""
}
```