Amplify
=======

List of Amplify Apps and Source Repositories
--------------------------------------------

.. code:: bash

   aws amplify list-apps | jq -r '.apps[] | .name+" "+.defaultDomain+" "+.repository'

.. code:: ini

   fe-vn  d9d5bb1e3c281f.amplifyapp.com  https://bitbucket.org/aws/frontend-vn
   fe-hk  db64e7e9b3cc22.amplifyapp.com  https://bitbucket.org/aws/frontend-hk
   fe-sg  d5e3221cf8b921.amplifyapp.com  https://bitbucket.org/aws/frontend-sg
