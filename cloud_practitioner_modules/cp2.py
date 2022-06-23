"""multi_option_from_correct_incorrect
make_items_question_from_correct_incorrect
make_items_question_from_pairs
posneg_pairs
new_pairs
multi_option_pairs
order_from_pairs
code_block_question
"""

questions = {
    'EC2_memory_optimisation': {
        'question_with_0':'Which is a description of PLACEHOLDER EC2 instances?',
        'question_with_1':'Which AWS service is described by the following: PLACEHOLDER',
        'positive_negative':('',' not'),
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('Memory optimized','Ideal for high-performance databases'),
            ('Storage optimized',['Suitable for data warehousing applications','designed for workloads that require high, sequential read and write access to large datasets on local storage']),
            ('General purpose',['Balances compute, memory and networking resources','instances provide a balance of compute, memory, and networking resources']),
            ('Compute optimized',['Offers high-performance processors', 'suitable for a batch processing workload']),
        ),
        'fillers': ()
    },
    'Instance_pricing_plans': {
        'question_with_0':'Which is a description of the PLACEHOLDER compute option?',
        'question_with_1':'Which AWS service is described by the following: PLACEHOLDER',
        'positive_negative':('',' not'),
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('Savings Plans',['reduces costs when you commit to a consistent amount of compute usage for a 1-year or 3-year term','Any usage up to the commitment is charged at the discounted plan rate']),
            ('Reserved Instances',['a billing discount that is applied to the use of On-Demand Instances in your account','do not require you to commit to a consistent amount of compute usage over the duration of the contract']),
            ('Spot Instances',['ideal for workloads with flexible start and end times or that can withstand interruptions','leverage unused EC2 computing capacity and offer you cost savings']),
            ('Dedicated Hosts',['physical servers with EC2 instance capacity that is fully dedicated to your use','You can use your existing per-socket, per-core, or per-VM software licenses to help maintain license compliance']),
            ('On-Demand', ['ideal for short-term, irregular workloads that cannot be interrupted','No upfront costs or minimum contracts apply','instances run continuously until you stop them, and you pay for only the compute time you use','Sample use cases include developing and testing applications and running applications that have unpredictable usage patterns','not recommended for workloads that last a year or longer because these workloads can experience greater cost savings using Reserved Instances']),
        ),
        'fillers': ()
    },
    'AWS_services_and_tools': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'Which AWS service isPOSNEG described by the following: PLACEHOLDER',
        'positive_negative':('',' not'),
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            (['Amazon Simple Notification Service','Amazon SNS'],'best choice for publishing messages to subscribers'),
            (['Amazon Simple Queue Service','Amazon SQS'],['a message queuing service','It does not use the message subscription and topic model']),
            ('Amazon EC2 Auto Scaling','enables you to automatically add or remove Amazon EC2 instances in response to changing application demand'),
            ('Elastic Load Balancing','automatically distributes incoming application traffic across multiple resources'),
        ),
        'fillers': ()
    },
    'AWS_compute_and_container_services': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'Which isPOSNEG described by the following: PLACEHOLDER',
        'positive_negative':('',' not'),
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('AWS Lambda',['a service that lets you run code without needing to provision or manage servers', 'you pay only for the compute time that you consume','charges apply only when your code is running','you can run code for virtually any type of application or backend service, all with zero administration']),
            (['Amazon Elastic Container Service','Amazon ECS'],['a highly scalable, high-performance container management system that enables you to run and scale containerized applications on AWS','supports Docker containers', 'you can use API calls to launch and stop Docker-enabled applications']),
            ('Docker','a software platform that enables you to build, test, and deploy applications quickly'),
            (['Amazon Elastic Kubernetes Service','Amazon EKS'],'a fully managed service that you can use to run Kubernetes on AWS'), 
            ('Kubernetes','open-source software that enables you to deploy and manage containerized applications at scale','apply new Kubernetes features and functionalities updates to your applications'),
            ('AWS Fargate',['a serverless compute engine for containers','works with both Amazon ECS and Amazon EKS','you do not need to provision or manage servers','manages your server infrastructure for you','you pay only for the resources that are required to run your containers']),
        ),
        'fillers': ()
    },
    'AWS_processes': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'Which is described by the following: PLACEHOLDER',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('Elastic Load Balancing','Ensuring that no single Amazon EC2 instance has to carry the full workload on its own'),
            ('Auto Scaling',['Adding a second Amazon EC2 instance during an online store\'s popular sale','Automatically adjusting the number of Amazon EC2 instances to meet demand','Removing unneeded Amazon EC2 instances when demand is low']),
            ('Elastic Load Balancing',['acts as a single point of contact for all incoming web traffic to your Auto Scaling group','requests are routed to the load balancer first and then spread across multiple resources that will handle them']),
            ('AWS Auto Scaling','A service that monitors your applications and automatically adds or removes capacity from your resource groups in response to changing demand'),
            ('Amazon CloudWatch','A service that provides data that you can use to monitor your applications, optimize resource utilization, and respond to system-wide performance changes'),
            ('Amazon ElastiCache','A service that enables you to set up, manage, and scale a distributed in-memory or cache environment in the cloud'),

        ),
        'fillers': ()
    },
}
"""

"""