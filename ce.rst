Cost Explorer
=============

Get Cost by Month
-----------------

.. code:: bash

   aws ce get-cost-and-usage --granularity MONTHLY --metrics BlendedCost \
      --time-period Start=2023-10-01,End=2023-12-31 | \
      jq '.ResultsByTime[]|.TimePeriod.Start+" "+.Total.BlendedCost.Amount'

.. code:: ini

   2023-10-01 1000.000000
   2023-11-01 2000.000000
   2023-12-01 3000.000000