# Release Notes

(newest release at the top plase)

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
