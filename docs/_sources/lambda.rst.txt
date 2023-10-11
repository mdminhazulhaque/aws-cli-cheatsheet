Lambda
======

List Lambda Functions, Runtime and Memory
-----------------------------------------

.. code:: bash

   aws lambda list-functions | jq -r '.Functions[] | .FunctionName+" "+.Runtime+" "+(.MemorySize|tostring)'

.. code:: ini

   backend-api-function           nodejs8.10  512
   backend-signup-email-function  nodejs10.x  128
   partner-api-8XJAP1VVLYA7       python3.7   128
   marketing-promo-sqs-function   nodejs10.x  128

List Lambda Layers
------------------

.. code:: bash

   aws lambda list-layers | jq -r '.Layers[] | .LayerName'

.. code:: ini

   imagemagik-layer
   django-layer
   nodejs-extra-layer

List of Source Event for Lambda
-------------------------------

.. code:: bash

   aws lambda list-event-source-mappings | jq -r '.EventSourceMappings[] | .FunctionArn+" "+.EventSourceArn'

.. code:: ini

   arn:aws:lambda:function:backend-api-function           arn:aws:dynamodb:table/prod-user-list/stream
   arn:aws:lambda:function:backend-signup-email-function  arn:aws:dynamodb:table/prod-user-email/stream
   arn:aws:lambda:function:partner-api-8XJAP1VVLYA7       arn:aws:sqs:partner-input-msg-queue
   arn:aws:lambda:function:marketing-promo-sqs-function   arn:aws:sqs:promo-input-msg-queue

Download Lambda Code
--------------------

.. code:: bash

   aws lambda get-function --function-name DynamoToSQS | jq -r .Code.Location

.. code:: ini

   https://awslambda-ap-se-1-tasks.s3.ap-southeast-1.amazonaws.com/snapshots/987654321/backend-api-function-1fda0de7-a751-4586-bf64-5601a410c170

