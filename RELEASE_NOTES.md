# Release Notes

<!-- newest release at the top please) -->

# 2019/12/17 Prod Release Notes

## Ingest Service
### Version(s): 
### Core	from v0.11.1 (a1078fc) to v0.12.1 (57dd203)
### Change(s):
* Changes to have only one open submission per project
* Project submissions now returns all submissions for all projects with the same UUID
* Bug fix to not return null references to submissions
* Project query is case insensitive
* Submission errors use resource processing as the rest of core
* Delete submission envelope also deletes submission errors
### UI:	from v0.11.4 (74b270b) to v0.12.1 (fbedb57)
### Change(s):
* Hide "Create Submission" button on projects that have an open submission
* Filter project query to filter out update projects and get unique list of projects by UUID
* Hide delete button if it will not be possible to delete submission
* Delete Submission button on: Submission List, Project Page, Submission Detail
* Show loading icon while deleting
* Fix Project ID (project_short_name) search.
* Snyk Security Fixes
### Broker	from v0.10.3 (3e124ee8) to v0.12.1 (c452a55)
### Change(s):
* Updated ingest-client version from 9180ee20 to 4472037
* Avoid Duplicate bundles
* Redact Utils
* Handle large spreadsheet
* Handle HTTP Errors
* Use dcpVersion instead of updateDate on Ingest metadata document
### Exporter: from v0.10.1 (d75dee7) to v0.12.1 (f52fa0f)
### Change(s):
* Updated ingest-client version from 88e02a9d to 4472037
* Avoid Duplicate bundles
* Redact Utils
* Handle large spreadsheet
* Handle HTTP Errors
* Use dcpVersion instead of updateDate on Ingest metadata document
* New Parser Errors
* Add latests Schema to Schema tab
* Refactored SchemaTemplate
* Fix for retrieving all files in bundle

