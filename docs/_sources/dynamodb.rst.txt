DynamoDB
========

List Tables
-----------

.. code:: bash

   aws dynamodb list-tables | jq -r .TableNames[]

.. code:: ini

   userdata_hk
   userdata_vn
   userdata_sg
   providers
   events

Get All Items from a Table
--------------------------

|:warning:| This command will stream ALL items untill SIGINT is sent

.. code:: bash

   aws dynamodb scan --table-name events 

Get Item Count from a Table
---------------------------

.. code:: bash

   aws dynamodb scan --table-name events --select COUNT | jq .ScannedCount

.. code:: ini

   726119

Get Item using Key
------------------

.. code:: bash

   aws dynamodb get-item --table-name events --key '{"email": {"S": "admin@mdminhazulhaque.io"}}'

.. code:: json

   {
       "Item": {
           "email": {
               "S": "admin@mdminhazulhaque.io"
           },
           "created_at": {
               "N": "1554780667296"
           },
           "event_type": {
               "S": "DISPATCHED"
           }
       }
   }

Get Specific Fields from an Item
--------------------------------

.. code:: bash

   aws dynamodb get-item --table-name events --key '{"email": {"S": "admin@mdminhazulhaque.io"}}' --attributes-to-get event_type

.. code:: json

   {
       "Item": {
           "event_type": {
               "S": "DISPATCHED"
           }
       }
   }

Delete Item using Key
---------------------

.. code:: bash

   aws dynamodb delete-item --table-name events --key '{"email": {"S": "admin@mdminhazulhaque.io"}}'