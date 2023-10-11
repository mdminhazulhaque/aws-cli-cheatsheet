CloudFront
==========

List Distributions and Origins
------------------------------

.. code:: bash

   aws cloudfront list-distributions | jq -r '.DistributionList.Items[] | .DomainName+" "+.Origins.Items[0].DomainName'

.. code:: ini

   d9d5bb1e3c281f.cloudfront.net  frontend-prod-hk.s3.amazonaws.com
   d12b09e8a0a996.cloudfront.net  frontend-prod-vn.s3.amazonaws.com
   db64e7e9b3cc22.cloudfront.net  frontend-prod-sg.s3.amazonaws.com
   d5e3221cf8b921.cloudfront.net  cdn.mdminhazulhaque.io

Create Cache Invalidation
-------------------------

.. code:: bash

   aws cloudfront create-invalidation --distribution-id D12B09E8A0A996  --path '/blog/*' '/blog/assets/*' | jq -r '.Invalidation.Id'

.. code:: ini

   IALJ5AL93ZD79

Check Cache Invalidation Status
-------------------------------

.. code:: bash

   aws cloudfront get-invalidation --distribution-id D12B09E8A0A996 --id IALJ5AL93ZD79 | jq -r '.Invalidation.Status'

.. code:: ini

   Completed
