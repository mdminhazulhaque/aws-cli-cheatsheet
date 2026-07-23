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

Create a Repository
--------------------

.. code:: bash

   aws ecr create-repository --repository-name prod-web-api | jq -r '.repository.repositoryUri'

.. code:: ini

   987654321.dkr.ecr.ap-southeast-1.amazonaws.com/prod-web-api

Delete a Repository
--------------------

.. code:: bash

   aws ecr delete-repository --repository-name prod-web-api --force

Login to ECR with Docker
-------------------------

.. code:: bash

   aws ecr get-login-password | docker login --username AWS --password-stdin 987654321.dkr.ecr.ap-southeast-1.amazonaws.com