## Data Store Service
### Version(s): 809d42f949b8c597cf0b8f37be52286c49a51ee3
### Change(s):
* 809d42f - (HEAD -> integration, tag: 2019-11-26-17-38-53-integration.release, origin/master, origin/integration, origin/HEAD, master) DSS Checkout Observers: Broad Service accounts (#2618) (10 hours ago)
* 5e37aa5 - Update dss-events-scribe daemon config (#2628) (32 hours ago)
* 38cc772 - Bump flashflood to 0.4.3 (#2629) (33 hours ago)
* 4882e78 - Check Fusillade hotfix - fix broken script (#2625) (4 days ago)
* 4970b21 - Check Fusillade hotfix - make script executable (#2624) (4 days ago)
* fb37d68 - Fusillade Check - Add Fusillade-related checks to CI/CD (#2619) (4 days ago)
* 782e83c - Remove newlines popluating the version in the SSM. (#2617) (5 days ago)
* 677a234 - (tag: 2019-11-20-23-49-50-staging.release, tag: 2019-11-19-17-40-17-integration.release) Refactor notify v2 event handler (#2607) (8 days ago)
* ad50b0d - Include event logging info to aid debugging (#2606) (11 days ago)
* 48d1cc6 - Include `bundle_info` in bundle metadata document (#2604) (11 days ago)
* d00b7de - Fix API formatting issue (#2582) (11 days ago)
* c307daf - Refactor _upload_bundle in tests/test_events.py (#2603) (11 days ago)
* 5bc5b5d - Confirm flashflood writes during journaling/update (#2600) (11 days ago)
* cc68c49 - Improve jmespath/dss-notify-v2 documentation (#2599) (11 days ago)
* 3806f54 - Extend the test expectation TTL for notifications (#2601) (12 days ago)
* 9671e74 - Operational tooling: IAM fixups (#2580) (12 days ago)
* 64b03a2 - Move check of whether allspark is behind github to prod stage only (#2591) (12 days ago)
* c797245 - Add docstrings to some events methods (#2598) (13 days ago)
* dfd75be - [Easy] Fix `get_tombstoned_bundles` docstring (#2597) (13 days ago)
* ba820a5 - Remove tombstoned bundles from event journals (#2596) (13 days ago)
* 7680656 - Generalize name of v2 event handler (#2595) (13 days ago)
* 573e7ac - Private event method should be public (#2594) (13 days ago)
* 07f2778 - (tag: 2019-11-13-20-30-03-integration.release) Include error message in api logs (#2586) (13 days ago)
* edd9116 - DSS GitLab: TimeStamps (#2589) (13 days ago)
* 129d493 - DSS Smoketest: --no-pagination (#2590) (13 days ago)
* 5bcffc4 - Use dss-ops instead of populate_lambda_ssm_params (#2581) (2 weeks ago)
* 7bf36ed - (tag: 2019-11-12-23-38-32-integration.release) DSS Security: Pipeline Destination (#2587) (2 weeks ago)
* 3e3b3b0 - (tag: 2019-11-12-19-57-33-integration.release) Revert timeout increase for dss-index lambda. (2 weeks ago)
* 74c40c4 - [Easy] Set dss-indexer lambda concurrency to 200; increase timeout by 1 minute. (#2584) (2 weeks ago)
* 5e0a4a7 - Move tombstone identifiers, update test (#2575) (2 weeks ago)
* e9dee89 - Only setup fusillade for main branches (#2577) (3 weeks ago)
* 4fb60e5 - (tag: 2019-11-08-21-32-29-integration.release) Remove unsed imports from event ops (#2574) (3 weeks ago)
* 05a930c - Add method to list bundle zombies (#2573) (3 weeks ago)
* 282aeb1 - added resources to help issues (#2572) (3 weeks ago)
* 8dec6cf - Reorganize test code for storage utilities (#2571) (3 weeks ago)
* f084e35 - Collect flashflood garbage with s3 lifecycle (#2566) (3 weeks ago)
* 23396bc - Add IAM auditing functionality to dss-ops script (redux) (#2509) (3 weeks ago)
* 7507cfa - Vim was only a marginal improvement over vi. (#2564) (3 weeks ago)
* 02b45aa - Remove duplicated keys in API spec (#2529) (3 weeks ago)
* 1adf090 - Events journaling and update daemon (#2559) (3 weeks ago)
* 061e71e - Add service account viewers in staging and prod. (#2560) (4 weeks ago)
* 3a7721d - Suppress test output on a per-test basis (4 weeks ago)
* e8d7743 - Suppress test output for passing tests. (4 weeks ago)
* 5302dca - Update to new staging bucket names. (#2499) (4 weeks ago)
* 53c89c0 - Add checkout sync operation. (#2557) (4 weeks ago)
* e516599 - Refactor checkout operations. (#2549) (4 weeks ago)
* 862c614 - Add new service account direct view access. (#2555) (4 weeks ago)
* 46b6fb7 - Pin to working version of boto3 for gcp cloud fn. (#2552) (4 weeks ago)
* a05299c - Improve events operations, bump flashflood to 0.4.1 (#2533) (5 weeks ago)
* aaa5592 - Method to time limit iterated work (#2534) (5 weeks ago)
* 2530dbf - Back up collections, subscriptions (#2488) (5 weeks ago)
* defba62 - Update smoketest to new FlashFlood API (#2545) (5 weeks ago)
* b82a580 - DSS Infra: dev acm (#2537) (5 weeks ago)
* 74eec3e - Fix events paging, bump flashflood to 0.4.0 (#2527) (5 weeks ago)
* d8ad738 - Revert "Gentle refactor of tombstoning code" (#2535) (5 weeks ago)
* a63b794 - add help to subcommand subparsers (#2531) (5 weeks ago)
* ef135a3 - Typo fix for dss/operations/secrets.py (#2530) (5 weeks ago)
* beb6a61 - add links to swagger API docs (#2514) (5 weeks ago)
* 3f0342a - Update tombstone format for deletion RFC (#2516) (5 weeks ago)
* 4ae6560 - Hotfix for lambda params (#2526) (6 weeks ago)
* 9e732f5 - Add event tests to smoketest (#2518) (6 weeks ago)
* fadfc10 - Remove Visitation and old admin CLI (#2506) (6 weeks ago)
* f954db3 - Reduce event doc construction concurrency (#2517) (6 weeks ago)
* 2dbeb29 - Avoid recording tombstones into events (#2515) (6 weeks ago)
* 05be5e5 - Merge dss/operations/ssm_params.py into dss/operations/lambda_params.py (#2487) (6 weeks ago)
* 45bfad4 - Fixes for optional reindex notifications (#2505) (7 weeks ago)
* c0d32ff - DSS Bundle Enumeration: bundle enumeration page breaks (#2498) (7 weeks ago)
* f16b982 - Optionally send notifications during reindex (#2504) (7 weeks ago)
* cf5f022 - Add Elasticsearch reindex operation (#2503) (7 weeks ago)
* 56cd043 - Add Mock Fusillade Server (#2502) (7 weeks ago)
* 8f72458 - DSS Bundle Enumeration: Test Refactor (#2495) (7 weeks ago)
* d33a9d1 - Send X-OpenAPI-Paginated-Content-Key even when only one page is present (#2497) (7 weeks ago)
* 8be83e4 - fixes tombstone issues, refactor tests (#2494) (7 weeks ago)
* ef483a6 - Incorporate mock Fusillade server into tests (re-merge) (#2490) (8 weeks ago)
* 23d38f7 - Operation scripting for recording and journaling events (#2481) (8 weeks ago)
* 4649c73 - Update tombstone_bundles.py [EZ] (#2485) (8 weeks ago)
* cc152a4 - Update check_deployment_secrets.py (#2486) (8 weeks ago)
* ba50d4b - Update infrastructure to use dss-ops.py and not set_secret/fetch_secret (redux) (#2475) (8 weeks ago)
* 3105ad9 - DSS SmokeTest: jmespath support (#2480) (8 weeks ago)
* 8714844 - [easy] Print response when error handling for security checks. (#2476) (8 weeks ago)
* 23896cb - added logger.info (#2477) (8 weeks ago)
* 9b2304f - Avoid mangling key for queued notifications (#2479) (8 weeks ago)
* 8a4c205 - Fix exception being instantiated but not raised (8 weeks ago)
* 713a900 - (tag: 2019-10-01-15-33-51-integration.release) Revert "Update infrastructure to use dss-ops.py and not set_secret/fetch_secret (#2370)" (#2474) (8 weeks ago)
* 5d4c696 - Update infrastructure to use dss-ops.py and not set_secret/fetch_secret (#2370) (8 weeks ago)
* 6a01f5a - Allow multiple flashflood writes (#2472) (8 weeks ago)
* cb1c8af - Dss Sync Filter: Integration Test Refactor (#2469) (9 weeks ago)
* ca40591 - DSS Sync: skip sync on file parts (#2416) (9 weeks ago)
* 69d412c - In CICD moving fusillade to after deployment (#2465) (9 weeks ago)
* 12d3837 - Improve security in dss-ops secrets handling (#2451) (9 weeks ago)
* 4bfe048 - [easy] Add GCP function error handling. (#2463) (9 weeks ago)
* 5968902 - Add lambda parameter functionality to dss-ops (#2436) (9 weeks ago)
* ba5f444 - (tag: 2019-09-24-04-02-19-integration.release) Adding fusillade to bundle write operation (#2450) (9 weeks ago)
* a35044e - Add fusillade stage and setup fusillade step to CI/CD (#2437) (9 weeks ago)
* e590f25 - Testing upload, get_bundle, and checkout with different replicas. (#2458) (9 weeks ago)

## Data Processing Pipelines and Execution Service
### Lira: v0.22.9
### Change(s):
* Update Google pubsub batch configuration
* Update 10x subscription query to match either 10x v2 or v3 sequencing with a 3 prime end bias, or the more specific ontologies for "10x 3' v2 sequencing" and "10x 3' v3 sequencing"
* Update to pipeline-tools version that adds Optimus chemistry into the hashed inputs
### Adapter-pipelines: v1.3.0
### Change(s):
* Pass in chemistry parameter to Optimus analysis workflow
* Update how the analysis outputs are passed into the submit workflow since the zarr outputs are no longer optional
### Optimus: optimus_v1.4.0:
### Change(s):
* Addition of support for V3 chemistry
* Addition of input parameter validation step
* Greatly improved documentation
* Updates to Zarr outputs:
    * Addition of a zarr schema version tag (this is v1.0.0)
    * Updated Zarr schema (see documentation)
    * Header lengths bug fix: headers are no longer being truncated

## Data Portal - Azul
### Version(s): 34b304a9eb8e9559b4b049318e653484f57545a6
### Change(s):
* b57053e6 Backport: Hotfix: `list_dss_bundles` returns tombstoned bundles (#1488)
* e946c299 Merging Gitlab permissions hotfix from `prod`
* 5e4e6a46 Sanitize sys.path in envhook.py; defeat PyCharm docrunner.py (#1470, PR #1471)
* 7938295e Requirements should always be installed with `--update` (#1438, PR #1439)
* 1171346f Clarify exception to wrap all or none rule for logging statements (PR #1479)
* 84dcccd4 Mention use of EAFP in contributing guide (PR #1483)
* df94367e Refactor services & manifest generation (#1242, PR #1477)


# 2019/12/03 Prod Release Notes

## HCA Metadata
### No schema changes. Minor changes to issue template.
### Change(s):
* Updated schema linter to indicate environment for the OLS API URL
* Updated travis config to use the environment proper environment when executing the schema linter.

## Data Store Service
### Version(s): 809d42f949b8c597cf0b8f37be52286c49a51ee3
### Change(s):
* 809d42f - (HEAD -> integration, tag: 2019-11-26-17-38-53-integration.release, origin/master, origin/integration, origin/HEAD, master) DSS Checkout Observers: Broad Service accounts (#2618) (10 hours ago)
* 5e37aa5 - Update dss-events-scribe daemon config (#2628) (32 hours ago)
* 38cc772 - Bump flashflood to 0.4.3 (#2629) (33 hours ago)
* 4882e78 - Check Fusillade hotfix - fix broken script (#2625) (4 days ago)
* 4970b21 - Check Fusillade hotfix - make script executable (#2624) (4 days ago)
* fb37d68 - Fusillade Check - Add Fusillade-related checks to CI/CD (#2619) (4 days ago)
* 782e83c - Remove newlines popluating the version in the SSM. (#2617) (5 days ago)
* 677a234 - (tag: 2019-11-20-23-49-50-staging.release, tag: 2019-11-19-17-40-17-integration.release) Refactor notify v2 event handler (#2607) (8 days ago)
* ad50b0d - Include event logging info to aid debugging (#2606) (11 days ago)
* 48d1cc6 - Include `bundle_info` in bundle metadata document (#2604) (11 days ago)
* d00b7de - Fix API formatting issue (#2582) (11 days ago)
* c307daf - Refactor _upload_bundle in tests/test_events.py (#2603) (11 days ago)
* 5bc5b5d - Confirm flashflood writes during journaling/update (#2600) (11 days ago)
* cc68c49 - Improve jmespath/dss-notify-v2 documentation (#2599) (11 days ago)
* 3806f54 - Extend the test expectation TTL for notifications (#2601) (12 days ago)
* 9671e74 - Operational tooling: IAM fixups (#2580) (12 days ago)
* 64b03a2 - Move check of whether allspark is behind github to prod stage only (#2591) (12 days ago)
* c797245 - Add docstrings to some events methods (#2598) (13 days ago)
* dfd75be - [Easy] Fix `get_tombstoned_bundles` docstring (#2597) (13 days ago)
* ba820a5 - Remove tombstoned bundles from event journals (#2596) (13 days ago)
* 7680656 - Generalize name of v2 event handler (#2595) (13 days ago)
* 573e7ac - Private event method should be public (#2594) (13 days ago)
* 07f2778 - (tag: 2019-11-13-20-30-03-integration.release) Include error message in api logs (#2586) (13 days ago)
* edd9116 - DSS GitLab: TimeStamps (#2589) (13 days ago)
* 129d493 - DSS Smoketest: --no-pagination (#2590) (13 days ago)
* 5bcffc4 - Use dss-ops instead of populate_lambda_ssm_params (#2581) (2 weeks ago)
* 7bf36ed - (tag: 2019-11-12-23-38-32-integration.release) DSS Security: Pipeline Destination (#2587) (2 weeks ago)
* 3e3b3b0 - (tag: 2019-11-12-19-57-33-integration.release) Revert timeout increase for dss-index lambda. (2 weeks ago)
* 74c40c4 - [Easy] Set dss-indexer lambda concurrency to 200; increase timeout by 1 minute. (#2584) (2 weeks ago)
* 5e0a4a7 - Move tombstone identifiers, update test (#2575) (2 weeks ago)
* e9dee89 - Only setup fusillade for main branches (#2577) (3 weeks ago)
* 4fb60e5 - (tag: 2019-11-08-21-32-29-integration.release) Remove unsed imports from event ops (#2574) (3 weeks ago)
* 05a930c - Add method to list bundle zombies (#2573) (3 weeks ago)
* 282aeb1 - added resources to help issues (#2572) (3 weeks ago)
* 8dec6cf - Reorganize test code for storage utilities (#2571) (3 weeks ago)
* f084e35 - Collect flashflood garbage with s3 lifecycle (#2566) (3 weeks ago)
* 23396bc - Add IAM auditing functionality to dss-ops script (redux) (#2509) (3 weeks ago)
* 7507cfa - Vim was only a marginal improvement over vi. (#2564) (3 weeks ago)
* 02b45aa - Remove duplicated keys in API spec (#2529) (3 weeks ago)
* 1adf090 - Events journaling and update daemon (#2559) (3 weeks ago)
* 061e71e - Add service account viewers in staging and prod. (#2560) (4 weeks ago)
* 3a7721d - Suppress test output on a per-test basis (4 weeks ago)
* e8d7743 - Suppress test output for passing tests. (4 weeks ago)
* 5302dca - Update to new staging bucket names. (#2499) (4 weeks ago)
* 53c89c0 - Add checkout sync operation. (#2557) (4 weeks ago)
* e516599 - Refactor checkout operations. (#2549) (4 weeks ago)
* 862c614 - Add new service account direct view access. (#2555) (4 weeks ago)
* 46b6fb7 - Pin to working version of boto3 for gcp cloud fn. (#2552) (4 weeks ago)
* a05299c - Improve events operations, bump flashflood to 0.4.1 (#2533) (5 weeks ago)
* aaa5592 - Method to time limit iterated work (#2534) (5 weeks ago)
* 2530dbf - Back up collections, subscriptions (#2488) (5 weeks ago)
* defba62 - Update smoketest to new FlashFlood API (#2545) (5 weeks ago)
* b82a580 - DSS Infra: dev acm (#2537) (5 weeks ago)
* 74eec3e - Fix events paging, bump flashflood to 0.4.0 (#2527) (5 weeks ago)
* d8ad738 - Revert "Gentle refactor of tombstoning code" (#2535) (5 weeks ago)
* a63b794 - add help to subcommand subparsers (#2531) (5 weeks ago)
* ef135a3 - Typo fix for dss/operations/secrets.py (#2530) (5 weeks ago)
* beb6a61 - add links to swagger API docs (#2514) (5 weeks ago)
* 3f0342a - Update tombstone format for deletion RFC (#2516) (5 weeks ago)
* 4ae6560 - Hotfix for lambda params (#2526) (6 weeks ago)
* 9e732f5 - Add event tests to smoketest (#2518) (6 weeks ago)
* fadfc10 - Remove Visitation and old admin CLI (#2506) (6 weeks ago)
* f954db3 - Reduce event doc construction concurrency (#2517) (6 weeks ago)
* 2dbeb29 - Avoid recording tombstones into events (#2515) (6 weeks ago)
* 05be5e5 - Merge dss/operations/ssm_params.py into dss/operations/lambda_params.py (#2487) (6 weeks ago)
* 45bfad4 - Fixes for optional reindex notifications (#2505) (7 weeks ago)
* c0d32ff - DSS Bundle Enumeration: bundle enumeration page breaks (#2498) (7 weeks ago)
* f16b982 - Optionally send notifications during reindex (#2504) (7 weeks ago)
* cf5f022 - Add Elasticsearch reindex operation (#2503) (7 weeks ago)
* 56cd043 - Add Mock Fusillade Server (#2502) (7 weeks ago)
* 8f72458 - DSS Bundle Enumeration: Test Refactor (#2495) (7 weeks ago)
* d33a9d1 - Send X-OpenAPI-Paginated-Content-Key even when only one page is present (#2497) (7 weeks ago)
* 8be83e4 - fixes tombstone issues, refactor tests (#2494) (7 weeks ago)
* ef483a6 - Incorporate mock Fusillade server into tests (re-merge) (#2490) (8 weeks ago)
* 23d38f7 - Operation scripting for recording and journaling events (#2481) (8 weeks ago)
* 4649c73 - Update tombstone_bundles.py [EZ] (#2485) (8 weeks ago)
* cc152a4 - Update check_deployment_secrets.py (#2486) (8 weeks ago)
* ba50d4b - Update infrastructure to use dss-ops.py and not set_secret/fetch_secret (redux) (#2475) (8 weeks ago)
* 3105ad9 - DSS SmokeTest: jmespath support (#2480) (8 weeks ago)
* 8714844 - [easy] Print response when error handling for security checks. (#2476) (8 weeks ago)
* 23896cb - added logger.info (#2477) (8 weeks ago)
* 9b2304f - Avoid mangling key for queued notifications (#2479) (8 weeks ago)
* 8a4c205 - Fix exception being instantiated but not raised (8 weeks ago)
* 713a900 - (tag: 2019-10-01-15-33-51-integration.release) Revert "Update infrastructure to use dss-ops.py and not set_secret/fetch_secret (#2370)" (#2474) (8 weeks ago)
* 5d4c696 - Update infrastructure to use dss-ops.py and not set_secret/fetch_secret (#2370) (8 weeks ago)
* 6a01f5a - Allow multiple flashflood writes (#2472) (8 weeks ago)
* cb1c8af - Dss Sync Filter: Integration Test Refactor (#2469) (9 weeks ago)
* ca40591 - DSS Sync: skip sync on file parts (#2416) (9 weeks ago)
* 69d412c - In CICD moving fusillade to after deployment (#2465) (9 weeks ago)
* 12d3837 - Improve security in dss-ops secrets handling (#2451) (9 weeks ago)
* 4bfe048 - [easy] Add GCP function error handling. (#2463) (9 weeks ago)
* 5968902 - Add lambda parameter functionality to dss-ops (#2436) (9 weeks ago)
* ba5f444 - (tag: 2019-09-24-04-02-19-integration.release) Adding fusillade to bundle write operation (#2450) (9 weeks ago)
* a35044e - Add fusillade stage and setup fusillade step to CI/CD (#2437) (9 weeks ago)
* e590f25 - Testing upload, get_bundle, and checkout with different replicas. (#2458) (9 weeks ago)

## Data Portal - Azul
### Version(s): f43fa13f7cf1282f62379509ba32dff48ea0111e
### Change(s):
* 1f3a05fd Optimize metadata generator (#1190)
* 186cb3d2 Blocking 'make reindex'; simplify queue listing (#1425, #1448, PR #1462)
* 5e322696 Limit AZUL_DEBUG=0 to `make test` on Gitlab and Travis (#1444, #1464, PR #1467)
* 9814a1b9 Eliminate all imports of `lambdas.{service,indexer}.app` (#1461, PR #1466)
* 993572d9 Add portal registration API specs (#1197, PR #1225)
* 93499025 Fix: OpenAPI UI renders incorrect server URL (#1262, PR #1431)
* 4939a1d2 Convert architecture diagram in README to SVG (PR #1458)
* 511975c2 Log exceptions even if AZUL_DEBUG is 0 (#1414, PR #1457)
* e227bae0 Add SCP495 to portals DB (#1455, PR #1456)

## DCP Auth Service
### Version(s): 0.2.1 to 0.4.0 
### Change(s):
* openapi version follows the release version (#326)
* fixing upgrade_schema (#328)
* Policies in JSON (#325)
* updating fusillade yml to include the new fields returned from userinfo (#320)
* Adding group, role, and scope info from fusillade to userinfo (#306)
* Backup (#314) (#318)
* Redirect fix (#315)
* changing userinfo endpoint is a redirect (#293)
* adding logout out to openid connect discovery endpoint (#294)
* Implicit Flow (#289)


# 2019/11/26 Prod Hotfix Release Notes

## Ingest Service
### Version(s): 
### Broker (v0.10.2 -> v0.10.3)
* Updated schema processing
* Importer fixes 
* New file search endpoint
### Core (v0.11.0 -> v0.11.1)
* Data migration
* Delete submission
### State Tracking (v0.7.5 -> v0.7.6)
* Updated processing to limit to single submission envelope
### Validator (v0.6.9 -> v0.6.10)
* Single submission updates
* Handling of ontology validation request error
### UI (v0.11.3 -> v0.11.4)
* Updates to metadata detail view
* Submission deletion

## Data Processing Pipelines and Execution Service
### Version(s): 
### Lira: v0.22.6 -> v0.22.7
* Improve the logging by linking the Pub/Sub message Id to the bundle, which helps to debug.
### Adapter-pipelines: v1.1.0 -> v1.2.0
* Add default max_retries to SmartSeq2 workflow options
* Pass pipeline version used by the Lira config into the adapter workflow inputs

## Data Portal - Azul
### Version(s): 
### bb0adac45d81e35e329daf981375aa011a36b03f 
* dcd82371 Set AZUL_DEBUG to 0 on CI; log ES queries only if 2 (#1444, PR #1451)
* 8800e66a Don't purge fail queues before reindex (#1422, PR #1437)
* d194dc74 Upgrade HCA CLI dependency to 6.4.0 (#1379, PR #1453)
* 2910fc5b [R] Ensure that sharing an ES domain uses correct number of shards (#1412, PR #1420)
* 07634af5 Fix: IT logs requested URL with trailing question mark (#1426)
* 911a8f2c Set AZUL_DEBUG=1 in `dev` and `sandbox` (#1413, PR #1421)
* 225699a3 Add support for blank `/integrations?entity_id=` (#1340, PR #1394)
* ca5fae51 Gitlab boundary allows reading DSS parameter store (#1314, no PR)
* d53b054d Parallelize delete notifications for integration test (#1410, PR #1419)
* c408e1ac Update README.md for setup/build instructions (#1384, #1370, PR #1385)
* 140cfad9 Add support mandatory parameters in validation (#1353, PR #1392)
* e7eda2b8 [R] Fix: Indexer ignores mismatch between _foo and _foo_types (#1344, PR #1382)
* 2b1ec338 [R] Add support for `file_core.content_description` (#1364, PR #1377)
* 355e759b Use DSS parameter store to determine bucket names (#1314, PR #1369)
* d97597cb [R] Allow sorting on donor count (#1378, PR #1391)
* f4bf7a04 Include species count in summary (#1388, PR #1393)
* f67de593 Switch to `GET /bundles/all` (#1313, #1357, #1347, #1174, PR #1371)
* 5c310943 Add `project.supplementary_links` (#1338, PR #1389)
* 5ac76ad9 Backport hotfix for #1331 from staging to develop
* 9e5b706e Remove health endpoint duplication in indexer & service lambdas (#1290, PR #1353)
* ab8eb600 Disable check_autosquash on Travis (#1386, PR #1387)
* b9c847fa List all matrix files in manifest (#1226, PR #1286)
* f0369191 Fix: IT fails at times unless reindex has been run (#1174, PR #1352)


# 2019/11/14 Prod Hotfix Release Notes
## Ingest
### Version(s):
#### Core 0.11.0
* Migrate internal mongo database to latest version (4.2)

# 2019/11/07 Prod Release Notes
## Ingest
### Version(s):
#### Ontology 1.0.11
* New release of HCAO and EFO slim with new assay, sample enrichment and library preparation terms.


# 2019/11/05 Prod Release Notes
## Ingest
### Version(s):
#### UI v0.11.3
* Security fixes
#### Exporter v0.10.1
* Pointing to latest ingest client version which is using new SchemaTemplate & SchemaParser
#### Staging Manager v0.5.5
* Pointing to latest ingest client version which is using new SchemaTemplate & SchemaParser
#### Validator v0.6.9
* Return INVALID ValidationReport when describedBy schema can't be retrieved

## Secondary Analysis
### Lira: v0.22.3 -> v0.22.6
* Pass pipeline version from the Lira config to the workflow inputs
* Add monitoring image from the Lira config to the workflow options (if defined)
* Fix monitoring image set-up to record workflow metadata in BigQuery
* Fix path to final workflow log directory

## Azul
### Version: 77e059d62a314db11d4af9818db8929fe0dbfb81
* cae54095 Fully qualify dynamodb-local image reference (#1380, PR #1381)
* 3788b6a5 Add -U to `pip` invocation in README (PR #1375)
* c52d4918 Remove SCEA E-EHCA-1 portal integration (#1372, PR #1373)
* 7d521adf Remove SCP495 study from portals db (#1360, PR #1362)
* f5ad4bdb Improve deployment cleanup process (#1303, PR #1307)
* f0db7c71 Refactor DSS client creation; upgrade metadata-api (#1365, PR #1366)
* 7e977eea Add entity_ids param to integrations endpoint (#1318, PR # 1329)
* 405d79da Add azul.dss to doctests (PR #1363)
* d084b147 Enforce source code formatting rules (#1358, PR #1359)
* 7e317af0 Enforce pep8 (#1355, PR #1356)
* 460cb781 Rename local_integration_test to integration_test (#1348, PR #1351)
* 5c8eeb51 Add Xena portal integrations (#1345, PR #1346)
* bb892538 Generate release notes with script (PR #1349)
* b67bb4f1 [r] Include fields that allow CLI downloads for full manifest (#1273, PR #1343)
* f183e9d5 Format OpenAPI spec JSON for apidev.py (PR #1341)
* 34f465a9 Update SCEA portal details (#1337, PR #1339)
* f2cd57e1 Limit 'size' parameter to 1000 or less (#1257, PR #1323)
* f35c804f Prefix TEST_MODE with AZUL_ and reduce chance of leaving it set (#1316, #1317, PR #1332)


# 2019/10/29 Prod Release Notes
## Secondary Analysis
### Version(s):
#### Lira: v0.22.2 -> v0.22.3
* Write the timestamp to inputs for adapters
* Update the SmartSeq2 query to match mouse data and remove the unnecessary "should" clause
* Update testing data to reflect moving adapter pipelines into a new repo
* Update scripts that get/create/delete DSS subscriptions to use elasticsearch as the default query type
* Turn on subscriptions for mouse ss2 and mouse 10x data.

#### pipeline-tools: v0.56.6 -> v1.1.0
* Migrate the following existing adapter pipelines and associated inputs from the pipeline-tools repo:
optimus
* cellranger
* smartseq2-paired-end
* smartseq2-single-end
* Migrate the submit pipeline from the pipeline-tools repo.
* Add readme files for the repo and the pipelines added to the repo.
* Add the ability to disable call-caching in the prep task using a timestamp parameter
* Remove file format input parameter (moved into the pipeline-tools code)

## Azul
### Version(s): 5f4994f51ee1277f7e5f278d234afd00ee89c919
* 58d3124d Fix deployment destruction, make example use DSS integration (#1334, PR #1336)
* ba4f1a39 Remove `reindex.py --sync` and suppress deletions in TEST_MODE (#1276, PR #1310)
* 70703f27 Monitor latency for Azul health checks (#1151, PR #1321)
* 9805f3d5 Ensure tearDown runs when tests are cancelled (#1298, PR #1300)
* 0d1f0330 Cache health check response to reduce service load (#1224, PR #1297)
* b263edaf Prevent signature expiration in copy bundles script (#1325, PR #1326)
* 572d62c9 Fix: CloudWatch Alarm resolution does show up on Slack (#1233, PR #1322)
* 5b80bff6 Rename `tsv` format to `compact` & `bdbag` to `terra.bdbag` (#1086, PR #1306)
* 207f1963 Fix: DSS staging bucket swap (PR #1331)


# 2019/10/08 Prod Release Notes
## Ingest
### Broker v0.10.2
* Return list of parsing errors
* Pinned schema version in submitted spreadsheets
### UI v0.11.2
* Security fixes
* Hide spreadsheet upload component while loading submission
* Hide Integration Tests from Project List

## Azul
### Version(s): 077b4e033a7bc834f785afd398786906b23b7c61
* bb61965f Fix broken log messages in MiniDSS (PR #1328)
* f6e77949 Update portal integration UUIDs (#1324, PR #1327)
* a2f9817c Add tests of request logging (#1079, PR #1301)
* 408c3374 Archive artifacts from secrets clean-up with BFG (#1194, PR #1308)
* b1569858  Add `GET /integrations` API endpoint (#1243, PR #1288)
* 491c2a65 Add generic request/response logging (#1079, PR #1281)
* 719dbda1 Add script for copying bundle between DSS instances (#386)
* 45eb2228 Modify work-around for zarray files (#1302, PR #1304)
* 08b78f35 Fix bugs in apidev.py script (#1291, PR #1296)
* 74d2dee4 More type checker fixes (PR #1294)
* 574742fd Explain deploying for apidev.py docs (#1292)
* a696d76c Switch sandbox and dev to DSS integration (#1282, #1311)
* 4fe28c39 Added assertion to validate full manifest file name (#1283, PR #1293)
* 2545676b Automatically provision Azul/DB health checks in DCP-wide composite #(1150, PR #1150)
* d3dc27ef Validate request parameters (#840, #240, PR #1135)
* 2fdb8f3d Backport hotfix for #1282 to develop (PR #1287)
* d1002020 Change BDBag column header names from `dos` to `drs` (#1279, PR #1280)

# 2019/10/02 Prod Release Notes

## Ingest
### Broker v0.10.1
* Fix linking
### Validator v0.6.8
* Fix retrying of file validation
* Security Fixes
### UI v0.11.1
* Remove unnecessary logging
* Added link to project view from the submission view

## Data Store
### Version: 4b10ceea51249995cbe89ba9f109dcb980188a01
* 4b10cee - (tag: 2019-09-25-17-08-46-staging.release, origin/staging, origin/integration) Fix signature in daemons/dss-notify-v2/app.py (#2449) (7 days ago)
* 8910328 - Define the API to retrieve and playback events (#2435) (7 days ago)
* 8ba6787 - Use the flash-flood library to record bundle events (#2434) (10 days ago)
* 91a381d - Define the bucket hosting DSS event data (#2433) (10 days ago)
* 9b69d3d - Add SSM parameter store functionality to dss-ops (#2432) (12 days ago)
* fa26b6d - Add response-content-disposition to GET /file. (#2371) (13 days ago)
* f8ffee9 - Bump cloud-blobstore version to 3.2.0. (#2431) (13 days ago)
* c6b42d7 - Bump httpie from 1.0.2 to 1.0.3 (closes #2404) (13 days ago)
* 68784a6 - forgot to fix this endpoint here too (#2430) (13 days ago)
* 9c74f3b - DSS SmokeTest: Test Order (#2428) (2 weeks ago)
* acdb110 - Bundle: enumeration (#2318) (2 weeks ago)
* 561cfb3 - [easy] Add file-type and file-size for ttfb fetching. (#2425) (2 weeks ago)
* 4d85a89 - update terraform in docker file (#2424) (2 weeks ago)

# 2019/09/24 Prod Release Notes

## Secondary Analysis
## Version(s): N/A

* Update subscription queries to specify latest metadata versions and trigger analysis off of ingested datasets (not just testing data).

## Data Store
## Version: fbb073543290082aab4f2950c5a71858bde4ba4f

* fbb0735 - (tag: 2019-09-18-15-32-10-staging.release, tag: 2019-09-09-14-43-05-integration.release, origin/staging) Adding a document to explain the action and resource relationship for… (#2395) (3 weeks ago)
* fa24dd1 - (origin/master-copy) Requirements Update (#2410) (4 weeks ago)
* 2263c9e - Increase dss notify workers. (#2408) (4 weeks ago)
* 4a3416b - Revert "Bump httpie from 1.0.2 to 1.0.3 (#2397)" (#2401) (4 weeks ago)
* ef3476b - Bump httpie from 1.0.2 to 1.0.3 (#2397) (4 weeks ago)
* 71957eb - Fix flaky test: TestFileApi.test_file_get_checkout . (#2396) (4 weeks ago)

## Azul
## Version(s): 4b9cacd802e0233a43add740614e8d2618d8f912

* 367099f Remove prefix for 'integration' integration test (#1282, PR #1285)
* 4b265f4 Generalise aggregation field translations (#1191, PR #1246)
* 4f1fb84 Tweak README instructions for determining when to reindex (PR #1267)
* 74690a1 Quote file name in Content-Disposition header of full manifests (#1247, PR #1261)
* 150332c Remove BFG redaction from TruffleHog and gitsecrets config (#1194, PR #1263)
* b0f8367 Document fix for hung test containers on Gitlab (PR #1258)
* 8ddf31f Change DOS URIs to use `drs` scheme (#1252, PR #1255)
* a7f73b6 Display Swagger UI with docs from app.py (#1163, PR #1227)
* 2df1946 Improve automation of PR branch squashing (#1245, PR #1254)
* 9390d46 Assorted README changes (PR #1250)
* 65abdda Make request config a plugin method (#1234)
* cbe399a Update changelog generation command in README (PR #1236)
* 433c03a Clarify contribution guidelines on logging and string interpolation (PR #1239)
* 2d2138e Hotfix: Quote file name in CD header of full manifests (#1266, PR #1268)
* b3a2852 Quote file name in Content-Disposition header of full manifests (#1247)

# 2019/09/13 Hotfix Release Notes
## Ingest
## Version(s)
### Core: v0.10.1
* Tracking uuid of staged metadata files
* Handling bundle manifest null fields
* Logging unhandled exporting exceptions
* Updated primary submission documentation

### Exporter: v0.10.0
* Fix simple updates issue when staging shared metadata files among bundles

# 2019/09/11 Hotfix Release Notes
## Secondary Analysis
## Version(s):
### Lira: v0.22.2
* Update pipeline-tools version to fix getting metadata from the production data store
* Add config flag for testing mode
* Add hash-id backfill script

## Ingest
## Version(s)
### Core: 2c5f56c
* Handling bundle manifest null fields
* Logging unhandled exporting exceptions
* Updated primary submission documentation

# 2019/09/10 Production Release Notes

## Secondary Analysis
## Version(s):
## Lira: v0.22.1
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

## Skylab: optimus_v1.3.5
* Increase memory for GeneSortBam, CellSortBam, CalculateCellMetrics and CorrectUMItools

## Pipeline-tools: v0.56.6
* Fix bug in passing deployment to dss_client
* Fix to handle bundles missing lane index
* Fix getting metadata for bundles in the production data store
* Remove data file checkout when only retrieving bundle metadata
* Remove max_retries parameter from adapter WDLs so that it can be set by the workflow options file

## Falcon: v0.4.3
* Get labels when de-duping to properly prioritize duplicate on-hold workflows
* Update logic for determining whether to release an on-hold workflow to handle duplicate notifications or updates in quick succession

## Azul
### Version(s): 1c201594c23e1f9355ec8305dcebfcf9f6be92c5

* 6723a51 Add DRS domain to sandbox deployment
* 2270875 Change to DRS URI (#919)
* 942d7eb Add Content-Disposition header to the full TSV (#1139)
* dd19699 Inline silly method
* c602003 Remove unused code
* 1ab9146 Simplify use of abstract class
* f1351cb Fix name warnings
* 7a90379 Fix type miscellaneous type check warnings
* 2679001 Remove unused code
* 691208a Fix source code formatting
* 8351e25 Improve distinction between mutable and immutable JSON

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

* Fixed RegEx loose pattern matching in biomaterial_core schema_version and insdc_sample_accession properties

## Data Browser
### Version: 4f57e772d1a1a1d1ce48edcf943bd599d84fafe7

* 4f57e77 Add a link to the data release policy to all project pages. Resolves #775. (#847)
* d927091 Create tests to cover Terra functionality in get data flow. Resolves #757. (#844)
* 07025f1 Fixed display of check mark on download of TSV. Resolves #843. (#846)
* 8e424ee Added poll for TSV on project table and detail. Resolves #712. (#842)

# 2019/09/04 Production Adhoc Release Notes

## Ingest
### Core (v0.10.0)
* Added persistence support for keeping track of staged metadata files.
### Exporter (v0.9.0)
* Modified file staging mechanism to address file staging issues.
### Broker (v0.10.0)
* Updated error message handling.
### UI (v0.11.0)
* Added support for new error message operations.

# 2019/09/03 Production Release Notes

## Data Store
### Version: fc8d411b022bfbc8c6c023e59c5e81476d0efe1d

* fc8d411 - (tag: 2019-08-28-15-43-56-staging.release, tag: 2019-08-27-14-32-26-integration.release, origin/staging, origin/integration) Add retries to verification in _test_gs_cache(). (#2372) (8 days ago)
* 64ee180 - Added details of notify intervals (#2368) (11 days ago)
* 2e73ab3 - Fix failing collections tests (12 days ago)
* 258e4b5 - Add pagination response headers (closes #2287) (12 days ago)
* c23811d - Fix improper markdown (#2367) (13 days ago)
* 2feac5f - (origin/natanlao-limit-put-collections) Fix 500 on delete nonexistent bundle, again (fixes #1918) (#2351) (13 days ago)
* 9fd58d3 - Add ttl to async db items. (#2363) (2 weeks ago)
* d846f4d - DSS Operations: Checkout (#2366) (2 weeks ago)


## Azul
### Version(s): 493d2c6a3e02c5d25fb929c0be4bf84c4a0a8ce1

*  e7ee681 Purge queues during reindexing (#1185, PR #1231)
*  b433157 Document process for deleting a deployment (#1054, PR #1232)
*  6ed60f3 Add missing target to .PHONY in Makefile
*  f9e960b Add `make` check for personal deployments
*  889c8b6 Cache full manifests (#1138, PR #1215)
*  a217844 Reduce code duplication and fix formatting of manifest tests
*  1a9559a Reorder lambda policy for clarity
*  478ad38 Avoid 403 when accessing missing objects in DSS bucket
*  dab847b Change `/health/all` to `/health/`
*  b013197 Explicitly activate `responses` in test_laziness
*  44dc573 Remove FIXME refering to ticket closed as `won't fix`
*  70bbec1 Fix missing test logger configuration
*  74e2dfd Optimize imports in azul.time
*  fc44fb1 Renamed manifest tests to be more descriptive
*  3b71b54 Log ES requests at DEBUG level, not INFO
*  6e543c9 Fix formatting
*  415a3f1 Fix type check warnings with translate_fields
*  f4b73e6 Remove handling of sets when translating fields
*  f4cd2c0 Receive Slack warning if fail queues are not empty (#1168)
*  21d9d6f Re-enable date detection, unmap contents.metadata in ES (#1173)


# 2019/08/27 Production Release Notes

## Data Store
### Version: 1af301db8a5935e63b9407cfcebd86a184f3fa2c

* 1af301d - (tag: 2019-08-21-15-14-21-staging.release, tag: 2019-08-19-21-44-19-integration.release, origin/* * staging, origin/integration) Revert "DSS/Operations: Checkout  (#2264)" (#2365) (8 days ago)
* dea261a - DSS/Operations: Checkout  (#2264) (8 days ago)
* ac88643 - remove hard-coded stage name in secrets tests (#2364) (8 days ago)
* ad90efb - (tag: 2019-08-19-14-54-49-integration.release) This pins pyyaml <= 5.1 for aws cli compatibility (#2348) (11 days ago)
* df13ac9 - Update like to security policy (#2361) (11 days ago)
* 006e7d8 - Relax sync size limit (#2354) (11 days ago)
* 63568a3 - Add secrets management to dss-ops script (#2325) (11 days ago)
* 81df1db - Schema typo fix (s/it/is) (12 days ago)
* de45167 - Assert we don't checkout to the main bucket (avoiding a sync error). (#2350) (13 days ago)
* 53fc89a - Revert "Fix 500 on delete nonexistent bundle (fixes #1918)" (13 days ago)
* 3b0fd70 - Fix 500 on delete nonexistent bundle (fixes #1918) (13 days ago)
* ecde208 - Simplify release scripting (#2347) (2 weeks ago)
* e44563e - More informative release status (#2345) (2 weeks ago)

## Azul
### Version(s): e101fd2e81cb0f56fc025d756e6d6070ac3d9a5b

* e101fd2 Merge branch 'staging' into prod
* 21f6ade Merge branch 'integration' into staging
* a64583c Merge branch 'develop' into integration
* f4cd2c0 Receive Slack warning if fail queues are not empty (#1168)
* 21d9d6f Re-enable date detection, unmap contents.metadata in ES (#1173)
* 32a47ff [r] Re-enable date detection, unmap contents.metadata in ES (#1173)

# Prod 2019/08/20
## Ingest
### Core v0.9.4
* Memory-optimized findAssays() for stability
* Updated primary and secondary submission documentation
* New API endpoints for linking process to input bundle and input files

### Exporter v0.8.8
* Exporting major/minor schema versions in provenance
* Fix null:null submission error

### UI v0.10.1
* Display project uuid in submission view

### Validator v0.6.7
* Display project uuid in submission view

## Data Store
### Version c952076c08a3045f996f63241ac2ea42026d12e8
* 62c60d9 - (tag: 2019-08-14-16-06-17-staging.release, tag: 2019-08-13-17-57-16-integration.release, origin/staging, origin/integration) Dedicated Trufflehog CI/CD stage (#2342) (7 days ago)
* 03dea6f - Check the correct DCP branch status (#2339) (7 days ago)
* 64ef9e3 - Fix daemon import test CI (#2338) (7 days ago)
* f9cc3c3 - (tag: 2019-08-10-19-48-30-integration.release) Terraform v0.12.6 compatibility updates (#2337) (9 days ago)
* 5d1314a - Limit a user's v2 subscriptions to 100 per replica. (#2310) (10 days ago)
* 0ea5a2f - Limit user v1 subscriptions to 100 per replica. (#2309) (10 days ago)
* 7de0b14 - fixed integration test errors (#2326) (13 days ago)
* 56259b5 - Delete Test Subscription (#2304) (2 weeks ago)
* 04c0221 - Tagging Updates: Name (#2322) (2 weeks ago)
* d564509 - Revert "1k item limit in PUT /collections (closes #2281)" (2 weeks ago)
* 5679e8f - 1k item limit in PUT /collections (closes #2281) (2 weeks ago)
* 7bc38dc - Remove unused infra variables (#2316) (3 weeks ago)
* ee410fc - Bump requirements (#2288) (3 weeks ago)
* debaa1f - Update Readme.md (#2290) (3 weeks ago)
* 961601f - Use chalice request context (#2307) (3 weeks ago)
* dcb00b2 - Require version in PUT /collections (closes #2280) (#2306) (3 weeks ago)
* 45600d3 - update ENV (#2291) (3 weeks ago)
* 003a314 - Make sync cleanup less flaky (#2289) (3 weeks ago)

## Azul
### Version(s): 4c9fd20cf8a4ff818f2a7082b19ab4cb00821bbc
* 6d07848 Test logs list thread name and timestamps (#1222)
* 17b5aa8 Initial request for full manifest returns no hits (#1219)
* 96150c8 Fix None filter for missing fields (#1202)
* a2637e7 Update README.md with changes to promotion procedure
* 0c83f55 Refine documentation on AZUL_DEBUG (#419)
* c7fffb3 Refactor queue management script (#1204)
* c48ebd1 Refactor lambda management script
* cef3f21 Update pip req to 10.0.1 (#1195)

## Metadata Schema
### Version(s):
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

### Functionality changes:
* Added two optional fields to represent schema major and minor versions in provenance. Fixes#1076.


# Prod 2019/08/13
## Ingest
### UI: v0.10.0
* Disabled retry-validation workaround button
* Upgraded Angular to version 8, NodeJS to 12.7.0

### Core: v0.9.3
* Fixed bug when attempting to parse submission errors from the importer/exporter

### Broker: v0.9.2
* Fixed bug when sending submission errors to ingest-core

## Upload
### Version: 4.4.3
* Internal cleanup

## Data Portal
### Version(s): d03ee3cbd3299028688424620cad4f6a2cc88e3c
* d03ee3c Replace icons on home page and contribute page. First pass - home page only. #450. (#476)
* 507c03b null in summary response cause portal to go blank. Resolves #480.


## Data Store
### Version: dd76aa91b74e7e02c70f3f5c7e8a0541cf92f409
* 6a2c2c4 - Broad Integration Test Accounts update (#2283) (3 weeks ago)
* b74823c - Notify V2 Payload Context (#2277) (3 weeks ago)
* 208caeb - Add retries within collections testing. (#2274) (3 weeks ago)
* 4797c01 - Operations for managing the ES index and subscriptions (#2269) (3 weeks ago)
* ffc5e76 - Use better name for verify sync op (#2278) (3 weeks ago)
* c6a768b - Increase concurrency safety of sync cleanup (#2272) (3 weeks ago)

## Azul
### Version(s): 729ec15646e5dbd6a14da7d2e0c597f523de0711
*  45daaaa Fix: None filter crashes summary response (#1199, PR #1201)
*  04e6ee0 Add a script for resetting the indexer (#451, PR #1182)
*  3da1db4 Fix app, test and script logging (#419, #1175, PR #1189)
*  ad89518 Fix: Service response leaks `null` substitutes (#1179, PR #1180)
*  a373baf Eliminate empty columns in full TSV (#1147, PR #1160)
*  de423c2 Add 'full' TSV format validation to integration test (#1171, PR #1187)
*  370ba09 CONTRIBUTING.rst states meaning of PR assignment
*  e8f6e13 Fix: Creating full TSV manifest without filter yields Chalice error (#1134, PR #1142)
*  258576a Backport: Remove project exclusions on `prod` (#1161)
*  479feed Absorb browser domain move from `prod.data` to `data`
*  a05d442 Remove project exclusions on `prod` (#1161)
*  301bdba Eliminate catch-all except clause in `BaseSummaryResponse` (#421, PR #1181)
*  a2f3445 Fix: Can't index `HPSI human cerebral organoids` (#1152, PR #1167)
*  8863c8d Disable date and numeric detection for mappings in ES indexes (#1152)
*  3fb640d Introduce test that reproduces bug in dynamic mapping ES (#1152)
*  7fbb4ea Revert "Hotfix: Can't index `HPSI human cerebral organoids`" (#1152)
*  d898068 Elaborate on promotions in README
*  0ab37e9 Add `make delete` target to only delete indices
*  b432f4d Partially revert logging changes (3a0dc5f, #637)
*  af6e1f5 Temporary removal of broken doctest (#989)
*  d537d81 Translate None values for Elasticsearch (#989)
*  1641039 Check for existing sitecustomize.py for envhook (#608)
*  d1c7401 Add `file_uuid` and `file_version` columns to full metadata TSV (#1068)
*  74237ed Incorporate changes from original hca_bundle_to_csv (#1068)
*  b2c9d97 Document tag for artificial notifications (#995)
*  4f96c54 Log transaction IDs during remote reindex (#1030)
*  3a0dc5f Fix: Importing app.py overrides test logging config (#637)
*  ae36559 Fix formatting in local_integration_test.py
*  fe009fc Fix: Direct bundle access does not check preconditions (#1153)
*  3e45be4 Upgrade Terraform to version 0.12.5 (#1145)
*  9261873 Pin version of Terraform null provider
*  5fb2500 Rename elasticsearch in health endpoint
*  a8c1661 Reduce load caused by health endpoint (#1124)
*  b12a3f7 Consolidate health check configurations
*  a159d3b Revert "Hot Fix: Exclude API endpoints call from health check to reduce load"
*  32dfccd [2/2] Add ability to requeue failed notifications (#1002)
*  1eac659 [1/2] Add ability to requeue failed notifications (#1002)
*  f0b0c96 Backport: Hotfix: Can't index `HPSI human cerebral organoids` project (#1152)
*  d3f4a72 Make organism age range searchable via contains, within and intersects (#512)



# Prod 2019/08/06
## Ingest
### Broker v0.9.2
* Fix reporting of submission error

### Core v0.9.3
* Fix failure in POSTing submission endpoint

### Exporter v0.8.7
* Reinstantiate DSS client to prevent token expiration

### UI v0.9.7
* Removing button to do retry when metadata is invalid

### Validator v0.6.6
* Multiple file validation jobs fix

## Secondary-Analysis
### Optimus v1.3.3
* Disable the preemptible for `Calculate Cell Metrics`

# Prod 2019/07/31
## Ingest
### Core v0.9.2
* Put back authentication for PUT & PATCH requests

## Data Store
### Version 2d05ab4c429452c1977857c9d347a59befa2fa91
* 2d05ab4 - Retry-After header values added for 500 responses. (#2144)
* 9c71a79 - Add operation to output bundle metadata document (#2244)
* d1c2b59 - Use a tempdir in smoketest when downloading. (#2260)
* 99a8bce - Extend test_creation_date_updated time. (#2263)

## Secondary Analysis
### Pipeline-tools v0.56.1
* Increase the number of maxRetries for Optimus workflows.
* Improve error-handling in confirm submission step.
* Add default maxRetries to Optimus workflows.

## Data Portal
### Version de786aa91b1a8e0343db0901c398654b9587f139
* 6132385 update gatsby config for moved content dir
* b4fa82f closes #410, #468 set metadata content repo and read content repo outside of npm
* 3c9a60d content bump for exploring projects
* 07bd9c4 Add 'Draft Mode' for documents. Resolves #444. (#460)
* 2992e8f Bug fix conflicting banner messages with mobile menu. (#461)
* 4d81f3d update gitlab to only test prod in prod and lower in lower

## Data Browser
### Version d23546df5aa61840f608f49506bf1441e0989feb
* d23546d Removed maintenance banner. Resolves #738. Resolves #739. (#740)
* 9ad9040 On the projects detail page make the publications blue and clickable like a link (instead of view here) for publications that have a link. Resolves #735. (#737)
* ada2745 Fix link style on system down message. Resolves #638. (#736)
* 018ffa0 setup cache control for other environments
* 3fd22da fix bucket name
* 2f12e80 test index.html cache contol in dev
* 5d9d083 Removed unsued package-lock.json. Resolves #723.
* ca170d3 Change project table 'Download/Export' heading to 'Project Downloads'. Partial completion of project matrix download UI nits (#721). Resolves #728. (#734)
* dec6d6e Fixed matrix HEAD requests on pagination/filter. Resolves #722. (#727)
* 45dc00f Security updates (#726)
* 9fdd029 Refactored matrix URL to match manifest. Resolves #717. (#720)
* 070cbef Updated tests. Resolves #707. (#719)
* 5c8c7ee Dupe meta url (#718)
* 9aa3ae7 Prepared matrix download on project list. Resolves #707. (#715)
* 1f83489 Update project list metadata download link

## Azul
### Version 8aa9b0c1957c4ee904dbccf6cdab417b1df3217d
* 4c42c3d Retire /repository/files/export endpoint (#586)
* 438dade Use HMAC key ID instead of secret for idempotent subscriptions (#993)
* 82d898e Remove projectSummary from response (#1021)

## Metadata Schema
### Versions
* file_content_ontology.json v1.0.1
* analysis_file.json v6.1.1
* image_file.json v2.1.1
* file_core.json v6.1.1
* supplementary_file.json v2.1.1
* reference_file.json v3.1.1
* sequence_file.json v9.1.1
### Functionality Changes
* None


# Prod Hot-fix 2019/07/25
## Secondary Analysis
### Pipeline-tools: v0.56.0
* Improve error-handling in confirm submission step
* Add default maxRetries to Optimus workflows

## Skylab
### Optimus: optimus_v1.3.2
* Increase memory allocated to RunEmptyDrops task

### Lira v0.20.0
* Updated subscription queries for SmartSeq2 and Optimus to only get notified of testing data to unblock updating existing submissions.

### Falcon v0.4.1
* Fixes an issue with the noop implementation in v0.4.0
* Add a security.txt file to indicate where security issues should be logged
* Update falcon linting settings
* Add logic to not run a workflow on data that have already been run in Cromwell based on a "hash-id" label

# Prod 2019/07/23
## Upload
### Version: v4.4.2
* Before uploading a file, check to see if the file has already been uploaded by checking its filename and checksums and if it has, skip uploading it and return the file that already exists.
* Validation of clientside checksum against serverside checksum calculation
* fix for deregistering job definitions as part of deployments
* Updated resources for batch jobs

## Data Store
### Version: 2019-07-23-15-14-25-prod.release
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

## Data Browser
### Version(s): b9bff65285efca2b5855f6836270469a8de7bbf3
* b9bff65 Updated references to removed projectSummary. Resolves #713. (#714)
* 70f16a5 update matrix and tsv download urls
* 1b40df3 update metadata url to use https and new cloudfront
* c8d51e7 Project matrix (#704)
* 6fcd3f3 Updated parse of health response to match new API. Resolves #678. (#702)
* 87fbe14 Updated search parameter values. (#701)
* 2701d50 Matrix manifest (#700)
* 521887a Get Data: Project Detail Page Updates Two Column Layout. Show query logic in selected terms list. Resolves 624. Resolves 689. (#697)
* ba9685b Get Data: Project Detail Page Updates Two Column Layout. Resolves #689. (#695)
* 1dfd471 Show query logic in selected terms list and update selected facet chips. Resolves #591. Resolves #624. (#693)
* 0a86e18 Update Azul healthcheck endopoint to /health/progress. Resolves #678

## Azul
### Version(s): 0d86e3e96729a9c2426d0cd7f79cb6f9b541972a
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
* ffdd34b Fix: /health/progress is not lazy and  therefore slow (#1084)
* 9b29a39 Add test for laziness of /health/foo (#1084)
* 976ad06 Use DistinctAccumulator in CellSuspensionAggregator (#1039)
* 09a24cf REVERT ME: Avoid dots in entity ID column of Terra TSV (#1071)
* cf43fa6 REVERT ME: Switch from bundle to participant for Terra (#1070)
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
* a332176 Revert "DELETE ME: Disable `make subscribe` on Gitlab"




# Prod 2019/07/19 Hotfix
## Ingest
### Optimus v1.3.1
* This is a fix for the gene id and also we store gene id to gene name map into the zrr files.

# Prod 2019/07/17 Hotfix
## Ingest
### Core v0.9.2
* APIs for performing simple updates to bundles
* APIs for viewing JSONPatch diffs when performing updates
* Search submissions by project
* Disabled “Submit” button when linking hasn’t yet been completed(spreadsheet submissions only)
* Now using Java 11, Spring boot 2

###  Exporter v0.8.6
* Handles update submissions and performs simple bundle updates as necessary
* Separate AMQP listener for update messages
* Duplicate links in links.json fix
* Fix date format check

### Broker v0.9.1
* Handles update spreadsheets
* Providing a mechanism for generating and downloading update-spreadsheets from submitted spreadsheets
* Fix updating of file metadata when data file is uploaded first

### UI v0.9.6
* Widgets for uploading and downloading an update-spreadsheet
* Paginated project dashboard
* Widget to search for projects by title, shortname, etc.
* Submissions table view inside the projects tab

### Validator v0.6.5
* Added ontology validation keyword
* Ontology service updates
* fastq subprocess fix

### Staging manager v0.5.4
* ingest-client library updates, refactoring

### State tracker v0.7.5
* Now using Java 11


# Prod 2019/07/02
## Data Store 2019-07-02-15-33-47-prod.release-1-ga23f0ed
* De-register percolate queries across all indices (#2196)
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

## Metadata Schema
### Optimus 1.2.0
* reverting from Optimus 1.3.0 due to an error which was discovered

## Metadata Schema
### Versions
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
* analysis_file: 6.1.0
* image_file: 2.1.0
* reference_file: 3.1.0
* sequence_file: 9.1.0
* supplementary_file: 2.1.0
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
* file_core - 6.1.0
* file_content_ontology - 1.0.0
* file_format_ontology - 1.0.0

### Functionality
* Switched to pre-commit commit package
* Added pull approve functionality
* Changed travis conf file for multi-stage build
* Changed print statements to errors for linter musts
* Added check for required ontology schema properties
* Added the linter to the pre-commit hook
* Added python to travis. Added call to linter.
* Added new file_format_ontology ontology schema.
* Added optional content_description field.
* Added new file_content_ontology schema.
* Updated integration test spreadsheets to contain new optional content_description field.


# Prod 2019/06/11
## Ingest
### Core v0.9.1
* Added endpoints to find bundles by project UUID
### Exporter v0.8.4
* Retries when alerting state-tracker of completed bundles
* Improved connection management to AMQP broker

## Data Store
### Version: e0932c28634a407c96cd8e175321ecb3cc07c7aa
* fix tests/test_api.py test mode (#2165)
* Storage operations errors log object info (#2164)
* Async state convenience methods and bug fixes (#2136)
* Use STANDARD storage class to mark non-cached checkout objects (#2152)
* Resume unfinished GS copies (#2135)
* Increase file checkout test timeouts (#2163)
* Expose TimedThread exceptions to caller (#2157)
* Separate GCP and AWS collections paging testing. (#2162)
* Add short retry to get-item test (#2161)
* Specify replicas in sync test content-type (#2158)
* Change how content-type is propagated when caching. (#2154)
* Remove trailing whitespace
* Direct URLs for Files (#2138)
* Updated Authorization Endpoint Checks (#2146)
* Operation to repair file blob metadata (#2123)
* Verify checksums on `PUT /file/{uuid}` (closes #2000)
* update lambda-iam for accessing resource by tag (#2131)
* Update TTL (#2130)
* Pull logging into copy clients (#2134)
* We don't use travis for deploys anymore; update release.sh doc accordingly (#2132)
* Add verification storage operations (#2121)
* improve bucket mapping util (#2120)
* Fix typo in checksum parsing
* Increase operations daemon log level (#2119)
* Operations utils (#2115)
* Operations cloud executor (#2114)
* Operations CLI framework (#2111)
* Revert most pylib versions so that they fit in the lambda's size limit. (#2116)
* Add retries to PUT collection method when testing. (#2112)
* bucket names hot patch
* Add python shebangs to scripts. (#2110)
* Bump dependencies. (#2088)

## Data Portal
### Version(s): 46c81edabefc01119b093327e758d7c3ceb074fa
* 46c81ed Update README.md
* 1c69b99 Update readme for git-secrets
* 640a038 update gatsby version
* c021f9c Sticky header. Modification for Browse Metadata: Move TOC to RHS and prevent TOC from scrolling off screen (#436).
* 1ebb111 TOC
* b6eabf2 Updated summary response to handle new API. Resolves #452.

## Data Browser
### Version(s): e25307f53b0d2bedb16f15e4b25773ee2b030f95
* e25307f Update README.md
* a8dacb5 update readme for git-secrets
* 7622d6b Verify table heading/column names are readable on 13'' mac laptop screen. Resolves #649. (#677)
* bf0b323 Remove daos (#676)
* 80dcbd4 update node and npm versions for building and npm update
* 61f998e Fix for metadata column width. Modification to Update column name display to add an extra row and move counts below baseline. Resolves #664. (#671)
* 7b59be2 Update column name display to add an extra row and move counts below baseline. (#670)
* 4e3e222 Updated data tables to use generic data source. Resolves #660. (#669)
* e0c51ec Updated summary to match new API. Resolves #656. (#661)
* 363d5d7 Added maintenance mode banner to prod. Resolves #663. (#668)

## Azul
### Version(s): 4b02a27109ff8e15b2bff0fdaea36f09edeec194
* 7b4aa6d Fix: certain summaries truncated to 10 terms (#1047)
* fd06455 Return `gs://…` url with DRS endpoint (#920)
* 6310b7e Add imaging-specific facets (#885)
* 65cf8cb Ensure integration tests always clean up bundles (#994)
* 4e10eda Make trufflehog rules file hidden
* f9510c7 Require `git secrets` to be installed (#755)
* 36bbc58 Speed up indexing tests with  (#1040)
* c7d39b7 Revert "Return `gs://` url with DRS endpoint (#920)"
* 2c4a8b2 Return `gs://` url with DRS endpoint (#920)
* f083e0c Add DRS alias domain for service lambda (#918)
* 6b753af Add utility for interning immutable value objects


# Prod 2019/06/06
## Secondary Analysis
### Optimus v1.2.0
- Increase disk size for TagGeneExon scaled by input size
- Improve Performance of SplitBamByCellBarcode


# Prod 2019/05/28
## Ingest
- UI v0.9.4.rc
- Use Fusillade integration

## Upload  v4.3.2
- Add validation-scheduler and area-deletion lambdas to Big Red Button commands (`uploadctl` `runlevel` `stop/start/status`)
- Upgrade urllib3 for security
- Put API Gateway ID in terraform.tfvars instead of searching for it during deploys

## Metadata Schema
### Versions
- imaging_protocol.json schema - v11.1.1
- process.json - v9.1.0

### Functionality

- Fixed probe field to reference correct schema. Fixes #980.
- Added optional start_time and end_time fields. Fixes #742.
- Archived unused 10x integration test spreadsheet. Fixes #957.


# Prod 2019/05/08
## Ingest
### Ingest-ui v0.9.2
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
### Version: 6a3639a97acc46cde7d98530c604f777ecee99fd
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


# Prod 2019/04/30
## Ingest
### Validator v0.6.4
* Only perform file validation if the the File metadata document is valid

## Data Store
### Version: 2019-04-30-15-17-36-prod.release
* modified description for /PUT/Collection (#2046)
* Send deletion JMESPath notifications (#2049)
* Exclude very large bundle manifests from ES document (#2031)
* Resource Tagging with Terraform (#2010)
* Add paging to collections. (#2013)
* Update Readme.md Flow
* Retain Elasicsearch logs for 5 years (#1987)
* Add support for PATCH /bundle (#1978)
* Centralize SECURITY.md, and delete security.txt. (#1983)
* Swagger docs: follow common style (#1974)
* Update swagger with explicit retry-after headers. (#1961)
* Add a security.txt file. (#1965)
* Update deployment documentation (closes 1902)
* Update get file description. (#1958)
* Change prod bucket names for new encrypted buckets. (#1953)
* Add swagger descriptions based on dcp-cli issue #221. (#1930)
* Document subscriptions in swagger (#1916)
* Support GET /bundle paging (#1913)
* Fix JMESPath notification eventing bug (#1928)

## Secondary Analysis
### Pipeline-tools v0.48.3
* Update version of dcp cli to use at least version 5.1.0, which includes a fix for uploading large files

## Azul
### Version: 62164e4ec502b9a3549ff537b972e46397a4578a
* 62164e4 Exclude old BM_PC dataset in prod (#944)
* 46dc3ec Exclude old neuron_diff dataset in prod (#915)
* a1deea7 Fix: Terra requires name of first column to end in `_id` (#911)
* 51d8848 Fix: Terra rejects `.` in column names (#912)
* 8bf8aae Fix: Terra requires `samples.tsv`, rejects `bundles.tsv` in BDBag (#910)
* a1b5854 Added security.txt (#761)
* d5deca6 Added script to disable/reenable lambdas (#238)


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
