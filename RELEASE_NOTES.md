# Release Notes

<!-- newest release at the top please) -->
## Prod 2019/01/29

### Ingest

#### Core v0.8.0
* Expose API endpoints for rabbitmq communication
* Accept and verify JWT tokens from DCP Auth and GCP Service accounts
* Point to schema https urls

#### Exporter v0.7.7
* Reporting export errors in submission envelope
* Remove unused schema env var in the exporter

#### UI v0.5.3
* Use DCP Auth (Fusillade) for Authentication
* Display submission errors
* Display commit hash build

### Secondary Analysis

Version(s):
* Lira: v0.15.0 -> v0.16.0
* Pipeline-tools: v0.43.2 -> v0.44.0
* Skylab: smartseq2_v2.1.0 -> smartseq2_v2.2.0

#### Lira and subscriptions
* Use HTTPS for all of the Ingest API endpoints.
* Re-subscribe to Data-Store service to let the project_uuid show as a workflow label

#### Pipeline-tools
* Use HTTPS for all of the Ingest API endpoints.
* Let the Adapter SmartSeq2 WDL accept optional output, e.g. the Zarr output.

#### Scientific Pipelines
* The Zarr format conversion task is now optional in SmartSeq2, but it will still always be called in HCA DCP by default.

### Data Browser

Version(s): commit 11333a07dd4bf44eb9b06b6889d5a60bcd635a79

* `23d7a339` - Updated manifest download API call.
* `bc40bd8d` - Updated file download to use native browser download.
* `87b1056f` - Fixed file download  where initial response is 302.
* `be576746` - Update spa/src/app/files/hca-download-file/hca-download-file.component.html
* `55db1710` - Removed download attribute.
* `101a7776` - Added manifest download params.
* `0bca8a70` - Added file name to file download GET.
* `af4ee977` - Augment pagination control for usability
* `ca2b9b96` - Improve specimen and files data on files tab
* `0ab6e2a2` - Pagination component
* `b26d107c` - Show data column at all times
* `45dd37f1` - Pagination css
* `24957af3` - Responsive adjustments to the filters
* `11333a07` - Fix for filters when height is limited


### Azul

Version(s): deployed/prod/2019-01-29__08-26, 8266ac30b897d1514af77883b4a189d61234a191

