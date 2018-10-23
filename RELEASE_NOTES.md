# Release Notes

<!-- newest release at the top please) -->

## Prod 2018/10/23

### Ingest

#### State Tracker v0.7.3
Fixed bug determining the URI for persisted state machines
Fixed state tracking persistence
Ensuring envelopes go to the Cleanup state when more than the number of expected bundles are generated

#### Exporter v0.7.5
Fixed bug in analysis export, analysis bundles should reference same metadata file version from input bundle
Reverted to 20 retries spaced a minute apart for operations on the DSS API
Using ingest's update timestamp for creating .json files in the DSS, averting needless duplicates
Polling DSS Files to confirm their full creation prior to creating a bundle containing said Files

#### Broker v0.8.3
Fixed bug whereby file metadata updates fail if a file is uploaded prior spreadsheet upload
Fix to submission error message

#### Core v0.7.6
Lazy load biomaterial dbrefs
Logging when submission envelope is created and submitted
Optimization in finding assay processes for export
Fix to slow-down caused by synchronous UUID generation
Bug fixes

#### Staging Manager v0.5.2
Using HTTP HEAD when asserting existence of upload area resources in the upload service

### Upload Service
Version: v2.4.1

- Add head method to v1/area/upload_area_id endpoint
- Daily health check lambda
- Move lambda deployments to shared s3 bucket
- Batch vcpus 2 -> 4
- increase lambda timeout (5 min -> 15 min)  and file size (4gb -> 10 gb) for inline checksumming
- recheck file content type after checksumming
- Add ability to disable/enable Lambdas and batch deployments (uploadctl runlevel start|stop|status)
- Remove uploadctl setup|teardown functionality

### Data Store
Version: prod-2018-09-18-15-58-07.release

- Remove unnecessary lambda Get/List permissions for s3.
- Lambda env vars are read from SSM during deploy
- Making notification logs less noisy
- Adding info log messages to subscriptions
- Update integration checkout bucket whitelist
- reparameterize backend bucket
- GS event relay: Get all available GRTC env vars in one go
- refactor and optimize get bundle to serve existing checkout bundles when possible
- adding google project to whitelist
- adding 422 when metadata checksums are missing for put_file
- optimize get file to always return immediately if checkout is available
- Multiplex GS events between indexer and sync daemons using SNS-SQS
- SFN Sync daemon: Loosen SQS name constraint in IAM policy
- Describing auth env var in readme
- Give GCP service account read access.
- Parameterize GCP checkout bucker viewers
- Fix timeout handling for API lambda


### Secondary Analysis
Version(s):
- Lira: v0.13.2 -> v0.14.0
- Pipeline-tools v0.28.2 -> v0.36.0

Changes:

Lira and subscriptions
- The scripts for making subscriptions are using the new HCA DCP Auth method to communicate with Data-Storage service now.
- Update default 10x WDL config parameters in deployment script to reference CellRanger adapter WDL files
- Update SS2 WDL parameters in deployment script to includes the zarr utils analysis wdl
- Improve SS2 subscription query to use ontology IDs instead of the text field

Pipeline-tools
- Removed a lot of unused files in the repo.
- Instead of querying Cromwell during the submission, pipeline-tools is getting the versions of the pipelines directly from the WDL files.
- Update SS2 analysis outputs in the SS2 adapter pipeline
- Uses metadata-api v1.0b4.
- Add Adapter WDL for the CellRanger count pipeline for 10x data
- Update the Adapter WDL for SmartSeq2 so it accepts Zarr files from the analysis pipeline and submits back to Ingest.
- Improve the analysis result file format mapping, as well as add zarr to the mapping.
- Add web_summary.html to CellRanger adapter outputs.
- Fix disk space for stage_files task in submit WDL.
- Rename cellranger outputs so that they are unique.
- Have cellranger adapter WDL pass in max_cromwell_retries parameter to submit WDL.

(Pipelines)
- (no 10x subscription active)10x pipeline: N/A -> cellranger_v1.0.0
- Add wdl to build gencode and ensemble references for cellranger.
- (no ss2 subscription active) Smart-seq2 pipeline: smartseq2_v2.0.0 -> smartseq2_v2.1.0
- Update zarr creation task

