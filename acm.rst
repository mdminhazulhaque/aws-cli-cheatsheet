ACM
===

List Certificate ARNs and DomainName
------------------------------------

.. code:: bash

   aws acm list-certificates | jq -r '.CertificateSummaryList[] | .CertificateArn+" "+.DomainName'

.. code:: ini

   arn:aws:acm:ap-southeast-1:987654321:certificate/88c10c4e-a0ba-41e9-bbd4-734e0191e363 *.example.com

Request a Certificate for Apex and Wildcard Domain
---------------------------------------------------

|:arrow_right:| Covers both ``example.com`` and ``*.example.com`` in a single certificate

.. code:: bash

   aws acm request-certificate --domain-name example.com --subject-alternative-names "*.example.com" --validation-method DNS | jq -r .CertificateArn

.. code:: ini

   arn:aws:acm:ap-southeast-1:987654321:certificate/88c10c4e-a0ba-41e9-bbd4-734e0191e363

Get DNS Validation Records
---------------------------

.. code:: bash

   aws acm describe-certificate --certificate-arn arn:aws:acm:ap-southeast-1:987654321:certificate/88c10c4e-a0ba-41e9-bbd4-734e0191e363 | jq -r '.Certificate.DomainValidationOptions[] | .DomainName+" "+.ResourceRecord.Name+" "+.ResourceRecord.Type+" "+.ResourceRecord.Value'

.. code:: ini

   example.com      _a79865eb4cd1a6ab990a45779b4e0b27.example.com.   CNAME  _424c7224e1614c7c987ac.acm-validations.aws.
   *.example.com    _a79865eb4cd1a6ab990a45779b4e0b27.example.com.   CNAME  _424c7224e1614c7c987ac.acm-validations.aws.

Check Certificate Validation Status
-------------------------------------

.. code:: bash

   aws acm describe-certificate --certificate-arn arn:aws:acm:ap-southeast-1:987654321:certificate/88c10c4e-a0ba-41e9-bbd4-734e0191e363 | jq -r .Certificate.Status

.. code:: ini

   PENDING_VALIDATION

Wait Until Certificate is Issued
-----------------------------------

.. code:: bash

   aws acm wait certificate-validated --certificate-arn arn:aws:acm:ap-southeast-1:987654321:certificate/88c10c4e-a0ba-41e9-bbd4-734e0191e363

Delete a Certificate
----------------------

.. code:: bash

   aws acm delete-certificate --certificate-arn arn:aws:acm:ap-southeast-1:987654321:certificate/88c10c4e-a0ba-41e9-bbd4-734e0191e363
