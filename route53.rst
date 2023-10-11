Route53
=======

List Domains
------------

.. code:: bash

   aws route53 list-hosted-zones | jq -r '.HostedZones[]|.Id+" "+.Name'

.. code:: ini

   /hostedzone/ZEB1PAH4U mysite.com.
   /hostedzone/ZQUOHGH3G yoursite.com.
   /hostedzone/ZEADEA0CO staywith.us.

List Records for a Domain (Zone)
--------------------------------

.. code:: bash

   aws route53 list-resource-record-sets --hosted-zone-id /hostedzone/ZEB1PAH4U | jq -r '.ResourceRecordSets[]| if (.AliasTarget!=null) then .Type+" "+.Name+" "+.AliasTarget.DNSName else .Type+" "+.Name+" "+.ResourceRecords[].Value end'

.. code:: ini

   A      mysite.com.              dualstack.mysite-lb-967522168.ap-southeast-1.elb.amazonaws.com.
   A      mysite.com.              11.22.33.44
   TXT    _amazonses.mysite.com.   6c6d761371f0480bbe60de0df275b550
   A      test.mysite.com.         55.66.77.88
   CNAME  www.mysite.com.          mysite.com
