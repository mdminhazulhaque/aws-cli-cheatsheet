SNS
===

List SNS Topics
---------------

.. code:: bash

   aws sns list-topics | jq -r '.Topics[] | .TopicArn'

.. code:: ini

   arn:aws:sns:ap-southeast-1:987654321:backend-api-monitoring
   arn:aws:sns:ap-southeast-1:987654321:dynamodb-count-check
   arn:aws:sns:ap-southeast-1:987654321:partner-integration-check
   arn:aws:sns:ap-southeast-1:987654321:autoscale-notifications

List SNS Topic and related Subscriptions
----------------------------------------

.. code:: bash

   aws sns list-subscriptions | jq -r '.Subscriptions[] | .TopicArn+" "+.Protocol+" "+.Endpoint'

.. code:: ini

   arn:aws:sns:ap-southeast-1:autoscale-notifications    lambda  arn:aws:lambda:function:autoscale-function
   arn:aws:sns:ap-southeast-1:backend-api-monitoring     email   alert@mdminhazulhaque.io
   arn:aws:sns:ap-southeast-1:dynamodb-count-check       email   alert@mdminhazulhaque.io
   arn:aws:sns:ap-southeast-1:partner-integration-check  lambda  arn:aws:lambda:function:partner-function
   arn:aws:sns:ap-southeast-1:autoscale-notifications    lambda  arn:aws:lambda:function:autoscale-function

Publish to SNS Topic
--------------------

.. code:: bash

   aws sns publish --topic-arn arn:aws:sns:ap-southeast-1:987654321:backend-api-monitoring \
       --message "Panic!!!" \
       --subject "The API is down!!!"