### Data Portal
No changes.

### Metadata Schema
Version(s):
- imaging_protocol: 8.0.3
- sequencing_protocol: 9.0.3

- Changed description for paired_end in sequencing_protocol.json
- Removed required field `protocol_type` from imaging_protocol (not actually in the schema).
- Added dcp_scale_test_pancreas6decades.xlsx spreadsheet

## Prod 2018/10/02

### Metadata Schema
- Less stringent term restriction for organ ontology.
- `project_core` required in `project.json`
- "not provided" valid value for `strand` field in `library_preparation_protocol.json`
- `publication` field in `cell_line.json` takes only a single publication
- Version Changes:
  - organ_ontology.json - v5.3.5
  - cell_line.json - v9.0.0
  - donor_organism.json - v10.1.2
  - project.json - v9.0.3
  - library_preparation_protocol.json - v4.3.3
  - specimen_from_organism.json - v6.3.3
  - organoid.json - v8.3.8


## Prod 2018/09/18

### Ingest

#### Core v0.7.2
  - Optimizations regarding sending of unnecessary messages to the rabbit-mq broker
  - Integration with the state tracker’s HTTP API
  - Indexing on Process resources’ input and output biomaterials/files enabling faster bundle generation and export
  - Endpoint in monitoring state transitions of submission envelope
  - Added File indices in mongo for faster uploading of files metadata
  - Fixed bug when adding input bundle manifests for restructured bundles to processes
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

#### State Tracking v0.7.0
  - Race condition bug fix whereby state updates were processed out of order
  - Added a HTTP API for processing state update messages
  - Optimizations in sending state tracker messages
  - Fix to race condition when processing state tracker messages

#### Exporter v0.7.1
  - Caching of previously retrieved documents for faster export time
  - Retrying 20 times with 1 minute between for idempotent requests to the DSS

#### Accessioner v0.5.0
  - New Accessioner using Node.js

#### Broker v0.8.0
  - Ability to upload supplementary files
  - Ability to Link entity to entity with same concrete type in the spreadsheet
  - Changes Submission report format
  - Configurable submission report
  - Error handling changes during spreadsheet upload
  - Support for additional project modules in spreadsheet
  - Handling schema /system links during spreadsheet upload
  - Upgraded dependencies for hca-ingest module
  - Fix bug in Schema template api to point to correct schema environment

#### Validator v0.6.0
  - New JavaScript Validator
  - Support for Draft-07 JSON schema

#### Staging Manager v0.5.1
  - Now waits for  for Ingest Core to come online before consuming messages

#### Exporter v0.7.1
  - Using latest version of input data files in secondary bundle export
  - Bundles now contain supplementary files
  - Using latest version of links.json schema
  - Respecting the “triggerAnalysis” flag on envelopes to toggle triggering of analysis on primary submissions
  - Bundle restructure
  - Fixed bug when fetching documents from ingest-core
  - Remove hca dependency on the exporter listener and use the ingest-client version which uses hca v0.5

#### UI v0.5.2
  - Fix submission dashboard pagination


### Upload Service

- Fixes to schema for get validation and checksum statuses
- Fix for validating files with hashes
- Fix to upload area sync and create scripts to account for new credentials format
- Fix for ChecksummingSink() method call with upgrade of dcplib package
- Fix: allow filenames to have a hash in them
- Fix: Notify ingest if an identical file is re-uploaded, even if it has already been checksummed

- Update to Upload Api's token logic triggered by hca client file upload
- Api endpoint to check validation statuses
- Scripts to schedule and retrieve validation statuses
- Return error when attempting to schedule validation for file larger than 1tb

- Update to checksum lambda infra
- Add SQS queue between S3 object creation and checksum Lambda function (better scalability)
- Stop using Chalice to deploy checksum Lambda.  Package it ourselves. Allow Terraform to deploy it.

- Gitlab deployment setup and general deployment config cleanup
- Pinning of all dependencies

- Increase of validation job definitions to 2048mb and 2vCPUs
- Changing max vcpus for validation batch infrastructure to 512
- Increase in checksum lambda memory to 3008mb to avoid lambda out of memory errors

