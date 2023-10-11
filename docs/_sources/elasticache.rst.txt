ElastiCache
===========

List Machine Type and Name
--------------------------

.. code:: bash

   aws elasticache describe-cache-clusters | jq -r '.CacheClusters[] | .CacheNodeType+" "+.CacheClusterId'

.. code:: ini

   cache.t2.micro  backend-login-hk
   cache.m5.large  backend-login-vn
   cache.t3.small  backend-login-sg

List Replication Groups
-----------------------

.. code:: bash

   aws elasticache describe-replication-groups | jq -r '.ReplicationGroups[] | .ReplicationGroupId+" "+.NodeGroups[].PrimaryEndpoint.Address'

.. code:: ini

   backend-login-hk backend-login-hk.6da35.ng.0001.apse1.cache.amazonaws.com
   backend-login-vn backend-login-vn.6da35.ng.0001.apse1.cache.amazonaws.com
   backend-login-sg backend-login-sg.6da35.ng.0001.apse1.cache.amazonaws.com

List Snapshots
--------------

.. code:: bash

   aws elasticache describe-snapshots | jq -r '.Snapshots[] | .SnapshotName'

.. code:: ini

   automatic.backend-login-hk-2020-02-27-00-27
   automatic.backend-login-vn-2020-02-27-00-27
   automatic.backend-login-sg-2020-02-27-00-27

Create a Snapshot
-----------------

.. code:: bash

   aws elasticache create-snapshot --snapshot-name backend-login-hk-snap-0001 --replication-group-id backend-login-hk --cache-cluster-id backend-login-hk

Delete a Snapshot
-----------------

.. code:: bash

   aws elasticache delete-snapshot --snapshot-name backend-login-hk-snap-0001

Scale Up/Down a Replica
-----------------------

.. code:: bash

   aws elasticache increase-replica-count --replication-group-id backend-login-hk --apply-immediately
   aws elasticache decrease-replica-count --replication-group-id backend-login-hk --apply-immediately

