SQS
===

List Queues
-----------

.. code:: bash

   aws sqs list-queues | jq -r '.QueueUrls[]'

.. code:: ini

   https://ap-southeast-1.queue.amazonaws.com/987654321/public-events.fifo
   https://ap-southeast-1.queue.amazonaws.com/987654321/user-signup

Create a Queue
--------------

.. code:: bash

   aws sqs create-queue --queue-name public-events.fifo | jq -r .QueueUrl

.. code:: ini

   https://ap-southeast-1.queue.amazonaws.com/987654321/public-events.fifo

Count Messages in a Queue
-------------------------

.. code:: bash

   aws sqs get-queue-attributes --queue-url https://ap-southeast-1.queue.amazonaws.com/987654321/public-events.fifo | jq -r '.Attributes | .QueueArn + " " + .ApproximateNumberOfMessages'
 
.. code:: ini

   arn:aws:sqs:ap-southeast-1:987654321:events.fifo 42
   arn:aws:sqs:ap-southeast-1:987654321:uploads     1036

Send Message to a Queue
-----------------------

.. code:: bash

   aws sqs send-message --queue-url https://ap-southeast-1.queue.amazonaws.com/987654321/public-events.fifo --message-body Hello
 
.. code:: json

   {
       "MD5OfMessageBody": "37b51d194a7513e45b56f6524f2d51f2",
       "MessageId": "4226398e-bab0-4bee-bf5a-8e7ae18c855a"
   }

Receive Message from a Queue
----------------------------

.. code:: bash

   aws sqs receive-message --queue-url https://ap-southeast-1.queue.amazonaws.com/987654321/public-events.fifo | jq -r '.Messages[] | .Body'

.. code:: ini

   Hello I am a Message

Delete a Message from a Queue
-----------------------------

.. code:: bash

   aws sqs delete-message --queue-url https://ap-southeast-1.queue.amazonaws.com/987654321/public-events.fifo --receipt-handle "AQEBpqKLxNb8rIOn9ykSeCkKebNzn0BrEJ3Cg1RS6MwID2t1oYHCnMP06GnuVZGzt7kpWXZ5ieLQ=="

Purge a Queue
-------------

.. code:: bash

   aws sqs purge-queue --queue-url https://ap-southeast-1.queue.amazonaws.com/987654321/public-events.fifo

Delete a Queue
--------------

.. code:: bash

   aws sqs delete-queue --queue-url https://ap-southeast-1.queue.amazonaws.com/987654321/public-events.fifo

Query Message Count in a Queue
------------------------------

.. code:: bash

   aws sqs get-queue-attributes --attribute-names ApproximateNumberOfMessages --queue-url https://ap-southeast-1.queue.amazonaws.com/987654321/public-events.fifo