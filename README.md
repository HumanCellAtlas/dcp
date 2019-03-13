# Data Coordination Platform

This repository servers two purposes.

1. It contains the manifest of which versions of which components
   are deployed to each environment.
2. It is the home of system-wide integration tests.

To run the tests locally, use Python 3.6:

    pip install -r requirements.txt
    CI_COMMIT_REF_NAME=staging make

Be aware that you will be uploading bundles to the staging deployment of the DCP and running secondary analysis.
The test currently takes about 18 minutes to run.

## Security Policy
See our [Security Policy](SECURITY.md).
