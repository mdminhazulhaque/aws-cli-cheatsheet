SES
===

Send Mail
---------

.. code:: bash

   aws ses send-email \
    --to user@example.com \
    --subject Howdy \
    --html '<h1>Hello, Mate!</h1>' \
    --from noreply@example.com

List Identities
---------------

.. code:: bash

   aws ses list-identities | jq -r '.Identities[]'

.. code:: ini

   mdminhazulhaque.io
   test.com
   example.com
   google.com

Get DKIM Verification Status
----------------------------

.. code:: bash

   aws ses get-identity-dkim-attributes --identities example.com

.. code:: ini

   ...
   "DkimEnabled": true,
   ...

Tag identity
------------

.. code:: bash

   aws sesv2 tag-resource --resource-arn arn:aws:ses:us-west-2:987654321:identity/example.com \
    --tags Key=environment,Value=prod Key=team/backend
