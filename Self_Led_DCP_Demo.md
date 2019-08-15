## DCP Demo (self-led)
**Target Audience:** DCP Staff

**Purpose:** Serve as a learning resource for end-to-end data flow in the DCP

**Components:** Ingest, Upload, Data store, Data pipelines/Analysis, Azul, Data Portal, Matrix

**Reference Document:** https://docs.google.com/document/d/1-9k9tcuIc4aTuxIo-KAT34R_OSca0j9_3LDNJwqksBQ/edit#heading=h.kuwifzq1d62x.

**Note:** This document was published in June 2018 so may have inconsistencies and steps missing. A v2 document will be published soon and linked here.)

### FAQ
**Who do I contact if I encounter any any issues while following the steps?**
Feel free reach out to #dcp-ops-help, create an issue in the DCP repository, or ping Parth.

**Do I need to have a certain level of technical proficiency to follow the steps?**
Technical proficiency should not be a requirement. Please reach out if you encounter any issues, as this indicates that the instructions need additions or modifications.

**How can I make edits to this document?**
Please create a PR in the DCP repository.

**Can I run this in production?**
No. Please follow the instructions and only utilize the staging environment.

**Will this project be available at tracker.staging.data.humancellatlas.org?**
No. The tracker ignores all test projects in order to not overload the view.

**What ids do I need to keep track of?**
Submission ID, Project UUID, Primary Bundle UUID, Primary Bundle FQID, Workflow UUID, Analysis Bundle UUID, Analysis Bundle FQID. These will be defined as a part of the demo.

### Demo
**Requirements**
```
    python version >= 3.6
    pip install hca
```
#### Phase 1: Primary submission preparation
**Components:** Ingest, Upload  
**Description:** In this phase, you will be uploading a spreadsheet through the ingest UI in order to create a submission. Then, you will utilize the HCA cli to upload the data files for the submission. Both ingest and upload are currently running in AWS infrastructure.
1) Please download a spreadsheet found at https://github.com/HumanCellAtlas/metadata-schema/tree/master/infrastructure_testing_files/current. These are test spreadsheets that are run through the DCP wide integration tests. Feel free to choose any of the options (Currently smart-seq-2/ss2 and 10x/optimus spreadsheets are available).
2) Open up the spreadsheet and browse through the tabs. This is a simple example that shows how the metadata is inputted into the system. The spreadsheet also has references to all the data files that we will upload in a later step.
3) Now it is time to create you own submission! Lets go to the Ingest UI at `https://ui.ingest.staging.data.humancellatlas.org` and log in with your organization (Broad/CZI/EBI/Stanford/UCSC) email. Please reach out to #dcp-ops-help if you encounter permission issues.
4) Click on `Start a new submission` in the upper right hand corner and upload the spreadsheet you downloaded in Step 1. Ingest is now processing the spreadsheet and parsing out the metadata into separate entities. You can click on the `metadata` and `data` files to watch as ingest populates and validates the metadata and file entities. This should be a relatively quick step.
5) Now click on the `data` tab. You should see the `Upload Area Location` populated with an S3 URI. Go ahead and copy this URI to your clipboard. This is the upload area pertaining with this submission.
6) Now lets upload some files to your upload area! The test files are available in a public s3 bucket. Open up the terminal of your choice and type in the following:
```
        hca upload select {URI_FROM_STEP_5}
        
        # For 10x/Optimus spreadsheet
        hca upload files s3://org-humancellatlas-dcp-test-data/optimus/
        
        # For SS2 spreadsheet
        hca upload files s3://org-humancellatlas-dcp-test-data/smart-seq2-one-bundle/
```
7) Your files have now been uploaded to the upload area. The upload service will checksum the files to ensure there was no corruption and notify ingest. Ingest will then move the file entities in the `data` tab to `Validating` and request that the Upload service validates the fastq files. The current fastq validator can be found at https://github.com/HumanCellAtlas/fastq_utils. Validation may take anywhere from 30 seconds to 10 minutes+ depending on a) whether the system is at cold start and b) how much load is already present in the validation queue. Under cold start, it will take some time for spot ec2 instances to spin up to validate your files. Go grab a coffee!
8) Lets go back to the ingest UI. Now your file entities in the data tab should have gone Valid and the submission also should have gone Valid. Your submission is ready for the next phase!

#### Phase 2: Primary submission exporting
**Components:** Data Store, Ingest, Upload  
**Description:** In this phase, you will be depositing your submission into the data-store. A submission can deposit many data bundles into the data store; however, the test spreadsheets used in this demo will only deposit one primary bundle.
1) In the Ingest UI `Submit` tab, go ahead and click on submit! **Do not change the default checkbox for triggering workflows**. The envelope should now transition into `Submitted`, `Processing`, and `Completed` states. These transitions may occur within 5 minutes but may take longer if the exporting queue is large. In the exporting stage, Ingest is depositing all of the data and metadata files into the data store. Under the hood, the data store is copying these files from your upload area. Each data and metadata file will have a fully qualified ID composed of a UUID and Version.
2) After the submission moves into the `Completed` state, you should now see your bundle in the `Submit` tab! Go ahead and click on the `dss api` link to see the bundle manifest stored in the DSS. Each bundle in the data store has a fully qualified ID that is composed of a UUID and Version. The bundle manifest is generated by Ingest and is a composition of the file FQIDS mentioned above. Your bundle and files were stored in AWS and are now being synced over to GCP. You will notice that some of the files in the manifest are indexed and others are not. In general, all metadata files are indexed in order to allow for searchability via the data store's elastic search cluster.
3) Lets go ahead and download the bundle using the HCA cli. This step will download the bundle into a directory named after bundle UUID.
        hca dss download --bundle-uuid {BUNDLE_UUID_FROM_STEP_2) --replica {AWS OR GCP}
