# Release Notes

## Staging 2018/07/25

### Ingest
No Changes

### Upload Service
- Api endpoint to check validation statuses
- Scripts to schedule and retrieve validation statuses
- Fix to upload area sync and create scripts to account for new credentials format

### Data Portal
No Changes

### Data Store
No Changes

### Secondary Analysis
Pipeline-tools:
- Respect Retry-After headers when following redirects
- Submit real md5 checksums along with pipeline outputs
- Make submission tasks idempotent


## Staging 2018/07/11

### Ingest

Ingest Core
- Data File UUID
- Find Process by input Bundle UUID
- Idempotent Analysis File reference
- UUID index for Submission Envelope collection in Ingest database

Ingest Broker
- Process details support
- Submission summary
- Fix for phantom entries in Spreadsheets during import

Staging Manager
- Processing credentials

State Tracking
- Minor changes to state transition rules


### Upload Service

Remove reliance on individual IAM users for upload area access (“IAM-Not” feature).


### Data Store

- checkout functionality is now in `GET /v1/bundles`
- collections API
- internal changes resulting from scale testing


### Secondary Analysis

Lira:
- Increase Lira deployment replicas
- Make the Gunicorn parameter more portable
- Update dependencies' version and refactor the version endpoint
- Exclude results bundles in subscription query

Pipeline-tools:
- Update to use v4 hca cli
- Restrict dependencies to a single major version
- Add logging related to http request retries
- Fix bug in parsing analysis workflow id from Cromwell metadata



## Staging 2018/06/28

### Ingest

ingest-core
- metadata schemas in schema.humancellatlas.org tracked and searchable under /schemas
- find envelopes by UUID and state
- added /submissionManifests, which track the expected number of documents in a submission
- using jvm garbage collector to optimize release of memory back to the OS
- fixed bug where file upload before File resource creation resulted in discrepent submission UX
- fixed optimistic lock exceptions on add input bundle
- bug fix for unknown staging area UUIDs

ingest-broker
- using the shared ingest-client libs with PyPi
- submissions not created if there is an error parsing the spreadsheet
- updated title page
- using Importer V2
- endpoint for generating a submission summary and project summary
- simplified directory layout

ingest-exporter
- using python 3
- using shared ingest client libs

ingest-validator
- non existent schemas no longer throw a critical error, instead ask user to refer to their broker

ingest-state-tracking
- using persistent Redis storage for state machines
- misc bug fixes


ingest-staging-manager
- using python 3
- using shared ingest-libs


### Upload Service
No changes

### Data Store
No changes

### Secondary Analysis
Version endpoint: https://pipelines.staging.data.humancellatlas.org/version
Lira and subscriptions
1) Scalability and stability Improvements:
    - Increasing the number of Gunicorn workers.
    - Increasing the timeout and graceful timeout of Gunicorn workers.
    - Replacing the sync workers with gevent workers.
2) Adds the option to include additional metadata in notifications to the utility script when it is making subscriptions.
3) Enables Lira to on hold workflows when it is submitting to Cromwell.
4) Add "v6" subscription queries for SmartSeq2 and 10x data
5) Include the fields in notification metadata attachments as workflow labels
6) Set max_cromwell_retries in workflow inputs (defaults to 0)
7) Support HMAC auth for notifications
8) Fix url for registering service account in FireCloud.
9) Move dss_url, ingest_url and Cromwell-as-a-Service params into Lira config for greater flexibility.
10) Hard code kubernetes cluster name to "listener" in lira-deploy Jenkins job to prevent error when multiple clusters are present.
11) Require both user and password when not using Cromwell-as-a-Service
Improve instructions for updating a certificate
12) Update subscriptions to use v1.0.0 Pipeline for all SmartSeq2 data.


Pipeline-tools
1) The Python codes in adapter workflows are not using buffering anymore, so the stdout won't run into some intermittent-empty problems.
2) The stub submit workflow now uses a slim version of Python docker image for efficiency.
3) All the requests to Ingest now will retry on ReadTimeout exception by default, in case Ingest is unavailable.
4) Submit workflow now has separate and sorted stage_files and confirm_submission tasks, this decoupled structure helps debugging and workflow management.
5) Some documentation style fixes.
6) Pass Cromwell automated retries parameter to analysis wdl
7) Add support for changes to the latest HCA metadata schema:
    - Update the analysis json file to follow the "process" to "protocol" schema changes
    - Update getting the sample id from links_json
8) Fix stub submission wdl to include analysis_file_version parameter


Cromwell-tools
1) Add on_hold parameter to start_workflow

### Data Portal
N/a
