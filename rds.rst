RDS
===

List DB Clusters
----------------

.. code:: bash

   aws rds describe-db-clusters | jq -r '.DBClusters[] | .DBClusterIdentifier+" "+.Endpoint'

.. code:: ini

   backend-prod   backend-prod.cluster-b6da07d35.ap-southeast-1.rds.amazonaws.com
   internal-prod  internal-dev.cluster-b6da07d35.ap-southeast-1.rds.amazonaws.com

List DB Instances
-----------------

.. code:: bash

   aws rds describe-db-instances | jq -r '.DBInstances[] | .DBInstanceIdentifier+" "+.DBInstanceClass+" "+.Endpoint.Address'

.. code:: ini

   backend-dev   db.t3.medium  backend-prod.b6da07d35.ap-southeast-1.rds.amazonaws.com
   internal-dev  db.t2.micro   internal-dev.b6da07d35.ap-southeast-1.rds.amazonaws.com

Take DB Instance Snapshot
-------------------------

.. code:: bash

   aws rds create-db-snapshot --db-snapshot-identifier backend-dev-snapshot-0001 --db-instance-identifier backend-dev
   aws rds describe-db-snapshots --db-snapshot-identifier backend-dev-snapshot-0001 --db-instance-identifier general

Take DB Cluster Snapshot
------------------------

.. code:: bash

   aws rds create-db-cluster-snapshot --db-cluster-snapshot-identifier backend-prod-snapshot-0002 --db-cluster-identifier backend-prod
   aws rds describe-db-cluster-snapshots --db-cluster-snapshot-identifier backend-prod-snapshot-0002 --db-cluster-identifier backend-prod
