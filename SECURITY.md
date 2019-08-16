# Human Cell Atlas Security

This document provides guidelines on vulnerabilities in the components
that the Human Cell Atlas project manages and how to report them.

## Vulnerabilities

Many of the Human Cell Atlas repos are a part of a large and complex system
built on cloud architecture in AWS and GCP, whose vulnerabilities these projects
are also subject to.  They also depend on a large set of third party libraries
(e.g., `google-auth`, `Jinja2`, and others listed 
[here](https://github.com/HumanCellAtlas/data-store/blob/master/requirements.txt) ),
though we attempt to mitigate this with Snyk in projects such as the `data-store`.

It is possible that a project or its dependent libraries contain
vulnerabilities that would allow triggering unexpected or dangerous behavior
with specially crafted inputs.

### What is a vulnerability?

Given the Human Cell Atlas's many components and projects, a vulnerability
could occur in multiple places, and particularly in the parts making up
our deployment platform, such as:
[ingest](https://github.com/HumanCellAtlas/upload-service), 
the [data-store](https://github.com/humancellatlas/data-store) itself, 
the [data-browser](https://github.com/HumanCellAtlas/data-browser), 
the [data-portal](https://github.com/HumanCellAtlas/data-portal).
or the [dcp-cli](https://github.com/humancellatlas/dcp-cli).

By default, public read access to files in, for example, data-store is intended and does
not require authentication, however, any method that circumvents the normal 
auth process for other endpoints **is** a vulnerability (check the swagger 
for endpoints that do or do not require auth: https://dss.data.humancellatlas.org/ )
and should be reported.

One of the most critical parts of any system is input handling. If malicious
input can trigger side effects or incorrect behavior, this is a bug, and likely
a vulnerability.

### Reporting vulnerabilities

Please email reports about any security related issues you find to
`security-leads@data.humancellatlas.org`.  This mail is delivered to a small 
security team.  Your email will be acknowledged within one business day, 
and you'll receive a more detailed response to your email within 7 days 
indicating the next steps in handling your report.

Please use a descriptive subject line for your report email.  After the initial
reply to your report, the security team will endeavor to keep you informed of
the progress being made towards a fix and announcement.

In addition, please include the following information along with your report:

* Your name and affiliation (if any).
* A description of the technical details of the vulnerabilities. It is very
  important to let us know how we can reproduce your findings.
* An explanation who can exploit this vulnerability, and what they gain when
  doing so -- write an attack scenario.  This will help us evaluate your report
  quickly, especially if the issue is complex.
* Whether this vulnerability public or known to third parties. If it is, please
  provide details.

If you believe that an existing (public) issue is security-related, please send
an email to `security-leads@data.humancellatlas.org`.  The email should include 
the issue ID and a short description of why it should be handled according to 
this security policy.

Past security advisories will be listed below.  We credit reporters for identifying
security issues, although we keep your name confidential if you request it.

:question: For information on our incident response process see [humancellatals/dcp-community/rfc/text/0009-Incident-Response-Plan](https://github.com/HumanCellAtlas/dcp-community/blob/master/rfcs/text/0009-Incident-Response-Plan.md)
