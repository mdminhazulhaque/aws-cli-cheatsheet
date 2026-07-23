Lightsail
=========

List Instances
--------------

.. code:: bash

   aws lightsail get-instances | jq -r '.instances[] | .name + " " + .bundleId + " " + .state.name'

.. code:: ini

   outline-server   small_2_0   running
   wp-demo          medium_2_0  running

Get a Single Instance
---------------------

.. code:: bash

   aws lightsail get-instance --instance-name wp-demo

Create an Instance
------------------

.. code:: bash

   aws lightsail create-instances \
       --instance-names wp-demo \
       --availability-zone ap-southeast-1a \
       --blueprint-id ubuntu_22_04 \
       --bundle-id nano_3_0 \
       --key-pair-name minhaz-tech

|:bulb:| Discover valid values with ``aws lightsail get-blueprints`` and ``aws lightsail get-bundles``.

Stop an Instance
----------------

.. code:: bash

   aws lightsail stop-instance --instance-name wp-demo

Start an Instance
-----------------

.. code:: bash

   aws lightsail start-instance --instance-name wp-demo

Reboot an Instance
------------------

.. code:: bash

   aws lightsail reboot-instance --instance-name wp-demo

Delete an Instance
------------------

.. code:: bash

   aws lightsail delete-instance --instance-name wp-demo

List Key Pairs
--------------

.. code:: bash

   aws lightsail get-key-pairs | jq -r '.keyPairs[] | .name + " " + .fingerprint'

.. code:: ini

   minhaz-tech    2d:78:a6:7b:27:ca:44:bd:b5:6c:1e:4d:48:de:03:90

Create a Key Pair
-----------------

.. code:: bash

   aws lightsail create-key-pair --key-pair-name minhaz-tech \
       | jq -r '.privateKeyBase64' > minhaz-tech.pem
   chmod 600 minhaz-tech.pem

Delete a Key Pair
-----------------

.. code:: bash

   aws lightsail delete-key-pair --key-pair-name minhaz-tech

List Instance Snapshots
-----------------------

.. code:: bash

   aws lightsail get-instance-snapshots \
       | jq -r '.instanceSnapshots[] | .name + " " + .fromInstanceName + " " + .state'

.. code:: ini

   wp-demo-2026-04-13   wp-demo   available
   wp-demo-2026-03-01   wp-demo   available

Get a Single Instance Snapshot
------------------------------

.. code:: bash

   aws lightsail get-instance-snapshot --instance-snapshot-name wp-demo-2026-04-13

Create an Instance Snapshot
---------------------------

.. code:: bash

   aws lightsail create-instance-snapshot \
       --instance-name wp-demo \
       --instance-snapshot-name wp-demo-2026-04-13

Delete an Instance Snapshot
---------------------------

.. code:: bash

   aws lightsail delete-instance-snapshot \
       --instance-snapshot-name wp-demo-2026-04-13

Restore an Instance from a Snapshot
-----------------------------------

.. code:: bash

   aws lightsail create-instances-from-snapshot \
       --instance-names wp-demo-restored \
       --availability-zone ap-southeast-1a \
       --bundle-id nano_3_0 \
       --instance-snapshot-name wp-demo-2026-04-13
