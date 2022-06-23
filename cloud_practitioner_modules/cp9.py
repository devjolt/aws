from random import choice, randint

"""multi_option_from_correct_incorrect
make_items_question_from_correct_incorrect
make_items_question_from_pairs
posneg_pairs
new_pairs
multi_option_pairs
order_from_pairs
name_attribute_pairs
code_block_question
"""

questions = {
    "Recalling_the_six_core_perspectives_of_the_cloud_adoption_framework":{
        'question':'Which of the following is PLACEHOLDER one of the six core perspectives of the cloud adoption framework?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'business',
            'people',
            'governance',
            'platform',
            'security',
            'operations'
        ),
        'incorrect': (
            'national',
            'oversight',
            'audience',
            'stakeholder',
            'customer',
            'management',
            'compliance',
            'proceedural',
            'object oriented',
            'development',
            'financial',
            'application',
            'infrastructural',
            'architechtural',
        ),
    },
    'Defining_the_six_core_perspectives_of_the_cloud_adoption_framework': {
        'question_with_0':'Which isPOSNEG a description of the PLACEHOLDER perspective of the cloud adoption framework?',
        'question_with_1':'Which perspective of the cloud adoption framework is described by this: PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            ('business',['ensure that your strategies and goals align with your IT strategies and goals','reate a strong case for cloud adoption and prioritize cloud adoption initiatives','ensures that IT aligns with business needs','ensures that IT investments link to key business results']),
            ('people',['supports development of an organization-wide change management strategy for successful cloud adoption','evaluate organizational structures and roles, new skill and process requirements, and identify gaps','helps prioritize training, staffing, and organizational changes']),
            ('governance',['focuses on the skills and processes to align IT strategy with business strategy','ensures that you maximize the business value and minimize risks','understand how to update the staff skills and processes necessary to ensure business governance in the cloud','manage and measure cloud investments to evaluate business outcomes']),
            ('platform',['helps you design, implement, and optimize your AWS infrastructure based on your business goals and perspectives','includes principles and patterns for implementing new solutions on the cloud, and migrating on-premises workloads to the cloud','use a variety of architectural models to understand and communicate the structure of IT systems and their relationships','describe the architecture of the target state environment in detail']),
            ('security',['ensures that the organization meets objectives for visibility, auditability, control, and agility','use the AWS CAF to structure the selection and implementation of controls that meet the organization\'s needs']),
            ('operations',['helps you to enable, run, use, operate, and recover IT workloads to the level agreed upon with your business stakeholders','define how day-to-day, quarter-to-quarter, and year-to-year business is conducted','align with and support the operations of the business','AWS CAF helps these stakeholders define current operating procedures and identify the process changes and training needed to implement successful cloud adoption']),
        ),
        'fillers': ()
    },
    'Parties_involved_in_the_six_core_perspectives_of_the_cloud_adoption_framework': {
        'question_with_0':'Which isPOSNEG a role in the PLACEHOLDER perspective of the cloud adoption framework?',
        'question_with_1':'Which perspective of the cloud adoption framework is the following role involved in: PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            ('business',['Business managers','Finance managers','Budget owners','Strategy stakeholders']),
            ('people',['Human resources','Staffing','People managers']),
            ('governance',['Chief Information Officer','CIO','Program managers','Enterprise architects','Business analysts','Portfolio managers']),
            ('platform',['Chief Technology Officer','CTO','IT managers','Solutions architects']),
            ('security',['Chief Information Security Officer','CISO','IT security managers','IT security analysts']),
            ('operations',['IT operations managers','IT support managers']),
        ),
        'fillers': ()
    },
    
    'Snow_family':{
        'question_with_name':'Which best describes an AWS PLACEHOLDER?',
        'question_with_attribute':'Which member of the Snow family is described by the following: PLACEHOLDER',
        'type':'pairs_name_dict_attributes',
        'name_attribute_pairs':(
            ('Snowcone',{'description':'a small, rugged, and secure edge computing and data transfer device', 'CPUs':'2 CPUs', 'memory':'4 GB memory', 'storage':'8 TB storage'}),
            ('Snowball Edge Storage Optimised ',{'description':['well suited for large-scale data migrations and recurring transfer workflows', 'well suited for local computing with higher capacity needs'], 'CPUs':'40 vCPUs', 'memory':'80 GiB memory', 'storage':'80 TB HDD for S3 compatible storage and 1 TB SSD for block volumes'}),
            ('Snowball Edge Compute Optimised ',{'description':'provides powerful computing resources for use cases such as machine learning, full motion video analysis, analytics, and local computing stacks', 'CPUs':['52 vCPUs', 'optional NVIDIA Tesla V100 GPU'], 'memory':'208 GiB memory', 'storage':'42 TB HDD for S3 compatible storage and 7.68 TB SDD for block volumes'}),
            ('Snowmobile',{'description':['an exabyte-scale data transfer service used to move large amounts of data to AWS', 'a 45-foot long ruggedized shipping container, pulled by a semi trailer truck'], 'CPUs':'Number of CPUs not applicable', 'memory':'memory not applicable', 'storage':'100 petabytes storage'}),
        ),
        'fillers':(
            (['Snowboard', 'Snowman', 'Icecream', 'Glacier', 'SnowPop'],{'description':['a high capacity EC2 instance', 'an AWS laptop connected to the cloud',], 'CPUs':f"{choice([4, 6, 8, 100])} {choice(['CPUs', 'vCPUs'])}", 'memory':f"{choice(['2 GB', '6 GB', '8 GB', '40 GiB', '42 GiB', '50 GiB'])} memory", 'storage':[f"{randint(10, 100)} {choice(['GB', 'GiB', 'TB'])} HDD for S3 compatible storage and {randint(1, 10)} {choice(['GB', 'GiB', 'TB'])} SSD for block volumes", f"{randint(10, 100)} {choice(['GB', 'GiB', 'TB'])} storage"]}),
        )
    },
    "Recalling_the_six_Rs_of_migration":{
        'question':'Which of the following is PLACEHOLDER one of the six Rs of migration?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'rehosting',
            'replatforming',
            'refactoring',
            're-architecting',
            'repurchasing',
            'retaining',
            'retiring'
        ),
        'incorrect': (
            'remaining',
            'reversing',
            'reimplementing',
            'reorganising',
            'reordering',
            'repeating',
            'releaving',
            're-engineering'
        ),
    },
    'Defining_the_six_strategies_for_migration': {
        'question_with_0':'Which isPOSNEG a description of the PLACEHOLDER strategy for migration?',
        'question_with_1':'Which strategy for migration is described by: PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            ('rehosting',['also known as "lift-and-shift"','involves moving applications without changes','In the scenario of a large legacy migration, in which the company is looking to implement its migration and scale quickly to meet a business case, the majority of applications do this']),
            ('replatforming',['involves selectively optimizing aspects of an application to achieve benefits in the cloud without changing the core architecture of the application','also known as "lift, tinker, and shift"','involves making a few cloud optimizations to realize a tangible benefit','optimization is achieved without changing the core architecture of the application']),
            (['refactoring','re-architecting'],['involves changing how an application is architected and developed, typically by using cloud-native features','involves reimagining how an application is architected and developed by using cloud-native features','driven by a strong business need to add features, scale, or performance that would otherwise be difficult to achieve in the application\'s existing environment']),
            ('repurchasing',['involves replacing an existing application with a cloud-based version','involves moving from a traditional license to a software-as-a-service model','a business might choose to implement the repurchasing strategy by migrating from a customer relationship management (CRM) system to a third party product']),
            ('retaining',['consists of keeping applications that are critical for the business in the source environment','might include applications that require major refactoring before they can be migrated, or, work that can be postponed until a later time']),
            ('retiring',['involves removing an application that is no longer used or that can be turned off','the process of removing applications that are no longer needed']),
            
        ),
        'fillers': ()
    },
    'Innovation_with_AWS_services': {
        'question_with_0':'Which isPOSNEG a description of PLACEHOLDER?',
        'question_with_1':'Which is described by: PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            ('AWS Lambda',['refers to applications that don\'t require you to provision, maintain, or administer servers','you don\'t need to worry about fault tolerance or availability','a serverless application','you can bypass the need to manage a fleet of servers','enables your developers to focus on their core product instead of managing and operating servers']),
            ('Amazon Transcribe','convert speech to text with artificial intelligence'),
            ('Amazon Comprehend','use artificial intelligence to discover patterns in text'),
            ('Amazon Fraud Detector','use artificial intelligence to identify potentially fraudulent online activities'),
            ('Amazon Lex','Build voice and text chatbots using artificial intelligence'),
            ('Amazon SageMaker',['uses machine learning','removing the difficult work from the process and empower you to build, train, and deploy ML models quickly','analyze data','solve complex problems','predict outcomes before they happen']),
            ('Amazon Textract','a machine learning service that automatically extracts text and data from scanned documents'),
            ('AWS DeepRacer','an autonomous 1/18 scale race car that you can use to test reinforcement learning models'),
        
        ),
        'fillers': ()
    },
}