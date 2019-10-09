# Release Notes

# Staging 2019/10/09

## Ingest
### Core (dfdcbe0)
* Lazy load DB Refs for performance improvements
* Validator (9ddaeaf)
* Fixes for retries
* Return Validation Report
### UI (2e1cd40)
* Security Fixes
### Client (2787fe7)
* Fix to return all files in get_bundle
* Fix importer code
* Use new SchemaTemplate SchemaParser
* Broker (810771c)
* Exporter (d75dee7)
* Staging Manager (47cbd64)

## Secondary Analysis
### Lira: v0.22.3
* Write the timestamp to inputs for adapters
* Update the SmartSeq2 query to match mouse data and remove the unnecessary "should" clause
* Update testing data to reflect moving adapter pipelines into a new repo
* Update scripts that get/create/delete DSS subscriptions to use elasticsearch as the default query type
* Update pipeline-tools version to fix getting metadata from the production data store
* Add config flag for testing mode
* Add hash-id backfill script

### Adapter-pipelines [formerly part of pipeline-tools]: v1.1.0
* Add the ability to disable call-caching in the prep task using a timestamp parameter
* Remove file format input parameter (moved into the pipeline-tools code)
* Migrate the following existing adapter pipelines and associated inputs from the pipeline-tools repo:
- optimus
- cellranger
- smartseq2-paired-end
- smartseq2-single-end
* Migrate the submit pipeline from the pipeline-tools repo.
* Add readme files for the repo and the pipelines added to the repo.

