# Deletion and deprecation of data in the DCP

One of the DCP's primary objectives is to ensure the durability of the
(meta)data it contains and to maintain a complete record of the changes made to
it. The DCP achieves this by never overwriting a (meta)data file but instead
treating an update to such a file as the addition of a new version of that
file. And instead of physically removing a file version, the DCP hides that
file version behind a deletion marker.

Under certain circumstances however, the *physical deletion* of an file version
is required. The first section of this specification describes the
circumstances and mechanisms for logical and physical deletion of files and the
bundles that contain them.

Independently, it may be required to discourage the use of (meta)data managed
by the DCP, be it for replication, analysis or aggregation, without actually
preventing that use. The DCP handles this by *deprecating* the (meta)data as
specified in section 2.

## 1. Deletion

### 1.1. Reasons

Reasons for deletion of (meta)data are

* consent to share (meta)data derived from a donor's specimens is withdrawn by
  that donor after the (meta)data was submitted to DCP
  
* that consent was never given but this fact is revealed only after the
  (meta)data was submitted to the DCP
  
* storing or processing the (meta)data causes a serious disruption of service
  within the DCP

* the (meta)data was submitted to the DCP by a malicious party in violation of
  the DCP's data sharing agreement. This includes (meta)data that violates the
  laws or regulations in a jurisdiction applicable to the DCP or the (meta)data
  it stores

Whether any of the reasons require a physical or logical deletion is at the
discretion of the administrator performing the deletion. That discretion is
guided by a standard operating procedure (SOP).

### 1.2. Process

Once it is determined that a (meta)data file needs to be physically deleted –
the details of this determination are the scope of an SOP – the following
procedure takes place:

1) An administrator identifies the Data Store file versions to be deleted. The
   administrator then identifies the Data Store bundle versions referencing
   those file versions.

2) The administrator issues `DELETE /bundles/{uuid}?version={version}` requests
   for those bundle versions against the Data Store REST API. If all versions
   of a bundle contain a file that is to be deleted, the administrator places
   such a request against every bundle version individually. Support for
   unversioned delete request as currently implemented by the Data Store will
   be removed in order to prevent the unintended deletion of bundle versions
   submitted to the Data Store after the deletion request is made.

   The body of the deletion request contains a JSON structure that is valid
   against the following JSON schema (as YAML):


   ```yaml
   type: object
   additionalProperties: false
   properties:
     admin_deleted:
       title: Always `true`. For backwards compatibility only.
       enum:
       - true
     deletion:
       type: object
       additionalProperties: false
       properties:
         reasons:
           title: |
              At least one reason for the bundle deletion. See above for an 
              explanation of each reason.
           type: array
           items:
             enum:
             - consent_withdrawn
             - consent_absent
             - service_disruption
             - legal
           minItems: 1
           uniqueItems: true
         type:
           enum:
           - logical
           - physical
           title: Describes the action to take on files in the deleted bundle.
           description: |
              - `logical`: Remove the metadata files in this bundle from any 
                           index and make the data files inaccessible but do not 
                           physically delete it. Remove or make inaccessible any 
                           secondary copies of those files.
              - `physical`: Physically and irreversibly delete the data and 
                            metadata files in the bundle, and any copy thereof.
         contact:
           type: string
           format: email
           title: |
              The email address to contact with questions regarding this 
              deletion.
   ```
   
   An example deletion marker body:
   
   ```json
   {
     "admin_deleted": true,
     "deletion": {
       "type": "physical",
       "reasons": [
         "consent_withdrawn"
       ],
       "contact": "hannes@ucsc.edu"
     }
   }
   ```

3) The DSS places a deletion marker (also known as "tombstone") in the
   underlying storage (S3 or GCP bucket). The marker's content is the body of
   the `DELETE /bundle` request. The marker causes `GET /bundle/{uuid}` to
   return a 404. If `{version}` signifies the latest version of the bundle
   identified by `{uuid}`, requests for `GET /bundle/{uuid}` without a version
   also return a 404. The same applies to HEAD requests, both versioned and
   unversioned. The file versions referenced by the deleted bundle version are
   not immediately affected by the deletion and remain accessible.

4) An administrator runs the DSS admin CLI to initiate a deletion daemon
   against one of the data store replicas. The deletion daemon runs in the
   background as an AWS Step Functions execution. The CLI can be used to
   periodically inquire about the progress of the daemon and retrieve its
   output.

   The deletion daemon enumerates all bundle deletion markers. For each bundle
   deletion marker the daemon performs the following actions:

   a) If the bundle deletion marker specifies `"type": "logical"`, the deletion
   daemon places a file deletion marker for every file version referenced by
   the deleted bundle version. This will make HEAD and GET requests against
   those file versions return a 404.

   b) If the bundle deletion marker specifies `"type": "physical"`, the daemon
   enumerates all blobs referenced by all file versions in the deleted bundle
   version and physically deletes those blobs from the underlying storage.

   The deletion daemon does not perform more than *N* logical file deletions or
   physical blob deletions per invocation. *N* should be configurable with a
   default of 10.

   The deletion daemon can optionally be invoked in "dry run" mode in which it
   simply logs the actions it would perform in a wet run. In dry-run mode, *N*
   is ignored.

   The deletion daemon is idempotent. Already deleted blobs and already
   existing deletion markers do not count against *N*.

### Primary indexes

Bundle deletion markers are indexed verbatim by the Data Store. The JSON schema
for deletion markers is defined such that there are no conflicts with the
top-level keys in the index documents for regular bundles (`files`, `manifest`,
`uuid`, `version` etc). Bundle deletion markers are therefore compatible with
regular bundle documents with respect to in the same index even if
Elasticsearch's dynamic mapping is enabled.

### 1.3. Replication

The replication process in Data Store replicates file and bundle deletion
markers. It does not replicate physical deletion of blobs. To physically delete
blobs in all replicas, an administrator needs to repeatedly run the Data Store
admin CLI to initiate a deletion process against each of the replicas.

### 1.4. Consistency

It is the administrator's responsibility to enumerate all bundles referring to
a file that is to be deleted and issue `DELETE /bundles` requests for each of
them. If the administrator misses such a bundle (a *dangling bundle*), users
requesting `GET /bundle` for a dangling bundle will be able to retrieve its
manifest. Likewise, `POST /search` requests will return the metadata for
dangling bundles. Secondary indexes like the Data Browser (Orange Box) will
continue to hand out (meta)data for dangling bundles. If users request `GET
/files` for a file contained in a dangling bundle and the requested file was
referenced by another already logically (physically) deleted bundle, the Data
Store will respond with a 404 (500) status code.

The administrator can initiate a consistency check against a storage replica to
list dangling bundles. The administrator can then issue more `DELETE /bundles`
requests for those dangling bundles.

### Secondary indexes

The Data Store can optionally notify subscribers about the creation of a bundle
deletion marker. Secondary index services need to register a subscription using
a query that matches deletion markers. When they are notified about a deletion
marker, they need to take the necessary actions to remove the data from their
database or index.

### Derived data

The metadata in bundles containing derived data must reference the input bundle
versions. Administrators are responsible for tracking down data bundles with
data derived from data in deleted bundles and to issue deletion requests for
them.

### Tiered storage

Physical deletion of blobs is effective across all tiered storage classes in
the underlying blob store (S3, GCP, ...).

TBD: Does deletion from Glacier involve a delay?

### Undoing logical deletions

TBD: 

### Open Issues

TODO: remove support for `all-versions` tombstone in Data Store

TODO: implement consistency check for dangling bundles
 
## 2. Deprecation

TODO:
