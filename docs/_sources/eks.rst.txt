EKS
===

List Clusters
-------------

.. code:: bash

   aws eks list-clusters | jq -r .clusters[]

.. code:: ini

   devtest
   mobileapi-prod
   usermanagement-prod

Generate KUBECONFIG for Cluster
-------------------------------

.. code:: bash

   aws eks update-kubeconfig --name devtest

.. code:: ini

   Updated context arn:aws:eks:ap-southeast-1:987654321:cluster/devtest in /home/mdminhazulhaque/.kube/config