## Azul
### Version(s): 38a5d8222232a2c43492ba06a70ddc10c9ba5500
* 58d3124d Fix deployment destruction, make example use DSS integration (#1334, PR #1336)
* ba4f1a39 Remove `reindex.py --sync` and suppress deletions in TEST_MODE (#1276, PR #1310)
* 70703f27 Monitor latency for Azul health checks (#1151, PR #1321)
* 9805f3d5 Ensure tearDown runs when tests are cancelled (#1298, PR #1300)
* 0d1f0330 Cache health check response to reduce service load (#1224, PR #1297)
* b263edaf Prevent signature expiration in copy bundles script (#1325, PR #1326)
* 572d62c9 Fix: CloudWatch Alarm resolution does show up on Slack (#1233, PR #1322)
* 5b80bff6 Rename `tsv` format to `compact` & `bdbag` to `terra.bdbag` (#1086, PR #1306)
* 207f1963 Fix: DSS staging bucket swap (PR #1331)

# Staging 2019/10/03
## Ingest
### Version(s):

### Broker (8d62167)
* List of parsing errors
* Pinned schema version in submitted spreadsheets
### UI (afd4397)
* Security fixes
* Hide spreadsheet upload component while loading submission

## Azul
### Version(s): 5b0a3a7969c0ea4fc1fc417d4b84dbed7877cada
* bb61965 Fix broken log messages in MiniDSS (PR #1328)
* f6e7794 Update portal integration UUIDs (#1324, PR #1327)
* a2f9817 Add tests of request logging (#1079, PR #1301)
* 408c337 Archive artifacts from secrets clean-up with BFG (#1194, PR #1308)
* b156985  Add `GET /integrations` API endpoint (#1243, PR #1288)
* 491c2a6 Add generic request/response logging (#1079, PR #1281)
* 719dbda Add script for copying bundle between DSS instances (#386)
* 45eb222 Modify work-around for zarray files (#1302, PR #1304)
* 08b78f3 Fix bugs in apidev.py script (#1291, PR #1296)
* 74d2dee More type checker fixes (PR #1294)
* 574742f Explain deploying for apidev.py docs (#1292)
* a696d76 Switch sandbox and dev to DSS integration (#1282, #1311)
* 4fe28c3 Added assertion to validate full manifest file name (#1283, PR #1293)
* 2545676 Automatically provision Azul/DB health checks in DCP-wide composite #(1150, PR #1150)
* d3dc27e Validate request parameters (#840, #240, PR #1135) 
* 2fdb8f3 Backport hotfix for #1282 to develop (PR #1287)
* d100202 Change BDBag column header names from `dos` to `drs` (#1279, PR #1280)  
* d3562ff Add Github action for labeling new issues `orange`

# Staging 2019/09/25
## Ingest
## Version(s):

* Broker: v0.11.0.rc
* Raising errors when encountering unexpected spreadsheet columns instead of ignoring

## Data Store
## Version: 4b10ceea51249995cbe89ba9f109dcb980188a01

* 4b10cee - (HEAD -> integration, origin/integration) Fix signature in daemons/dss-notify-v2/app.py (#2449) (25 hours ago)
* 8910328 - Define the API to retrieve and playback events (#2435) (25 hours ago)
* 8ba6787 - Use the flash-flood library to record bundle events (#2434) (4 days ago)
* 91a381d - Define the bucket hosting DSS event data (#2433) (5 days ago)
* 9b69d3d - Add SSM parameter store functionality to dss-ops (#2432) (6 days ago)
* fa26b6d - Add response-content-disposition to GET /file. (#2371) (7 days ago)
* f8ffee9 - Bump cloud-blobstore version to 3.2.0. (#2431) (7 days ago)
* c6b42d7 - Bump httpie from 1.0.2 to 1.0.3 (closes #2404) (7 days ago)
* 68784a6 - forgot to fix this endpoint here too (#2430) (8 days ago)
* 9c74f3b - DSS SmokeTest: Test Order (#2428) (8 days ago)
* acdb110 - Bundle: enumeration (#2318) (8 days ago)
* 561cfb3 - [easy] Add file-type and file-size for ttfb fetching. (#2425) (11 days ago)
* 4d85a89 - update terraform in docker file (#2424) (11 days ago)


# Staging 2019/09/18
## Ingest
## Version(s):
### Broker (bbd176a)
* Added support for multiple submission errors.
* Fix linking of entities

## Upload Service
## Version(s): v4.4.4
* No significant functionality changes

# Data Store
## Version: fbb073543290082aab4f2950c5a71858bde4ba4f
* fbb0735 - (tag: 2019-09-09-14-43-05-integration.release, origin/integration) Adding a document to explain the action and resource relationship for… (#2395) (13 days ago)
* fa24dd1 - (origin/master-copy) Requirements Update (#2410) (2 weeks ago)
* 2263c9e - Increase dss notify workers. (#2408) (2 weeks ago)
* 4a3416b - Revert "Bump httpie from 1.0.2 to 1.0.3 (#2397)" (#2401) (3 weeks ago)
* ef3476b - Bump httpie from 1.0.2 to 1.0.3 (#2397) (3 weeks ago)
* 71957eb - Fix flaky test: TestFileApi.test_file_get_checkout . (#2396) (3 weeks ago)

# Azul
## Version(s): b191eda878a28335b795e1067406d38edb06cc81
* d1002020 Change BDBag column header names from `dos` to `drs` (#1279, PR #1280)
* 367099f9 Remove prefix for 'integration' integration test (#1282, PR #1285)
* 4b265f4e Generalise aggregation field translations (#1191, PR #1246)
* 4f1fb842 Tweak README instructions for determining when to reindex (PR #1267)
* 74690a19 Quote file name in Content-Disposition header of full manifests (#1247, PR #1261)
* 150332c6 Remove BFG redaction from TruffleHog and gitsecrets config (#1194, PR #1263)
* b0f8367e Document fix for hung test containers on Gitlab (PR #1258)
* 8ddf31f7 Change DOS URIs to use `drs` scheme (#1252, PR #1255)
* a7f73b6b Display Swagger UI with docs from app.py (#1163, PR #1227)
* 2df19463 Improve automation of PR branch squashing (#1245, PR #1254)
* 9390d465 Assorted README changes (PR #1250)
* 65abdda7 Make request config a plugin method (#1234)
* cbe399aa Update changelog generation command in README (PR #1236)
* 433c03a1 Clarify contribution guidelines on logging and string interpolation (PR #1239)



# Staging 2019/09/11
## Ingest
## Version(s)
### Core: c54cf190
* Tracking uuid of staged metadata files
* Handling bundle manifest null fields
* Logging unhandled exporting exceptions
* Updated primary submission documentation

### Exporter: 311950c
* Fix simple updates issue when staging shar    ed metadata files among bundles

### Validator: e52fafb
* Fix retrying of file validation
* Security Fixes

### UI: f42dac1
* Remove unnecessary logging
* Added link to project view from the submission view


# Staging 2019/09/09 (hotfix)

## Secondary Analysis
### Pipeline-tools: v0.56.6
* Fix bug in passing deployment to dss_client
* Fix to handle bundles missing lane index

### Skylab: optimus_v1.3.5
* Increase memory for GeneSortBam, CellSortBam, CalculateCellMetrics and CorrectUMItools


# Staging 2019/09/04

## Secondary Analysis
### Pipeline-tools: v0.56.4
* Fix getting metadata for bundles in the production data store.

### Falcon: v0.4.3
* Get labels when de-duping to properly prioritize duplicate on-hold workflows.
* Update logic for determining whether to release an on-hold workflow to handle duplicate notifications or updates in quick succession.

## Azul
### Version(s): de23fd421c9d38fd95c06f0061afeddc39bc1686
*  8563bb7 Change DRS URI to use stable hostname (#919, PR #1241)
*  e2614eb Add Content-Disposition header to full manifest (#1139, PR #1216)
*  e8df9a9 Fix type checker warnings (PR #1235)

## Metadata Schema
### Version(s):
* biomaterial_core.json - v8.2.0
* specimen_from_organism.json - v10.4.0
* cell_suspension.json - v13.3.0
* imaged_specimen.json - v3.3.0
* cell_line.json - v14.5.0
* donor_organism.json - v15.5.0
* organoid.json - v11.3.0

### Functionality:
* Changed RegEx pattern matching for version_number on biomaterial_core to be less loose.
* Changed RegEx pattern matching for insdc_sample_accession to avoid matching "|" on first character.

# Staging 2019/09/02 (hotfix)
## Ingest
## Version(s)
### Core (v0.10.0)
* Added persistence support for keeping track of staged metadata files
* Submission Errors Repository
### Exporter (v0.9.0)
* Modified file staging mechanism to address file staging issues.
* Broker (v0.10.0)
* Updated error message handling.
### UI (v0.11.0)
Added support for new error message operations.


# Staging 2019/08/29
## Azul
### Version: 641e310d16460bcf81d001a04dad42ba005247e4
*  fc54ae8 Hotfix: upgrade Terraform version
*  e7ee681 Purge queues during reindexing (#1185, PR #1231)
*  b433157 Document process for deleting a deployment (#1054, PR #1232)
*  889c8b6 Cache full manifests (#1138, PR #1215)
*  b82b32b Various cosmetic fixes
*  f4cd2c0 Receive Slack warning if fail queues are not empty (#1168)
*  21d9d6f Re-enable date detection, unmap contents.metadata in ES (#1173)
*  32a47ff [r] Re-enable date detection, unmap contents.metadata in ES (#1173)

## Secondary Analysis
### Lira v0.22.1
* Fixes to Lira API definition
* Add data store notifications to pub/sub queue
* Update DSS subscription queries to pin to metadata schema versions
* Use max_cromwell_retries config field to set Cromwell default workflow options
* Add DSS subscription queries for test data
* Remove outdated snyk badge
* Fix linting tests
* Remove deploy and scripts directory (moved to secondary-analysis-deploy repo)
* Label every workflow with a hash of its bundle-specific inputs
* Refactor the directory of subscriptions for better file organization
* Update Optimus subscription to match human or mouse data
* Add query for single-end SS2 bundles
* Subscription query migration from ElasticSearch to JMESPath

### Pipeline-tools v0.56.3
* Remove data file checkout when only retrieving bundle metadata
* Remove max_retries parameter from adapter WDLs so that it can be set by the workflow options file


# Staging 2019/08/28
## Data Store
### Version: fc8d411b022bfbc8c6c023e59c5e81476d0efe1d

* fc8d411 - (HEAD -> integration, tag: 2019-08-27-14-32-26-integration.release, origin/master, origin/integration, origin/HEAD, master) Add retries to verification in _test_gs_cache(). (#2372) (21 hours ago)
* 64ee180 - Added details of notify intervals (#2368) (4 days ago)
* 2e73ab3 - Fix failing collections tests (5 days ago)
* 258e4b5 - Add pagination response headers (closes #2287) (6 days ago)
* c23811d - Fix improper markdown (#2367) (6 days ago)
* 2feac5f - (origin/natanlao-limit-put-collections) Fix 500 on delete nonexistent bundle, again (fixes #1918) (#2351) (6 days ago)
* 9fd58d3 - Add ttl to async db items. (#2363) (8 days ago)
* d846f4d - DSS Operations: Checkout (#2366) (8 days ago)

# Staging 2019/08/21
## Data Store
### Version: 1af301db8a5935e63b9407cfcebd86a184f3fa2c
* 1af301d - (tag: 2019-08-19-21-44-19-integration.release, origin/integration) Revert "DSS/Operations: Checkout  (#2264)" (#2365) (2 days ago)
* dea261a - DSS/Operations: Checkout  (#2264) (2 days ago)
* ac88643 - remove hard-coded stage name in secrets tests (#2364) (2 days ago)
* ad90efb - (tag: 2019-08-19-14-54-49-integration.release) This pins pyyaml <= 5.1 for aws cli compatibility (#2348) (5 days ago)
* df13ac9 - Update like to security policy (#2361) (5 days ago)
* 006e7d8 - Relax sync size limit (#2354) (5 days ago)
* 63568a3 - Add secrets management to dss-ops script (#2325) (5 days ago)
* 81df1db - Schema typo fix (s/it/is) (6 days ago)
* de45167 - Assert we don't checkout to the main bucket (avoiding a sync error). (#2350) (7 days ago)
* 53fc89a - Revert "Fix 500 on delete nonexistent bundle (fixes #1918)" (7 days ago)
* 3b0fd70 - Fix 500 on delete nonexistent bundle (fixes #1918) (7 days ago)
* ecde208 - Simplify release scripting (#2347) (8 days ago)
* e44563e - More informative release status (#2345) (8 days ago)

## Azul
### Version 21f6ade6968ee1de16d29d755ab8f83b7875b3c4
* 2c6d13b Receive Slack warning if fail queues are not empty (#1168)
* 32a47ff [r] Re-enable date detection, unmap contents.metadata in ES (#1173)


# Staging 2019/08/15
## Secondary Analysis
### Lira: no version change
* Update configuration to support new metadata schema released on 8/14/2019


# Staging 2019/08/14
## Ingest
### Core v0.9.4.rc
* Memory-optimized findAssays() for stability
* Updated primary and secondary submission documentation
* New API endpoints for linking process to input bundle and input files

### Exporter v0.8.8.rc
* Exporting major/minor schema versions in provenance
* Fix null:null submission error

### UI v0.10.1.rc
* Display project uuid in submission view

## Data Store
### Version: 2019-08-14-16-06-17-staging.release
* f9cc3c3 - (tag: 2019-08-10-19-48-30-integration.release, origin/integration) Terraform v0.12.6 compatibility updates (#2337) (2 days ago)
* 5d1314a - Limit a user's v2 subscriptions to 100 per replica. (#2310) (3 days ago)
* 0ea5a2f - Limit user v1 subscriptions to 100 per replica. (#2309) (3 days ago)
* 7de0b14 - fixed integration test errors (#2326) (6 days ago)
* 56259b5 - Delete Test Subscription (#2304) (7 days ago)
* 04c0221 - Tagging Updates: Name (#2322) (7 days ago)
* d564509 - Revert "1k item limit in PUT /collections (closes #2281)" (10 days ago)
* 5679e8f - 1k item limit in PUT /collections (closes #2281) (10 days ago)
* 7bc38dc - Remove unused infra variables (#2316) (11 days ago)
* ee410fc - Bump requirements (#2288) (11 days ago)
* debaa1f - Update Readme.md (#2290) (12 days ago)
* 961601f - Use chalice request context (#2307) (13 days ago)
* dcb00b2 - Require version in PUT /collections (closes #2280) (#2306) (13 days ago)
* 45600d3 - update ENV (#2291) (2 weeks ago)
* 003a314 - Make sync cleanup less flaky (#2289) (2 weeks ago)

## Data Browser
### Version(s): 54e7802c85edbcdcabc8ab1ad35965d1b463f279
* 54e7802 Updated matrix supported query. (#800)
* 75ae53b Associate contributors with their institute on the project detail page. Resolves #731. (#751)
* c3cf5fd Updated filters during matrix partial query detection. Resolves #795. (#798)
* 44e1612 Fixed jiggle of matrix download text. (#794)
* b5be386 Updated get data summary title. Resolves #791. (#793)
* 75fad73 Updated tests.
* 06cbaa8 Updated get manifest/matrix  UI. Resolves #782. (#792)
* 3336821 Add back HCA contributors to the project detail page. 733. (#789)
* 969a3d5 Update dev to point to staging matrix service closes #790
* e9bf396 Add Library Construction Method and Species to get Data Summary. 780. (#788)
* 640d176 Updated manifest and matrix messaging. (#787)
* 007f78f Completed get data flow. (#779)
* af86961 Data Browser is gong to mobile/tablet portrait mode too quickly showing only 3 columns on a 13 inch MBP when not in full screen. Resolves #768. (#774)
* 1c8fbba Return link on error page is broken. Resolves #763. (#771)

## Azul
### Version(s): e035e5195049f93e093961ef678a480a977dd350
* 5232949 Test logs list thread name and timestamps (#1222, PR #1223)
* 12902bd Initial request for full manifest returns no hits (#1219, PR #1220)
* d94c253 Fix None filter for missing fields (#1202, PR #1214)
* d543430 Update README.md with changes to promotion procedure
* 90f3276 Refine documentation on AZUL_DEBUG (#419)
* 9910a72 Disable indexer lambdas before purging queues (#1204)
* cef3f21 Update pip req to 10.0.1 (#1195)

## Metadata Schema
## Versions
* cell_morphology - v6.1.7
* human_specific - v1.0.11
* mouse_specific - v1.0.8
* preservation_storage - v6.1.1
* timecourse - v2.0.2
* biological_macromolecule_ontology - v5.3.5
* cell_cycle_ontology - v5.3.6
* cell_type_ontology - v5.3.6
* cellular_component_ontology - v1.0.5
* development_stage_ontology - v5.3.6
* disease_ontology - v5.3.8
* enrichment_ontology - v1.2.6
* ethnicity_ontology - v5.3.9
* instrument_ontology - v5.3.6
* length_unit_ontology - v5.3.5
* library_amplification_ontology - v1.2.5
* library_construction_ontology - v1.2.5
* mass_unit_ontology - v5.3.5
* microscopy_ontology - v1.0.5
* probe - v1.1.1
* provenance - v1.1.0
* cell_line - v14.4.0
* cell_suspension - v13.2.0
* donor_organism - v15.4.0
* imaged_specimen - v3.2.0
* organoid - v11.2.0
* specimen_from_organism - v10.3.0
* analysis_file - v6.2.0
* image_file - v2.2.0
* reference_file - v3.2.0
* sequence_file - v9.2.0
* supplementary_file - v2.2.0
* analysis_process - v11.1.0
* project - v14.1.0
* analysis_protocol - v9.1.0
* aggregate_generation_protocol - v2.1.0
* collection_protocol - v9.2.0
* differentiation_protocol - v2.2.0
* dissociation_protocol - v6.2.0
* enrichment_protocol - v3.1.0
* ipsc_induction_protocol - v3.2.0
* imaging_preparation_protocol - v2.2.0
* imaging_protocol - v11.2.0
* protocol - v7.1.0
* library_preparation_protocol - v6.2.0
* sequencing_protocol - v10.1.0
### Functional Changes
* Added two optional fields to represent schema major and minor versions in provenance schema.

# Staging 2019/08/07
## Ingest
### UI v0.10.0.rc
* Upgraded to Angular 8

## Upload
### Version: 4.4.3
* Internal Cleanup

## Data Store
### Version: "2019-08-07-15-16-08-staging.release"
* dd76aa9 Update wheels (#2286)
* 6a2c2c4 Broad Integration Test Accounts update (#2283)
* b74823c Notify V2 Payload Context (#2277)
* 208caeb Add retries within collections testing. (#2274)
* 4797c01 Operations for managing the ES index and subscriptions (#2269)
* ffc5e76 Use better name for verify sync op (#2278)
* c6a768b Increase concurrency safety of sync cleanup (#2272)

## Data Portal
### Version: 507c03bde51c195e1e2a7a80252dcf1743002529
* 507c03b null in summary response cause portal to go blank. Resolves #480.

## Azul
### Version(s): 1ed1df5d13cec6a6aa400f35e358a5271ffd8cc1
* 42a2bd1 Fix None filter crashes summary response (#1199)
* 7fc1292 Change SQS reset instructions to use purge script (#758)
* bd7273b Add a script for resetting the indexer (#451)
* 081d13c Eliminate instance loggers & use of .format in logs (#419)
* bff0fce Fix app, test and script logging (#419, #1175)
* 4f6d286 Fix source code formatting
* a037b4a Eliminate logging though root logger (#419)
* 8020008 Remove non-applicable comment
* 5fa76f4 Inline useless constants in service/app.py
* a7df459 Optimized imports
* 5856a86 [2/2] Fix translated None values (#1179)
* 6221ab9 Declare missing fields in SummaryRepresentation
* 01960a7 [1/2] Fix translated None values (#1179)
* fafea91 [2/2] Eliminate empty columns in full TSV (#1147)
* 1635559 [1/2] Eliminate empty columns in full TSV (#1147)
* ec868c6 Add 'full' metadata format validation to integration test suite (#1171)
* 370ba09 CONTRIBUTING.rst states meaning of PR assignment
* d25c091 Validate 'format' param for manifest generation and set 'tsv' as default
* 4589ac2 Save RAM by uploading full TSV in multiple parts (#1134)
* ead9e03 Fix: multipart TSV upload leaks memory
* 346d99f Rename methods for full TSV generation
* 97bd9ea Fix doctests in elastic_request_builder.py
* 479feed Absorb browser domain move from `prod.data` to `data`
* e15f6ca Removed catch-all except statement in BaseSummaryResponse (#421)
* 8863c8d Disable date and numeric detection for mappings in ES indexes (#1152)
* 3fb640d Introduce test that reproduces bug in dynamic mapping ES (#1152)
* 7fbb4ea Revert "Hotfix: Can't index `HPSI human cerebral organoids`" (#1152)
* d898068 Elaborate on promotions in README
* a05d442 Remove project exclusions on `prod` (#1161)
* 0ab37e9 Add `make delete` target to only delete indices
* b432f4d Partially revert logging changes (3a0dc5f, #637)
* af6e1f5 Temporary removal of broken doctest (#989)
* d537d81 Translate None values for Elasticsearch (#989)
* 1641039 Check for existing sitecustomize.py for envhook (#608)
* d1c7401 Add `file_uuid` and `file_version` columns to full metadata TSV (#1068)
* 74237ed Incorporate changes from original hca_bundle_to_csv (#1068)
* b2c9d97 Document tag for artificial notifications (#995)
* 4f96c54 Log transaction IDs during remote reindex (#1030)
* 3a0dc5f Fix: Importing app.py overrides test logging config (#637)
* ae36559 Fix formatting in local_integration_test.py
* fe009fc Fix: Direct bundle access does not check preconditions (#1153)
* 3e45be4 Upgrade Terraform to version 0.12.5 (#1145)
* 9261873 Pin version of Terraform null provider
* 5fb2500 Rename elasticsearch in health endpoint
* a8c1661 Reduce load caused by health endpoint (#1124)
* b12a3f7 Consolidate health check configurations
* a159d3b Revert "Hot Fix: Exclude API endpoints call from health check to reduce load"
* 32dfccd [2/2] Add ability to requeue failed notifications (#1002)
* 1eac659 [1/2] Add ability to requeue failed notifications (#1002)
* 162deab Hotfix: Can't index `HPSI human cerebral organoids` project (#1152)
* d3f4a72 Make organism age range searchable via contains, within and intersects (#512)
* 4c42c3d Retire /repository/files/export endpoint (#586)
* 438dade Use HMAC key ID instead of secret for idempotent subscriptions (#993)
* 82d898e Remove projectSummary from response (#1021)


# Staging 2019/07/24
## Ingest
### Core v0.9.2.rc
* Put back authentication for PUT & PATCH requests

## Data Store
### Version: 2019-07-24-17-32-47-staging.release
* Retry-After header values added for 500 responses.
* Add operation to output bundle metadata document.
* Use a tempdir in smoketest when downloading.
* Extend test_creation_date_updated time.

## Azul
### Version(s): 2e08ea3b036a4d6c94a7ac77994fc74ec8408e59
* 4c42c3d Retire /repository/files/export endpoint (#586)
* 438dade Use HMAC key ID instead of secret for idempotent subscriptions (#993)
* 82d898e Remove projectSummary from response (#1021)


# Staging 2019/07/18
## Ingest
### Optimus v1.3.1
* This is a fix for the gene id and also we store gene id to gene name map into the zrr files.


# Staging 2019/07/17
## Ingest
### Exporter v0.8.6.rc
* Fix date format check
### Validator v0.6.5.rc
* (same version) fastq subprocess fix
### Broker v0.9.1.rc
* Fix updating of file metadata when data file is uploaded first

## Upload
### Version: v4.4.1
* Before uploading a file, check to see if the file has already been uploaded by checking its filename and checksums and if it has, skip uploading it and return the file that already exists.
* Validation of clientside checksum against serverside checksum calculation
* fix for deregistering job definitions as part of deployments

## Data Store
### Version 2019-07-17-15-50-19-staging.release
* Verify content type. (#2258)
* remove hmac_secret_key from GET/FIND Subscriptions  (#2251)
* Remove unused code. (#2257)
* Checkout cached files when PUT file is called. (#2246)
* [EZ] GET/ Subscription_v1 HMAC Key Change (#2247)
* removing fargate folder (#2252)
* Fix typo in PUT subscription docstring (#2250)
* remove dss-monitor-fargate references (#2245)
* Adjust smoketest to wait a bit longer when downloading after a sync. (#2243)
* /FIND Subscriptions HMAC_SECRET_KEY (#2238)
* Parallelize local storage ops (#2234)
* Add operation to trigger Elasticsearch indexer (#2235)
* /GET Subscriptions HMAC Key (#2237)
* Don't change part layout when fixing object metadata (#2232)
* Storage ops accept input keys file in JSON format (#2228)
* Make prod test job dependent on deploy (#2233)
* Refactor indexer event parsing (#2224)
* create large bundle sync test (#2223)
* dependency bump: urllib1.25.3 (#2209)
* Parallelize bundle tombstone script (#2217)
* README Changes (#2208)
* Parallelize sync manifest deps check (#2221)
* increase sync daemon timeout to 900s (#2220)
* updated iam / cron for fargate (#2219)
* Include type for firecloud checkout viewer (#2218)
* Storage operations improvements (#2199)
* Allow Terra user read access to Google checkout bucket
* DSS Monitor Independent Deploy (#2201)
* Reformat request to analytics log message. (#2200)
* DSS Lambda Monitoring (#2198)
* De-register percolate queries across all indices (#2196)
* [Easy] Increase smoketest sync wait to 120s (#2195)
* Simplify operations job-id handling (#2194)
* [Easy] Fix sync operation logger bug (#2193)

## Secondary Analysis
### Pipeline tools: v0.55.0
* Add functions to get bundle-specific inputs for SmartSeq2 (paired end) and Optimus that determine whether a data bundle should be re-analyzed
*  
### Falcon: v0.4.1
* Fixes an issue with the noop implementation in v0.4.0

## Azul
### Version a56c023891b09ddf2b7ab1389ee7e436ca877279
* 98771f3 Revert "Reduce /health check frequency in Route53 to decrease load on ES"
* b9baf84 Make 'file_format' a single value (#612)
* 45a9e97 Revert "Revert metadata field in index roll back (#965, #966)"
* 54a27cd Reduce /health check frequency in Route53 to decrease load on ES
* d2a3951 Eliminate PyCharm warnings in test_hca_indexer.py
* 8c65faf Simplify index writer creation and customization
* 0ba619e Fix formatting
* 07ecce3 Fix unused import
* efeace9 Use the same writer for unit tests and deployment
* f5718ae Duplicate notifications for integration tests
* f1cebf6 Document --shared option for subscriptions script
* 17a780f Add unsubscribe target to Makefile
* 61dcd69 Support duplicate notification (#947)
* a72bac1 Add test for duplicate notifications (#947)
* 57e7f84 Refactor aggregation code slightly for clarity
* 3a35b0a Hot Fix: Exclude API endpoints call from health check to reduce load
* fb98182 Changed project_shortname to project_short_name (#191)
* 16205cb Revert metadata field in index roll back (#965, #966)
* e35dfc2 Remove excluded list and exclude whitelisted project (#1112)
* 22cfc66 Generate 'full metadata' TSV by optimizing on memory (#967, #968)
* 9be159b Bundles index disallows indexing of the metadata field
* 4598c53 Use JSON for filters (#537)
* 3b24935 Reduce manifest download request during Locust scale test (#931)
* 6a35619 Correct sorting and format parameters in locust test
* e5153d5 Exclude another neuron_diff dupe
* 98a7bfd Exclude test projects on prod

## Metadata Schema
### Versions
* file_content_ontology:1.0.1
* analysis_file: 6.1.1
* image_file: 2.1.1
* file_core: 6.1.1
* supplementary_file: 2.1.1
* reference_file: 3.1.1
* sequence_file: 9.1.1

### Functionality Changes
* No functionality changes.



# Staging 2019/07/15
## Ingest
### Core v0.9.2.rc
* APIs for performing simple updates to bundles
* APIs for viewing JSONPatch diffs when performing updates
* Search submissions by project
* Disabled “Submit” button when linking hasn’t yet been completed(spreadsheet submissions only)
* Now using Java 11, Spring boot 2
### Exporter v0.8.5.rc
* Handles update submissions and performs simple bundle updates as necessary
* Separate AMQP listener for update messages
* Duplicate links in links.json fix
### Broker v0.9.0.rc
* Handles update spreadsheets
* Providing a mechanism for generating and downloading update-spreadsheets from submitted spreadsheets
### UI v0.9.6.rc
* Widgets for uploading and downloading an update-spreadsheet
* Paginated project dashboard
* Widget to search for projects by title, shortname, etc.
* Submissions table view inside the projects tab
### Validator v0.6.5.rc
* Added ontology validation keyword
* Ontology service updates
* Fastq validator subprocess fix
### Staging manager v0.5.4.rc
* ingest-client library updates, refactoring
### State tracker v0.7.5.rc
* Now using Java 11


# Staging 2019/06/26
## Azul
Version(s): 9fbf3283a6f5c6b20d5a6be22dbb9d7fc08a4e52
* 1a9f8e6 Modify deletion notifications for integration tests
* 03408e7 Add test for direct file access fallback
* 0b1345a Prevent failure during teardown (#1049)
* 4de2892 Use direct access for DSS bundles
* 1e8dea4 Remove notebooks directory
* 816ce71 Fix type warning
* 7992c30 Speed up reading aggregates, using source filter
* 6dac2a9 [2/2] Fix races from indexing deletions (#611)
* f435634 [1/2] Fix races from indexing deletions (#611)
* 4a3d240 Fix races from indexing deletions (#611)
* e19f8d4 Isolate test fixtures for service tests (#1064)
* a26526d Rename manifest test file
* 1f10ee9 REVERT ME: Avoid dash and brackets in BDBag column names (#1091)
* feeaadc Parallelize API endpoint health checks (#1085)
* fbbea21 Fix: /health/progress is not lazy and  therefore slow (#1084)
* 8f979e0 Add test for laziness of /health/foo (#1084)
* b244b34 Parallelize API endpoint health checks (#1085)
* 976ad06 Use DistinctAccumulator in CellSuspensionAggregator (#1039)
* 09a24cf REVERT ME: Avoid dots in entity ID column of Terra TSV (#1071)
* cf43fa6 REVERT ME: Switch from bundle to participant for Terra (#1070)

## Metadata Schema
Versions
* File_core: 6.1.0
* file_content_ontology: 1.0.0
* file_format_ontology: 1.0.0
* analysis_file: 6.1.0
* image_file: 2.1.0
* reference_file: 3.1.0
* sequence_file: 9.1.0
* supplementary_file: 2.1.0

Functionality
* Added new file_format_ontology ontology schema.
* Added optional content_description field.
* Added new file_content_ontology schema.
* Updated integration test spreadsheets to contain new optional content_description field.


# Staging 2019/06/05
## Ingest

## Upload

## Data Store
Version: 74b216e20ba34156dcd2d1c17469296200dadb6e
* [easy] Use the same regex for all uuids. (#2185)
* Retry V2 notifications every 6 hours for 3 days (#2169)
* Miscellaneous fixes (#2188)
* Revert "Begin DSS builder (#1149)" (#2187)
* Add operation to trigger sync (#2180)
* Use sqs batch send from dcplib (#2179)
* bump requirements (#2186)
* Remove notifier-v2 retries for non-existent objects (#2183)
* Remove indexer retries for non-existent objects (#2182)
* Add operation to verify entity replication (#2178)
* Lambda Layers (#2168)
* Lambda Tagging (#2150)


## Secondary Analysis
### Pipeline-tools v0.52.0
* Make the pipeline-tools input processor more tolerant with sequencing output formats.

## Data Portal

## Data Browser
Version(s): 63fda8f7227637cd37b350f10e3d4915399ce901
* 63fda8f Fixed set of pagination on select of facet. Resolves #675. (#683)
* f760f16 Added protection against bad data. Standardized binding of project and project row mapping. Added specs. Resolves #674. (#682)
* 4a47efc Updated specs.
* 353daf2 Enabled export to terra in dev and ux-dev. Resolves #680. (#681)

## Azul
Version(s): ef51cb90836c68d4b7e9ef32279b633026a97257
* 6b3cac4 Fix `git log` example in README
* 49cf081 Add CONTRIBUTING document (#750)
* 98676bf Check current branch before `make reindex`, `make subscribe` et al (#1061)
* c4235bc Refactor `KeywordSearchResponse.make_sample()` again
* 9116b94 Remove unused import, shebang
* e7b905a Refactor `KeywordSearchResponse.make_sample()`
* 76900d8 Add effectiveOrgan facet (#1022)
* f83bc9b Optimize imports in HCA transformer
* 8131914 Eliminate obsolete suppression of PyCharm warning
* 51a28c2 Pull up sample discovery method into Transformer base class
* 044d6ae Fix more type warnings in HCA transformer module
* 5d484af Suppress deprecation warning in HCA transformer module
* 04deeda Reorder classes in HCA transformers module
* 73e98d5 Removed unused import; fix quoting
* 4bc7438 [4 of 4] Make …_dict functions methods of the Transformer class
* 176d8a2 [3 of 4] Make …_dict functions methods of the Transformer class
* 5bb187f [2 of 4] Make …_dict functions methods of the Transformer class
* 481c023 [1 of 4] Make …_dict functions methods of the Transformer class
* 7bfd343 Fix: `git secrets` check fails in sub directories (#1057)
* dd8e22a Replace `*` with `sample` in manifests (#1055)
* 994b57e Exclude `contents.metadata` from being indexed (#1020)
* 07ba957 Add `/health/progress`, test service endpoints in `/health` (#971)
* 9bf8238 Add `metadata` field to documents in bundles index (#965, #966)
* c37d439 Reformat `metadata_generator`
* 3c55b87 Introducing Simon's script for generating metadata csv
* 2eed794 Rewrite parsing of ES index names
* a6a4499 Add separate index for cell suspensions (#1038)

## Metadata Schema
Version(s):
* death: 5.5.1
* contact: 8.0.1
* channel: 2.0.4
* provenance: 1.0.4
* cell_line: 14.3.1
* cell_suspension: 13.1.1
* donor_organism: 15.3.2
* imaged_specimen: 3.1.1
* organoid: 11.1.2
* specimen_from_organism: 10.2.1
* analysis_file: 6.0.1
* image_file: 2.0.1
* reference_file: 3.0.1
* sequence_file: 9.0.1
* supplementary_file: 2.0.1
* analysis_process: 11.0.2
* process: 9.1.1
* project: 14.0.2
* analysis_protocol: 9.0.1
* aggregate_generation_protocol: 2.0.1
* collection_protocol: 9.1.1
* differentiation_protocol: 2.1.1
* Dissociation_protocol: 6.1.1
* enrichment_protocol: 3.0.1
* ipsc_induction_protocol: 3.1.2
* imaging_preparation_protocol: 2.1.1
* imaging_protocol: 11.1.3
* protocol: 7.0.1
* library_preparation_protocol: 6.1.1
* sequencing_protocol: 10.0.2

Functionality:
* Switched to pre-commit commit package
* Added pull approve functionality
* Changed travis conf file for multi-stage build
* Changed print statements to errors for linter musts
* Added check for required ontology schema properties
* Added the linter to the pre-commit hook
* Added python to travis. Added call to linter.



# Staging 2019/06/05
## Ingest
### Exporter v0.8.3.rc
- Fix submissions stuck in Processing due to failed state tracker bundle complete notification

### UI v0.9.5.rc
- Make Fusillade url configurable thru env var
- Fix greetings and picture display

## Secondary Analysis
### Optimus v1.2.0
- Increase disk size for TagGeneExon scaled by input size
- Improve Performance of SplitBamByCellBarcode

## Data Portal
Version(s): 46c81edabefc01119b093327e758d7c3ceb074fa
- 46c81ed Update README.md
- 1c69b99 Update readme for git-secrets
- 640a038 update gatsby version
- c021f9c Sticky header. Modification for Browse Metadata: Move TOC to RHS and prevent TOC from scrolling off screen (#436).
- 1ebb111 TOC
- b6eabf2 Updated summary response to handle new API. Resolves #452.

## Data Browser
Version(s): e25307f53b0d2bedb16f15e4b25773ee2b030f95
- e25307f Update README.md
- a8dacb5 update readme for git-secrets
- 7622d6b Verify table heading/column names are readable on 13'' mac laptop screen. Resolves #649. (#677)
- bf0b323 Remove daos (#676)
- 80dcbd4 update node and npm versions for building and npm update
- 61f998e Fix for metadata column width. Modification to Update column name display to add an extra row and move counts below baseline. Resolves #664. (#671)
- 7b59be2 Update column name display to add an extra row and move counts below baseline. (#670)
- 4e3e222 Updated data tables to use generic data source. Resolves #660. (#669)
- e0c51ec Updated summary to match new API. Resolves #656. (#661)
- 363d5d7 Added maintenance mode banner to prod. Resolves #663. (#668)

## Azul
Version(s): 6e5f6ca3512938e8b532eb80a5b3d7edf6d1c1bb

- dcc46a4 DELETE ME: Disable `make subscribe` on Gitlab
- 7b4aa6d Fix: certain summaries truncated to 10 terms (#1047)
- fd06455 Return `gs://…` url with DRS endpoint (#920)
- 8ffcd07 Hot fix failing IT in prod (#1049)
- 3cdf684 Revert "REVERT ME: Whitelist pre-reingestion projects for Japan demo"
- 98226d0 Exclude old fetal-maternal interface dataset in prod (#1025)
- 3097b1a Exclude old cell_hashing (rsatija) dataset in prod (#1024)
- 67db667 Exclude old 10x_mouse_brain dataset in prod (#1023)
- 7a0e7a4 Exclude old CD4+_lymphocytes (EGEOD106540) dataset in prod (#1019)
- 2e8a0ff Exclude old neuron_diff dataset in prod (#1018)
- 4a1c423 Exclude old bone marrow (ido_amit) dataset in prod (#1017)
- 807f39c Exclude old cardiomyocytes_basu (basu) dataset in prod (#1016)
- 825f5eb Exclude old kidney_biopsy_scRNA-seq (humphreys) dataset in prod (#1015)
- 31fe1e5 Exclude old mouse melanoma dataset in prod (#1014)
- 742d8d0 Exclude old tissue sensitivity dataset in prod (#1013)
- 78ff367 Exclude old cerebral organoid dataset in prod (#1005)
- 5a9901f Exclude secondary "peer" and "Regev-ICA" bundles
- f24962b Revert "REVERT ME: Whitelist pre-reingestion projects for Japan demo"
- 1797cd9 Revert "REVERT ME: Whitelist pre-reingestion projects for Japan demo"
- 6310b7e Add imaging-specific facets (#885)
- 65cf8cb Ensure integration tests always clean up bundles (#994)
- 4e10eda Make trufflehog rules file hidden
- f9510c7 Require `git secrets` to be installed (#755)
- 36bbc58 Speed up indexing tests with  (#1040)
- c7d39b7 Revert "Return `gs://` url with DRS endpoint (#920)"
- 2c4a8b2 Return `gs://` url with DRS endpoint (#920)
- f083e0c Add DRS alias domain for service lambda (#918)
- 6b753af Add utility for interning immutable value objects
- 08f34b0 Cosmetics
- 9d15b62 REVERT ME: Whitelist pre-reingestion projects for Japan demo
- b6a5421 REVERT ME: Whitelist pre-reingestion projects for Japan demo
- cc04d30 REVERT ME: Whitelist pre-reingestion projects for Japan demo


# Staging 2019/05/28
## Ingest
### Exporter 0.8.2.rc
- Minor changes to prevent creation of Pika connections unncessarily.

## Data Store
### 2019-05-29-15-42-27-staging.release
- fix tests/test_api.py test mode (#2165)
- Storage operations errors log object info (#2164)
- Async state convenience methods and bug fixes (#2136)
- Use STANDARD storage class to mark non-cached checkout objects (#2152)
- Resume unfinished GS copies (#2135)
- Increase file checkout test timeouts (#2163)
- Expose TimedThread exceptions to caller (#2157)
- Separate GCP and AWS collections paging testing. (#2162)
- Add short retry to get-item test (#2161)
- Specify replicas in sync test content-type (#2158)
- Change how content-type is propagated when caching. (#2154)
- Remove trailing whitespace
- Direct URLs for Files (#2138)
- Updated Authorization Endpoint Checks (#2146)
- Operation to repair file blob metadata (#2123)
- Verify checksums on `PUT /file/{uuid}` (closes #2000)
- update lambda-iam for accessing resource by tag (#2131)
- Update TTL (#2130)
- Pull logging into copy clients (#2134)
- We don't use travis for deploys anymore; update release.sh doc accordingly (#2132)
- Add verification storage operations (#2121)
- improve bucket maping util (#2120)
- Fix typo in checksum parsing
- Increase operations daemon log level (#2119)
- Operations utils (#2115)
- Operatios cloud executor (#2114)
- Operations CLI framework (#2111)
- Revert most pylib versions so that they fit in the lambda's size limit. (#2116)
- Add retries to PUT collection method when testing. (#2112)
- Add python shebangs to scripts. (#2110)
- Bump dependencies. (#2088)

## Secondary-analysis
### Pipeline-tools: v0.50.2 -> v0.51.1
- Raise HTTP error for 409 responses.
- Add Adapter for single-end SS2 scientific pipeline.
- Remove references to gtf_file in ss2 adapters.
- Add adapter static JSON for mouse data for Optimus.
- Upgrade to use smartseq2_v2.4.0 for smartseq2_v2.3.0

# Staging 2019/05/22
## Ingest
### Exporter v0.8.1.rc
* Do not inform user when there’s a failure creating a duplicate bundle

### UI v0.9.4.rc
* Use Fusillade integration

## Data Browser
### Version: fb8587e4176aad2341df284429b276fef87bdd6b

* Fb8587e Update manifest modal layout  #499
* d506f9f Added download buttons to manifest modal. Closes #499 (#652)
* 4389fb5 Removed curl command from matrix copy. #625 (#650)
* 2345a67 Removed retry on error from /health. #637 (#648)
* b489cc7 Update project view for new samples API Closes #643
* a21f5cc Fix for #640 Use samples instead of specimens on project list for organ and organ part


## Azul
### Version: bb092dafe26477887baba63d6ed016b8ee2ec4c1
* 589a787 Fix: BDBag archive contains non-deterministic directory name (#991)
* 42fcc67 Tweak ACM certificate settings
* ce89f1d Add config method to detect main deployments
* 38246b9 Reformat Terraform config template
* ce21bfb Fix: 500 error with cell suspensions linked to sample without organ
* 2d4e509 Combine workflow and version facets (#985)
* 0767cf4 Rename get_hits to be more explicit
* 4ed62e0 Revert to previous version of deleted entities (#986)

## Metadata
### Versions:
* type/protocol/imaging/imaging_protocol.json schema - v11.1.1
* type/process/process.json - v9.1.0

### Functionality:
* Fixed probe field to reference correct schema. Fixes #980.
* Added optional start_time and end_time fields. Fixes #742.
* Archived unused 10x integration test spreadsheet. Fixes #957.


# Staging 2019/05/15
## Azul
### Version: 13e721394f1de12d39fa1ec2ad2205357f1f04f0
* 975fd08 Make indexing of organs more consistent (#977)
* e98e0e3 Exclude old EMTAB5061 dataset (#1000)
* 79b4b85 Fix spelling in exclusion comment
* 60dbd43 Exclude old/incorrect pancreas6decades data (#999)
* cc26e06 Exclude old pancreas6decades dataset (#978)
* 23f4fe6 Fix: update version of metadata-api
* 1cf7f03 Remove translation lookups from transform_summary
* ad7ee57 Get SummaryResponse organCount from samples
* 276f96f Index cell_line fields (#930)
* b59050f BDBag and manifest TSV use same set of fields (#892)
* 9a497f4 Add deletion to integration test (#838)
* d39ecef Ignore Retry-After from DSS for small file downloads (#686)
* 3d8b2ba Update urllib3 to 1.24.3 (#970)
* e4b2a95 Refine lambda timeouts for clarity and consistency
* d5cf682 Patch DSS client to use direct bucket access if possible (#942)
* 2cdd42a Remove unused integration test property



# Staging 2019/05/08
## Ingest
### Ingest-ui v0.9.2.rc
* Setting of row height automatically to show all validation errors
* Do not allow creation of project metadata thru UI

## Upload  v4.3.1
* Remove "list upload area" REST API endpoint
* Added client-side checksumming (temporarily disabled).
* Much Internal refactoring and cleanup.

## Data Store
### Version: 2019-05-08-02-45-24-staging.release
* Improve `PUT /files/{uuid}` description
* Clarify and fix test expectations
* Add basic indexing for collections.
* Fix multipart sync completion criteria
* Simplify GitLab job definitions
* Prod Smoke Test Query
* Change String Comparison
* Isolate Terraform State File Buckets
* Remove trufflehog dependency
* Update TF to remove DEPRECATED messages
* Increase GS client connection pool size
* Cache for content type like 'application/json; foo'
* Sync daemon sets destination content-type equal to source
* Update subscription_v2 ddb interface calls
* Use dynamoDB methods in async_state
* Abstract out dynamoDB functionality from subscriptions

## Secondary Analysis
### Pipeline-tools v0.49.1
* Update metadata schema when formatting analysis results:
    * Change process/protocol_type to type
    * Change file_format to format
* Update to metadata-api library release/1.0b15
* Subscriptions queries process_type -> type, dissociation_method -> method

## Data Browser
### Version: 156f751de3b693ffa8dabcb78ee7550bcee5fe7f
* Samples Tab

## Azul
### Version: 53f0b12c25364a8c5f527ad2119fee48df096b40
* 947b099a Absorb addtion of paging to `GET /bundles/{uuid}` in DSS
* f051f862 Fix projectSummary.donorCount (#953)
* a09ff818 Expose secondary analysis workflow type (#896)
* dc3b3f95 Upgrade to metadata-api 1.0b15 (#957) (Absorbs metadata schema changes)
* 2f38c58e Fix: freezing and sorting of JSON objects with None values
* caa917d9 Fix unused imports
* ae04ee61 One manifest row per occurrence of a file in a bundle (#955) Fixes https://github.com/HumanCellAtlas/dcp-cli/issues/327
* bbd155ac Create bundles index (#903)
* 5e2becff Travis build scans for secrets committed accidentally (#764)
* 28fd68ec Securely store keys for notification HMAC and Google service account (#794)
* ad82e394 Securely store keys for notification HMAC and Google service account (#794)
* 3ffe606d Handle multiple bundles per file in manifest integration test
* dc6d87be Manifest integration test filters on test project
* c053f1fd Refine Gitlab pipline
* a6c4e90f Updated urllib3 to 1.24.2 (#927)
* e11fbb2f Fixes to deployment section of README (#888)
* e3a3590d Fix test query filter for samples tab changes
* 62164e4e Exclude old BM_PC dataset in prod (#944)
* 46dc3eca Exclude old neuron_diff dataset in prod (#915)
* 71f8e1e0 Nest projectId under project termFacet (#894)
* 239f0fa4 Replace Specimens tab with Samples tab (#707)
* 54f332bc Eliminate indirection in cart item config
* 0fd69736 Added validation for manifest types (#839)

## Metadata Schema
### Versions
* core/biomaterial/biomaterial_core.json - v8.1.0
* core/file/file_core.json - v6.0.0
* core/procces/process_core.json - v10.0.0
* module/biomaterial/death.json - 5.5.0
* module/biomaterial/preservation_storage.json - v6.1.0
* module/ontology/contributor_role_ontology.json - v1.0.0
* module/process/purchased_reagents.json - v6.1.0
* module/project/contact.json - v8.0.0
* module/project/publication.json - v6.0.0
* module/protocol/probe.json - v1.1.0
* module/protocol/target.json - v1.1.0
* type/biomaterial/cell_line.json - v14.3.0
* type/biomaterial/cell_suspension.json - v13.1.0
* type/biomaterial/donor_organism.json - v15.3.0
* type/biomaterial/imaged_specimen.json - v3.1.0
* type/biomaterial/organoid.json - v11.1.0
* type/biomaterial/specimen_from_organism.json - v10.2.0
* type/file/analysis_file.json - v6.0.0
* type/file/image_file.json - v2.0.0
* type/file/reference_file.json - v3.0.0
* type/file/sequence_file.json - v9.0.0
* type/file/supplementary_file.json - v2.0.0
* type/process/analysis/analysis_process.json - v11.0.1
* type/process/process.json - v9.0.0
* type/project/project.json - v14.0.0
* type/protocol/analysis/analysis_protocol.json - v9.0.0
* type/protocol/biomaterial_collection/collection_protocol.json - v9.1.0
* type/protocol/biomaterial_collection/differentiation_protocol.json - v2.1.0
* type/protocol/biomaterial_collection/dissociation_protocol.json - v6.1.0
* type/protocol/biomaterial_collection/enrichment_protocol.json - v3.0.0
* type/protocol/biomaterial_collection/ipsc_induction_protocol.json - v3.1.0
* type/protocol/imaging/imaging_preparation_protocol.json - v2.1.0
* type/protocol/imaging/imaging_protocol.json - v11.1.0
* type/protocol/protocol.json - v7.0.0
* type/protocol/sequencing/library_preparation_protocol.json - v6.1.0

### Functionality
* Changed protocol_type to type. Fixes #931.
* Changed contact_name to name. Fixes #927.
* Changed file_format to format. Fixes #375.
* Changed selected_cell_type to selected_cell_types. Fixes #923.
* Changed ipsc_induction_method to method, ipsc_induction_factors to reprogramming_factors, protocol_reagents to reagents. Removed ipsc_induction_produced_in_house. Fixes #926.
* Added new probe.json module. Fixes #813.
* Changed process_location to location and operator to operators. Fixes #930.
* Changed enrichment_method to method, min_size_selected to minimum_size and max_size_selected to maximum_size. Fixes #925.
* Changed differentiation_method to method. Fixes #924.
* Changed biosd_biomaterial to biosamples_accession and insdc_biomaterial to insdc_sample_accession. Fixes #929
* Changed publication_title to title and publication_url to url. Fixes #928.
* Changed cell_line_type to type. Fixes #935.
* Changed project_role from enum to ontology. Fixes #894
* Added new contributor_role_ontology schema. Fixes #893.


# Staging 2019/04/24
## Data Store
### Version:  2019-04-24-15-26-53-staging.release
* 9098aa1 Bundle manifest memcache replica specific (#2068)
* 559c6bf Amend secret checking error handling to catch return code. (#2063)
* 8d81cc6 Raise if an error occurs while secret checking. (#2062)
* b4c834c Modify file names in metadata document (#2060)
* 07b271d Lambda invocation test examines correct JSON object (#2061)
* 7b483c5 Consistent JMESPath metadata doc inclusion (#2059)
* 8433503 Production Smoke Tests (#2029)
* 91049a0 Spelling error. (#2056)
* 7af5da0 modifed description for /PUT/Collection (#2046)
* ccbc514 Dynamic DynamoDB Table Fetching (#2052)
* 7631c96 Send deletion JMESPath notifications (#2049)
* 0216271 Lambda invoke test outputs complete response (#2053)
* cb82880 Event relay forwards object deletion events. (#2048)
* 9194e61 Bucket var input for caching. (#2051)
* 1598f97 Bundle manifest memcaching (#2043)
* abca05a Use s3 multipart upload for large bundle manifests (#2020)
* f43a376 Parallelize JMESPath notification delivery (#2034)
* b7a95c3 Add parallelization to JMESPath filter doc construction (#2033)
* 7c68322 Exclude very large bundle manifests from ES document (#2031)
* ce468b0 Give travis access to notify-v2 queue (#2040)
* 1cbd5bf changed owner tag (#2035)
* 42fce7b Owner Tagging Fix (#2026)
* ec6732a Resource Tagging with Terraform (#2010)
* 2639cf5 Dissalow PATCH on tombstoned bundles (#2018)
* 174f133 PATCH /bundle sets new version correctly (#2017)
* 02aceec Add paging to collections. (#2013)
* faa9bf7 Add a root collections endpoint. (#2006)
* ca1d1d3 parallelize bundle file verification (#1992)
* 71d1ed8 Increase collection verification parallelization (#1995)
* 5458255 Increase Lambda mem+cpu (#1994)
* ddc278e Verify deployment  environment variables (#1979)
* 6e55050 Increase max number of botocore connections (#1993)
* 6c19414 Update Readme.md Flow
* 2c9194b Remove dangling reference from infra (#1988)
* afc6b98 Additional test cases for JWT Audience (#1970)
* 7a8080b Retain Elasicsearch logs for 5 years (#1987)
* 2a6a009 Add support for PATCH /bundle (#1978)
* 65c2410 Implement trufflehog test check. (#1985)
* 13f1a1b Centralize SECURITY.md, and delete security.txt. (#1983)
* dbc2942 Add script to ensure consistent credentials. (#1967)
* 1785abc Swagger docs: follow common style (#1974)
* 5eb9007 Fix ACM_CERTIFICATE_IDENTIFIER in environment.prod (#1969)
* 99a25ac Update swagger with explicit retry-after headers. (#1961)
* 6185db1 Add a security.txt file. (#1965)
* cfc210a Update deployment documentation (closes 1902)
* e8bc74a Truncate ci-cd.json to get around the file size restriction AWS imposes. (#1962)
* 99cdd1d Update get file description. (#1958)
* 58bd8e5 Fix JMESPath notification race condition (#1956)
* a12ef7e Change prod bucket names for new encrypted buckets. (#1953)
* 35f1e49 Add swagger descriptions based on dcp-cli issue #221. (#1930)
* b925bbd Travis dynamoDB permission additions. (#1954)
* 7d6ca5b removed hard-coded reference (#1942)
* 80c6b1a Document subscriptions in swagger (#1916)
* 519e27a Support GET /bundle paging (#1913)
* 5b63819 FIx JMESPath notification eventing bug (#1928)

## Azul
### Version: a55ab35db79e7e079d1512c24b4bc0e0c4e491bc
* a1deea7 Fix: Terra requires name of first column to end in `_id` (#911)
* 51d8848 Fix: Terra rejects `.` in column names (#912)
* 8bf8aae Fix: Terra requires `samples.tsv`, rejects `bundles.tsv` in BDBag (#910)
* a1b5854 Added security.txt (#761)
* d5deca6 Added script to disable/reenable lambdas (#238)


# Staging 2019/04/17
## Secondary Analysis
### Optimus optimus_v1.0.0_increase_empty_drops_memory
* Increase the memory allocated to the Optimus RunEmptyDrops task

## Azul
### Version: acac64791e271c2a46069ce8f950b2f0ba9f98e1
* 4847ce79 Exclude old Mouse Melanoma project on `prod` (#895)
* fc06b2e4 Add facet for sequencing_protocol.paired_end (#867)
* fe2f9fe6 Increase CloudWatch log retention to 1827 days (#832)
* d63ec67f Indexer logs the time needed to download bundle metadata
* b622852e Fix: /repository/…/{uuid} only works for projects (#879)
* 5ca1f11e Prevent tagging on wrong deployment
* 8c62e847 [1/2] Filters used in IT are more portable between deployments
* fe8ee3cf [2/2] Filters used in IT are more portable between deployments
* ae3d5967 Support for multiple files per BDBag TSV row (#866)
* 67d3c5fd Refactor manifest TSV generation
* dd7ff978 Added script for uploading metadata TSVs to a S3 bucket (#860)
* 3a3b394b Add --no-ff flag to README section about releases (#891)
* 1b9e0af0 Add timestamp to integration test logging (#858)
* ec9def7b README describes getting personal Google Cloud credentials (#872)


## Staging 2019/04/10
### Ingest
#### Ingest-ui v0.9.1.rc
* Presenting all validation errors

### Data Browser
#### Azul 857fcaebca2d6905532ab3debfdb672c4d18d318
* 5523064 Minimal support for imaging data sets (#881)
* b344ea9 Rename `es_results` to `hits` in indexer tests
* 9ab393a Add test for filtering by project UUID aka `projectId` (#796)
* fe5b68e Include DRS endpoint in integration test (#789, #790)
* 760388b Work around AWS Step Function's eventual consistency (#877)

## Staging 2019/04/04
### Ingest
#### Validator v0.6.3.rc
* Validator fixes for non-recoverable errors

#### UI v0.1.0.rc
* UI release

### Upload v4.2.7
* No important functional changes.

### Secondary Analysis
#### Optimus v0.1.0
* The first major version release for the Optimus pipeline.

#### Falcon v0.3.0
* Add status endpoint to check health of falcon threads
* Add snyk github integration
* Add formatter and linting check in tests

### Data Portal
#### Azul deployed/staging/2019-04-04__09-23 (b158c00)
* Don't require new projects to be whitelisted in staging
* Run `terraform plan` before `apply -auto-approve` on Gitlab
* Include `prod`'s URL shortening bucket in security boundary
* Grant Gitlab write access to Elasticsearch log groups (#825)
* Add Gitlab instance for `prod` (#748)
* Update Gitlab CE from 11.8.0 to 11.8.3
* Add cell_suspension.selected_cell_type (#800)
* Delete file_metadata_to_csv.py (#848)
* Hard-code subscription ID in synthetic reindexer notifiactions (#382)
* kibana-proxy.pl uses containers for signing proxy and Kibana
* Clean-up README.md
* Fixed error responses for `/repository/{entity}/{uuid}` endpoints (#355, #448)
* Update cheatsheet for deployment / promotion (#797)
* Revert "Have Gitlab create deployment tags (on gitlab fork)"
* Have Gitlab create deployment tags (on gitlab fork)
* Don't require new projects to be whitelisted in staging
* Fix manifest integration test on `integration` (#847)
* Include Grafana dashboard definition for Data Portal and Browser (#815)
* Updates Grafana dashboard uid and name for Azul (#816)
* Blocks csv, txt, pdf and all zarr! (except .zarr!.zattrs) files  (#807)
* Ignores files blocked by data-browser (#807)
* Added option to split tsv by project (#807)
* Added file_metadata_to_csv.py to /scripts (#807)
* Names of TSV files in BDBag use plural (#842)
* Omit content disposition header from BDBag responses (#841)
* Skip indexing part of integration test on `prod`
* Consolidate Elasticsearch instances for lesser main deployments (#809)
* Pin dcplib to 1.5.1 as 1.6.0 breaks the build
* Add BDBag support to new manifest endpoint (#827)
* Make manifest column names consistent with metadata schema (#792)
* Relax assertion on `file_version` in DRS endpoint (#828)
* Moved bundle deletion functionality to AzulClient
* Require auth for notifications (#96)
* Changing definition of self.indexer_url in AzulClient
* Renamed Reindexer class to AzulClient
* Check BDBag endpoint during integration test (#565)
* Enable monitoring and Grafana publishing in sandbox deployment
* Distinguish Azul and Data Portal monitoring resources (#787)
* Consolidate Elasticsearch instances for lesser main deployments (#809)
* Pin dcplib to 1.5.1 as 1.6.0 breaks the build

### Metadata Schema
* module/protocol/channel.json - v2.0.3
* type/protocol/imaging/imaging_protocol.json - v11.0.13
* type/project/project.json - v11.1.0
* Changed example and guidelines in filter_range. Fixes#878.
* Changed example and guidelines in filter_range. Fixes#878.
* Added optional biostudies_accesssion field. Fixes #852.


## Staging 2019/03/27
### Ingest

### Upload
#### Broker v0.8.9.rc
* Fixed uploading of file metadata

#### Core v0.9.0.rc
* Updated process of assigning UUIDs to exported bundles
* Fixed format of version timestamp

#### Exporter v0.8.0.rc
* Updated handling of bundle UUID and version timestamp
* Added handling for duplicate export messages

### Upload v4.2.6
* Switch Batch cluster instance types from "m4" to "m5" with updated validation ami
* changes to allow for clean delete of unused environments
* fix for s3 load to account for recently uploaded files
* change log group retention in days to match dcp expectations
* Change validator timeout to 1hr
* Lock jsonschema at 2.6.0
* remove lock/unlock api functionality
* update health check to not be nested within /v1 and check health of db
* Don't trigger monitoring daemons for non standard environments
* use dynamic maintainence window for rds
* Always use Docker images with version numbers

### Metadata Schema
* module/process/sequencing/plate_based_sequencing.json - v3.0.0
* Changed well and plate ID to label. Fixes #837.
* type/biomaterial/cell_suspension.json - v11.0.0
* Changed well and plate ID to label. Fixes #837.
* Updates to ‘property_migrations.json’ file for programmatically looking up where fields have moved.

## Staging 2019/03/13

### Ingest
#### Core v0.8.5.rc
* Exclude property_migrations file when retrieving latest schemas from s3 bucket listing
* Log INFO messages
* Fix intermittent issue where file validation fails due to many validation events
* Find by validation ID using the ID of the validation job
* Always setting to DRAFT when updating a file's cloudUrl/checksums

#### Validator v0.6.1.rc
* Bug fix validating files which do not trigger job
* Handling errors
* Added checking of checksum when triggering validation job
* Added methods in ingest-client for fetching file checksum info
* Bug fix when refusing to validate File resources with no content/metadata
* Security patches
* Targetting a newer version of the fastq validation image

### Upload Service v4.2.4
* Use write/read for s3 consistency on s3 put

### Azul deployed/staging/2019-03-13__10-49

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


## Staging 2019/03/20

### Ingest v0.6.2.rc
* Bug fix: rejecting unprocessable validation messages that were previously being retried indefinitely
* Configurable protocol scheme for HTTP connections to the upload and ingest API

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

### Optimus pipeline: v0.4.0

## Azul
Version: deployed/staging/2019-03-20__08-46
* dbe86cbd Fix: DSS proxy test fails on integration deployment
* e86d1fb7 Fix handling of missing permissions boundary (#239)
* 720478a0 Refined timeout conditions (#785)
* 8aa368ec Retain original file name when downloading resolved DRS object
* 16692311 Include DSS checkout buckets in security boundary
* dda157f7 DSS checkout bucket name changed in integration and staging
* c0cc1e01 Add manual job for reindexing on Gitlab
* 14ad0e11 Move subscription from integration test; add to regular build steps
* ed109aaa Blacklist Meyer dataset in `prod` (HumanCellAtlas/data-store#1976)
* 55670a4b Fix invalid regex in authenticator.py; cosmetics
* 47578ccd Refactor DRS support, fix DRS URLs (#774)
* 69f80136 Rename `azul.dos` to `azul.drs`
* 64195230 Add non-fetch variant of DSS proxy; add server-side wait (#778)
* da5b6161 Add project accessions fields (#714)
* 79f378b9 Add all metadata to manifest (#720)

## Metadata Schema
### Versions
* state_of_specimen - v6.0.0
* insdc_experiment - v2.0.0
* plate_based_sequencing - v2.0.0
* cell_line - v11.0.0
* cell_suspension - v10.0.0
* specimen_from_organism - v9.0.0
* sequence_file - v8.0.0
* analysis_process - v9.0.0
* process - v7.0.0
* collection_protocol - v9.0.0
* dissociation_protocol - v6.0.0
* library_preparation_protocol - v6.0.0
* sequencing_protocol - v10.0.0
* project - v11.0.1
* image_file - v1.0.4
* ethnicity_ontology - v5.3.8
* contact - v6.1.5
* channel - v2.0.2
* target - v1.0.9
* donor_organism - v14.0.7
* imaging_preparation_protocol - v2.0.3
* imaging_protocol - v11.0.12
* human_specific - v1.0.10
* medical_history - v5.2.8
* preservation_storage - v6.0.2

### Changes
* Changed array field names (gross_image and microscopic_image) to be plural to adhere to Style Guide. Fixes #792.
* Changed insdc_experiment to insdc_experiment_accession to adhere to Style Guide. Fixes #809.
* Changed cell_quality to well_quality. Fixes #809.
* Changed date_established from date-time to date format. Fixes #821
* Changed cell_quality to well_quality. Fixes #809.
* Changed organ_part to organ_parts to adhere to Style Guide. Fixes #648.
* Changed array field names (gross_image and microscopic_image) to be plural to adhere to Style Guide. Fixes #792.
* Change insdc_run to insdc_run_accessions to adhere to Style Guide. Fixes #805.
* Removed required outputs fields to adhere to metadata model. Fixes #664.
* Changed insdc_experiment to insdc_experiment_accession to adhere to Style Guide. Fixes #809.
* Changed protocol_reagents and collection_method to reagents and method to remove redundancy to adhere to Style Guide. Fixes #807.
* Changed protocol_reagents and dissociation_method to reagents and method to remove redundancy to adhere to Style Guide. Fixes #807.
* Changed nucleic_acid_source field to be required. Fixes #824.
* Changed library_construction_approach to library_construction_method to be consistent with other protocols. Fixes #807.
* Changed sequencing_approach to sequencing_method to be consistent with other protocols. Fixes #807.
* New `property_migrations.json` files added for programmatically looking up where fields have moved.

## Staging 2019/03/06

### Ingest

#### Broker

Version: v0.8.8.rc

* minor fix to code

#### Core

Version: v0.8.4.rc

* authentication related security related patches

### Upload Service

Version: v4.2.3

* Reraise original errors where tenacity retries are used instead of throwing a tenacity retry error
* Bug fix for large file checksum notification flow
* Disable batch watcher in terraform
* use latest version of hca against upload service
* Updates to README: link to release instructions. Add new system architecture diagram
* Add function to delete all job definitions after each deployment
* Updates to retry for s3 eventual consistency
* Update terraform version to 0.11.11
* fix up pgbouncer and use image version rather than latest in ecs task definition

### Data Store

Version: 2019-03-06-16-15-17-staging.release

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


### Secondary Analysis

Version: Lira: v0.18.1

* Make the subscription query for 10x v2 data more specific.
* Update the version of Connexion App and standardize the Lira API.
* Update the Swagger UI of Lira, which is the /ui endpoint of Lira.
* Update the controllers of Lira to adapt to the new API definitions.
* Update the Lira readme and add new badges.

### Azul

Version: deployed/staging/2019-03-05__22-14 (ef051ba5bd0f4dd992fbababce96bededada601f)

* bf9d799 Mark canned bundles as generated
* ae48aaa Change organ_part to an array (#699)
* c0937a7 Fix deletion of bundles with > 10 entities (#734)
* 2c2522d Test deletion of bundles with > 10 entities (#734)
* fc53e91 Fix bdbag manifest test to be order independent
* 5bc566b Use fewer shards for aggregate index (#680)
* d195fe9 Copy `manifest` as `bdbag` in request_config.json (#740)
* 3e5c8ae Add health check for data portal (#731)
* 8e67a37 Script to simulate a deletion notification (#723)
* 6d7f807 Added `reindex` to changelog entry for #604
* 6151860 Export manifest in BDBag to Terra (#604)
* 4c0a6a8 Document how to reset an ongoing indexing operation (#715)
* ad1c60a Fix: SQS trigger initially disabled (#335)
* 51c0667 Mention `make clean` in deployment cheat sheet
* 916b61d Fix pastie error from 576f8546f89fc39148a455ee1b0eb5a4baa360fd
* 576f854 Configure API Gateway logging with Terraform (#653)
* 2584cad Rename API Gateway Terraform file
* 1d83ace Improve deployment and promotion cheat sheet
* e2ed1be Rename integration test target
* 21ee567 Enforce that main deployment matches protected branch
* a7dbce6 Various Makefile fixes
* b0c17b8 Prototype exporting carts to DSS collections (#627)

### Metadata Schema
No metadata schema updates
* Updates to 2 infrastructure testing spreadsheets:
infrastructure_testing_files/current/dcp_integration_test_metadata_1_10X_bundle.xlsx
infrastructure_testing_files/current/dcp_integration_test_metadata_1_SS2_bundle.xlsx


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
