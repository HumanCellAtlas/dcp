# Release Notes

<!-- newest release at the top please) -->

# Prod 2019/04/23

## Azul 
### Version: d7c2e6d0dde94f884da91a8a77e9defc8a5a8c22
* fc06b2e Add facet for sequencing_protocol.paired_end (#867)
* fe2f9fe Increase CloudWatch log retention to 1827 days (#832)
* d63ec67 Indexer logs the time needed to download bundle metadata
* b622852 Fix: /repository/…/{uuid} only works for projects (#879)
* 5ca1f11 Prevent tagging on wrong deployment
* 8c62e84 Filters used in IT are more portable between deployments
* fe8ee3c Filters used in IT are more portable between deployments
* ae3d596 Support for multiple files per BDBag TSV row (#866)
* 67d3c5f Refactor manifest TSV generation
* dd7ff97 Added script for uploading metadata TSVs to a S3 bucket (#860)
* 3a3b394 Add --no-ff flag to README section about releases (#891)
* 1b9e0af Add timestamp to integration test logging (#858)


# Prod 2019/04/16

## Ingest
### Ingest-ui v0.9.1
* Presenting all validation errors

## Secondary Analysis
### Pipeline-tools: v0.48.2
* Comment out conditions for checking jenkins tests in pull approve
* Add snyk check
* Add security.txt file to indicate where security issues should be logged
* Update and add settings for the linting test
* Pass empty drops output to submit wdl

## Azul 
### Version: 4847ce79732b4606332fde9439c7cd64241308b6
* 4847ce79 Exclude old Mouse Melanoma project on `prod` (#895)
* 5523064b Minimal support for imaging data sets (#881)
* b344ea9c Rename `es_results` to `hits` in indexer tests
* 9ab393a7 Add test for filtering by project UUID aka `projectId` (#796)
* fe5b68e2 Include DRS endpoint in integration test (#789, #790)
* 760388bc Work around AWS Step Function's eventual consistency (#877)
* 2339f348 Don't require new projects to be whitelisted in staging


# Prod 2019/04/09

## Ingest
### Ingest-ui v0.9.0
* Configuring whitelisted domains thru env vars
### Ingest-validator v0.6.3
* Robust nack()ing of unprocessable messages

## Secondary Analysis
### Optimus v1.0.0
* The first major version release for the Optimus pipeline
### Falcon v0.3.0 
* Add status endpoint to check health of falcon threads
* Add snyk github integration
* Add formatter and linting check in tests

## Data Portal
### Azul deployed/prod/2019-04-09__08-59 (d91f3b10)
* Fix: staging subscription query
* Don't require new projects to be whitelisted in staging
* Merge branch 'develop' into integration
* Run `terraform plan` before `apply -auto-approve` on Gitlab
* Include `prod`'s URL shortening bucket in security boundary
* Grant Gitlab write access to Elasticsearch log groups (#825)
* Add Gitlab instance for `prod` (#748)
* Fix merge error in Terraform config for Gitlab
* Update Gitlab CE from 11.8.0 to 11.8.3
* Add cell_suspension.selected_cell_type (#800)
* Delete file_metadata_to_csv.py (#848)
* Hard-code subscription ID in synthetic re-indexer notifications (#382)
* kibana-proxy.pl uses containers for signing proxy and Kibana
* Clean-up README.md
* Fixed error responses for `/repository/{entity}/{uuid}` endpoints (#355, #448)
* Update cheatsheet for deployment / promotion (#797)
* Revert "Have Gitlab create deployment tags (on gitlab fork)"
* Have Gitlab create deployment tags (on gitlab fork)
* Don't require new projects to be whitelisted in staging
* Exclude old Tissue Sensitivity project on `prod` (#870)
* Skip obsolete bundle versions when reindexing (#868)

## Metadata Schema
### module/protocol/channel.json - v2.0.3
### type/protocol/imaging/imaging_protocol.json - v11.0.13
### type/project/project.json - v11.1.0
* Added optional biostudies_accesssion field. Fixes #852.




# Prod 2019/04/02

## Ingest

### Broker v0.8.9
* Fixed uploading of file metadata

### Core v0.9.0
* Updated process of assigning UUIDs to exported bundles
* Fixed format of version timestamp

### Exporter v0.8.0
* Updated handling of bundle UUID and version timestamp
* Added handling for duplicate export messages

## Upload Service
Version v4.2.6
* Clean deletion of unused environments
* Remove lock/unlock API functionality
* Switch Batch cluster instance types from "m4" to "m5"

## Secondary Analysis

### Cromwell-tools v1.1.1
* Add on_hold parameter to start_workflow
* Add workflow validation capability
* Add Sphinx autodoc and readthedocs hook
* Bugfix: Allow workflows without labels to be executed
* Bugfix: Fix docker container build issues
* Add a new function to query workflows.
* Add a new function to release workflows from status On Hold to Submitted.
* A breaking refactoring work on both the CLI and API.
* More sophisticated unit tests.
* Support both Python2 and Python3, having tests run on both versions.
* Updated ReadMe file and docstrings.
* For /submit endpoint, we support both path to the file and file contents as inputs now.
* We have a quickstart example Jupyter Notebook now.
* Update requests to avoid security issues.
* Fix API calls in CLI.
* We have accessory tools with cromwell-tools, such as the workflow monitoring script.
* Other slight improvements and bug fixes.
* Fix a bug with the service account key that prevents users from using any authentication methods.
* Fix a bug with /validate command in CLI.
* Fix a bug with /health endpoint in API.
* Improve the output of the CLI commands.
* Update the documentation, quickstart Jupyter notebook, and docstrings.
* Update the authentication dependency from the deprecated oauth2client to google-auth.
* Allow no-auth with Cromwell.
* Improve the help messages of CLI and add shorthands for submit command.
* Fix an issue that can stop local file from being normally processed.
* Fix the failing test by cleaning up the Dockerfile that relies on Oracle Java installer and move to use OpenJDK instead.
* Take the retry policy based on tenacity out from the cromwell-tools for clarity.
* Add token checker before making the header to avoid token expiration with OAuth.
* Fix a bug that prevents generating correct pagination parameters for POST /query endpoint.
* Update the pull-request-template.
* Fix a bug that prevents submitting a zipped file as a dependency of a workflow.

### Lira v0.19.0
* Update field name in subscriptions (library_construction_approach -> library_construction_method )
* Use latest version of cromwell-tools

### Pipeline-tools v0.48.1
* Update format of the Cromwell url used to fetch metadata
* Replace deprecated setup.py dependency_links
* Remove unused Cromwell metadata docker folder
* Update the adapter workflow for Optimus pipeline, tested with 4k_pbmc dataset.
* Remove the outputs field from the analysis_process metadata generated by the pipelines.
* Fix payload for adding file references via the ingestion service API

### Falcon v0.2.0
* Refactor and cleaning up deployment-related files.
* Update cromwell-tools version.
* Update example config.json in README

## Data Portal

### Azul  deployed/prod/2019-04-02__09-02 (20e526b6)
* 5b343a94 Fix manifest integration test on `integration` (#847)
* a314e95a Include Grafana dashboard definition for Data Portal and Browser (#815)
* 1df15f3c Updates Grafana dashboard uid and name for Azul (#816)
* ef3e8f7e Names of TSV files in BDBag use plural (#842)
* 5ced99b6 Omit content disposition header from BDBag responses (#841)
* 312f6d9f Skip indexing part of integration test on `prod`
* 29e29b4d Consolidate Elasticsearch instances for lesser main deployments (#809)
* 91d920f6 Pin dcplib to 1.5.1 as 1.6.0 breaks the build
* b5ac26ee Merge branch develop into integration
* b88b2d35 Add BDBag support to new manifest endpoint (#827)
* 178c74b8 Make manifest column names consistent with metadata schema (#792)
* fc5e3b3c Relax assertion on `file_version` in DRS endpoint (#828)
* 3f8b8d3a Moved bundle deletion functionality to AzulClient
* 3d23ee20 Require auth for notifications (#96)
* 2d791b15 Changing definition of self.indexer_url in AzulClient
* 5c7ce143 Renamed Reindexer class to AzulClient
* ce5cdd3a Check BDBag endpoint during integration test (#565)
* 7f79d89a Enable monitoring and Grafana publishing in sandbox deployment
* ea159585 Distinguish Azul and Data Portal monitoring resources (#787)
* 5516f8be Consolidate Elasticsearch instances for lesser main deployments (#809)
* 64f24692 Pin dcplib to 1.5.1 as 1.6.0 breaks the build
* 37a47550 Skip indexing part of integration test on `prod`
* dbe86cbd Fix: DSS proxy test fails on integration deployment
* 720478a0 Refined timeout conditions (#785)
* 8aa368ec Retain original file name when downloading resolved DRS object
* 16692311 Include DSS checkout buckets in security boundary
* dda157f7 DSS checkout bucket name changed in integration and staging
* c0cc1e01 Add manual job for reindexing on Gitlab
* 14ad0e11 Move subscription from integration test; add to regular build steps
* 55670a4b Fix invalid regex in authenticator.py; cosmetics
* 47578ccd Refactor DRS support, fix DRS URLs (#774)
* 69f80136 Rename `azul.dos` to `azul.drs`
* 64195230 Add non-fetch variant of DSS proxy; add server-side wait (#778)
* da5b6161 Add project accessions fields (#714)
* 79f378b9 Add all metadata to manifest (#720)
* dd6ce916 Blacklist Meyer dataset in `prod` (HumanCellAtlas/data-store#1976)
* ce363155 Fix handling of missing permissions boundary (#239)

## Metadata Schema
### state_of_specimen - v6.0.0
* Changed array field names (gross_image and microscopic_image) to be plural to adhere to Style Guide. Fixes #792.
### insdc_experiment - v2.0.0
* Changed insdc_experiment to insdc_experiment_accession to adhere to Style Guide. Fixes #809.
### plate_based_sequencing - v2.0.0
* Changed cell_quality to well_quality. Fixes #809.
### cell_line - v11.0.0
* Changed date_established from date-time to date format. Fixes #821.
### cell_suspension - v10.0.0
* Changed cell_quality to well_quality. Fixes #809.
### specimen_from_organism - v9.0.0
* Changed organ_part to organ_parts to adhere to Style Guide. Fixes #648.
* Changed array field names (gross_image and microscopic_image) to be plural to adhere to Style Guide. Fixes #792.
### sequence_file - v8.0.0
* Change insdc_run to insdc_run_accessions to adhere to Style Guide. Fixes #805.
### analysis_process - v9.0.0
* Removed required outputs fields to adhere to metadata model. Fixes #664.
### process - v7.0.0
* Changed insdc_experiment to insdc_experiment_accession to adhere to Style Guide. Fixes #809.
### collection_protocol - v9.0.0
* Changed protocol_reagents and collection_method to reagents and method to remove redundancy to adhere to Style Guide. Fixes #807.
### dissociation_protocol - v6.0.0
* Changed protocol_reagents and dissociation_method to reagents and method to remove redundancy to adhere to Style Guide. Fixes #807.
### library_preparation_protocol - v6.0.0
* Changed nucleic_acid_source field to be required. Fixes #824.
* Changed library_construction_approach to library_construction_method to be consistent with other protocols. Fixes #807.
### sequencing_protocol - v10.0.0
* Changed sequencing_approach to sequencing_method to be consistent with other protocols. Fixes #807.
### project - v11.0.1
### image_file - v1.0.4
### ethnicity_ontology - v5.3.8
### contact - v6.1.5
### channel - v2.0.2
### target - v1.0.9
### donor_organism - v14.0.7
### imaging_preparation_protocol - v2.0.3
### imaging_protocol - v11.0.12
### human_specific - v1.0.10
### medical_history - v5.2.8
### preservation_storage - v6.0.2
### module/process/sequencing/plate_based_sequencing.json - v3.0.0
* Changed well and plate ID to label. Fixes #837.
### type/biomaterial/cell_suspension.json - v11.0.0
* Changed well and plate ID to label. Fixes #837.




# Prod 2019/03/19

### Ingest

#### Validator v0.6.1
* Typescript
* Fixed bug where Files would be stuck in validating if metadata was missing(i.e files uploaded before complete spreadsheet import)
* Asserting that Files aren’t already validating before requesting file-validation
* No longer triggering file-validation if a validation job has already been completed for the same checksums

#### Core v0.8.5
* Added ValidationJobs to track running/completed file-validation jobs
* Bug fix attempting to parse property migration files from the Schemas bucket

#### Ingress
* Using HTTP->HTTPS redirection

### Azul deployed/prod/2019-03-19__08-29, e3e6baa0
* 96dfd2f9 Fix: DSS proxy test fails on integration deployment
* c0b82d25 Prevent echoing environment variables containing secrets
* 53e40c09 Gitlab posts status check on Github
* 104ec775 Add missing Gitlab permissions for deploying a main branch
* e8e044a6 Improve integration testing of subscriptions
* 3de56679 Add sandbox deployment for validating PRs and CI/CD experiments
* c8dd5483 Document CI/CD on Gitlab
* 1202d507 Improve `make clean` and clean cached HCA swagger spec
* a26d4619 Force destruction of non-empty buckets if applicable
* ff217aaa Minor cosmetic fixes
* e28d3599 Continuous deployment for lesser environments (#239)
* 1f795b42 Add `auto_apply` and `auto_deploy` targets to terraform/Makefile
* 3400fd38 Add AWS service model and script that produces it
* a30cb73e Gitlab builds custom Docker image to run actual build on
* 8bed2fe9 Ensure that tests don't use instance profile credentials
* 280a3a1b Fix: Manifest requests use wrong type for Retry-After
* 1772f7da Integration test honors Retry-After header (#752)
* caf7fb0f Cosmetic fixes to integration test
* 9ff12972 Validate syntax for incoming notifications (#736)
* 973b28e7 Changed notification endpoint response status code from 200 to 202
* eb744299 Include DOS file URL in BDBag (#749)
* 4adccda1 Removed duplicate `indexer_endpoint` property in Config (#728)
* a485f3a2 Fix sorting by `fileSize` in service (#713)
* b66023d1 Pass `subscription_type` when subscribing to DSS (#771)
* 921c6f7a Fix `sample_id` to be specimen's `document_id` (#744)
* 2bbd08df Fix bdbag upload to S3 (#743)
* 06ca56c7 Test deletion of updated bundle
* 54eb3cde Test deletion of bundle sharing entities with non-deleted bundles (#424)
* f82cc6f7 Refactor azul.config so that `azul` doesn't import `azul.deployment`
* d1158705 Convert static config properties to attributes
* 4876f101 Separate out Terraform state related to Gitlab resources (#239)
* 971e8d1e Remove duplicated config properties
* 4ff01390 Pass `subscription_type` when subscribing to DSS (#771)
* c6413e43 Blacklist Meyer dataset in `prod` (HumanCellAtlas/data-store#1976)


## Prod 2019/03/12

### Ingest

#### Broker v0.8.8
* Fix handling of file metadata when data file is uploaded first

#### Core v0.8.4
* authentication related security related patches

### Upload Service v4.2.3
* Cleanup job definitions after each deployment
* Disable batch watch in terraform
* Update terraform version to 0.11.11.

### Data Store 2019-03-12-15-15-14-prod.release
* Change regex for PUT file/{uuid}. (#1926)
* Fix scripts/populate_lambda_ssm_parameters.py (#1919)
* Changed PUT files/{uuid} regex pattern to support slashes with caveats.  Added testing for good and bad paths.
* Default subscription is JMESPath (#1915)
* L2 Health Checks (#1868)
* Log API exceptions (#1912)
* Reduce checkout ttl since caching is functional (#1903)
* removed TEST_USER buckets, added mocking to tests (#1908)
* added CHECKOUT_CACHE_CRITERIA to lambda env (#1907)
* added TEST_USER to envsubst (#1906)
* Metadata caching build deploy var (#1905)
* Fixes to add new infra to terraform. (#1904)
* Metadata Caching. (#1887)
* changed ci-cd.json for ddb query (#1898)
* Scale up the prod ES domain (#1883)
* Revert "Add HTTP request handler preconfigured with timeout and retry policies"
* Basic notifications with JMESPath filters and redrive queue (#1822)
* Fix import typo in scripts/tombstone_bundles.py (#1888)
* Add HTTP request handler preconfigured with timeout and retry policies

### Secondary Analysis, Lira: v0.18.1
* Make the subscription query for 10x v2 data more specific.
* Update the version of Connexion App and standardize the Lira API.
* Update the Swagger UI of Lira, which is the /ui endpoint of Lira.
* Update the controllers of Lira to adapt to the new API definitions.
* Update the Lira readme and add new badges.

### Azul f54b6927 (deployed/prod/2019-03-12__08-17)
* 971b4452 Pass `subscription_type` when subscribing to DSS (#771)
* bf9d799e Mark canned bundles as generated
* ae48aaa4 Change organ_part to an array (#699)
* c0937a7d Fix deletion of bundles with > 10 entities (#734)
* 2c2522d4 Test deletion of bundles with > 10 entities (#734)
* fc53e914 Fix bdbag manifest test to be order independent
* 5bc566bb Use fewer shards for aggregate index (#680)
* d195fe91 Copy `manifest` as `bdbag` in request_config.json (#740)
* 3e5c8aec Add health check for data portal (#731)
* 8e67a377 Script to simulate a deletion notification (#723)
* 6d7f807b Added `reindex` to changelog entry for #604
* 61518602 Export manifest in BDBag to Terra (#604)
* 4c0a6a8c Document how to reset an ongoing indexing operation (#715)
* ad1c60a6 Fix: SQS trigger initially disabled (#335)
* 51c06674 Mention `make clean` in deployment cheat sheet
* 916b61d0 Fix pastie error from 576f8546f89fc39148a455ee1b0eb5a4baa360fd
* 576f8546 Configure API Gateway logging with Terraform (#653)
* 2584cad8 Rename API Gateway Terraform file
* 1d83aceb Improve deployment and promotion cheat sheet
* e2ed1be5 Rename integration test target
* 21ee5672 Enforce that main deployment matches protected branch
* a7dbce6c Various Makefile fixes
* b0c17b83 Prototype exporting carts to DSS collections (#627)

### Metadata Schema
* No metadata schema updates.
* Updates to 2 infrastructure testing spreadsheets:
  * infrastructure_testing_files/current/dcp_integration_test_metadata_1_10X_bundle.xlsx
  * infrastructure_testing_files/current/dcp_integration_test_metadata_1_SS2_bundle.xlsx

## Prod 2019/03/05

### Ingest

#### Broker v0.8.7
* Bug fixes in the importer: trailing space and number field conversion

#### UI v0.5.4
* Show linking progress in the UI
* Upgrade to component versions

### Azul

Version: deployed/prod/2019-03-05__08-31 (c56f00698ef8bff00efc3d1c72300f6f46fd5203)

* 2d8a701f Delete empty aggregates (#709)
* c88434b2 Prioritize organoid organ fields (#695)
* c815bc8b Deploy Grafana dashboard during `make terraform`
* 7817477a Migrate monitoring resources from dcp-monitoring (#622)
* c81bde06 Rename `AZUL_ENABLE_CLOUDWATCH_ALARMS` to `AZUL_ENABLE_MONITORING`
* 94ca44e1 Refactor app.py with individual services (#678)
* 3885e511 Implement the integration with Fusillade (#58)
* d5a19a01 Ignored everything in lambdas/\*/vendor except 'azul'
* 354a129f Fix cheat sheet in README to reflect 904883e
* 904883e5 Fix deployment issues with `python -m venv` and make it the default (#340)
* b5edf68c Implemented the default cart logic (#629)
* 12da6c1c Blacklist test projects in prod
* 494c49ec Sync threads more reliably in concurrent indexer test (#696)
* 97214c9c Blacklist test projects in prod
* aae9244c Add rudimentary script for counting bundles


## Prod 2019/02/20

### Ingest

#### Broker v0.8.6
* Utilizing submission envelope's link/edge counter

#### Core v0.8.3
* Added submission envelope field to track number of expected links/edges in the metadata graph
* Hotfix to use different environment variables for user and service JWTs

### Upload Service
* Added support for paired file validation
* Add retry around loading files from upload area (fixes scale test issue)
* Put sqs between upload api and adding to validation batch queue
* Fix checksumming to allow for simultaneous file upload and reliability of checksum tags on s3 objects.
* Communicating with Ingest via HTTPS API endpoint instead of RabbitMQ

### Data Store 2019-02-20-16-05-58-prod.release
* adding current stage to audience (#1865)
* Fix daemons/dss-sync-sfn/Readme.md typo (#1882)
* Use jq -r instead of shelling out to Python (#1873)
* Notification sent out for all versions of a deleted bundle (#1872)
* Fix typo in Swagger doc (#1867)
* [Easy] Sync logs INFO instead of ERROR for existing keys (#1870)
* Allow custom handlers in local test server. (#1863)
* Add s3:GetObjectTagging permissions to the visitation lambda explicitly. (#1869)
* moved ADMIN_USER_EMAILS to be stored within AWS SecretManager (#1829)
* Search when Version is None (#1862)
* Ignore cache objects when syncing (#1861)
* Added X-AWS-REQUEST-ID to chalice API (#1845)
* Fixed paging with bundle tombstones (#1846)
* adding delete and tombstone notifications to smoke test (#1856)
* [Easy] Use correct document when notifying on delete (#1851)
* Update domovoi and change naming to reflect changes in domovoi. (#1847)
* adjust infra make clean (#1830)
* Adding Source IP and Decoded JWT to logs (#1839)
* Change staging bucket names to encrypted buckets. (#1840)
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

### Secondary Analysis

#### Lira v0.17.0
* Authenticate Cromwell VMs with the Cromwell-as-a-Service (CaaS) service account by using the “google_compute_service_account” workflow options parameter

#### Pipeline-tools v0.46.1
* Standardize Cromwell timestamps to follow the date-time format required by the analysis process JSON schema
* Use the default application credentials of the VM when requesting metadata from Cromwell instead of storing the JSON key in a private docker image
* Use JWT created from CaaS service account for authentication to Ingest API


### Metadata Schema
biomaterial_core - v7.0.5
cell_morphology - v6.1.6
human_specific - v1.0.9
mouse_specific - v1.0.7
preservation_storage - v6.0.1
timecourse - v2.0.1
barcode - v5.2.6
plate_based_sequencing - v1.0.6
channel - v2.0.1
target - v1.0.6
links - v1.1.5
cell_line - v10.0.4
cell_suspension - v9.0.0
donor_organism - v14.0.3
maged_specimen - v2.0.7
organoid - v10.0.2
specimen_from_organism - v7.0.3
analysis_file - v5.3.6
image_file - v1.0.3
reference_file - v2.2.10
supplementary_file - v1.1.8
analysis_process - v8.0.8
process - v6.0.7
project - v11.0.0
analysis_protocol - v8.0.7
aggregate_generation_protocol - v2.0.0
collection_protocol - v8.2.11
dissociation_protocol - v5.0.8
enrichment_protocol - v2.2.9
imaging_preparation_protocol - v2.0.1
imaging_protocol - v11.0.9
protocol - v6.3.9
library_preparation_protocol - v4.4.6
sequencing_protocol - v9.0.11
biological_macromolecule_ontology - v5.3.4
cell_cycle_ontology - v5.3.5
cell_type_ontology - v5.3.5
cellular_component_ontology - v1.0.4
development_stage_ontology - v5.3.5
disease_ontology - v5.3.7
enrichment_ontology - v1.2.5
ethnicity_ontology - v5.3.7
instrument_ontology - v5.3.5
length_unit_ontology - v5.3.4
library_amplification_ontology - v1.2.4
library_construction_ontology - v1.2.4
mass_unit_ontology - v5.3.4
microscopy_ontology - v1.0.4
organ_ontology - v5.3.7
organ_part_ontology - v5.3.4
process_type_ontology - v5.3.4
protocol_type_ontology - v5.3.4
sequencing_ontology - v1.1.4
species_ontology - v5.3.4
strain_ontology - v5.3.5
time_unit_ontology - v5.3.4

* Changed total_estimated_cells to estimated_cell_count.
* Added timecourse field to cell_suspension schema.
* Changed familial_relationship field to be plural.
* Changed accession fields to arrays and changed corresponding field names in project schema.
* Added required model_organ field to cell line schema.
* Removed organoid_type field from organoid schema.
* Changed field names in aggregate_generation_protocol.


## Prod 2019/02/12

### Ingest

#### Broker v0.8.5.rc

* Reporting all import errors to the submission envelope

#### Core v0.8.1.rc

* Bug fixes in JSON parsing upload-service messages
* Logging auth failures

### Data Browser

### Azul

These changes were actually deployed on 02/05/2019 but release notes weren't published then.

Version(s): deployed/prod/2019-02-05__16-31, 959e886d2b1c3aa79123769413e60159fe373379

* 959e886 - (HEAD -> prod, tag: deployed/prod/2019-02-05__16-31, origin/prod) Blacklist test projects in prod
* 4376e31 - Upgrade to metadata-api 1.0b9
* 1ee8a82 - Implement integration test (#262)
* 9c32e93 - Make default sort specific to each entity type (#683)
* 5275671 - Temporarily disable gitlab in prod
* 38f0858 - Blacklist test projects in prod from 1/22/2019
* 78e9511 - Fix misc typos and formatting in README
* 193ffcc - Add Locust script for scale testing (#542)
* a8fd104 - Add GA4GH Data Repository Service (DRS) GET for files (#638)
* a2313a4 - Fix: Health check tests only pass with `dev` selected (#670)
* 5289bfd - Move to Azul-specific bucket for Terraform state (#645)
* 5b14c64 - Blacklist test projects in prod from 1/22/2019
* 56abed4 - Move to Azul-specific bucket for Terraform state (#645)

### Metadata Schema

Version(s):

* imaging_preparation_protocol.json - v2.0.0
* project.json - v10.0.0
* specimen_from_organism.json - v7.0.0
* funder.json - v2.0.0
* preservation_storage.json - v6.0.0

Functionality changes:

* change enum list for storage_method to remove commas from values
* changed grant_id and funder_name to be required
* changed funders to be required


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
