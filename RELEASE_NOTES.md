# Release Notes

<!-- newest release at the top please) -->

## Prod 2018/07/17

### Ingest

#### Ingest-core
- Metadata schemas in schema.humancellatlas.org tracked and searchable under /schemas
- Find envelopes by UUID and state
- Added /submissionManifests, which track the expected number of documents in a submission
- Using jvm garbage collector to optimize release of memory back to the OS
- Fixed bug where file upload before File resource creation
- Fixed optimistic lock exceptions on add input bundle
- Bug fix for unknown staging area UUIDs
- Data File UUID
- Find Process by input Bundle UUID
- Idempotent Analysis File reference
- UUID index for Submission Envelope collection in Ingest database
- hotfix: Updated hca-ingest library to use the hca 4.1.0

#### ingest-broker
- Using the shared ingest-client libs with PyPi
- Submissions not created if there is an error parsing the spreadsheet
- Updated title page
- Using Importer V2
- Endpoint for generating a submission summary and project summary
- Simplified directory layout
- Process details support
- Submission summary
- Fix for phantom entries in Spreadsheets during import

#### ingest-exporter
- using python 3
- using shared ingest client libs

#### ingest-validator
- Non existent schemas no longer throw a critical error, instead ask user to refer to their broker

#### ingest-state-tracking
- Using persistent Redis storage for state machines
- Misc bug fixes
- Minor changes to state transition rules

#### ingest-staging-manager
- Using python 3
- Using shared ingest-libs
- Processing credentials

#### ingest-ui
- Angular Material components conversion
- Filtering metadata by state
- Display the expected count for each entity type in the metadata table
- Ability to specify page in the url in submissions dashboard
- Display of UUIDs
- User must be redirected to login page when session expires
- Fix to disappearing loading icon when doing a submission upload


### Upload Service

Remove reliance on individual IAM users for upload area access [“IAM-Not” feature](http://docs.google.com/document/d/1JFO75A9OR1gnCT1nYHH5p-vEaf0-TdOtOme3M3b9g3A/edit)

### Data Store

- Collections API added
- Distributed tracing added to API with AWS X-Ray
- Artifact fully compiled to python bytecode
- Adding retries for failed GCP requests
- Make typing declaration uniform for config variables.

### Secondary Analysis
N/A

### Data Portal
N/A


## Prod 2018/06/13

### Ingest
See https://github.com/HumanCellAtlas/ingest-kube-deployment/blob/prod-2018-06-13/prod/changelog.md

### Upload Service
Version: 1.3.1

- Upload Database
- Pgbouncer
- Return of inline checksumming
- Batch retry and definition changes
- L1 health check endpoint

### Data Store
Version: 4e9e1e52375a59bfcbddc72137a9694a1ffd6367

- Remove backlink from file to bundle
- Support for notification attachments
- The Big Red Button: Script for an emergency halt of the DSS
- Add reliable and asynchronous notifications
- Offer more content types and HTTP methods for notifications
- Add an L1 health check endpoint
- new PUT /bundle error incorrect_file_bundle_uuid
- Make email optional for checkout service API
- add API gateway metrics to dashboard

### Secondary Analysis
N/A

### Data Portal
N/A


## Staging 2018/05/31

### Ingest

See https://github.com/HumanCellAtlas/ingest-kube-deployment/blob/staging-2018-05-31/staging/changelog.md

### Upload Service
No manual steps or migrations required.
1) Inline checksumming of files
2) PGBouncer setup for transaction based db connection pooling
3) Retry for all AWS Batch API calls and db queries
4) Allow checksum daemon to respond to ObjectCreated::Copy events

### Data Store
Make notifier timeout configurable

### Secondary Analysis
Version endpoint: https://pipelines.staging.data.humancellatlas.org/version

#### Lira and subscriptions
1) Lira is now starting workflows in Cromwell-as-a-Service dev version.
2) Add options to include additional metadata fields in the notification when creating a subscription to the data store. This version now has project_shortname, sample_id and submitter_id information in the notifications.

#### Pipeline-tools
1) Added the ability to optionally record HTTP requests and responses made by pipeline-tools code.
2) Retry logic has been centralized and all retry parameters like timeout and max interval are now exposed as workflow parameters in the Smart-seq2 WDL. A timeout for individual requests has been added and exposed as a workflow parameter for Smart-seq2.
3) ConnectionErrors are now get retried. 4xx errors are no longer retried.

### Data Portal
N/a
