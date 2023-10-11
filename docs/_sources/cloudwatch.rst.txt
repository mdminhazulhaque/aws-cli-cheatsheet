Cloudwatch
==========

List Alarms and Status
----------------------

.. code:: bash

   aws cloudwatch describe-alarms | jq -r '.MetricAlarms[] | .AlarmName+" "+.Namespace+" "+.StateValue'

.. code:: ini

   backend-autoscale  AWS/EC2             OK
   backend-lb         AWS/ApplicationELB  OK
   partner-hk         AWS/ECS             ALARM
   partner-vn         AWS/ECS             ALARM
   partner-sg         AWS/ECS             ALARM
   userdata-read      AWS/DynamoDB        OK
   userdata-write     AWS/DynamoDB        OK

Create Alarm on High CPUUtilization
-----------------------------------

.. code:: bash

   aws cloudwatch put-metric-alarm --alarm-name high-cpu-usage --alarm-description "Alarm when CPU exceeds 70 percent" --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period 300 --threshold 70 --comparison-operator GreaterThanThreshold  --dimensions "Name=InstanceId,Value=i-123456789" --evaluation-periods 2 --alarm-actions arn:aws:sns:ap-southeast-1:987654321:System-Alerts --unit Percent

Create Alarm on StatusCheckFailed_Instance
------------------------------------------

.. code:: bash

   aws cloudwatch put-metric-alarm --alarm-name EC2-StatusCheckFailed-AppServer --alarm-description "EC2 StatusCheckFailed for AppServer" --metric-name StatusCheckFailed_Instance --namespace AWS/EC2 --statistic Average --period 60 --threshold 0 --comparison-operator GreaterThanThreshold  --dimensions "Name=InstanceId,Value=i-123456789" --evaluation-periods 3 --alarm-actions arn:aws:sns:ap-southeast-1:987654321:System-Alerts --unit Count
