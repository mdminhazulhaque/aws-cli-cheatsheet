IAM
===

List UserId and UserName
------------------------

.. code:: bash

   aws iam list-users | jq -r '.Users[]|.UserId+" "+.UserName'

.. code:: ini

   AIDAZBWIOJIQFOLNBXXCVSUQ kaiser
   AIDAZCTWYVXYOKSHVWXPYPLR thornton
   AIDAZUYALCGFQJENBCZFJTVX maldonado
   AIDAZKQAFIGQJWOKKSKRBLGE key
   AIDAZXUDGQVQCEWBFGIJOWWY nelson

Get a Single User
-----------------

.. code:: bash

   aws iam get-user --user-name kaiser

Add a User
----------

.. code:: bash

   aws iam create-user --user-name audit-temp

Delete a User
-------------

.. code:: bash

   aws iam delete-user --user-name audit-temp

List Access Keys for a User
---------------------------

.. code:: bash

   aws iam list-access-keys --user-name audit-temp | jq -r .AccessKeyMetadata[].AccessKeyId

.. code:: ini

   AKIABWIOJIQFOLNBXXCVSUQ
   AKIACTWYVXYOKSHVWXPYPLR

Delete Access Key for a User
----------------------------

.. code:: bash

   aws iam delete-access-key --user-name audit-temp --access-key-id AKIABWIOJIQFOLNBXXCVSUQ

Activate/Deactivate Access Key for a User
-----------------------------------------

.. code:: bash

   aws iam update-access-key --status Inactive --user-name audit-temp --access-key-id AKIABWIOJIQFOLNBXXCVSUQ
   aws iam update-access-key --status Active   --user-name audit-temp --access-key-id AKIABWIOJIQFOLNBXXCVSUQ

Generate New Access Key for a User
----------------------------------

.. code:: bash

   aws iam create-access-key --user-name audit-temp | jq -r '.AccessKey | .AccessKeyId+" "+.SecretAccessKey'

.. code:: ini

   AKIABWIOJIQFOLNBXXCVSUQ p9ge02ebLX9jobdQKmfikRqCiEw3HBylwHyXq0z

Change Console Password for a User
----------------------------------

.. code:: bash

   aws iam update-login-profile --user-name bob-marketing --password '5tr0nGp@$$w0rD'

List Groups
-----------

.. code:: bash

   aws iam list-groups | jq -r .Groups[].GroupName

.. code:: ini

   developers
   administrators
   testers
   marketing-ro

Add/Delete Groups
-----------------

.. code:: bash

   aws iam create-group --group-name business-ro
   aws iam delete-group --group-name business-ro

List Policies and ARNs
----------------------

.. code:: bash

   aws iam list-policies               | jq -r '.Policies[]|.PolicyName+" "+.Arn'
   aws iam list-policies --scope AWS   | jq -r '.Policies[]|.PolicyName+" "+.Arn'
   aws iam list-policies --scope Local | jq -r '.Policies[]|.PolicyName+" "+.Arn'

List User/Group/Roles for a Policy
----------------------------------

.. code:: bash

   aws iam list-entities-for-policy --policy-arn arn:aws:iam::987654321:policy/Marketing-ReadOnly

List Policies for a Group
-------------------------

.. code:: bash

   aws iam list-attached-group-policies --group-name business-ro

Add Policy to a Group
---------------------

.. code:: bash

   aws iam attach-group-policy --group-name business-ro --policy-arn arn:aws:iam::aws:policy/DynamoDBReadOnlyAccess

Add User to a Group
-------------------

.. code:: bash

   aws iam add-user-to-group --group-name business-ro --user-name marketing-michael

Remove User from a Group
------------------------

.. code:: bash

   aws iam remove-user-from-group --group-name business-ro --user-name marketing-alice

List Users in a Group
---------------------

.. code:: bash

   aws iam get-group --group-name business-ro

List Groups for a User
----------------------

.. code:: bash

   aws iam list-groups-for-user --user-name qa-bob

Attach/Detach Policy to a Group
-------------------------------

.. code:: bash

   aws iam detach-group-policy --group-name business-ro --policy-arn arn:aws:iam::aws:policy/DynamoDBFullAccess
   aws iam attach-group-policy --group-name business-ro --policy-arn arn:aws:iam::aws:policy/DynamoDBFullAccess
