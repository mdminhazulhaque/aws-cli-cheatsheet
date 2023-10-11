ACM
===

List Certificate ARNs and DomainName
------------------------------------

.. code:: bash

   aws acm list-certificates | jq -r '.CertificateSummaryList[] | .CertificateArn+" "+.DomainName'

.. code:: ini

   arn:aws:acm:ap-southeast-1:987654321:certificate/88c10c4e-a0ba-41e9-bbd4-734e0191e363 *.example.com
