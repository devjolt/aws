from random import randint, choice

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
    'AWS_pricing_and_support_services': {
        'question_with_0':'Which isPOSNEG a description of PLACEHOLDER?',
        'question_with_1':'Which of the following is described by this: PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            ('AWS Billing and Cost Management Dashboard',['Compare your current compute time with the previous month, and get a forecast of the next month based on current usage','View month-to-date spend by instance','View Free Tier usage by month','create new EC2 instances','create new Lambda code','View logs','Purchase and manage reserve capacity','Analyse cloudwatch logs']),
            ('AWS free tier',['always free', 'trials', '12 months free']),
            ('AWS pricing concept',['pay for exactly the amount of resources that you actually use, without requiring long-term contracts or complex licensing','a significant discount compared to On-Demand Instance pricing','tiered pricing, so the per-unit cost is incrementally lower with increased usage']),
            ('AWS Budgets',['updates three times a day','helps you to accurately determine how close your usage is to your budgeted amounts or to the AWS Free Tier limits','In AWS Budgets, you can also set custom alerts when your usage exceeds (or is forecasted to exceed) the budgeted amount']),
            ('AWS Cost Explorer',['enables you to visualize, understand, and manage your AWS costs and usage over time','includes a default report of the costs and usage for your top five cost-accruing AWS services','apply custom filters and groups to analyze your data','view resource usage at the hourly level']),
            ('AWS Pricing Calculator',['lets you explore AWS services and create an estimate for the cost of your use cases on AWS']),
            ('AWS Support Plans',['helps you to enable, run, use, operate, and recover IT workloads to the level agreed upon with your business stakeholders','define how day-to-day, quarter-to-quarter, and year-to-year business is conducted','align with and support the operations of the business','AWS CAF helps these stakeholders define current operating procedures and identify the process changes and training needed to implement successful cloud adoption']),
            ('AWS Market Place',['a digital catalog that includes thousands of software listings from independent software vendors','find, test, and buy software that runs on AWS']),
            ('consolidated billing',['share bulk discount pricing, Savings Plans, and Reserved Instances across the accounts in your organization','enables you to receive a single bill for all AWS accounts in your organization','easily track the combined costs of all the linked accounts in your organization','maximum number of accounts allowed for an organization is 4, but you can contact AWS Support to increase your quota, if needed']),
            ('AWS Personal Health Dashboard','provides alerts and remediation guidance when AWS is experiencing events that may affect you'),
            ('AWS Organizations','enables you to manage multiple AWS accounts from a central location'),
            ('AWS QuickSight',[f"understand data by {choice(['asking questions in natural language','exploring through interactive dashboards','automatically looking for patterns and outliers powered by machine learning'])}","Connect to all your data in AWS, 3rd party clouds, or on-premises","SPICE in-memory storage to scale data exploration to thousands of users","Forecast business metrics and perform interactive what-if analysis with point-and-click","Pay-per-session optimizes costs by only paying for actual usage","Q enables end-users to dive deep into data through simple questions without BI training"])
        ),
        'fillers': ()
    },
    
    "Recalling_AWS_free_tiers":{
        'question':'Which of the following is PLACEHOLDER one of the six core perspectives of the cloud adoption framework?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'always free',
            'trials',
            '12 months free',
        ),
        'incorrect': (
            'sometimes free',
            'testing',
            f'{randint(1,11)} months free',
            f'{randint(1,5)} years free',
            'there are no free tiers',
        ),
    },
    'AWS_pricing_examples': {
        'question_with_0':'Which isPOSNEG a description of PLACEHOLDER pricing?',
        'question_with_1':'Which perspective service is described by this: PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            ('always free',['1 million free requests in AWS Lambda','3.2 million seconds of compute time per month in AWS Lambda','Amazon DynamoDB allows 25 GB of free storage per month']),
            ('trials',['Amazon Inspector','Amazon Lightsail']),
            ('12 months free',['Amazon S3 Standard Storage','thresholds for monthly hours of Amazon EC2 compute time','amounts of Amazon CloudFront data transfer out']),
            ('Lambda',['save on costs by signing up for Compute Savings Plans','you are charged based on the number of requests','you are charged for the time that it takes to run', 'allows 1 million free requests oer month', 'allows up to 3.2 million seconds of compute time per month']),
            ('EC2',['length of time that Elastic Load Balancing has been used','pay for only the compute time that you use while your instances are running','reduce costs by using Spot Instances','find additional cost savings by considering Savings Plans and Reserved Instances']),
            ('Amazon S3',['no cost to transfer data between different buckets','pay for requests made to objects and buckets','pay for only the storage that you use','the rate to store objects is based on your objects\' sizes, storage classes, and how long you have stored each object during the month']),
        ),
        'fillers': ()
    },
    "AWS_billing_and_cost_management_dashboard":{
        'question':'Which of the following is PLACEHOLDER an activity which can be done through the AWS Billing and Cost Management Dashboard?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'Compare your current month-to-date balance with the previous month, and get a forecast of the next month based on current usage',
            'View month-to-date spend by service',
            'View Free Tier usage by service',
            'Access Cost Explorer and create budgets',
            'Purchase and manage Savings Plans',
            'Publish AWS Cost and Usage Reports',
        ),
        'incorrect': (
            'Compare your current compute time with the previous month, and get a forecast of the next month based on current usage',
            'View month-to-date spend by instance',
            'View Free Tier usage by month',
            'create new EC2 instances',
            'create new Lambda code',
            'View logs',
            'Purchase and manage reserve capacity',
            'Analyse cloudwatch logs',
        ),
    },   
    'AWS_support_plans': {
        'question_with_0':'Which POSNEG describe the PLACEHOLDER support plan?',
        'question_with_1':'Which includes the following: PLACEHOLDER?',
        'positive_negative':('does','does not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            ('Basic',['free for all AWS customers','access to whitepapers, documentation, and support communities','contact AWS for billing questions and service limit increases','access to a limited selection of AWS Trusted Advisor checks','use the AWS Personal Health Dashboard']),
            ('Developer',['Best practice guidance','Client-side diagnostic tools','Building-block architecture support, which consists of guidance for how to use AWS offerings, features, and services together']),
            ('Business',['all AWS Trusted Advisor checks at the lowest cost','Use-case guidance to identify AWS offerings, features, and services that can best support your specific needs','All AWS Trusted Advisor checks','Limited support for third-party software, such as common operating systems and application stack components']),
            ('Enterprise',['Application architecture guidance','a consultative relationship to support your company\'s specific use cases and applications','Infrastructure event management','A short-term engagement with AWS Support that helps your company gain a better understanding of your use cases','architectural and scaling guidance','A Technical Account Manager']),
        ),
        'fillers': ()
    },



}