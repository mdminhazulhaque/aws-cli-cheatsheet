OpenSearch
==========

List Domains
------------

.. code:: bash

   aws opensearch list-domain-names --output json | jq -r '.DomainNames[]|.DomainName'

.. code:: ini

   prod-orders
   prod-products
   prod-metadata