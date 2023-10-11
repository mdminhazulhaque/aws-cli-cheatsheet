EFS
===

List of Filesystems
-------------------

.. code:: bash

   aws efs describe-file-systems | jq -r '.FileSystems[] | .FileSystemId + " " + .Name'

.. code:: ini

   fs-1894c355 production-images
   fs-964dc315 production-docs
   fs-257dc779 production-export
