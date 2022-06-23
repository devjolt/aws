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

    'pillars_of_AWS_Well-Architectured_Framework': {
        'question':'Which of the following is PLACEHOLDER a pillar of the AWS Well-Architectured Framework?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'Operational Excellence',
            'Security',
            'Reliability',
            'Performance Efficiency',
            'Cost Optimisation'
        ),
        'incorrect': (
            'Operational Security',
            'Security Excellence',
            'Efficiency',
            'Performance Reliability',
            'Performance Optimisation'
            'Performance Excellence'
            'Performance security'
            'Excellence',
            'Efficiency',
            'Cost',
            'Optimisation',
            'Operational Performance'
            'Operational Efficiency',
            'Operational Cost',
            'Optimisation',
            'Performance',
            'Security Excellence',
            'Security Efficiency',
            'Security Cost',
            'Reliability Excellence',
            'Reliability Efficiency',
            'Reliability Cost',
        ),
    },
    'AWS_Well-Architectured_Framework_concepts': {
        'question_with_0':'Which isPOSNEG a description of the PLACEHOLDER pillar of the AWS Well-Architectured Framework?',
        'question_with_1':'Which Pillar of the AWS Well-Architectured Framework is described by this: PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            ('Operational Excellence',['the ability to run workloads effectively and gain insights into their operations','focuses on running and monitoring systems to deliver business value','continually improving processes and procedures','automating changes with deployment pipelines','responding to events that are triggered']),
            ('Security',['priority number 1 at AWS','checking integrity of data and, for example, protecting systems by using encryption']),
            ('Reliability',['ability of a workload to consistently and correctly perform its intended functions','recovery planning','recovery from an Amazon DynamoDB disruption','recovery from EC2 node failure','how you handle change to meet business and customer demand']),
            ('Performance Efficiency',['using computing resources efficiently to meet system requirements and to maintain that efficiency as demand changes and technologies evolve','using IT and computing resources efficiently','using the right Amazon EC2 type, based on workload and memory requirements','making informed decisions, to maintain efficiency as business needs evolve']),
            ('Cost Optimisation',['ability to run systems to deliver business value at the lowest price point','optimizing full cost','controlling where money is spent','checking if you have overestimated your EC2 server size']),
        ),
        'fillers': (
            ([
            'Operational Security',
            'Security Excellence',
            'Efficiency',
            'Performance Reliability',
            'Performance Optimisation'
            'Performance Excellence'
            'Performance security'
            'Excellence',
            'Efficiency',
            'Cost',
            'Optimisation',
            'Operational Performance'
            'Operational Efficiency',
            'Operational Cost',
            'Optimisation',
            'Performance',
            'Security Excellence',
            'Security Efficiency',
            'Security Cost',
            'Reliability Excellence',
            'Reliability Efficiency',
            'Reliability Cost'
            ],'predicting resource needs in advance'
            )
        )
    },
    "Advantages_of_cloud_computing":{
        'question':'Which of the following is PLACEHOLDER an advantage of cloud computing?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'trade upfront expense for variable expense',
            'benefit from massive economies of scale',
            'stop guessing capacity',
            'increase speed and agility',
            'stop spending money running and maintaining data centers',
            'go global in minutes'
        ),
        'incorrect': (
            'increased security',
            'stop spending money on online storage',
            'stop guessing server uptime',
            'benefit from increased security',
            'benefit from increased storage capacity',
            'benefit from increase compute power',
            'develop apps in minutes',
            'trade compute power for convenience',
            'trade upfront expense for more security',
            'go serverless in minutes',
            'go online in minutes',
            'stop spending money on third party apps'
        ),
    },
    'Matching_advantages_of_cloud_computing': {
        'question_with_0':'Considering the advantages of could computing, which POSNEG to the following: PLACEHOLDER',
        'question_with_1':'Which advantage of cloud computing applies to the following: PLACEHOLDER?',
        'positive_negative':('applies','does not apply to'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            ('trade upfront expense for variable expense','you can pay only when you consume computing resources'),
            ('benefit from massive economies of scale',['ower pay-as-you-go prices as the result of AWS customers\'s aggregated usage of services','lower pay-as-you-go prices','usage from hundreds of thousands of customers aggregating in the cloud']),
            ('stop guessing capacity',['you don’t have to predict how much infrastructure capacity you will need before deploying an application','pay only for the compute time you use','you can access only the capacity that you need','scale in or out in response to demand']),
            ('increase speed and agility','development teams with more time to experiment and innovate'),
            ('stop spending money running and maintaining data centers','focus less on infrastructure and more on your applications and customers'),
            ('go global in minutes',['deploying an application in multiple Regions around the world','low latency for all customers','deployment to customers around the world']),
        ),
        'fillers': ()
    },
    

}

"""

    

Trade upfront expense for variable expense.
Benefit from massive economies of scale.
Stop guessing capacity.
Increase speed and agility.
Stop spending money running and maintaining data centers.
Go global in minutes.
"""