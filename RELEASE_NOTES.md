# Release Notes


## Staging 2019/02/21

### Ingest

#### Broker v0.8.7.rc

* Bug fixes in the importer: trailing space and number field conversion

####  UI v0.5.4.rc

* Show linking progress in the UI
* Upgrade to component versions

### Azul

Version: 321320c3b4e459ec932c57db57b196bf8c3be78b (deployed/staging/2019-02-21__08-38)

* 2d8a701f Delete empty aggregates (#709)
* c88434b2 Prioritize organoid organ fields (#695)
* c815bc8b Deploy Grafana dashboard during `make terraform`
* 7817477a Migrate monitoring resources from dcp-monitoring (#622)
* c81bde06 Rename `AZUL_ENABLE_CLOUDWATCH_ALARMS` to `AZUL_ENABLE_MONITORING`
* 94ca44e1 Refactor app.py with individual services (#678)
* 3885e511 Implement the integration with Fusillade (#58)
* d5a19a01 Ignored everything in lambdas/*/vendor except 'azul'
* 354a129f Fix cheat sheet in README to reflect 904883e
* 904883e5 Fix deployment issues with `python -m venv` and make it the default (#340)
* b5edf68c Implemented the default cart logic (#629)
* 12da6c1c Blacklist test projects in prod
* 494c49ec Sync threads more reliably in concurrent indexer test (#696)
* 97214c9c Blacklist test projects in prod
* aae9244c Add rudimentary script for counting bundles


## Staging 2019/02/13

### Ingest

#### Core v0.8.2.rc

* Added submission envelope field to track number of expected links/edges in the metadata graph

#### Broker v0.8.6.rc

* Utilizing submission envelope's link/edge counter

### Upload Service

Version: v4.1.0 -> v4.2.0

* Support for paired file validation
* Improve reliability when AWS Batch is slow to respond

### Data Store

Version:  2019-02-13-17-06-40-staging.release

* Fixed paging with bundle tombstones (#1846)
* adding delete and tombstone notifications to smoke test (#1856)
* [Easy] Use correct document when notifying on delete (#1851)
* Update domovoi and change naming to reflect changes in domovoi. (#1847)
* adjust infra make clean (#1830)
* Adding Source IP and Decoded JWT to logs (#1839)
* Change staging bucket names to encrypted buckets.  Add venv to git ignore. (#1840)
* Update the build image to Terraform v0.11.11 (#1841)
* Script for ad-hoc tombstoning (#1831)
* Reducing the DSS permission to deny deletion privilages (#1826)
* Increase checkout TTL to 90 days (#1836)
* Use AWS ACM identifier to id domain cert (#1835)
* Use terraform to deploy custom domain natively (#1834)
* added --dry-run functionality to set_secrets (#1833)
* Put admin user emails in SSM store (#1828)
* Switch to on-demand capacity for async state db (#1827)
* Update infra defs for prod (#1824)
* Populating lambda SSM warns on undefined vars (#1817)
* Parameterize SSM store name in environment (#1814)
* Change buckets names over to new encrypted buckets. (#1815)
* Refreshing requirements (#1820)
* Add permissions to dss-checkout-sfn lambdas to access test fixture buckets. (#1819)
* Error returned if partial results are returned. (#1813)
* Remove url from GitLab environments (#1786)
* Restrict encryption to only certain buckets. (#1799)
* Correct for bracket syntax in s3.tf. (#1797)
* Encrypt S3 buckets at rest, should solve issue #1754 for AWS (#1755)
* Change buckets in dev to new buckets with encryption. (#1796)
* Set CORS policy on checkout bucket (#1793)
* Fix Unwritable bucket (#1780)
* Tagging terraform deployed resources with Terraform and DSS (#1766)
* Configurable swagger security. (#1746)
* moved dst_bucket sanitation to bundle checkout (#1767)

### Secondary Analysis

#### Lira: v0.17.0

* Authenticate Cromwell VMs with the Cromwell-as-a-Service (CaaS) service account by using the “google_compute_service_account” workflow options parameter

#### Pipeline-tools v0.46.1

* Standardize Cromwell timestamps to follow the date-time format required by the analysis process JSON schema
* Use the default application credentials of the VM when requesting metadata from Cromwell instead of storing the JSON key in a private docker image
* Use JWT created from CaaS service account for authentication to Ingest API

### Azul

Version(s): 25f1a4413b302c655ce6134ad138b7a67cf12156 deployed/staging/2019-02-05__16-16

* 4376e31e Upgrade to metadata-api 1.0b9
* 1ee8a827 Implement integration test (#262)
* 9c32e931 Make default sort specific to each entity type (#683)
* 52756717 Temporarily disable gitlab in prod
* 38f0858e Blacklist test projects in prod from 1/22/2019
* 78e95117 Fix misc typos and formatting in README
* 193ffcc2 Add Locust script for scale testing (#542)
* a8fd104d Add GA4GH Data Repository Service (DRS) GET for files (#638)
* a2313a40 Fix: Health check tests only pass with `dev` selected (#670)
* 5289bfd2 Move to Azul-specific bucket for Terraform state (#645)
* 5b14c644 Blacklist test projects in prod from 1/22/2019
* 56abed45 Move to Azul-specific bucket for Terraform state (#645)
* 6f8ffe6b Blacklist test projects in prod from 1/22/2019
* 4cbe65fc Move to Azul-specific bucket for Terraform state (#645)

### Metadata Schema

Version(s): 

* biomaterial_core - v7.0.5
* cell_morphology - v6.1.6
* human_specific - v1.0.9
* mouse_specific - v1.0.7
* preservation_storage - v6.0.1
* timecourse - v2.0.1
* barcode - v5.2.6
* plate_based_sequencing - v1.0.6
* channel - v2.0.1
* target - v1.0.6
* links - v1.1.5
* cell_line - v10.0.4
* cell_suspension - v9.0.0
* donor_organism - v14.0.3
* maged_specimen - v2.0.7
* organoid - v10.0.2
* specimen_from_organism - v7.0.3
* analysis_file - v5.3.6
* image_file - v1.0.3
* reference_file - v2.2.10
* supplementary_file - v1.1.8
* analysis_process - v8.0.8
* process - v6.0.7
* project - v11.0.0
* analysis_protocol - v8.0.7
* aggregate_generation_protocol - v2.0.0
* collection_protocol - v8.2.11
* dissociation_protocol - v5.0.8
* enrichment_protocol - v2.2.9
* imaging_preparation_protocol - v2.0.1
* imaging_protocol - v11.0.9
* protocol - v6.3.9
* library_preparation_protocol - v4.4.6
* sequencing_protocol - v9.0.11
* biological_macromolecule_ontology - v5.3.4
* cell_cycle_ontology - v5.3.5
* cell_type_ontology - v5.3.5
* cellular_component_ontology - v1.0.4
* development_stage_ontology - v5.3.5
* disease_ontology - v5.3.7
* enrichment_ontology - v1.2.5
* ethnicity_ontology - v5.3.7
* instrument_ontology - v5.3.5
* length_unit_ontology - v5.3.4
* library_amplification_ontology - v1.2.4
* library_construction_ontology - v1.2.4
* mass_unit_ontology - v5.3.4
* microscopy_ontology - v1.0.4
* organ_ontology - v5.3.7
* organ_part_ontology - v5.3.4
* process_type_ontology - v5.3.4
* protocol_type_ontology - v5.3.4
* sequencing_ontology - v1.1.4
* species_ontology - v5.3.4
* strain_ontology - v5.3.5
* time_unit_ontology - v5.3.4

Changes:

* Changed total_estimated_cells to estimated_cell_count.
* Added timecourse field to cell_suspension schema.
* Changed familial_relationship field to be plural.
* Changed accession fields to arrays and changed corresponding field names in project schema.
* Added required model_organ field to cell line schema.
* Removed organoid_type field from organoid schema.
* Changed field names in aggregate_generation_protocol.


## Staging 2019/01/30

### Ingest

#### Broker(v0.8.5.rc)
* Reporting all import errors to the submission envelope

#### Core(v0.8.1.rc)
* Bug fixes in JSON parsing upload-service messages
* Logging auth failures

### Upload Service (v4.1.0)
* Send notifications to new Ingest REST endpoints instead of AMQP
* Checksumming has been restructured to be more resilient to multiple-simultaneous-uploads-of-the-same-file attacks.

### Metadata Schema

#### Versions
* preservation_storage.json - v6.0.0
* specimen_from_organism.json - v7.0.0
* imaging_preparation_protocol.json - v2.0.0
* funder.json - v2.0.0
* project.json - v10.0.0

#### Changes
* change storage_method enum list to remove commas from values
* change funder_name to organization
* change grant_id and organization to be required
* change funders to be required

## Staging 2019/01/23

### Ingest

Versions:
* Core v0.8.0.rc
* Exporter v0.7.7.rc
* UI v0.5.3.rc

Core
* Expose API endpoints for rabbitmq communication
* Accept and verify JWT tokens from DCP Auth and GCP Service accounts
* Point to schema https urls

Exporter
* Reporting export errors in submission envelope
* Remove unused schema env var in the exporter

UI
* Use DCP Auth (Fusillade) for Authentication
* Display submission errors
* Display commit hash build

### Secondary Analysis

Versions:
* Lira v0.16.0
* Pipeline-tools v0.44.0
* Skylab:
    * smartseq2_v2.2.0

Lira and subscriptions
* Use HTTPS for all of the Ingest API endpoints.
* Re-subscribe to Data-Store service to let the project_uuid show as a workflow label

Pipeline-tools
* Use HTTPS for all of the Ingest API endpoints.
* Let the Adapter SmartSeq2 WDL accept optional output, e.g. the Zarr output.

Scientific Pipelines
* The Zarr format conversion task is now optional in SmartSeq2, but it will still always be called in HCA DCP by default.

### Azul

Version: deployed/staging/2019-01-23__09-05, (b80a05db398e2e144006042523becca2dc653e90)

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

Functionality:
* Changed fields to remove timecourse_. Fixes #745.
* Updated field names to remove organoid_ prefix. Fixes #480.


## Staging 2019/01/16

### Upload Service

#### Version(s)

v3.4.0

#### Changes

- Setup of asynchronous upload area deletion via sqs
- Increase csum lambda memory to 1500 due to bumping into 960 mb limit
- Reduce unecessary information posted by health check bot
- Make UploadArea database id an integer sequence
- Fix functional test to work with new upload_area db schema
- Fix a broken call to UploadException
- db: make file.s3_etag NOT NULL
- In create_db_record, use the same time for created_at/updated_at
- UploadDB: switch from SQLAlchemy MetaData(reflect=True) to .reflect()
- UploadArea: move DB methods together and prefix all with _db_
- Rename mock_upload_file to mock_upload_file_to_s3
- Fix order of assertEqual params in TestUploadApiClient
- Policies for upload from cloud url
- Upgrade hca cli to v4.6.0, move away from aws cp, and remove bucket to sqs notification post file upload

### Secondary Analysis

#### Version(s)
- Lira v0.14.1 -> v0.15.0
- Pipeline-tools v0.43.0 -> v0.43.2

#### Changes

- Lira and subscriptions
    - Update the pull-request-template.
    - Add project_uuid to the metadata attachment in subscriptions. (_Require re-subscribe to Data-Store service to take effect: We are skipping this change in this release and will deploy this change in the next release_)
    - Add Gitlab deployment support as an alternative deployment choice to Jenkins for Lira.

- Pipeline-tools
    - Update hca-cli version
    - By default use Google PAPIv2 API for all of the adapter workflows.

### Metadata Schema

#### Version(s)

- biomaterial_core -v7.0.4
- file_core -v5.2.5
- process_core -v9.0.3
- project_core -v7.0.5
- protocol_core -v5.2.5
- cell_morphology -v6.1.5
- death -v5.4.1
- familial_relationship -v6.0.3
- growth_conditions -v6.4.2
- human_specific -v1.0.7
- medical_history -v5.2.5
- mouse_specific -v1.0.6
- preservation_storage -v5.3.5
- state_of_specimen -v5.2.7
- timecourse -v1.1.5
- biological_macromolecule_ontology -v5.3.3
- cell_cycle_ontology -v5.3.3
- cell_type_ontology -v5.3.3
- cellular_component_ontology -v1.0.3
- development_stage_ontology -v5.3.3
- disease_ontology -v5.3.4
- enrichment_ontology -v1.2.4
- ethnicity_ontology -v5.3.5
- instrument_ontology -v5.3.3
- length_unit_ontology -v5.3.3
- library_amplification_ontology -v1.2.3
- library_construction_ontology -v1.2.3
- mass_unit_ontology -v5.3.3
- microscopy_ontology -v1.0.2
- organ_ontology -v5.3.6
- organ_part_ontology -v5.3.3
- process_type_ontology -v5.3.3
- protocol_type_ontology -v5.3.3
- sequencing_ontology -v1.1.3
- species_ontology -v5.3.3
- strain_ontology -v5.3.4
- time_unit_ontology -v5.3.3
- purchased_reagents -v6.0.4
- 10x -v1.0.5
- barcode -v5.2.5
- insdc_experiment -v1.1.5
- plate_based_sequencing -v1.0.4
- funder -v1.0.4
- publication -v5.2.5
- target -v1.0.3
- license -v1.0.0
- cell_line -v9.0.5
- cell_suspension -v8.6.6
- donor_organism -v12.0.5
- imaged_specimen -v2.0.4
- organoid -v8.3.12
- specimen_from_organism -v6.3.8
- analysis_file -v5.3.5
- image_file -v1.0.2
- reference_file -v2.2.8
- sequence_file -v7.0.2
- supplementary_file -v1.1.7
- analysis_process -v8.0.6
- process -v6.0.6
- project -v9.0.8
- analysis_protocol -v8.0.6
- aggregate_generation_protocol -v1.1.7
- collection_protocol -v8.2.10
- differentiation_protocol -v1.3.3
- dissociation_protocol -v5.0.7
- enrichment_protocol -v2.2.8
- ipsc_induction_protocol -v2.0.4
- imaging_preparation_protocol -v1.0.4
- imaging_protocol -v11.0.5
- protocol -v6.3.7
- library_preparation_protocol -v4.4.4
- sequencing_protocol - v9.0.8

#### Changes

- Removed normothermic_regional_perfusion from donor_organism schema
- Added normothermic_regional_perfusion to death schema
- Changed development_stage from optional to a required field in donor_organism schema

## Staging 2018/12/19

### Upload Service

#### Version(s)

v3.3.0

#### Changes

* Post file endpoint to trigger checksumming
* S3etag column for file record in db

## Staging 2018/12/12

### Ingest

Version(s): 
* Broker v0.8.4.rc
  - Fix to connection reset error during spreadsheet import
  - Fix schema parsing, defaults to string if there is no items obj inside array field in schema
  - Added fix to ensure that import doesn't fail due to erroneous max_row count
  - Fixes to raising and logging error details

* Exporter v0.7.6.rc
  - Fix to DSS datetime version format
  - DSS API Authentication
  - More info on logs
  - Deploy new exporter secrets

* Validator v0.6.0.rc (same version)
  - Deployment config change to make validator point to the latest fastq validator image (fastq_utils:v0.1.0.rc)

* Staging Manager v0.5.3.rc
  - Remove 10s wait when creating upload area
  - Fix setting for retry policy, retrying for ~20min

* Ontology
  - Redeploying to pick up new ontology values

### Metadata Schema

Version(s):
cell_line.json: 9.0.1
cell_suspension.json: 8.6.2
channel.json: 2.0.0
contact.json: 6.1.4
donor_organism.json: 10.2.1
imaged_specimen.json: 2.0.2
imaging_protocol.json: 11.0.1
imaging_target.json: 3.0.0
library_preparation_protocol.json: 4.4.0
links.json: 1.1.4
organoid.json: 8.3.9
project.json: 9.0.4
sequence_file.json: 7.0.0
specimen_from_organism.json: 6.3.4
target.json: 1.0.1

- Changed molecule_ID to lower case in target.json Fixes #666
- Added new schema target.json to replace deprecated imaging_target.json. Fixes #641
- Changed technical_replicate_group_id to library_preparation_id. Fixes #262.
- Changed channel_id from string to array
- Changed name of the required field channel_name to channel_id
- Added optional field timecourse.
- Changed channel field type to array
- Fixed a bug in the links schema still referencing core instead of system
- Changed channel field type to array
- Added new optional fields nominal_length and nominal_sdev. Fixes #594.

### Upload Service

Versions v2.4.3->v3.1.0

Changes
upgrades: 
terraform to 0.11.10
Moto to 1.3.7
Boto to  1.9.44
Botocore to 1.12.44
Validation image to 11
Requests to 2.20.0 (safe version)
Checksummer image to 5
Add tenacity to checksummer reqs

- Create validation harness
- ValidatorHarness: make staged_file_path a pathlib.Path
- publish humancellatlas/upload-validator-base-alpine:17 as latest
- Create new env local, allow tests to run offline in local env
- Add errors and retry on tags to s3 object 
- Add endpoint /area/file endpoint that adds file to pre checksum sqs which triggers checksum daemon lambda
- Add Batch watcher daemon 
- runs on hourly schedule and checks for failed jobs, killing any relevant instances in that env and rescheduling the validation/csum job
- retry on boto3 batch describe_job 
- policy on batch watcher to invoke checksum daemon
- refetch jobs after killing instances
- Update to daily health check to output number of failed validation and checksum events in report.
- Update chalice policy for batch jobs 
- Update validation scheduler to return validation_id
- Refactor tests to make more dry
- Refactor: wrap database_orm db initialization code in a class
- Refactor: wrap common/database code in a class: UploadDB
- fix from queue.url to queue.id in retrieving csum sqs url
- remove correlation ID from log entries
- remove obsolete "make secrets"
- remove unused imports
- DB migration
- Add "FAILED" status to checksum_event and validation_event statuses
- Add docker_image field to validation_event
- Add original_validation_id field to validation_event
- Mark all historical "SCHEDULED" and "VALIDATING"/"CHECKSUMMING" events as "FAILED".

### Data Store

Version(s): 2018-12-12-17-56-10-staging.release

Changes:
- Grab collections owner from gcp credentials (#1769)
- returning manifest data on put /Bundle , working tests, changed dss-api.yml to reflect changes.
- Update staging environment (#1757)
- Staging uses its own ES cluster (previously sharing dev)
- Make ES index logging optional
- Validating version format is DSS_VERSION (#1698)
- Note requirement of privileged access in README.md (#1748)
- Updating Auth in readme (#1741)
- Use async state to catch/expose copy sfn errors (#1706)
- updating patch collection to deduplicate contents (#1725)
- Store and recover chunks of state in dynamodb (#1705)
- Update DSS_VERSION after deploy succeeds (#1724)
- Provide fine grained management of Lambda environment variables (#1723)
- replacing scan with search after for notifications. (#1676)
- Added Architectural diagram to readme (#1692)
- Reorganize deployment and auth section of readme (#1695)
- Drive dss-index with SQS instead of SNS (#1691)
- restrict access to put bundle and files (#1609)
- Retry join state in s3 copy sfn (#1687)
- Send GS copy client exceptions to fail state (#1674)
- Update docs for some env vars (#1678)
- updating authorized domains in prod (#1681)
- Send S3 copy client exceptions to fail state (#1643)
- Raw Search Page Limit  to 10 (#1652)
- Accommodate TF changes plus minor infra updates (#1673)
- Check GitLab status, instead of GitHub, in release.sh (#1641)
- DSS_AUTHORIZED_DOMAINS should be quoted (#1642)
- Increase the number of ES nodes (#1660)
- remove unsupported azure from swagger (#1649)
- Adding documentation for subscription PUT to handle duplicate notifications. (#1622)

Are there changes that require the DCP to in read-only mode, or maintenance mode during deploy? No

## Staging 2018/12/10

### Secondary Analysis

Pipeline-tools: v0.43.0

- Get expected cell count from 10x bundles instead of using a static value in the cellranger adapter WDL

## Staging 2018/12/06


### Secondary Analysis

Pipeline-tools: v0.42.1

- Update version of HCA CLI to use at least version 4.4.9 as a security precaution

### Metadata Schema

imaging_target.json: 1.1.0
imaging_protocol.json: 8.1.0

- Changed channel field to optional in imaging_target.json.
- Changed channel field to optional in imaging_protocolol.json


## Staging 2018/10/17


### Ingest
Core v0.7.6.rc

- Optimizing retrieval of biomaterials from mongo
- Fix to slowdown caused by synchronous UUID generation
- Logging when submission envelope is created and submitted
- Optimization in finding assay processes for export
- Misc. bug fixes
- Logging when submission envelope is created and submitted
- Optimization in finding assay processes for export
- Bug fixes

State-tracking v0.7.2.rc

- Fix to state tracking persistence

Broker v0.8.3.rc

- Fixed bug whereby file metadata updates fail if a file is uploaded prior spreadsheet upload

### Upload Service
Version: v2.4.0

- Faster checksumming for larger files: files up to 10GB (was 4GB) in size are now checksummed "in-line" (in Lambda instead of Batch)
- Daily health check for upload service
- Merge Lambda deployment buckets into a single bucket per environment
- Big Red Button: uploadctl up|down|status commands.

### Data Store
No changes

### Secondary Analysis
Version(s):
Lira v0.14.0
Pipeline-tools v0.36.0 (was v0.34.0)
- Have cellranger adapter WDL pass in max_cromwell_retries parameter to submit WDL
10x pipeline: cellranger_v1.0.0 (no 10x subscription active)
Smart-seq2 pipeline: smartseq2_v2.1.0 (was smartseq2_v2.0.0)
- Update zarr creation task
- Add wdl to build gencode and ensemble references for cellranger

### Azul
No changes

### Data Browser
No changes

### Metadata Schema
Version(s):

imaging_protocol: 8.0.3
sequencing_protocol: 9.0.3

- Added dcp_scale_test_pancreas6decades.xlsx spreadsheet
- Bug fix in imaging_protocol.json schema.
- Patch in sequencing_protocol.json schema (update to field description).


## Staging 2018/10/11


### Ingest
Core v0.7.4.rc
- Logging when submission envelope is created and submitted
- Optimization in finding assay processes for export
- Bug fixes


### Upload Service
Version: v2.3.12
- aws_rds_cluster_instance engine version bumped from 9.6.3 -> 9.6.8


### Data Store
Version(s): 2018-10-11-15-48-22-staging.release
- Raise sync exception when s3/gs presigned urls fail to resolve (#1637)
- Add retry to join task in s3copyclient sfn (#1635)
- Define GitLab prod release/deploy (#1634)
- Define GitLab test for large blob sync (#1633)
- Use new Terraform version in Docker GitLab image (#1626)
- Remove unnecessary lambda Get/List permissions for s3. (#1631)
- Fix scripts/release.sh --help (#1602)
- Lambda env vars are read from SSM during deploy (#1612)
- Adding environment variable documentation (#1618)
- Making notification logs less noisy (#1619)
- Adding info log messages to subscriptions (#1608)
- Remove remnants of docker config (#1606)
- Fixing the errors returned by auth failures (#1605)
- Moved documentation badges under title (#1604)
- Remove Travis deploy jobs (#1601)
- Update integration checkout bucket whitelist (#1592)
- Fix Swagger YAML Docstring formatting
- .gitlab-ci.yml: break up long line 
- Don't run tests when tags are pushed (#1599)
- Organize README into sections
- Update environment.prod (#1587)
- Reparameterize backend bucket (#1591)
- gitlab-cy.yml simplifications (#1590) 
- GS event relay: Get all available GRTC env vars in one go (#1586)
- Use dev Auth0 until prod Auth0 is available. (#1588)


### Secondary Analysis
Version(s):

Lira v0.14.0 (was v0.13.2)
- Update default 10x WDL config parameters in deployment script to reference CellRanger adapter WDL files
- Update SS2 WDL parameters in deployment script to includes the zarr utils analysis wdl
- Improve SS2 subscription query to use ontology IDs instead of the text field
- The scripts for making subscriptions are using the new HCA DCP Auth method to communicate with Data-Storage service now

Pipeline-tools v0.34.0 (was v0.28.2)
- Fix disk space for stage_files task in submission workflow
- Update the adapter WDL for Smart-seq2 to submit zarr files to ingest
- Improve the analysis result file format mapping, as well as add zarr to the mapping
- Add web_summary.html to CellRanger adapter outputs.
- Use metadata-api v1.0b4
- Add CellRanger adapter WDL
- Update SS2 analysis outputs in the SS2 adapter pipeline
- Instead of querying Cromwell during the submission, pipeline-tools is getting the versions of the pipelines directly from the WDL files.

10x pipeline: (no 10x subscription active)

Smart-seq2 pipeline: smartseq2_v2.0.0 (was smartseq2_v1.0.0)
- QC metrics more rationally grouped
- Expression data and QC metrics in Zarr format
- Fix out of disk space problem for Hisat2 tasks


### Azul
Version: 1247300708cd0a95f5b28a4525dd301b3fd005d9 (deployed/staging/2018-10-11__11-47)
* Address token deficit and surplus (fixes #390)
* Implement service support for projects tab (resolves #57)

### Data Browser
Version: 17dcbc18b499efa7ef6a11c5403b3b8501741f4f
- Deploy moved from Elastic Beanstalk to S3
- Selected Facet shows in URLs
- Facet Selector Drop Downs Scrollbars Removed

### Metadata Schema
No changes


## Staging 2018/10/03

### Ingest
* Exporter v0.7.4.rc
  - Reverted to 20 retries spaced a minute apart for operations on the DSS API
  - Using ingest's update timestamp for creating .json files in the DSS, averting needless duplicates
  - Polling DSS Files to confirm their full creation prior to creating a bundle containing said Files
* Staging Manager v0.5.2.rc
  - Set to use HTTP HEAD when checking for existence of an upload area
* Broker v0.8.2.rc
  - Fix to submission error message


### Upload Service
Version: v2.3.11

- Head request for upload area
- Gitlab prod fixes
- Change job definition to 4 vcpus for batch
- Fix for csum deployment lambda bucket name
- Fix for new version of Postgres

### Data Store
No changes

### Secondary Analysis
No changes

### Azul
Version: 67bd504c0eda2471c088fbb3fd6d89dde7b3b641

- Add FIFO queue between transformers and writer (resolves #181)
- Temporarily disable ill-configured autocomplete (connected to #362)
- Specimen documents have singleton `specimens` lists (connected to #312)
- File documents have singleton `files` lists (fixes #312)
- Add test case for analysis bundles with derived files (connected to #312)
- Fix file type summaries returning in files response (fixes #352)
- Fixed Spacing and Formatting (fixes #265)
- Fixed Naming and Formatting (fixes #265)
- Added Exception when the missing/wrong index is requested (fixes #265)
- Upgrade `hca` to 4.4.1 and `metadata-api` to 1.0b4 (resolves #309)
- Document deployment and promotion procedure (fixes #344)
- Increase ES bulk API threshold (fixes #343)
- Updating Elasticsearch instance volume size. (fixes #338)
- Add support for bundle deletions (fixes #45)
- Change default sort criteria to specimenId (fixes #227)
- Added summary endpoint for specimens (fixes #156)
- Add infrastructure to share dev es index (fixes #221)
- Add "null" counter to facets (fixes #99)
- Switch to SQS trigger (resolves #180)
- Casting totalSize to int (resolves #251)
- Replace `files` with `fileTypeSummaries` in /specimens (resolves #170)
- Removed piecharts endpoint (fixes #236)
- Upgrade to Chalice 1.6.0 (resolves #179)

### Data Portal
No changes

### Metadata Schema
No changes


## Staging 2018/09/19


### Ingest

* Core v0.7.3.rc
  - Fix bug in sending messages to state tracker when adding reference files in a secondary submission
  - Reduce timeout when sending state tracking messages
  - Updated secondary submission documentation

* State Tracker v0.7.1.rc
  - Reducing timeout before the actual submission state update happens
  - Concurrent hash map for document states

* Exporter v0.7.2.rc
  - Use latest schema for links.json

* Broker v0.8.1.rc
  - Added support for multiple ontology processing


### Upload Service

- Add /validations (retrieve validation status for all files in an upload area)
- Add /checksums endpoint (retrieve checksum status for all files in an upload area)
- Lambda checksum memory 3008 -> 960
- Only notify ingest if file checksummed
- Fix race condition for file upload


### Data Store

- Fix timeout handling for API lambda (#1555)
- Parameterize GCP checkout bucker viewers (#1553)
- Give GCP service account read access. (#1547)
- Remove scheduled CI build daemon (#1560)
- Retrieving user email from custom JWT claim or email claim (#1562)
- DSS read-only mode (#1568)


### Secondary Analysis

#### Lira and subscriptions
- Fix the domain for the TLS cert created for Prod.
- Add submit and hold variable for Falcon to deployment script.
- Streamline the lira variable by combining the lira version and the lira docker image tag.
- Fixing an issue with the service name being too long.
- Add kubernetes admin IAM policy to the deployment service account.
- Update version endpoint of Lira to include "cache_wdls" and "submit_and_hold" configuration values.
- Fix a syntax issue in the Lira config ctmpl file.

#### Pipeline-tools
- Update to use hca CLI version v4.4.0, which fixes changed the mechanism to throw exceptions when an error occurs.
- Add cromwell maxRetries runtime parameter to the submit wdl tasks "get_metadata" and "stage_files"


### Azul
- Hot fix: Work around CommonMark dependency issue (connected to #306)


### Metadata Schema

#### Ontology changes
- Fixed organ validation issue by including embryo and its children as allowed values

#### Miscellaneous
- Updated release process SOP
- Added Metadata Style Guide


## Staging 2018/09/07

### Ingest
Version: 
State Tracking v0.6.1.rc -> v0.7.0.rc
Core  v0.7.1.rc -> v0.7.2.rc
Exporter v0.7.0.rc -> v0.7.1.rc 

Changes:

* Core v0.7.2.rc
    * Optimizations regarding sending of unnecessary messages to the rabbit-mq broker
    * Integration with the state tracker’s HTTP API
    * Indexing on Process resources’ input and output biomaterials/files enabling faster bundle generation and export
* State Tracking v0.7.0.rc
    * Race condition bug fix whereby state updates were processed out of order
    * Added a HTTP API for processing state update messages
* Exporter v0.7.1.rc
    * Caching of previously retrieved documents for faster export time
    * Retrying 20 times with 1 minute between for idempotent requests to the DSS

### Upload Service

Version: v2.3.0 => v2.3.5

* Fixes to schema for get validation and checksum statuses
* Changing max vcpus for validation batch infrastructure to 512
* Fix for validating files with hashes
* Increase of validation job definitions to 2048mb and 2vCPUs
* Increase in checksum lambda memory to 3008mb to avoid lambda out of memory errors

### Data Store

Version: staging-2018-09-12-16-53-24.release

* get_file performs synchronously when possible (#1347)
* get_bundle only performs checkout when necessary (#1347)


### Secondary Analysis

* Lira v0.13.0 (was v0.12.1)
    * Changed and improved the deployment scripts
    * Turned on throttling (set submit_and_hold = true)

* Submission v0.28.0 (was v0.25.0)
    * Retry HTTP requests with a 409 status code
    * Use CaaS Prod within the Cromwell-metadata docker image, which is used in Submit WDL task
    * Adding md5 checksums to results bundle metadata is optional and turned off by default due to HumanCellAtlas/secondary-analysis#287


### Data Portal
No changes.

### Metadata Schema

Version(s):
* biomaterial_core: 7.0.3
* file_core: 5.2.4
* process_core: 9.0.2
* project_core: 7.0.3
* protocol_core: 5.2.4
* cell_morphology: 6.1.3
* death: 5.3.3
* familial_relationship: 6.0.2
* growth_conditions: 6.4.1
* human_specific: 1.0.5
* medical_history: 5.2.4
* mouse_specific: 1.0.4
* preservation_storage: 5.3.3
* state_of_specimen: 5.2.6
* timecourse: 1.1.3
* biological_macromolecule_ontology: 5.3.2
* cell_cycle_ontology: 5.3.2
* cell_type_ontology: 5.3.2
* cellular_component_ontology: 1.0.2
* development_stage_ontology: 5.3.2
* disease_ontology: 5.3.3
* enrichment_ontology: 1.2.3
* ethnicity_ontology: 5.3.4
* instrument_ontology: 5.3.2
* length_unit_ontology: 5.3.2
* library_amplification_ontology: 1.2.2
* library_construction_ontology: 1.2.2
* mass_unit_ontology: 5.3.2
* microscopy_ontology: 1.0.1
* organ_ontology: 5.3.3
* organ_part_ontology: 5.3.2
* process_type_ontology: 5.3.2
* protocol_type_ontology: 5.3.2
* sequencing_ontology: 1.1.2
* species_ontology: 5.3.2
* strain_ontology: 5.3.3
* time_unit_ontology: 5.3.2
* purchased_reagents: 6.0.3
* 10x: 1.0.3
* barcode: 5.2.4
* insdc_experiment: 1.1.4
* plate_based_sequencing: 1.0.3
* contact: 6.1.3
* funder: 1.0.3
* publication: 5.2.4
* channel: 1.0.1
* imaging_target: 1.0.2
* links: 1.1.3
* provenance: 1.0.3
* cell_line: 8.6.2
* cell_suspension: 8.6.1
* donor_organism: 10.1.1
* imaged_specimen: 1.0.1
* organoid: 8.3.6
* specimen_from_organism: 6.3.1
* analysis_file: 5.3.4
* image_file: 1.0.1
* reference_file: 2.2.5
* sequence_file: 6.5.2
* supplementary_file: 1.1.5
* analysis_process: 8.0.3
* process: 6.0.2
* project: 9.0.2
* analysis_protocol: 8.0.3
* aggregate_generation_protocol: 1.1.5
* collection_protocol: 8.2.6
* differentiation_protocol: 1.3.0
* dissociation_protocol: 5.0.3
* enrichment_protocol: 2.2.5
* ipsc_induction_protocol: 2.0.1
* imaging_preparation_protocol: 1.0.1
* imaging_protocol: 8.0.2
* protocol: 6.3.5
* library_preparation_protocol: 4.3.2
* sequencing_protocol: 9.0.2

Changes:
* Schema changes
    * migrated from draft-04 to draft-07 JSON
    * title attribute changed to sentence case schema name
    * name attribute added as programmatic schema name
    * New schemas: cellular_component_ontology.json, channel.json, imaging_target.json, imaged_specimen.json, image_file.json, imaging_preparation_protocol.json, microscopy_ontology.json
* Field changes
    * “stem cell” added to enum for `cell_line.cell_line_type` field
    * New required field: `imaging_protocol.channel`
    * New required field: `imaging_protocol.imaging_target`
    * New required field: `imaging_protocol.microscopy_technique`
    * New required field: `imaging_protocol.magnification`
    * New required field: `imaging_protocol.numerical_aperture`
    * New required field: `imaging_protocol.overlapping_tiles`
    * New required field: `imaging_protocol.pixel_size`
    * New optional field: `imaging_protocol.immersion_medium_type`
    * New optional field: `imaging_protocol.microscope_setup_description`
    * New optional field: `imaging_protocol.immersion_medium_refractive_index`
    * New optional field: `imaging_protocol.number_of_tiles`
    * New optional field: `imaging_protocol.tile_size_y`
    * New optional field: `imaging_protocol.tile_size_x`
    * New optional field: `imaging_protocol.z_stack_step_size`
    * New optional field: `imaging_protocol.number_of_z_steps`
    * New optional field: `growth_conditions.culture_environment`
    * New optional field: `supplementary_file.provenance`
    * Changed field name: `donor_organism.disease` to `donor_organism.diseases`
    * Changed field name: `specimen_from_organism.disease` to `specimen_from_organism.diseases`
    * Changed field name: `differentiation_protocol.differentiation_media` to `differentiation_protocol.media`
    * Changed field name: `differentiation_protocol.differentiation_small_molecules` to `differentiation_protocol.small_molecules`
    * Changed field name: `differentiation_protocol.differentiation_target_cell_yield` to `differentiation_protocol.target_cell_yield`
    * Changed field name: `differentiation_protocol.differentiation_reagents` to `differentiation_protocol.reagents`
    * Changed field name: `differentiation_protocol.differentiation_target_pathway` to `differentiation_protocol.target_pathway`
    * Changed field name: `differentiation_protocol.differentiation_validation_method` to `differentiation_protocol.validation_method`
    * Changed field name: `differentiation_protocol.differentiation_validation_results` to `differentiation_protocol.validation_result`
    * Changed field name: `ipsc_induction_protocol.induced_pluripotent_cell_induction_method` to `ipsc_induction_protocol.ipsc_induction_method`
    * Changed field name: `ipsc_induction_protocol.induced_pluripotent_cell_induction_kit` to `ipsc_induction_protocol.ipsc_induction_kit`
    * Changed field name: `ipsc_induction_protocol.induced_pluripotent_cell_induction_produced_in_house` to `ipsc_induction_protocol.ipsc_induction_produced_in_house`
* Ontology changes
    * disease_ontology.json now accepts top-level values (MONDO:0000001, PATO:0000461) as valid
    * organ_ontology.json now accepts top-level values (UBERON:0000062, UBERON:0000179) as valid
    * strain_ontology.json now accepts top-level value (NCBITaxon:10090) as valid
    * ethnicity_ontology.json now uses HANCESTRO ontology


## Staging 2018/09/05

### Ingest
No changes.

### Upload Service
Version: v2.3.0

* Fix: allow filenames to have a hash in them
* Add SQS queue between S3 object creation and checksum Lambda function (better scalability)
* Stop using Chalice to deploy checksum Lambda.  Package it ourselves.  Allow Terraform to deploy it.
* Terraform: move Upload Service deployment to its own VPC
* Terraform: manage RDS security group
* Terraform: unlink Makefile and hard-code deployment stage

### Data Store
Version: staging-2018-09-05-22-09-40.release

* Improve error response documentation for PATCH /collections (#1490)
* Interpolate cli endpoint (#1502)
* Using Auth0 for authentication (#1542)

### Secondary Analysis

* Lira v0.12.1:
    * Fix an issue with the subscription queries which allows result bundles to trigger notifications

* Falcon v0.1.3:
    * Make query for Cromwell workflows configurable

### Data Portal
No changes.

### Metadata Schema
No changes.

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