- Terraform: Move Upload Service deployment to its own VPC
- Terraform: create RDS security group removing the need for passing around `vpc_rds_security_group_id`
- Terraform: unlink Makefile and hard-code deployment stage


### Data Store

- Setting ES timeout for all hosts (#1383)
- CI-CD Deployment scripting for GitLab (#1388)
- Version mandatory for PUT Files and Bundles (#1390)
- Shorten the expiration on the dev checkout bucket (#1405)
- infra/Makefile exits loops on error (#1394)
- Update README.md deployment instructions (#1413)
- Add missing 301 response to GET /v1/bundles/{uuid} swagger (#1418)
- Gitlab build script (#1403)
- TF scripting to deploy GCP service account (#1424)
- Admin repair will never send notifications (#1426)
- Include SFN execution name in visitation state (#1429)
- Add roles/cloudfunctions.developer to gcp service account (#1431)
- Deploy dev on the Build Box (#1423)
- add /version endpoint to DSS API
- Adding test cases when invalid version and uuid are supplied to bundle
- Add DSS HTTP client best practices docs (#1419)
- Separate GCP service accounts by stage (#1432)
- Added bundle_uuid as a parameter to TestBundle
- Cleaning up request response after get_request in LocalNotificationRe
- Changed the index backed default to notify only on bundle modificatio
- Set language locale to address Click issue (#1435)
- Adding additional retry errors to visitation (#1438)
- Promote to integration immediately given CI status (#1437)
- Update infra to reflect current state (#1442)
- Clean build directory before stage promotion (#1443)
- Move gitlab-ci.yml virtualenv out of project root (#1446)
- During ci/cd build, use terraform plan, not apply (#1444)
- Fixing spaces in smoketest when downloading from other replicas (#1448)
- Grab GCP credentials before release in gitlab-ci.yml (#1451)
- Admin repair's default is to not send notifications (#1450)
- Added test cases for test_file (#1436)
- Fixed multipart upload (#1456)
- Remove the submodule dependency on checksumming_io (#1458)
- Reject bundles containing duplicated filenames (#1454)
- Add manual GitLab action to release to staging (#1457)
- Bump awscli to 1.15.0 or greater (#1462)
- Add Index Design and search limitations documentation (#1461)
- Switch to the constants defined in dcplib (#1465)
- Add a bundle with new layout to test fixtures (#1468)
- Use folded block YAML style for docs in swagger (#1470)
- Check dcp-int status on GitLab (#1472)
- Use different staging folders for building requiremnts. (#1464)
- [Refactor] Changed TombstoneID to BundleTombstoneID (#1452)
- Move errcodes out of the catch-all default error handler. (#1482)
- Change illegal version to a 400. (#1483)
- Support new bundle layout (#1469)
- Fix shape_descriptor bug causing failed deploy
- Upgrade to dcplib 1.3.2 (#1478)
- Explicitly catch a malformed version error for PATCH /collections (#1485)
- Refresh all requirements. (#1476)
- Remove dss-chalice script
- Deploy before performing integration tests (#1494)
- Add force-release buttons to GitLab (#1489)
- Update indexer test to new fixture (#1500)
- Update fixture in tests/test_indexer.py (#1505)
- Update smoketest bundle fixture (#1504)
- Remove duplicated indexer test code (#1501)
- Don't mark job as failed when not releasing to int (#1512)
- Delete old bundle format fixtures (#1513)
- Interpolate cli endpoint (#1502)
- Improve error response documentation for PATCH /collections (#1490)
- Checkout from GitHub with token for releases (#1510)
- Remove unsused sample queries (#1503)
- Incorporate terraform workflow into daemon deployment (#1425)
- Update fixture for tests/test_api.py (#1514)
- create blob TTL env vars
- Remove unused test_api fixture. (#1519)
- Add missing quotes to fix tf scripts
- Add DSS_BLOB_TTL_DAYS to Terraform variables (#1526)
- Release to integration requires manual action. (#1525)
- Add link to CONTRIBUTING.md in README.md (#1528)
- Add test for bundle delete notifications (#1527)
- Prevent object modification rate limit touch test files (#1534)
- Put the shape descriptor in the ES index doc (#1529)
- Direct urls should point to checkout bucket (#1539)
- Add `--no-deploy` flag to scripts/release.sh (#1537)
- Refactor gitlab jobs (#1540)
- files are checked out to checkout_bucket/blob (#1541)
- directaccess and presignedurl should go to the checkout bucket (#1545)
- Adding Debug log message when a collection is identified by the index
- Remove unused dependency (moto) and its hazardous subdeps (#1544)
- Consolodate bundle fixture (#1535)
- Fix tests/test_smoketest.py typo (#1546)
- Using Auth0 for authentication (#1542)
- adding subtests to test_bundle (#1543)
- get_file performs synchronously when possible (#1347)
- get_bundle only performs checkout when necessary (#1347)


### Secondary Analysis

#### Falcon
- Stand up Falcon v0.1.3 in production, No workflow will be started at this time.

#### Lira and subscriptions
- Stand up Lira v0.13.2 in production, No subscriptions to DSS for now to avoid workflows running in production environment.

#### Pipeline-tools
- Let Lira use pipeline-tools v0.28.2 in production


## Azul

- Support for new bundle structure
- Internal build infrastructure improvements (unit tests, CI)


## Data Browser

- This time’s release process won’t include the Data Browser. DCP will figure out how to coordinate with the Data Browser team to work on the process before next release.


## Metadata Schema

### Schema changes
- New schemas
    - cellular_component_ontology.json, microscopy_ontology.json, 10x.json, channel.json, imaging_target.json, links.json, imaged_specimen.json, image_file.json, supplementary_file.json, analysis_process.json, imaging_preparation_protocol.json
- Changed schemas
    - smartseq2 to plate_based_sequencing, ingest_audit to provenance
- Removed schemas
    - bundle schemas
- Miscellaneous
    - migrated from draft-04 to draft-07 JSON, replacing id with $id
    - title attribute changed to sentence case schema name, name attribute added as programmatic schema name

### Field changes
- New fields
    - New optional fields: growth_conditions.culture_environment, growth_conditions.feeder_layer_type, contact.corresponding_contributor, cell_suspension.plate_based_sequencing, sequence_file.technical_replicate_group, sequencing_protocol.10x
    - provenance added to all type schemas
- Changed fields
    - Required and optional fields added/changed in imaging_protocol.json
    - Changed field names: project_core.project_shortname to project_core.project_short_name, familial_relationship.is_child_of to familial_relationship.parent, familial_relationship.is_parent_of to familial_relationship.child, familial_relationship.is_sibling_of to familial_relationship.sibling, smartseq2.well_name to plate_based_sequencing.well_id, ingest_audit.submissionDate to provenance.submission_date, ingest_audit.updateDate to provenance.update_date, donor_organism.biological_sex to donor_organism.sex, donor_organism.disease to donor_organism.diseases, specimen_from_organism.disease to specimen_from_organism.diseases, project.supplementary_files to project.supplementary_links, dissociation_protocol.nucleic_acid_source to library_preparation_protocol.nucleic_acid_source, sequencing_protocol.paired_ends to sequencing_protocol.paired_end
    - Changed field requirements: contact.email from required to optional, contact.institution from optional to required
    - differentiation_ removed from fields in differentiation_protocol.json
    - induced_pluripotent_cell_ changed to ipsc_ for fields in ipsc_induction_protocol.json
- Removed fields
    - smartseq2.well_row, smartseq2.well_column, sequence_file.smartseq2

### Ontology changes
- disease_ontology.json accepts as valid all children of (MONDO:0000001, PATO:0000461) including the top-level values
- organ_ontology.json accepts as valid all children of (UBERON:0000062, UBERON:0000179) including the top-level values
- strain_ontology.json accepts as valid all children of (NCBITaxon:10090) including the top-level values
- ethnicity_ontology.json uses HANCESTRO ontology

### Miscellaneous
- Updated repo documentation
- Updated metadata examples (JSON, spreadsheet, bundles)
- Updated schema integration test files



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
