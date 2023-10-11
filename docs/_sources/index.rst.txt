AWS CLI Cheatsheet
==================

Supercharge your daily acitivities related to AWS cloud using the combination of AWS CLI and JQ.

Prerequisites
-------------

-  `aws-cli <https://aws.amazon.com/cli/>`__
-  `jq <https://stedolan.github.io/jq/>`__

|:warning:| Disclaimer: All Resource, Account, ARN, Hostname etc are
generated using `Faker <https://faker.readthedocs.io/en/master>`__. They
should not match any real user data.

|:arrow_right:| If you have multiple AWS Accounts, you can use bash aliases
like the following. So you no longer need to pass ``--profile`` to
``aws`` tool repeatedly.

.. code:: bash

   alias aws-prod="aws --profile work-prod"
   alias aws-dev="aws --profile work-dev"
   alias aws-self="aws --profile personal"
   alias aws="aws --profile work-dev"

|:arrow_right:| To format ``aws`` command output into pretty tables, you can pipe the output to ``column -t``.

::

   # aws ec2 describe-instances | jq ...
   i-0f112d652ecf13dac c3.x2large fisher.com
   i-0b3b5128445a332db t2.nano robinson.com

   # aws ec2 describe-instances | jq ... | column -t
   i-0f112d652ecf13dac  c3.x2large  fisher.com
   i-0b3b5128445a332db  t2.nano     robinson.com

.. toctree::
   :caption: AWS Services
   :maxdepth: 100
   :hidden:

   acm
   amplify
   apigw
   cloudfront
   cloudwatch
   cognito
   dynamodb
   ec2
   ecr
   efs
   eks
   elasticache
   elb
   iam
   lambda
   opensearch
   rds
   route53
   s3
   sns
   sqs
   wafv2
