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
    'AWS_monitoring_and_analytics_services': {
        'question_with_0':'Which isPOSNEG a description of PLACEHOLDER?',
        'question_with_1':'Which of the following is described by this: PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            ('AWS Cloudwatch',['includes a dashboard feature which enables you to access all the metrics for your resources from a single location','a web service that enables you to monitor and manage various metrics and configure alarm actions based on data from those metrics','uses metrics to represent the data points for your resources','AWS services send metrics here','create graphs automatically that show how performance has changed over time']),
            ('CloudWatch alarms','automatically perform actions if the value of a metric has gone above or below a predefined threshold'),
            ('CloudWatch dashboard',['enables you to access all the metrics for your resources from a single location']),
            ('AWS CloudTrail',['records API calls for your account','records the identity of the API caller, the time of the API call, the source IP address of the API caller, and more','a log of actions','view a complete history of user activity and API calls for your applications and resources','Events are typically updated within 15 minutes after an API call','filter by specifying the time and date that an API call occurred, the user who requested the action, the type of resource that was involved in the API call, and more']),
            ('CloudTrail Insights',['an optional CloudTrail feature','allows automatic detection of unusual API activities in your AWS account']),
            ('AWS Trusted Advisor',['inspects your AWS environment and provides real-time recommendations in accordance with AWS best practices','compares its findings to AWS best practices in five categories','offers a list of recommended actions and additional resources to learn more about AWS best practices']),
            ('AWS Trusted Advisor dashboard','review completed checks for cost optimization, performance, security, fault tolerance, and service limits'),
        ),
        'fillers': ()
    },
    "AWS_cloudwatch":{
        'question':'Which of the following is PLACEHOLDER true about Cloudwatch and its features?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            "can automatically stop an Amazon EC2 instance when the CPU utilization percentage has remained below a certain threshold for a specified period",
            "can send an alert when an alarm is triggered",
            'includes a dashboard feature which enables you to access all the metrics for your resources from a single location',
            'a web service that enables you to monitor and manage various metrics and configure alarm actions based on data from those metrics',
            'uses metrics to represent the data points for your resources',
            'AWS services send metrics here',
            'create graphs automatically that show how performance has changed over time',
            'automatically perform actions if the value of a metric has gone above or below a predefined threshold',
            'enables you to access all the metrics for your resources from a single location'
        ),

        'incorrect': (
            f"{choice(['cost optimization','performance','security','fault tolerance','service limits'])} is a Trusted Advisor category",
            f"offers {choice(['a list of recommended actions','additional resources to learn more about AWS best practices'])}",
            f"completed checks for {choice(['cost optimization','performance','security','fault tolerance','service limits'])} are available on the dashboard",
            "green checks here indicate the number of items for which no problem was detected",
            "orange triangle indicates the number of recommended investigations",
            "the red circle here represents the number of recommended actions",
            'records API calls for your account',
            'records the identity of the API caller, the time of the API call, the source IP address of the API caller, and more',
            'a log of actions',
            'view a complete history of user activity and API calls for your applications and resources',
            'events are typically updated within 15 minutes after an API call',
            'filter by specifying the time and date that an API call occurred, the user who requested the action, the type of resource that was involved in the API call, and more',
            'has an optional feature which allows automatic detection of unusual API activities in your AWS account',
        )
    },
    "AWS_cloudtrail":{
        'question':'Which of the following is PLACEHOLDER true about CloudTrail and its features?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            'records API calls for your account',
            'records the identity of the API caller, the time of the API call, the source IP address of the API caller, and more',
            'provides a log of actions',
            'allows you to view a complete history of user activity and API calls for your applications and resources',
            'events are typically updated within 15 minutes after an API call',
            'can filter by specifying the time and date that an API call occurred, the user who requested the action, the type of resource that was involved in the API call, and more',
            'has an optional feature which allows automatic detection of unusual API activities in your AWS account',
        ),

        'incorrect': (
            f"{choice(['cost optimization','performance','security','fault tolerance','service limits'])} is a Trusted Advisor category",
            f"offers {choice(['a list of recommended actions','additional resources to learn more about AWS best practices'])}",
            f"completed checks for {choice(['cost optimization','performance','security','fault tolerance','service limits'])} are available on the dashboard",
            "green checks here indicate the number of items for which no problem was detected",
            "orange triangle here indicate the number of recommended investigations",
            "the red circle here represents the number of recommended actions",
            "can automatically stop an Amazon EC2 instance when the CPU utilization percentage has remained below a certain threshold for a specified period",
            "can send an alert when an alarm is triggered",
            'includes a dashboard feature which enables you to access all the metrics for your resources from a single location',
            'a web service that enables you to monitor and manage various metrics and configure alarm actions based on data from those metrics',
            'uses metrics to represent the data points for your resources',
            'AWS services send metrics here',
            'create graphs automatically that show how performance has changed over time',
            'automatically perform actions if the value of a metric has gone above or below a predefined threshold',
            'enables you to access all the metrics for your resources from a single location'
            
        )


    
    },
    "Trusted_advisor_categories_and_dashboard":{
        'question':'Regarding Trusted Advisor, which of the following is PLACEHOLDER true?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'',
        'negative':'not',
        'course_code':'',
        'correct':(
            f"{choice(['cost optimization','performance','security','fault tolerance','service limits'])} is a Trusted Advisor category",
            f"Trusted Advisor offers {choice(['a list of recommended actions','additional resources to learn more about AWS best practices'])}",
            f"completed checks for {choice(['cost optimization','performance','security','fault tolerance','service limits'])} are available on the Trusted Advisor dashboard",
            "the dashboard is accessed through the AWS Management Console",
            "green checks indicate the number of items for which no problem was detected",
            "orange triangle indicates the number of recommended investigations",
            "the red circle represents the number of recommended actions",
        ),

        'incorrect': (
            
            f"{choice(['performance optimization','implementation','cost savings','elastic load','instance runtime'])} is a Trusted Advisor category",
            f"offers {choice(['automatic adjustment of spending','alarms triggered by metrics', 'a way to track API activity'])}",
            f"completed checks for {choice(['performance optimization','implementation','cost savings','elastic load','instance runtime'])} are available on the Trusted Advisor dashboard",
            "the dashboard is accessed through the AWS CLI",
            f"{choice(['red', 'orange'])} {choice(['checks', 'triangles', 'circles'])} indicates the number of items for which no problem was detected",
            f"{choice(['red', 'green'])} {choice(['checks', 'triangles', 'circles'])} indicates the number of recommended investigations",
            f"the {choice(['green', 'orange'])} {choice(['check', 'triangle', 'circle'])} represents the number of recommended actions",
            "can automatically stop an Amazon EC2 instance when the CPU utilization percentage has remained below a certain threshold for a specified period",
            "can send an alert when an alarm is triggered",
            'includes a dashboard feature which enables you to access all the metrics for your resources from a single location',
            'a web service that enables you to monitor and manage various metrics and configure alarm actions based on data from those metrics',
            'uses metrics to represent the data points for your resources',
            'AWS services send metrics here',
            'create graphs automatically that show how performance has changed over time',
            'automatically perform actions if the value of a metric has gone above or below a predefined threshold',
            'enables you to access all the metrics for your resources from a single location',
            'records API calls for your account',
            'records the identity of the API caller, the time of the API call, the source IP address of the API caller, and more',
            'a log of actions',
            'view a complete history of user activity and API calls for your applications and resources',
            'events are typically updated within 15 minutes after an API call',
            'filter by specifying the time and date that an API call occurred, the user who requested the action, the type of resource that was involved in the API call, and more',
            'has an optional feature which allows automatic detection of unusual API activities in your AWS account',                       
        )
    },
}