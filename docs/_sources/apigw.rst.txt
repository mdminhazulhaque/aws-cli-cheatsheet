API Gateway
===========

List of API Gateway IDs and Names
---------------------------------

.. code:: bash

   aws apigateway get-rest-apis | jq -r '.items[] | .id+" "+.name'

.. code:: ini

   5e3221cf8  backend-api
   69ef7d4c8  frontend-api
   bb1e3c281  partner-api
   f99796943  internal-crm-api
   ee86b4cde  import-data-api

List of API Gateway Keys
------------------------

.. code:: bash

   aws apigateway get-api-keys | jq -r '.items[] | .id+" "+.name'

.. code:: ini

   ee86b4cde   backend-api-key
   69ef7d4c8   partner-api-key

List API Gateway Domain Names
-----------------------------

.. code:: bash

   aws apigateway get-domain-names | jq -r '.items[] | .domainName+" "+.regionalDomainName'

.. code:: ini

   backend-api.mdminhazulhaque.io   d-ee86b4cde.execute-api.ap-southeast-1.amazonaws.com
   frontend-api.mdminhazulhaque.io  d-bb1e3c281.execute-api.ap-southeast-1.amazonaws.com

List of Resources for Specific API Gateway
------------------------------------------

.. code:: bash

   aws apigateway get-resources --rest-api-id ee86b4cde  | jq -r '.items[] | .id+" "+.path'

.. code:: ini

   8c2d1097e  /v1/{proxy+}
   bb4aabda1  /v2/{proxy+}
   e44504cde  /health
   69ef7d4c8  /

Find Function for Specific API Gateway Resource
-----------------------------------------------

.. code:: bash

   aws apigateway get-integration --rest-api-id ee86b4cde --resource-id 69ef7d4c8 --http-method GET | jq -r '.uri'

.. code:: ini

   arn:aws:lambda:ap-southeast-1:987654321:function:backend-api-function-5d4daa47fe4a2:live/invocations