4) Go ahead and open up some of the files in the directory. You should notice that these metadata files have values tracing all the way back to the spreadsheet. The structure of the metadata files is defined by the schema as found at https://github.com/HumanCellAtlas/metadata-schema.

#### Phase 3: Analysis
**Components:** Analysis, Data Store, Ingest, Upload  
**Description:** In this phase, you will be taking a look at the analysis workflow corresponding with your bundle. You will follow the workflow as it completes and deposits the analysis result back into the data store via Ingest/Upload. Analysis is currently running workflows via cromwell in GCP infrastructure.
1) Go back to your submission in the Ingest UI and copy the `Project UUID` from the `Overview` tab.
2) Now replace the project uuid in the URL and visit the Job Manager UI at https://job-manager.caas-prod.broadinstitute.org/jobs?q=project_uuid%3D{PROJECT_UUID_FROM_ABOVE_STEP}. You should now see a workflow running corresponding with your bundle.  The data pipelines component maintains a subscription to the data store in order to trigger workflows. When a bundle is synced in GCP that meets the query, the data store notifies the analysis component. The rules of the subcription are based on metadata fields that are currently supported by production pipelines (factors like species, library construction approaches (10x/ss2), etc). The current subscriptions can be found at https://github.com/HumanCellAtlas/lira/tree/master/subscription/elasticsearch_queries.
3) Your workflow will move through `Prep`, `Analysis`, and `Submit` stages. In the final stage, it will interact with the ingest API and HCA cli to upload the workflow output files within a submission. The spreadsheet to JSON conversion is skipped, as the analysis component directly deposits JSON files via the ingest API. The workflow can take up to 2-3 hours. Go do some work!
4) After the workflow completes and the corresponding ingest envelope has a state of `Completed`, you should now be able to retrieve your analysis results from the data store. Lets switch it up and use some python and the HCA dss python bindings to find your bundle. Copy the python below to a file on your local machine. Invoke it with `python script.py --primary-bundle-uuid {YOUR_PRIMARY_BUNDLE_UUID}`. This script will print out the bundle FQID of your analysis results.
```
#!/usr/bin/env python
import argparse

from hca.dss import DSSClient
​

def find_secondary_bundle_fqids(client, replica, primary_bundle_uuid):
    q = {
        'query': {
            'match': {
                "files.analysis_process_json.input_bundles": primary_bundle_uuid
            }
        }
    }
    fqids = execute_query(client, replica, q)
    results = list()
    for secondary_fqid in fqids:
        results.append(secondary_fqid)
    print(results)
​

def execute_query(client, replica, query):
    resp = client.post_search(replica=replica, es_query=query)
    fqids = [hit['bundle_fqid'] for hit in client.post_search.iterate(replica=replica, es_query=query)]
    assert len(fqids) == resp['total_hits']
    return fqids
​
​
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replica", default="aws", choices=["aws", "gcp"])
    parser.add_argument("--primary-bundle-uuid")
    args = parser.parse_args()
    dss_client = DSSClient(swagger_url=f"https://dss.staging.data.humancellatlas.org/v1/swagger.json")
    find_secondary_bundle_fqids(dss_client, args.replica, args.primary_bundle_uuid)
```
5) Lets go ahead and download the analysis bundle using the HCA cli. This step will download the bundle into a directory named after bundle UUID.
        hca dss download --bundle-uuid {BUNDLE_UUID_PRINTED_FROM_SCRIPT) --replica {AWS OR GCP}
6) Go ahead and open up some of the files in the directory to get a feel for what is contained within an analysis bundle, including an individual gene x cell matrix.

#### Phase 4: Primary submission exporting
**Components:** Data Store, Azul, Data Browser  
**Description:** In this phase, you will be looking at your project in the data browser!
1) This is more of an informational step. Just as analysis has a subscription to the data store, azul (the browser backend) has a subcription to all bundles in the data store. Azul will then do a partial download of the bundle and index it based on the facets that are made available for search and exploration in the data browser.
2) Replace the project UUID in the url and browse your project at `https://staging.data.humancellatlas.org/explore/projects/{YOUR_PROJECT_UUID}`

#### Phase 5: Matrix Service
**Components:** Matrix Service  
**Description:** The matrix service provides concatenated matrices from the individual matrices produced by the workflows. Multiple output formats are supported and the matricies are accompanied by metadata values and cell IDs. The matrix service is currently not subscribed to a subscription in the staging environment. Please visit https://matrix.staging.data.humancellatlas.org for API documentation and to find data available in the staging environment.
