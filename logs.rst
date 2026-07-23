CloudWatch Logs
===============

List Log Groups
---------------

.. code:: bash

   aws logs describe-log-groups | jq -r '.logGroups[].logGroupName'

.. code:: ini

   /aws/lambda/user-signup
   /aws/lambda/order-processor
   /aws/events/billing-events

Filter Log Groups by Prefix
---------------------------

.. code:: bash

   aws logs describe-log-groups --log-group-name-prefix "/aws/lambda/" | jq -r '.logGroups[].logGroupName'

List Log Streams (Newest First)
-------------------------------

.. code:: bash

   aws logs describe-log-streams \
       --log-group-name "/aws/lambda/user-signup" \
       --order-by LastEventTime \
       --descending \
       --max-items 5 \
       | jq -r '.logStreams[] | .logStreamName + " " + (.lastEventTimestamp|tostring)'

.. code:: ini

   2026/04/13/[$LATEST]41b02a0430a74f8d9717f7921361e046 1744531200000
   2026/04/12/[$LATEST]c049d71f34cd45a081d544840e6bed3b 1744444800000

Get Latest Log Stream Name
--------------------------

.. code:: bash

   aws logs describe-log-streams \
       --log-group-name "/aws/lambda/user-signup" \
       --order-by LastEventTime \
       --descending \
       --max-items 1 \
       --query 'logStreams[0].logStreamName' \
       --output text

Tail Logs in Real Time
----------------------

.. code:: bash

   aws logs tail /aws/lambda/user-signup --follow

Tail Logs for Last N Minutes
----------------------------

.. code:: bash

   aws logs tail /aws/lambda/user-signup --since 10m
   aws logs tail /aws/lambda/user-signup --since 1h --follow

Get Events from a Log Stream
----------------------------

.. code:: bash

   aws logs get-log-events \
       --log-group-name "/aws/lambda/user-signup" \
       --log-stream-name "2026/04/13/[\$LATEST]41b02a0430a74f8d9717f7921361e046" \
       --start-from-head \
       --query 'events[*].message' \
       --output text

Filter Log Events by Pattern
----------------------------

.. code:: bash

   aws logs filter-log-events \
       --log-group-name "/aws/lambda/user-signup" \
       --filter-pattern "ERROR" \
       --query 'events[*].message' \
       --output text

Filter Log Events in a Time Range
---------------------------------

|:bulb:| CloudWatch Logs expects ``--start-time`` and ``--end-time`` in
epoch milliseconds. Compute them on the fly:

.. code:: bash

   # last 10 minutes (macOS and Linux)
   aws logs filter-log-events \
       --log-group-name "/aws/lambda/user-signup" \
       --filter-pattern "ERROR" \
       --start-time $(python3 -c "import time; print(int((time.time() - 600) * 1000))") \
       --query 'events[*].message' \
       --output text

.. code:: bash

   # specific ISO timestamp window
   aws logs filter-log-events \
       --log-group-name "/aws/lambda/user-signup" \
       --start-time $(python3 -c "from datetime import datetime; print(int(datetime.fromisoformat('2026-04-13T10:00:00').timestamp() * 1000))") \
       --end-time   $(python3 -c "from datetime import datetime; print(int(datetime.fromisoformat('2026-04-13T11:00:00').timestamp() * 1000))") \
       --query 'events[*].[timestamp,message]' \
       --output table

Start a CloudWatch Logs Insights Query
--------------------------------------

|:bulb:| ``start-query`` uses epoch **seconds** (not ms).

.. code:: bash

   aws logs start-query \
       --log-group-name "aws-cloudtrail-logs-987654321-c59299d1" \
       --start-time $(date -u -v-60M +%s) \
       --end-time   $(date -u +%s) \
       --query-string 'fields @timestamp, eventName, errorCode, errorMessage, userIdentity.arn, sourceIPAddress
                       | filter (errorCode like "UnauthorizedOperation" or errorCode like "AccessDenied")
                       | sort @timestamp desc
                       | limit 50'

.. code:: json

   {
       "queryId": "32e95c24-c554-4a7f-a1fb-d95ae91e6556"
   }

Fetch Insights Query Results
----------------------------

.. code:: bash

   aws logs get-query-results --query-id "32e95c24-c554-4a7f-a1fb-d95ae91e6556"

.. code:: bash

   # just the status
   aws logs get-query-results --query-id "32e95c24-c554-4a7f-a1fb-d95ae91e6556" \
       --query 'status' --output text

.. code:: bash

   # flatten field/value pairs
   aws logs get-query-results --query-id "32e95c24-c554-4a7f-a1fb-d95ae91e6556" \
       --query 'results[*][*].[field,value]' --output text

Delete a Log Group
------------------

.. code:: bash

   aws logs delete-log-group --log-group-name "/aws/lambda/user-signup"

Set Log Group Retention
-----------------------

.. code:: bash

   aws logs put-retention-policy \
       --log-group-name "/aws/lambda/user-signup" \
       --retention-in-days 14
