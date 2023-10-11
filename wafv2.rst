WAF
===

List Web ACLs
-------------

.. code:: bash

   aws wafv2 list-web-acls --scope REGIONAL | jq -r '.WebACLs[]|.Name'

.. code:: ini

   prod-api-allow
   prod-frontend-allow
   prod-bots-deny
   prod-testing-allow

List Rules under an Web ACL
---------------------------

.. code:: bash

   aws wafv2 get-web-acl --name prod-frontend-allow --scope REGIONAL --id 5cf184c3-d7f0-44af-8c99-f3f08aec0267 | jq -r '.WebACL.Rules[]|.Name'

.. code:: ini

   prod-allow-ip
   prod-allow-build-server
   prod-allow-office-network

List Resources for an Web ACL
-----------------------------

.. code:: bash

   aws wafv2 wafv2 list-resources-for-web-acl --web-acl-arn arn:aws:wafv2:us-east-2:123456789:regional/webacl/prod-frontend-allow/5cf184c3-d7f0-44af-8c99-f3f08aec0267 | jq -r '.ResourceArns[]|.'

.. code:: ini

   arn:aws:elasticloadbalancing:us-east-2:123456789:loadbalancer/app/k8s-backend-5cf184c3/f3f08aec0267
   arn:aws:elasticloadbalancing:us-east-1:123456789:loadbalancer/app/k8s-frontend-d7f084c3/44af8aec029a

List IP Sets
------------

.. code:: bash

   aws wafv2 list-ip-sets --scope REGIONAL | jq -r '.IPSets[]|.Name'

.. code:: ini

   prod-api-ipv4-set
   prod-api-ipv6-set
   prod-customer-ipv4-set
   prod-customer-ipv6-set

List IP Addresses under an IP Set
---------------------------------

.. code:: bash

   aws wafv2 get-ip-set --scope REGIONAL --name prod-api-ipv4-set --id 7cd71356-f6df-4cef-b058-6c174eb3f23a | jq -r '.IPSet.Addresses[]|.'

.. code:: ini

   103.10.127.0/24
   104.154.0.0/15