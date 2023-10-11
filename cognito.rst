Cognito
=======

List User Pools and Names
-------------------------

.. code:: bash

   aws cognito-idp list-user-pools --max-results 60 | jq -r '.UserPools[] | .Id+" "+.Name'

.. code:: ini

   ap-southeast-1_b6da07d35 prod-users
   ap-southeast-1_b6da07d34 dev-users

List Phone and Email of All Users
---------------------------------

.. code:: bash

   aws cognito-idp list-users --user-pool-id ap-southeast-1_b6da07d35 | jq -r '.Users[].Attributes | from_entries | .sub + " " + .phone_number + " " + .email'

.. code:: ini

   585fb96e-525c-4f9b-9d41-865d2dffde9b +601122334455 admin@mdminhazulhaque.io
   71f2778c-8e21-4775-94dc-e363c77d1ae1 +601122334455 foo@bar.com
   8fc1882e-e661-49db-88e6-45d370bc352a +601122334455 cli@aws.com
