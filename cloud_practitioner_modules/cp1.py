"""multi_option_from_correct_incorrect
make_items_question_from_correct_incorrect
make_items_question_from_pairs
posneg_pairs
new_pairs
multi_option_pairs
order_from_pairs
code_block_question
"""
from random import choice

questions = {
    'AWS_services_and_tools': {
        'question_with_0':'Which isPOSNEG a description of PLACEHOLDER?',
        'question_with_1':'Which AWS service is described by the following: PLACEHOLDER',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            (['AWS CLI', 'AWS Command Line Interface'], ['used to automate actions for AWS services and applications through scripts']),
            (['Amazon QLDB', 'Amazon Quantum Ledger Database'],['used to review a complete history of all the changes that have been made to your application data']),
            ('Amazon Redshift', ['a data warehousing service that you can use for big data analytics','offers the ability to collect data from many sources and help you to understand relationships and trends across your data']),
            ('Amazon SQS',['message queuing service','used to send, store, and receive messages between software components at any volume size, without losing messages or requiring other services to be available']),
            ('AWS Snowball',['a device that enables you to transfer large amounts of data into and out of AWS']),
            ('Amazon ElastiCache',['a service that adds caching layers on top of your databases to help improve the read times of common requests']),
            ('Amazon Route 53',['gives developers and businesses a reliable way to route end users to internet applications that are hosted in AWS','transfer DNS records for existing domain names that are currently managed by other domain registrars or register new domain names directly in Amazon Route 53']),
            ('AWS Snowmobile',['used for transferring up to 100 PB of data to AWS','a 45-foot long shipping container that is pulled by a semi-trailer truck']),
            ('Amazon Neptune',['a graph database service','build and run applications that work with highly connected datasets, such as recommendation engines, fraud detection, and knowledge graphs']),
            ('Amazon CloudFront',['content delivery service']),
            ('AWS DeepRacer',['an autonomous 1/18 scale race car that you can use to test reinforcement learning models']),
            ('AWS QuickSight',[f"understand data by {choice(['asking questions in natural language','exploring through interactive dashboards','automatically looking for patterns and outliers powered by machine learning'])}","Connect to all your data in AWS, 3rd party clouds, or on-premises","SPICE in-memory storage to scale data exploration to thousands of users","Forecast business metrics and perform interactive what-if analysis with point-and-click","Pay-per-session optimizes costs by only paying for actual usage","Q enables end-users to dive deep into data through simple questions without BI training"])
        ),
        'fillers': ()
    },
}
"""

Free, not a Support plan
Basic, imited selection of AWS Trusted Advisor checks
Developer, imited selection of AWS Trusted Advisor checks
Business, include access to all AWS Trusted Advisor checks
Enterprise, include access to all AWS Trusted Advisor checks




correct:(
    'To use AWS Lambda, you must configure the servers that run your code',
    'The first step in using AWS Lambda is provisioning a server'
    'Before using AWS Lambda, you must prepay for your estimated compute time.'
    'You pay only for compute time while your code is running.'

)



Which Perspective of the AWS Cloud Adoption Framework focuses on ?

('Operations Perspective','recovering IT workloads to meet the requirements of your business stakeholders'),
('Business Perspective','helps you to move from a model that separates business and IT strategies into a business model that integrates IT strategy'), 
('People Perspective','helps Human Resources (HR) employees prepare their teams for cloud adoption by updating organizational processes and staff skills to include cloud-based competencies'),
('Governance Perspective','helps you understand how to update the staff skills and organizational processes that are necessary to ensure business governance in the cloud'), 


In the S3 Intelligent-Tiering storage class, Amazon S3 monitors objects’ access patterns. If you haven’t accessed an object for 30 consecutive days, Amazon S3 automatically moves it to the infrequent access tier, S3 Standard-IA. If you access an object in the infrequent access tier, Amazon S3 automatically moves it to the frequent access tier, S3 Standard.



('AWS Marketplace','A digital catalog that includes thousands of listings from independent software vendors.'),
('AWS Support','A resource that can answer questions about best practices and assist with troubleshooting issues'),
(['Technical Account Manager','TAM'],'A resource that provides guidance, architectural reviews, and ongoing communication with your company as you plan, deploy, and optimize your applications'), 
('AWS Trusted Advisor.','An online tool that inspects your AWS environment and provides real-time guidance in accordance with AWS best practices'),


(['Amazon Augmented AI','Amazon A2I'],['build the workflows that are required for human review of machine learning predictions','reate your own workflows for machine learning models built on Amazon SageMaker or any other tools']),
('Amazon Textract','a machine learning service that automatically extracts text and data from scanned documents'), 
('Amazon Lex','enables you to build conversational interfaces using voice and text'),
('Amazon Aurora','an enterprise-class relational database'),


Which migration strategy involves
(['Refactoring','Rearchitecting'],'changing how an application is architected and developed, typically by using cloud-native features'),
('Repurchasing','replacing an existing application with a cloud-based version, such as software found in AWS Marketplace'),
('Rehosting','moving an application to the cloud with little to no modifications to the application itself','Also known as "lift and shift"'),
('Replatforming','selectively optimizing aspects of an application to achieve benefits in the cloud without changing the core architecture of the application','also known as "lift, tinker, and shift"'), 
('Retire','Get rid of'),
('Retain','revisit or do nothing'),



Which service

(['Amazon Elastic Kubernetes Service','Amazon EKS'],'is used to run containerized applications on AWS'),
('Amazon SageMaker','enables you to quickly build, train, and deploy machine learning models'),
('Amazon Aurora','an enterprise-class relational database'),
('Amazon Redshift','a data warehousing service that you can use for big data analytics'),


You want to PLACEHOLDER. Which service should you use?



Which actions can you perform in

('Amazon Route 53',['Connect user requests to infrastructure in AWS and outside of AWS','Manage DNS records for domain names']),
('Amazon CloudWatch','Monitor your applications and respond to system-wide performance changes'),
('AWS Artifact','Access AWS security and compliance reports and special online agreements'),
('AWS Quick Starts','Automate the deployment of workloads into your AWS environment'),


You want to store data in a key-value database. Which service should you use?






Which statement best describes
('Amazon GuardDuty','A service that provides intelligent threat detection for your AWS infrastructure and resources'),
('Amazon Inspector','A service that checks applications for security vulnerabilities and deviations from security best practices'),
('AWS WAF','A service that lets you monitor network requests that come into your web applications'),
('AWS Shield','A service that helps protect your applications against distributed denial-of-service (DDoS) attacks'),

Which tool enables you to visualize, understand, and manage your AWS costs and usage over time?
('AWS Cost Explorer','enables you to visualize, understand, and manage your AWS costs and usage over time'),
('AWS Pricing Calculator',['lets you explore AWS services and create an estimate for the cost of your use cases on AWS','enter details for your cloud computing requirements and then receive a detailed estimate that can be exported and shared']),
('AWS Artifact','a service that enables you to access AWS security and compliance reports and special online agreements'),
('AWS Budgets','lets you set custom alerts that will notify you when your service usage exceeds (or is forecasted to exceed) the amount that you have budgeted'),


Which service is used to



Which virtual private cloud (VPC) component controls inbound and outbound traffic for Amazon EC2 instances?
('Security group','controls inbound and outbound traffic for Amazon EC2 instances'),
(['access control list','ACL'],'a virtual firewall that controls inbound and outbound traffic at the subnet level'),
('internet gateway',['a connection between a VPC and the internet','allows public traffic from the internet to access a VPC']),
('subnet','a section of a VPC in which you can group resources based on security or operational needs'),


You want Amazon S3 to monitor your objects' access patterns. Which storage class should you use? 


('Elastic Load Balancing',['acts as a single point of contact for all incoming web traffic to your Auto Scaling group','requests are routed to the load balancer first and then spread across multiple resources that will handle them']),
('AWS Auto Scaling','A service that monitors your applications and automatically adds or removes capacity from your resource groups in response to changing demand'),
('Amazon CloudWatch','A service that provides data that you can use to monitor your applications, optimize resource utilization, and respond to system-wide performance changes'),
('Amazon ElastiCache','A service that enables you to set up, manage, and scale a distributed in-memory or cache environment in the cloud'),


('S3 Intelligent-Tiering','allow Amazon S3 to monitor object access patterns'),
('S3 Glacier',['low-cost storage class that is ideal for data archiving','retrieve objects stored in the S3 Glacier storage class within a few minutes to a few hours']),
('S3 Standard-IA storage class',['ideal for data that is infrequently accessed but requires high availability when needed','store data in a minimum of three Availability Zones','provides the same level of availability as S3 Standard but at a lower storage price']),
('S3 One Zone-IA','ideal for infrequently accessed data that does not require high availability'),
('AWS Elastic Beanstalk','quickly deploy and scale applications on AWS'),
('AWS Outposts','run infrastructure in a hybrid cloud approach'),
('Amazon CloudFront','a content delivery service'),
('AWS Snowball','transfer large amounts of data into and out of AWS'),
(['Amazon Elastic Block Store','Amazon EBS'],'store data in a volume that is attached to an Amazon EC2 instance'),
(['Amazon Simple Storage Service','Amazon S3'],['a service that provides object-level storage','stores data as objects within buckets']),
('AWS Lambda','lets you run code without provisioning or managing servers'),
('Amazon ElastiCache','adds caching layers on top of your databases to help improve the read times of common requests'),
('Amazon DynamoDB',['store data in a key-value database','add or remove attributes from items in the table at any time','not every item in the table has to have the same attributes]'),
(['Amazon Relational Database Service','Amazon RDS)'],'use structured query language (SQL)'),
('Amazon DocumentDB','a document database service that supports MongoDB workloads'),

You are running an Amazon EC2 instance and want to store data in an attached resource. Your data is temporary and will not be kept long term. Which resource should you use?
('Instance stores,['ideal for temporary data that does not need to be kept long term','When an Amazon EC2 instance is stopped or terminated, all the data that has been written to the attached instance store is deleted']),
('Amazon EBS',['ideal for data that needs to be retained','When an Amazon EC2 instance is stopped or terminated, all of the data is still available']),
('Amazon S3 bucket','cannot be attached to Amazon EC2 instances'),
('subnet','a section of a virtual private cloud (VPC) in which you can group resources based on security or operational need'),

Which service enables you to review details for user activities and API calls that have occurred within your AWS environment?
('AWS CloudTrail','enables you to review details for user activities and API calls that have occurred within your AWS environment','events are typically updated within 15 minutes after an API call was made','filter events by specifying the time and date that an API call occurred, the user who requested the action, the type of resource that was involved in the API call etc']),
('Amazon CloudWatch','a service that provides data that you can use to monitor your applications, optimize resource utilization, and respond to system-wide performance changes'),
('Amazon Inspector','a service that checks applications for security vulnerabilities and deviations from security best practices'),
('AWS Trusted Advisor','an online tool that inspects your AWS environment and provides real-time guidance in accordance with AWS best practices'),

Which AWS Trusted Advisor category includes checks for your service limits and overutilized instances?
('Performance','includes checks for your service limits and overutilized instances'),
('Security','includes checks that help you to review your permissions and identify which AWS security features to enable'),
('Cost Optimization','includes checks for unused or idle resources that could be eliminated and provide cost savings'),
('Fault Tolerance','includes checks to help you improve your applications’ availability and redundancy'),


Which service enables you to consolidate and manage multiple AWS accounts from a central location?
('AWS Organizations',['enables you to consolidate and manage multiple AWS accounts from a central location','centrally control permissions for the accounts in your organization by using service control policies (SCPs)',''use the consolidated billing feature in AWS Organizations to combine usage and receive a single bill for multiple AWS accounts']),
('AWS Identity and Access Management (IAM)','manage access to AWS services and resources'),
('AWS Artifact','a service that enables you to access AWS security and compliance reports and special online agreements'),
(['AWS Key Management Service','AWS KMS'],'enables you to create, manage, and use cryptographic keys'),


Responsiblilties

Maintaining virtualization infrastructure
Configuring AWS infrastructure devices

Training company employees on how to use AWS services
Configuring security groups on Amazon EC2 instances
Creating IAM users and groups


What is
('cloud computing','On-demand delivery of IT resources and applications through the internet with pay-as-you-go pricing'),
('hybrid cloud deployment',['connects infrastructure and applications between cloud-based resources and existing resources that are not in the cloud, such as on-premises resources','not equivalent to an on-premises deployment because it involves resources that are located in the cloud']),
('Private cloud deployment','on-premises deployment'),
('Cloud-based applications','fully deployed in the cloud and do not have any parts that run on premises'),



How
('does the scale of cloud computing help you to save costs','The aggregated cloud usage from a large number of customers results in lower pay-as-you-go prices'),
('Trade upfront expense','not having to invest in technology resources before using them'),
('Stop guessing capacity','Accessing services on-demand to prevent excess or limited capacity),
('Go global in minutes','Quickly deploying applications to customers and providing them with low latency'),




('',''),
('',''),






"""