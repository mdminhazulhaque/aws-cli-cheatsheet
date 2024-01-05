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

List NodeGroups for Cluster
---------------------------

.. code:: bash

   aws eks list-nodegroups --cluster-name devtest

.. code:: ini

   nodegroups:
   - dev-nodes
   - test-nodes
   - argocd-nodes

Modify NodeGroups for Cluster
-----------------------------

.. code:: bash

   aws eks update-nodegroup-config --cluster-name devtest --nodegroup-name dev-nodes --scaling-config minSize=1,desiredSize=5,maxSize=10
