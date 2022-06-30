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
    'AWS_storage_services': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'PLACEHOLDER best describes:',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(

            ('instance store', ['provides temporary block-level storage for an Amazon EC2 instance','disk storage that is physically attached to the host computer for an EC2 instance','has the same lifespan as the instance','When the instance is terminated, you lose any data']),
            ('Amazon EBS',['store data in a volume that is attached to an Amazon EC2 instance','ideal for data that needs to be retained','When an Amazon EC2 instance is stopped or terminated, all of the data is still available']),
            ('Amazon EBS snapshot',['incremental backup','first backup taken of a volume copies all the data','after first backup, only the blocks of data that have changed since the most recent snapshot are saved','different from full backups']),
            ('Amazon EC2', 'allows users to rent virtual computers on which to run their own computer applications'),
            ('Amazon EC2 instance', 'a virtual server for running applications'),


            ('Amazon Aurora','an enterprise-class relational database'),
            ('Amazon Redshift','a data warehousing service that you can use for big data analytics'),
            (['Amazon Simple Storage Service','Amazon S3'],['a service that provides object-level storage','stores data as objects within buckets']),
            ('Amazon ElastiCache','adds caching layers on top of your databases to help improve the read times of common requests'),
            (['Amazon QLDB', 'Amazon Quantum Ledger Database'],'used to review a complete history of all the changes that have been made to your application data'),
            ('Amazon Redshift', ['a data warehousing service that you can use for big data analytics','offers the ability to collect data from many sources and help you to understand relationships and trends across your data']),
            ('Amazon SQS',['message queuing service','used to send, store, and receive messages between software components at any volume size, without losing messages or requiring other services to be available']),
            ('AWS Snowmobile',['used for transferring up to 100 PB of data to AWS','a 45-foot long shipping container that is pulled by a semi-trailer truck']),
            ('Amazon Neptune',['a graph database service','build and run applications that work with highly connected datasets, such as recommendation engines, fraud detection, and knowledge graphs']),
            
            ('AWS Outposts','run infrastructure in a hybrid cloud approach'),
            ('AWS Snowball','transfer large amounts of data into and out of AWS'),
            
            ('Amazon DynamoDB',['store data in a key-value database','add or remove attributes from items in the table at any time','not every item in the table has to have the same attributes']),
            (['Amazon Relational Database Service','Amazon RDS)'],'use structured query language (SQL)'),
            ('Amazon DocumentDB','a document database service that supports MongoDB workloads'),
            ('Instance stores',['ideal for temporary data that does not need to be kept long term','When an Amazon EC2 instance is stopped or terminated, all the data that has been written to the attached instance store is deleted']),
            
            ('Amazon S3 bucket','cannot be attached to Amazon EC2 instances'),
        ),
        'fillers': ()
    },
    'AWS_basic_storage': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'PLACEHOLDER best describes:',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('instance store', ['provides temporary block-level storage for an Amazon EC2 instance','disk storage that is physically attached to the host computer for an EC2 instance','has the same lifespan as the instance','When the instance is terminated, you lose any data']),
            ('Amazon EBS',['store data in a volume that is attached to an Amazon EC2 instance','ideal for data that needs to be retained','When an Amazon EC2 instance is stopped or terminated, all of the data is still available']),
            ('Amazon EBS volume',['can be attached to an Amazon EC2 instance','size and volume can be defined']),
            ('Amazon EBS snapshot',['incremental backup','first backup taken of a volume copies all the data','after first backup, only the blocks of data that have changed since the most recent snapshot are saved','different from full backups']),
            ('Amazon EC2', 'allows users to rent virtual computers on which to run their own computer applications'),
            ('Amazon EC2 instance', 'a virtual server for running applications'),
            ('Amazon S3 bucket','cannot be attached to Amazon EC2 instances'),
        ),
        'fillers': ()
    },
    'Amazon_S3': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'PLACEHOLDER best describes:',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('object', ['includes data','includes metadata','includes a key', 'includes a unique identifier']),
            ('S3 Standard',['Designed for frequently accessed data','Stores data in a minimum of three Availability Zones','provides high availability for objects','good choice for a wide range of use cases, such as websites, content distribution, and data analytics', 'higher cost than other storage classes intended for infrequently accessed data and archival storage']),
            ('S3 Standard-IA storage class',['ideal for data that is infrequently accessed but requires high availability when needed','store data in a minimum of three Availability Zones','provides the same level of availability as S3 Standard but at a lower storage price', 'ideal for data infrequently accessed but requires high availability when needed','lower storage price and a higher retrieval price']),
            ('S3 One Zone-IA',['Stores data in a single Availability Zone','Has a lower storage price than S3 Standard-IA','ideal if you can easily reproduce your data in the event of an Availability Zone failure', 'lower storage costs than S3 Standard-IA']),
            ('S3 Intelligent-Tiering',['Ideal for data with unknown or changing access patterns','Requires a small monthly monitoring and automation fee per object','Amazon S3 automatically moves it to the infrequent access tier if not accessed for 30 days','If you access an object in the infrequent access tier, Amazon S3 automatically moves it to the frequent access tier, S3 Standard','allow Amazon S3 to monitor object access patterns']),
            ('S3 Glacier',['low-cost storage class that is ideal for data archiving','retrieve objects stored in the S3 Glacier storage class within a few minutes to a few hours','ideal for data archiving','use this storage class to store archived customer records or older photos and video files']),
            ('S3 Glacier Deep Archive',['Lowest-cost object storage class ideal for archiving','Able to retrieve objects within 12 hours','ideal for data archiving']),
            
            
        ),
        'fillers': ()
    },
    'EBS_vs_S3':{
        'type':'auto_correct_incorrect',
        'verbs':('will','are', 'can', 'does', 'is'),
        'negator':'not',
        'correct':(
            'Changing one part of a file in EBS will not result in the whole file being re-uploaded',
            'Changing one part of a file in S3 will result in the whole file being re-uploaded',
            'The cost of storing a certain amount of data on EBS is more than S3',
            'The cost of storing a certain amount of data on S3 is less than EBS',
            'S3 is serverless',
            'S3 does not have to be attached to an EC2 instance',
            'S3 is ideal for storing complete objects',
            'EBS is idea for making lots of reads and writes to what is stored',
            'S3 is not ideal making lots of reads and writes to what is stored',
        )
    },
    'S3_vs_EBS_use_cases_and_description':{
        'question_with_0':'Which isPOSNEG a PLACEHOLDER use case?',
        'positive_negative':('',' not'),
        'type':['multi_option_pairs','posneg_pairs'],
        'pairs':(
            (['S3','Simple Storage Service'],
            [
                'creating data lakes',
                'holding raw data in native format',
                'big data analytics',
                'use with machine learning tools',
                'robust backup solution',
                'backup and restoration',
                'reliable disaster recovery',
                'content management',
                'serving media',
            ]),
            (['EBS','Elastic Block Storage'],
            [
                'software testing',
                'software development',
                'business continuity',
                'running applications in multiple regions',
                'running enterprise-wide applications',
                'applications requiring low level latency',
                'transactional databases',
                'No SQL databases',
            ]),
        )
    },
    
    'S3_vs_EBS_security_integrity_availability':{
        'question_with_0':'Which POSNEG AWS PLACEHOLDER?',
        'positive_negative':('describes','does not describe'),
        'type':['multi_option_pairs','posneg_pairs'],
        'pairs':(
            (['S3','Simple Storage Service'],
            [
                'distributes data objects across several machines',
                'accessed using APIs',
                'accessed via the internet',
                'stores data accrosss multiple Availability Zones',
                'prevents unauthorised access using access management tools and encryption policies',
                'features which make it easier to comply with regulatory requirements',
                'uses versioning and cross-regional replication for backup',
                'can be used by multiple instances at the same time'
            ]),
            (['EBS','Elastic Block Storage'],
            [
                'stores files in multiple volumes',
                'each volume acts as a seperate hard drive',
                'accessible only by the attached instance',
                'accessed by a single attached instance',
                'provides durability by redundantly storing data in a single AZ',
                'unauthorised access to an instance is a vulnerability',
                'snapshots used to place resources and data in multiple locations',
                'uses automated backup',
                'better for geographic interchangability',
                'can only be used by one mounted instance',
                'cannot be used by multiple instances at a single time',
            ]),
        )
    },
    'S3_vs_EBS_storage_pricing_and_performance':{
        'question_with_0':'Which POSNEG AWS PLACEHOLDER?',
        'positive_negative':('describes','does not describe'),
        'type':['multi_option_pairs','posneg_pairs'],
        'pairs':(
            (['S3','Simple Storage Service'],
            [
                'object level data storage',
                'distributes data objects across several machines',
                'can store larger amounts of data',
                'stores data in buckets',
                'each bucket has untimited data capacity',
                'has no effective limit on storage capacity',
                'rapidly scalable',
                'resources can be provisioned in run time',
                'Free Tier - 5 GB',
                'First 50 TB/month - $0.023/GB',
                '450 TB/month - $0.022/GB',
                'slower storage',
                'more latency',
            ]),
            (['EBS','Elastic Block Storage'],
            [
                'block level data storage',
                'stores files in multiple volumes',
                'each volume acts as a seperate hard drive',
                'can store less data',
                'stored data in volumnes',
                'limit of 20 volumes',
                'each volume can hold up to 1TB',
                'has an upper limit on storage capacity'
                'storage resources must be manually increased',
                'faster storage',
                'less latency',
                'Free Tier - 30 GB'
                'General Purpose - $0.045/GB(1 month)',
                'Provisioned SSD - $0.125/GB(1 month)',
                'uses SSD volumes',
            ]),
        )
    },

    'Elastic_file_store_RDS_and_Aurora': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'PLACEHOLDER best describes:',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            (['Amazon EBS', 'Amazon Elastic Block Store'], ['stores data in a single availablily zone','requires an EC2 instance in the same availability zone']),
            (['Amazon EFS', 'Amazon Elastic File Store'],['Regional service','allows concurrent access','accessed through file paths']),
            (['Amazon RDS', 'Amazon Relational Database Service'],['enables you to run relational databases in the AWS Cloud','managed service that automates tasks such as hardware provisioning, database setup, patching, and backups',f"supports {choice(['Amazon Aurora','PostgreSQL','MySQL','MariaDB','Oracle Database','Microsoft SQL Server'])}"]),
            ('Amazon Aurora',['an enterprise-class relational database', 'compatible with MySQL and PostgreSQL relational databases','up to five times faster than standard MySQL databases and up to three times faster than standard PostgreSQL databases','reduces unnecessary input/output (I/O) operations, while ensuring that your database resources remain reliable and available','replicates six copies of your data across three Availability Zones and continuously backs up your data to Amazon S3']),
        ),
        'fillers': ()
    },
}



