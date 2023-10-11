ECR
===

List Repositories
-----------------

.. code:: bash

   aws ecr describe-repositories | jq -r '.repositories[] | .repositoryName'

.. code:: ini

   prod-web-api
   prod-frontend

List Images from a Repository
-----------------------------

.. code:: bash

   aws ecr list-images --repository prod-web-api | jq -r '.imageIds[] | .imageTag'

.. code:: ini

   prod-api:v101
   prod-api:v102
   prod-api:v103
   prod-api:v104
   prod-api:v105