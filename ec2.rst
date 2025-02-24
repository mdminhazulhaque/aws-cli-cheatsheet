EC2
===

List Instance ID, Type and Name
-------------------------------

.. code:: bash

   aws ec2 describe-instances | jq -r '.Reservations[].Instances[]|.InstanceId+" "+.InstanceType+" "+(.Tags[] | select(.Key == "Name").Value)'

.. code:: ini

   i-0f112d652ecf13dac  c3.xlarge  fisher.com
   i-0b3b5128445a332db  t2.nano    robinson.com
   i-0d1c1cf4e980ac593  t2.micro   nolan.com
   i-004ee6b792c3b6914  t2.nano    grimes-green.net
   i-00f11e8e33c971058  t2.nano    garrett.com

List Instances with Public IP Address and Name
----------------------------------------------

|:arrow_right:| Tip: You can directly put this into your ``/etc/hosts``

.. code:: bash

   aws ec2 describe-instances --query 'Reservations[*].Instances[?not_null(PublicIpAddress)]' | jq -r '.[][]|.PublicIpAddress+" "+(.Tags[]|select(.Key=="Name").Value)'

.. code:: ini

   223.64.72.64    fisher.com
   198.82.207.161  robinson.com
   182.139.20.233  nolan.com
   153.134.83.44   grimes-green.net
   202.32.63.121   garrett.com

List Instances with Specific Tag
--------------------------------

.. code:: bash

   aws ec2 describe-instances | jq -r '.Reservations[].Instances[] | select(.Tags[] | .Value == "my-project-name") | .InstanceId'

.. code:: ini

   i-0f112d652ecf13dac
   i-0b3b5128445a332db
   i-0d1c1cf4e980ac593

Tag Instances
-------------

.. code:: bash

   aws ec2 create-tags --resources i-0f112d652ecf13dac --tags Key=environment,Value=prod

List VPCs with CIDR IP Block
----------------------------

.. code:: bash

   aws ec2 describe-vpcs | jq -r '.Vpcs[]|.VpcId+" "+(.Tags[]|select(.Key=="Name").Value)+" "+.CidrBlock'

.. code:: ini

   vpc-0d1c1cf4e980ac593  frontend-vpc  10.0.0.0/16
   vpc-00f11e8e33c971058  backend-vpc   172.31.0.0/16

List Subnets under a VPC
------------------------

.. code:: bash

   aws ec2 describe-subnets --filter Name=vpc-id,Values=vpc-0d1c1cf4e980ac593 | jq -r '.Subnets[]|.SubnetId+" "+.CidrBlock+" "+(.Tags[]|select(.Key=="Name").Value)'

.. code:: ini

   subnet-0dae5d4daa47fe4a2  10.0.128.0/20  Public Subnet 1
   subnet-0641a25faccb01f0f  10.0.32.0/19   Private Subnet 2
   subnet-09fb8038641f1f36f  10.0.0.0/19    Private Subnet 1
   subnet-02a63c67684d8deed  10.0.144.0/20  Public Subnet 2

List Security Groups
-----------------------

.. code:: bash

   aws ec2 describe-security-groups | jq -r '.SecurityGroups[]|.GroupId+" "+.GroupName'

.. code:: ini

   sg-02a63c67684d8deed  backend-db
   sg-0dae5d4daa47fe4a2  backend-redis
   sg-0a56bff7b12264282  frontend-lb
   sg-0641a25faccb01f0f  frontend-https
   sg-09fb8038641f1f36f  internal-ssh

List Security Groups for an Instance
------------------------------------

.. code:: bash

   aws ec2 describe-instances --instance-ids i-0dae5d4daa47fe4a2 | jq -r '.Reservations[].Instances[].SecurityGroups[]|.GroupId+" "+.GroupName'

.. code:: ini

   sg-02a63c67684d8deed  backend-db
   sg-0dae5d4daa47fe4a2  backend-redis

Assign Security Groups to an Instance
-------------------------------------

|:arrow_right:| You have to provide existing Security Group IDs as well

.. code:: bash

   aws ec2 modify-instance-attribute --instance-id i-0dae5d4daa47fe4a2 --groups sg-02a63c67684d8deed sg-0dae5d4daa47fe4a2

List Security Group Rules in FromAddress/ToPort Format
------------------------------------------------------

.. code:: bash

   aws ec2 describe-security-groups --group-ids sg-02a63c67684d8deed | jq -r '.SecurityGroups[].IpPermissions[]|. as $parent|(.IpRanges[].CidrIp+" "+($parent.ToPort|tostring))'

.. code:: ini

   223.64.72.64/32    3306
   198.82.207.161/32  3306
   168.244.58.160/32  3306
   202.0.149.202/32   3306
   212.143.80.102/32  3306

Add Rule to Security Group
--------------------------

.. code:: bash

   aws ec2 authorize-security-group-ingress --group-id sg-02a63c67684d8deed --protocol tcp --port 443 --cidr 35.0.0.1/24

Remove Rule from Security Group
-------------------------------

.. code:: bash

   aws ec2 revoke-security-group-ingress --group-id sg-02a63c67684d8deed --protocol tcp --port 443 --cidr 35.0.0.1/24

Modify Rules of Security Group
------------------------------

|:arrow_right:| You have to provide All previous rules as well

.. code:: bash

   aws ec2 update-security-group-rule-descriptions-ingress --group-id sg-02a63c67684d8deed --ip-permissions 'ToPort=443,IpProtocol=tcp,IpRanges=[{CidrIp=202.171.186.133/32,Description=Home}]'

Delete Security Group
---------------------

.. code:: bash

   aws ec2 delete-security-group --group-id sg-02a63c67684d8deed

