ELB
===

Create an ALB
-------------

.. code:: bash

   aws elbv2 create-load-balancer --name lb-my-app --subnets subnet-006283cc641883340 subnet-0f824d8944b903079 subnet-0b6976fef09a3ed00 | jq -r .LoadBalancers[0].LoadBalancerArn

.. code:: ini

   arn:aws:elasticloadbalancing:ap-southeast-1:987654321:loadbalancer/app/lb-my-app/a1ecf6e769562994

Create a Target Group
---------------------

.. code:: bash

   aws elbv2 create-target-group --name tg-my-app --protocol HTTP --port 8000 --target-type instance --vpc-id vpc-0ae29454e100df108 | jq -r .TargetGroups[0].TargetGroupArn

.. code:: ini

   arn:aws:elasticloadbalancing:ap-southeast-1:987654321:targetgroup/tg-my-app/a7d3e159ca722a4d

Register EC2 to a Target Group
------------------------------

.. code:: bash

   aws elbv2 register-targets --target-group-arn arn:aws:elasticloadbalancing:ap-southeast-1:987654321:targetgroup/tg-my-app/a7d3e159ca722a4d --targets Id=i-00a8e8746f02bdf29

Create Listener and forward to a Target Group
---------------------------------------------

.. code:: bash

   aws elbv2 create-listener --load-balancer-arn arn:aws:elasticloadbalancing:ap-southeast-1:987654321:loadbalancer/app/lb-my-app/a1ecf6e769562994 --port 80 --protocol HTTP --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:ap-southeast-1:987654321:targetgroup/tg-my-app/a7d3e159ca722a4d | jq -r .Listeners[0].ListenerArn

.. code:: ini

   arn:aws:elasticloadbalancing:ap-southeast-1:987654321:listener/app/lb-my-app/a1ecf6e769562994/d77331a1038731de

Create HTTPS Listener with Host Based Rule
------------------------------------------

.. code:: bash

   aws elbv2 create-listener --load-balancer-arn arn:aws:elasticloadbalancing:ap-southeast-1:987654321:loadbalancer/app/lb-my-app/a1ecf6e769562994 --port 443 --protocol HTTPS --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:ap-southeast-1:987654321:targetgroup/tg-my-app/a7d3e159ca722a4d --certificates CertificateArn=arn:aws:acm:ap-southeast-1:987654321:certificate/88c10c4e-a0ba-41e9-bbd4-734e0191e363

.. code:: bash

   aws elbv2 create-rule --listener-arn arn:aws:elasticloadbalancing:ap-southeast-1:987654321:listener/app/lb-my-app/a1ecf6e769562994/d77331a1038731de --priority 1 --conditions Field=host-header,HostHeaderConfig={Values=app.example.com} --actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:ap-southeast-1:987654321:targetgroup/tg-my-app/a7d3e159ca722a4d

List LoadBalancer DNS Names
------------------------------

.. code:: bash

   aws elbv2 describe-load-balancers --query 'LoadBalancers[*].DNSName'  | jq -r 'to_entries[] | .value'

.. code:: ini

   frontend-lb-1220186848339.ap-southeast-1.elb.amazonaws.com
   backend-lb-6208709163457.ap-southeast-1.elb.amazonaws.com

List LoadBalancer ARNs
-------------------------

.. code:: bash

   aws elbv2 describe-load-balancers | jq -r '.LoadBalancers[] | .LoadBalancerArn'
   arn:aws:elasticloadbalancing:ap-southeast-1:987654321:loadbalancer/app/frontend-lb/1220186848339
   arn:aws:elasticloadbalancing:ap-southeast-1:987654321:loadbalancer/app/backend-lb/6208709163457

List Target Group ARNs
-------------------------

.. code:: bash

   aws elbv2 describe-target-groups | jq -r '.TargetGroups[] | .TargetGroupArn'

.. code:: ini

   arn:aws:elasticloadbalancing:ap-southeast-1:987654321:targetgroup/frontend/b6da07d35
   arn:aws:elasticloadbalancing:ap-southeast-1:987654321:targetgroup/backend/97ad3b13c

Find Instances for a Target Group
---------------------------------

.. code:: bash

   aws elbv2 describe-target-health --target-group-arn arn:aws:elasticloadbalancing:ap-southeast-1:987654321:targetgroup/wordpress-ph/88f517d6b5326a26 | jq -r '.TargetHealthDescriptions[] | .Target.Id'

.. code:: ini

   i-0b3b5128445a332db
   i-0d1c1cf4e980ac593
   i-00f11e8e33c971058