* Move to Azul-specific bucket for Terraform state (#645)
* Return content disposition header from manifest endpoints (#655)
* Improve health check endpoints (#624, #615, #548)
* Return content disposition header from /fetch/dss/files (#660)
* Replaced unsafe call to yaml.load() with yaml.safe_load()
* Limit impact reindexing on DSS in personal deployments (#646)
* Fix missing Slack notification on CloudWatch alarms (#621)
* Make web service tests use actual indexer input (#428)
* Terraform a Gitlab instance and run our tests on it (#632)
* Prototype carts API (fixes #480)
* Add endpoint for shortening URLs (fixes #66)
* Bump ES instance count to four in `dev`
* Upload manifests to S3 in multiple parts (#525)
* Delete indices when reindexing by default (connected to #610)
* Work around truncated results from DSS POST /search
* Amortized aggregation (fixes #86, …)
* Emulate HTTP redirects and retry-after in DSS file proxy (fixes #551)
* Make the manifest endpoint dual mode (fixes #567)
* Convert whitelist for DSS prod to blacklist (fixes #578)
* Replace `process` inner entity with `protocol` (fixes #540)
* Generate manifest using step functions (fixes #546)

### Metadata Schema

Versions:
* biomaterial/timecourse.json - v2.0.0
* biomaterial/donor_organism.json - v13.0.0
* biomaterial/organoid.json - v9.0.0

## Prod 2019/01/22

### Upload Service

Version: v3.4.0

* setup of asynchronous upload area deletion via sqs
* increase csum lambda memory to 1500 due to bumping into 960 mb limit
* reduce unnecessary information posted by health check bot
* Make UploadArea database id an integer sequence
* Fix functional test to work with new upload_area db schema
* fix a broken call to UploadException
* db: make file.s3_etag NOT NULL
* In create_db_record, use the same time for created_at/updated_at
* UploadDB: switch from SQLAlchemy MetaData(reflect=True) to .reflect()
* UploadArea: move DB methods together and prefix all with _db_
* Rename mock_upload_file to mock_upload_file_to_s3
* Fix order of assertEqual params in TestUploadApiClient
* policies for upload from cloud url
* upgrade hca cli to v4.6.0, move away from aws cp, and remove bucket to sqs notification post file upload
* Hotfix - allow for cross account copy from dcp-test-data s3 bucket

### Secondary Analysis

Versions
* Lira: v0.15.0
* Pipeline-tools: v0.43.2

Lira and subscriptions
* Update the pull-request-template.
* Add project_uuid to the metadata attachment in subscriptions. (Require re-subscribe to Data-Store service to take effect: We are skipping this change in this release and will deploy this change in the next release)
* Add Gitlab deployment support as an alternative deployment choice to Jenkins for Lira.

Pipeline-tools
* Update hca-cli version
* By default use Google PAPIv2 API for all of the adapter workflows.

### Metadata Schema

Versions
* biomaterial_core v7.0.4
* file_core v5.2.5
* process_core v9.0.3
* project_core v7.0.5
* protocol_core v5.2.5
* cell_morphology v6.1.5
* death v5.4.1
* familial_relationship v6.0.3
* growth_conditions v6.4.2
* human_specific v1.0.7
* medical_history v5.2.5
* mouse_specific v1.0.6
* preservation_storage v5.3.5
* state_of_specimen v5.2.7
* timecourse v1.1.5
* biological_macromolecule_ontology v5.3.3
* cell_cycle_ontology v5.3.3
* cell_type_ontology v5.3.3
* cellular_component_ontology v1.0.3
* development_stage_ontology v5.3.3
* disease_ontology v5.3.4
* enrichment_ontology v1.2.4
* ethnicity_ontology v5.3.5
* instrument_ontology v5.3.3
* length_unit_ontology v5.3.3
* library_amplification_ontology v1.2.3
* library_construction_ontology v1.2.3
* mass_unit_ontology v5.3.3
* microscopy_ontology v1.0.2
* organ_ontology v5.3.6
* organ_part_ontology v5.3.3
* process_type_ontology v5.3.3
* protocol_type_ontology v5.3.3
* sequencing_ontology v1.1.3
* species_ontology v5.3.3
* strain_ontology v5.3.4
* time_unit_ontology v5.3.3
* purchased_reagents v6.0.4
* 10x v1.0.5
* barcode v5.2.5
* insdc_experiment v1.1.5
* plate_based_sequencing v1.0.4
* funder v1.0.4
* publication v5.2.5
* target v1.0.3
* license v1.0.0
* cell_line v9.0.5
* cell_suspension v8.6.6
* donor_organism v12.0.5
* imaged_specimen v2.0.4
* organoid v8.3.12
* specimen_from_organism v6.3.8
* analysis_file v5.3.5
* image_file v1.0.2
* reference_file v2.2.8
* sequence_file v7.0.2
* supplementary_file v1.1.7
* analysis_process v8.0.6
* process v6.0.6
* project v9.0.8
* analysis_protocol v8.0.6
* aggregate_generation_protocol v1.1.7
* collection_protocol v8.2.10
* differentiation_protocol v1.3.3
* dissociation_protocol v5.0.7
* enrichment_protocol v2.2.8
* ipsc_induction_protocol v2.0.4
* imaging_preparation_protocol v1.0.4
* imaging_protocol v11.0.5
* protocol v6.3.7
* library_preparation_protocol v4.4.4
* sequencing_protocol v9.0.8

Functionality
* Removed normothermic_regional_perfusion from donor_organism.json
* Added normothermic_regional_perfusion to death.json
* Changed development_stage to required field in donor_organism.json

## Prod 2019/01/08

### Ingest

#### Version(s): 

* Exporter v0.7.6
* Fix to DSS datetime version format
* DSS API Authentication
* More info on logs
* Deploy new exporter secrets

### Data Store
Version: 2019-01-08-17-14-33-prod.release

* Grab collections owner from gcp credentials
* Update staging checkout bucket viewers
* working test modules for PUT/bundle response, changes to dss_api.yml for updates to swagger, changes to dss_api.py for responding within bundle manifest.
* Validating version format is DSS_VERSION
* Some improvements to README.md
* Note requirement of privileged access in README.md
* Update tf version in build Dockerfile
* Convenience function for temporary local storage of gcp credentials
* Updating Auth in readme
* Use async state to catch/expose copy sfn errors
* Prevent elasticsearch-dsl versioning above 5.x.
* updating patch collection to deduplicate contents
* Store and recover chunks of state in dynamodb
* Update DSS_VERSION after deploy succeeds
* Provide fine grained management of Lambda environment variables
* Test head File returns file metadata.
* DEFINE, not CREATE the bucket
* State that terraform is needed
* replacing scan with search after for notifications.
* Sort exported variables
* Adding Indexer idempotent test
* Refreshing Requirements
* Added Architectural diagram to readme
* Reorganize deployment and auth section of readme
* Drive dss-index with SQS instead of SNS
* restrict access to put bundle and files
* Retry join state in s3 copy sfn
* Send GS copy client exceptions to fail state
* Update docs for some env vars
* Send S3 copy client exceptions to fail state
* Raw Search Page Limit
* Accommodate TF changes plus minor infra updates
* Check GitLab status, instead of GitHub, in release.sh
* DSS_AUTHORIZED_DOMAINS should be quoted
* Increase the number of ES nodes
* remove unsupported azure from swagger
* Adding documentation for subscription PUT to handle duplicate notifications.


## Prod 2018/12/18

### Ingest

#### Version(s): 

* Broker v0.8.4
* Fix to connection reset error during spreadsheet import
* Fix schema parsing, defaults to string if there is no items obj inside array field in schema
* Added fix to ensure that import doesn't fail due to erroneous max_row count
* Fixes to raising and logging error details

#### Validator v0.6.0 (same version)

* Config change: Point to the latest fastq validator image (fastq_utils:v0.1.0.rc) when requesting fastq validation jobs from the upload validation service

#### Staging Manager v0.5.3

* Remove 10s wait when creating upload area
* Fix setting for retry policy, retrying for ~20min

#### State-tracking v0.7.4

* Addressed bug where a deleted state machine would be stored as null in the Redis database

#### Ontology

* Redeploying to pick up new ontology values

### Upload Service

#### Version(s)

v2.4.3->v3.1.0

#### Changes

* upgrade 
	* terraform to 0.11.10
	* Moto to 1.3.7
	* Boto to  1.9.44
	* Botocore to 1.12.44
	* Validation image to 11
	* Requests to 2.20.0 (safe version)
	* Checksummer image to 5
* Add tenacity to checksummer reqs
* Create validation harness
	* ValidatorHarness: make staged_file_path a pathlib.Path
	* publish humancellatlas/upload-validator-base-alpine:17 as latest
* Create new env local, allow tests to run offline in local env
* Add errors and retry on tags to s3 object 
* Add endpoint /area/file endpoint that adds file to pre checksum sqs which triggers checksum daemon lambda
* Add Batch watcher daemon 
	* runs on hourly schedule and checks for failed jobs, killing any relevant instances in that env and rescheduling the validation/csum job
	* retry on boto3 batch describe_job 
	* policy on batch watcher to invoke checksum daemon
	* refetch jobs after killing instances
* Update to daily health check to output number of failed validation and checksum events in report.
* Update chalice policy for batch jobs 
* Update validation scheduler to return validation_id
* Refactor tests to make more dry
* Refactor: wrap database_orm db initialization code in a class
* Refactor: wrap common/database code in a class: UploadDB
* fix from queue.url to queue.id in retrieving csum sqs url
* remove correlation ID from log entries
* remove obsolete "make secrets"
* remove unused imports
* DB migration
	* Add "FAILED" status to checksum_event and validation_event statuses
	* Add docker_image field to validation_event
	* Add original_validation_id field to validation_event
	* Mark all historical "SCHEDULED" and "VALIDATING"/"CHECKSUMMING" events as "FAILED".

### Data Store

No changes to promote.

### Secondary Analysis

No changes to promote.

### Data Portal

No changes to promote.

### Metadata Schema

#### Version(s)

* contact: 6.1.4
* channel: 2.0.0
* target: 1.0.1
* links: 1.1.4
* cell_line: 9.0.1
* cell_suspension: 8.6.2
* donor_organism: 10.2.1
* imaged_specimen: 2.0.2
* organoid: 8.3.9
* specimen_from_organism: 6.3.4
* sequence_file: 7.0.0
* project: 9.0.4
* imaging_protocol: 11.0.1
* library_preparation_protocol: 4.4.0

#### Changes

* Changed channel field to optional in imaging_target.json.
* Changed channel field to optional in imaging_protocolol.json
* Merges in the new validator (JS instead of python)
* Changed molecule_ID to lower case in target.json Fixes #666
* Added new schema target.json to replace deprecated imaging_target.json. Fixes #641
* Changed technical_replicate_group_id to library_preparation_id. Fixes #262.
* Changed channel_id from string to array
* Changed name of the required field channel_name to channel_id
* Added optional field timecourse.
* Changed channel field type to array
* Fixed a bug in the links schema still referencing core instead of system
* Changed channel field type to array
* Added new optional fields nominal_length and nominal_sdev. Fixes #594


## Prod 2018/12/10

This is an hot fix promotion for only Secondary-Analysis to address a issue with the 10x analysis pipeline: 
Get expected cell count from 10x bundles instead of using a static value in the cellranger adapter WDL

### Secondary Analysis

Version(s):
Pipeline-tools v0.42.0 -> v0.43.0


## Prod 2018/11/13

### Azul
Version: 2fb1b25c1bd8b3e6eda27d15e716fa849f80d4a5 (tagged deployed/prod/2018-11-13__14-41)

* Initial production release

## Prod 2018/10/25

This is an ad-hoc promotion for only Secondary-Analysis

### Secondary Analysis

Version(s):
Pipeline-tools v0.28.2 -> v0.38.0

Changes:

#### Lira and subscriptions
- Subscriptions are still turned off in production at this time point. 

#### Pipeline-tools
- Fix an [issue](https://github.com/HumanCellAtlas/secondary-analysis/issues/393) so now the analysis_protocol is linked to analysis_process properly.
- Fix an [issue](https://github.com/HumanCellAtlas/secondary-analysis/issues/392), where the GetInputs task of the CellRanger Adapter WDL output Array[File] i1_fastq = [""] for bundles with no I1 files.

## Prod 2018/10/23

### Ingest

#### State Tracker v0.7.3
- Fixed bug determining the URI for persisted state machines
- Fixed state tracking persistence
- Ensuring envelopes go to the Cleanup state when more than the number of expected bundles are generated

#### Exporter v0.7.5
- Fixed bug in analysis export, analysis bundles should reference same metadata file version from input bundle
- Reverted to 20 retries spaced a minute apart for operations on the DSS API
- Using ingest's update timestamp for creating .json files in the DSS, averting needless duplicates
- Polling DSS Files to confirm their full creation prior to creating a bundle containing said Files

#### Broker v0.8.3
- Fixed bug whereby file metadata updates fail if a file is uploaded prior spreadsheet upload
- Fix to submission error message

#### Core v0.7.6
- Lazy load biomaterial dbrefs
- Logging when submission envelope is created and submitted
- Optimization in finding assay processes for export
- Fix to slow-down caused by synchronous UUID generation
- Bug fixes

#### Staging Manager v0.5.2
- Using HTTP HEAD when asserting existence of upload area resources in the upload service

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

- Raise sync exception when s3/gs presigned urls fail to resolve
- Remove unnecessary lambda Get/List permissions for s3.
- Lambda env vars are read from SSM during deploy
- Making notification logs less noisy
- Adding info log messages to subscriptions
- Update integration checkout bucket whitelist
- reparameterize backend bucket
- GS event relay: Get all available GRTC env vars in one go
- Replace all storage buckets
- refactor and optimize get bundle to serve existing checkout bundles when possible
- adding google project to whitelist
- adding 422 when metadata checksums are missing for put_file
- optimize get file to always return immediately if checkout is available
- Multiplex GS events between indexer and sync daemons using SNS-SQS
- SFN Sync daemon: Loosen SQS name constraint in IAM policy
- Sync daemon: use SQS and state functions, ensure referential consistency
- DSS read-only mode
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
