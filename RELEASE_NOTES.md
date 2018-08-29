# Release Notes

## Staging 2018/08/29

### Ingest

Ingest Core

- Fixed bug when adding input bundle manifests for restructured bundles to processes.
- Added Submission Error entity and endpoints
- State tracker optimizations
- Core messaging optimizations
- Added DRAFT transition controller methods for each metadata resource
- Fixed schemas endpoint to correctly fetch latest schema
- Addressed concurrency issues when sending messages in the core 
- Modified schema parser to use URI directly.
- Set script to assemble package when running locally
- Added SCHEMA_BASE_URI in docker compose script
- Added triggersAnalysis flag in submission envelope
- Replaced embedded web server to improve stability
- Point schema url to s3 bucket url to get the xml file
- Replaced embedded Tomcat server with Jetty
- Set up to enable performance testing

Ingest Broker

- Handling schema /system links during spreadsheet upload
- Upgraded dependencies for hca-ingest module
- Using hca-ingest v0.5
- Fix bug in Schema template api to point to correct schema environment

Staging Manager

- Now waits for  for Ingest Core to come online before consuming messages

Exporter

- Using latest version of input data files in secondary bundle export
- Bundles now contain supplementary files
- Using latest version of links.json schema
- Respecting the “triggerAnalysis” flag on envelopes to toggle triggering of analysis on primary submissions
- Bundle restructure
- Fixed bug when fetching documents from ingest-core
- Remove hca dependency on the exporter listener and use the ingest-client version which uses hca v0.5

### Upload Service

No updates due to an out of band promotion last week.

### Data Store

- Removed dss-chalice script
- Refreshed all requirements. (#1476) Tue Aug 7 10:36:41 2018 -0700
- Explicitly catch a malformed version error for PATCH /collections (#1485)
- Supporting new bundle layout (#1469)
- Changed illegal version to a 400 response (#1483)
- Also changed missing file in a bundle to a 400 response not a 409.
- Bumped cryptography lib to 2.3 (#1466) to resolve  https://nvd.nist.gov/vuln/detail/CVE-2018-10903
- Add Index Design and search limitations documentation (#1461)
- Reject bundles containing duplicate file names (#1454)
- Fixed bug preventing the upload of files 64MB in size  (#1456)
- Admin repair's default is to not send notifications (#1450)
- Promote to integration immediately given CI status (#1437)
- Add DSS HTTP client best practices docs (#1419)
- Add roles/cloudfunctions.developer to gcp service account (#1431)
- Add missing 301 response to GET /v1/bundles/{uuid} swagger (#1418)
- Update README.md deployment instructions (#1413)
- Shorten the expiration on the dev checkout bucket (#1405)
- Prunes incomplete multipart uploads.
- Version mandatory for PUT Files and Bundles (#1390)
- Added CI-CD Deployment scripting for GitLab (#1388)
- Allow Terra Form to work with assumed roles (#1392)
- Moving badges to the top of readme (#1382)

### Secondary Analysis

Falcon

- V0.1.0 (This release is the first iter tion of this new service):
    - Implement the queue-handler component of the Falcon.
    - Implement the igniter component of the Falcon.
    - Initialize the Falcon repository with config files, readme, and dockerfile.
    - Add Quay.io docker image build status badge.
    - Add kubernetes YAML file and corresponding deploy script for Falcon.
    - Add Travis CI build status badge to the readme :)
    - Add config file for Travis CI.
    - Add test coverage report to the pytest outputs.
    - Implement unit test cases for the queue_handler component.
    - Implement unit test cases for the igniter component.
    - Add and use mock data for testing.
    - Implement unit test cases for the settings module.
    - Implement the basic unit tests and a Cromwell simulator for testing purposes.
    - Implement the settings helper function and the main function for Falcon.
    - Implement the queue-handler component of the Falcon.
    - Implement the igniter component of the Falcon.
- v0.1.1:
    - Fixes an issue with the deployment YAML template file, which causes a validation error during the deployment process.
    - Fixes an issue with the deploy script, which throws warnings if certain input parameters are missing.
- v0.1.2:
    - Fix a bug with the settings loader which can potentially prevent falcon from accessing to Cromwell-as-a-Service

Lira and subscriptions

- Update the subscription query so it matches the latest HCA metadata schema.
- Update the subscription metadata attachment query, so it matches the latest HCA metadata schema.
- Extend the `lira_utils` so both `schema_url` and `cromwell_url` are configurable and controlled by lira config, which are input parameters to adapter workflows.
- Refactor the Jenkins deploy script of Lira so the Kubernetes cluster name is configurable now.

Pipeline-tools

- v0.24.0:
    - Add `schema_url` parameter to configure with HCA metadata schemas to use when constructing the analysis JSON
- v0.25.0:
    - [Breaking Change] Update to the latest HCA metadata-schema:
        - `analysis_json` now is split into `analysis_process` and `analysis_protocol`, the former varies between runs, while the latter remains almost static given a specific version of the analysis pipeline.
        - Link `analysis_protocol` to `analysis_process` during the process of creating the submission envelope.
        - Update the testing data.
        - Update both SmartSeq2 and Optimus adapter workflows accordingly.
    - [Breaking Change] Update to the latest Bundle structure proposed by Ingest service, which breaks metadata file into smaller separate files.
    - [Breaking Change] Migrate to use the centralized `metadata-api` library to prepare inputs for SmartSeq2 pipeline. 
    - [Breaking Change] Migrate to Python3 and drop support for Python 2.x, update the dockerfile accordingly.
    - Migrate from unittest to pytest throughout the code base, update most of the testing cases, introduce a set of new testing fixtures.
    - Remove the redundant 10x adapter workflows.
    - Update the cromwell-metadata docker image.

### Azul

- Support for new bundle structure
- Internal build infrastructure improvements (unit tests, CI)

### Data Browser
This time’s release process does not include the Data Browser. DCP will figure out how to coordinate with the Data Browser team to work on the process before next release.

### Metadata Schema

No changes. DCP-wide integration test spreadsheet promoted from integration to staging branch.


## Staging 2018/08/15

**Special Circumstances:** The integration build is currently red which would normally
preclude a promotion to staging.  This is a special release to unblock data wrangers working with large
files.

### Upload Service
Version: v2.2.2
- Gitlab deployment setup and general deployment config cleanup
- Update to checksum lambda infra
- Update to Upload API's token logic triggered by hca client file upload
- Return error when attempting to schedule validation for file larger than 1tb
- Fix for ChecksummingSink() method call with upgrade of dcplib package

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