"""


('Amazon Redshift','a data warehousing service that you can use for big data analytics'),
(['Amazon Simple Storage Service','Amazon S3'],['a service that provides object-level storage','stores data as objects within buckets']),
('Amazon ElastiCache','adds caching layers on top of your databases to help improve the read times of common requests'),
(['Amazon QLDB', 'Amazon Quantum Ledger Database'],'used to review a complete history of all the changes that have been made to your application data'),
('Amazon Redshift', ['a data warehousing service that you can use for big data analytics','offers the ability to collect data from many sources and help you to understand relationships and trends across your data']),
('Amazon SQS',['message queuing service','used to send, store, and receive messages between software components at any volume size, without losing messages or requiring other services to be available']),
('AWS Snowmobile',['used for transferring up to 100 PB of data to AWS','a 45-foot long shipping container that is pulled by a semi-trailer truck']),
('Amazon Neptune',['a graph database service','build and run applications that work with highly connected datasets, such as recommendation engines, fraud detection, and knowledge graphs']),
('S3 Intelligent-Tiering','allow Amazon S3 to monitor object access patterns'),
('S3 Glacier',['low-cost storage class that is ideal for data archiving','retrieve objects stored in the S3 Glacier storage class within a few minutes to a few hours']),
('S3 Standard-IA storage class',['ideal for data that is infrequently accessed but requires high availability when needed','store data in a minimum of three Availability Zones','provides the same level of availability as S3 Standard but at a lower storage price']),
('S3 One Zone-IA','ideal for infrequently accessed data that does not require high availability'),
('AWS Outposts','run infrastructure in a hybrid cloud approach'),
('Amazon CloudFront','a content delivery service'),
('AWS Snowball','transfer large amounts of data into and out of AWS'),
(['Amazon Elastic Block Store','Amazon EBS'],'store data in a volume that is attached to an Amazon EC2 instance'),
('Amazon DynamoDB',['store data in a key-value database','add or remove attributes from items in the table at any time','not every item in the table has to have the same attributes]'),
(['Amazon Relational Database Service','Amazon RDS)'],'use structured query language (SQL)'),
('Amazon DocumentDB','a document database service that supports MongoDB workloads'),
('Instance stores,['ideal for temporary data that does not need to be kept long term','When an Amazon EC2 instance is stopped or terminated, all the data that has been written to the attached instance store is deleted']),
('Amazon EBS',['ideal for data that needs to be retained','When an Amazon EC2 instance is stopped or terminated, all of the data is still available']),
('Amazon S3 bucket','cannot be attached to Amazon EC2 instances'),
"""