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
    'Availability_zones': {
        'question_with_0':'Which is a description of PLACEHOLDER?',
        'question_with_1':'Which AWS concept is described by the following: PLACEHOLDER',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('Availability Zone', ['a single data center or a group of data centers within a Region','located tens of miles apart from each other','provides interconnectivity to support the services and applications that run within a Region']),
            ('Region', 'A separate geographical location with multiple locations that are isolated from each other'),
            ('origin', 'The server from which Amazon CloudFront gets your files'),
            ('Edge location', 'A site that Amazon CloudFront uses to cache copies of content for faster delivery to users at any location'),
            ('AWS Outposts',' a service that you can use to run AWS infrastructure, services, and tools in your own on-premises data center in a hybrid approach'),
        ),
        'fillers': ()
    },
    'AWS_services': {
        'question_with_0':'Which action can you perform in PLACEHOLDER?',
        'question_with_1':'What would you use to perform the following: PLACEHOLDER',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('Amazon CloudFront','Deliver content to customers through a global network of edge locations','uses a network of edge locations to cache content and deliver content to customers all over the world'),
            ('AWS Outposts','Run infrastructure in a hybrid cloud approach'),
            ('AWS CloudFormation','Provision resources by using programming languages or a text file'),
            (['Amazon Virtual Private Cloud','Amazon VPC'],'Provision an isolated section of the AWS Cloud to launch resources in a virtual network that you define'),
        ),
        'fillers': ()
    },
    'Factors_to_considered_when_selecting_a_region': {
        'question':'Which factors should PLACEHOLDER be considered when selecting a region?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'Proximity to your customers',
            'Available services within a Region',
            'Pricing',
            'Compliance with data governance and legal requirements',
        ),
        'incorrect': (
            'The level of support',
            'Assigning custom permissions',
            'The AWS Command Line Interface (AWS CLI)',
            'Availability of Lambda',
        ),
    },
    'Region_selection': {
        'question_with_0':'Which of the following factors are most related to PLACEHOLDER?',
        'question_with_1':'Which factor of selecting a region is the following related to: PLACEHOLDER',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('Proximity to your customers','get content to customers faster'),
            ('Available services within a Region','closest Region might not have all the features that you want to offer to customers'),
            ('Pricing','Less expensive compute time in one region compared to another'),
            ('Compliance with data governance and legal requirements',['GDPR', 'you might need to run your data out of specific areas']),
        ),
        'fillers': ()
    },
    'AWS_global_infrastructure': {
        'question':'Which is PLACEHOLDER for the AWS global infrastructure?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'true',
        'negative':'false',
        'course_code':'',
        'correct':(
            'A Region consists of two or more Availability Zones',
            'An Edge location is where end users access services located at AWS',
            'A Region is physical location around the world where AWS clusters data centers',
            'An AWS Local Zone location is an extension of an AWS Region',
            'An AWS wavelength zone is an infrastructure deployment that embeds AWS compute and storage services within telecommunications providers\' data centers at the edge of the 5G network',
        ),
        'incorrect': (
            'An Availability Zone consists of two or more Regions',
            'An Availability Zone consists of a single Region',
            'A Region is virtual location around the world where AWS clusters data centers',
            'An AWS Local Zone consists of two or more Availability zones',
        ),
    },
    'Actions performed with AWS': {
        'question_with_0':'Which action can you perform with PLACEHOLDER?',
        'question_with_1':'Which factor of selecting a region is the following related to: PLACEHOLDER',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            (['AWS Command Line Interface','AWS CLI'],'Automate actions for AWS services and applications through scripts'),
            ('AWS Management Console','Access wizards and automated workflows to perform tasks in AWS services'),
            (['Software development kits','SDKs'],'Develop AWS applications in supported programming languages'),
            ('AWS Outposts','Extend AWS infrastructure and services to your on-premises data center'),
            ('Elastic Beanstalk', ['Adjust capacity','Load balancing','Automatic scaling','Application health monitoring'])
        ),
        'fillers': ()
    },


    
    
}


"""


Which action can you perform in

provisioning
('AWS Management Console','a web-based interface for accessing and managing AWS services. You can quickly access recently used services and search for other services by name, keyword, or acronym. The console includes wizards and automated workflows that can simplify the process of completing tasks. You can also use the AWS Console mobile application to perform tasks such as monitoring resources, viewing alarms, and accessing billing information. Multiple identities can stay logged into the AWS Console mobile app at the same time.'),
('AWS Command Line Interface (AWS CLI)',' enables you to control multiple AWS services directly from the command line within one tool. AWS CLI is available for users on Windows, macOS, and Linux. By using AWS CLI, you can automate the actions that your services and applications perform through scripts. For example, you can use commands to launch an Amazon EC2 instance, connect an Amazon EC2 instance to a specific Auto Scaling group, and more.'
('software development kits (SDKs)','make it easier for you to use AWS services through an API designed for your programming language or platform. SDKs enable you to use AWS services with your existing applications or create entirely new applications that will run on AWS. To help you get started with using SDKs, AWS provides documentation and sample code for each supported programming language. Supported programming languages include C++, Java, .NET, and more'),
('AWS Elastic Beanstalk','you provide code and configuration settings, and Elastic Beanstalk deploys the resources necessary to perform the following tasks:

Adjust capacity
Load balancing
Automatic scaling
Application health monitoring'),
('AWS CloudFormation','you can treat your infrastructure as code. This means that you can build an environment by writing lines of code instead of using the AWS Management Console to individually provision resources.AWS CloudFormation provisions your resources in a safe, repeatable manner, enabling you to frequently build your infrastructure and applications without having to perform manual actions. It determines the right operations to perform when managing your stack and rolls back changes automatically if it detects errors'),
('',''),
('',''),
('',''),
('',''),






 

The other response options are incorrect because:

The AWS Command Line Interface (AWS CLI) is used to automate actions for AWS services and applications through scripts.
The AWS Management Console includes wizards and workflows that you can use to complete tasks in AWS services.
Software development kits (SDKs) enable you to develop AWS applications in supported programming languages.

actions ve descriptions

"""