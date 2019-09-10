# Data Coordination Platform

[![Snyk Vulnerabilities for GitHub Repo (Specific Manifest)](https://img.shields.io/snyk/vulnerabilities/github/HumanCellAtlas/dcp/requirements.txt.svg?style=flat-square&label=Snyk%20Scripts%20Vulnerabilities&logo=Snyk)](https://snyk.io/test/github/HumanCellAtlas/dcp?targetFile=requirements.txt)

This repository servers two purposes.

1. It contains the manifest of which versions of which components
   are deployed to each environment.
2. It is the home of system-wide integration tests.

Before you can run the tests, you need to setup your environment:

    pip install -r requirements.txt
    # ping in #dcp-ops or #dcp-ops-help if you need valid service account credentials
    export GOOGLE_APPLICATION_CREDENTIALS={PATH_TO_VALID_SERVICE_ACCOUNT_CREDS_WITH_ACCESS_TO_DSS}

Instructions for running tests locally in python 3.6:

Be aware that you will be uploading bundles to the specified deployment (integration/staging/prod) of the DCP and running secondary analysis.
The test currently takes about 120 minutes to run (longer for optimus, shorter for smart-seq-2).

    DEPLOYMENT_ENV={ENV} make

To only run one of the pipelines, smart-seq2 for example, and retain the bundles (disable tombstoning) use Python 3.6:

	RETAIN_BUNDLES=True DEPLOYMENT_ENV={ENV} python -m unittest tests.integration.test_end_to_end_dcp.TestSmartSeq2Run.test_smartseq2_run

To only run one of the pipelines, smart-seq2 for example, use Python 3.6:

    DEPLOYMENT_ENV={ENV} python -m unittest tests.integration.test_end_to_end_dcp.TestSmartSeq2Run.test_smartseq2_run

## Security Policy
See our [Security Policy](https://github.com/HumanCellAtlas/.github/blob/master/SECURITY.md).

## Operations Wiki
See https://allspark.dev.data.humancellatlas.org/dcp-ops/docs/wikis/home.
