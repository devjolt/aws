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
    'AWS_networking_concepts': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'"PLACEHOLDER" best describes:',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('AWS Direct Connect',['a service that enables you to establish a dedicated private connection between your data center and VPC','helps you to reduce network costs and increase the amount of bandwidth that can travel through your network']),
            ('Amazon CloudFront',['a content delivery service','uses a network of edge locations to cache content and deliver content to customers all over the world']),
            ('virtual private gateway',['enables you to establish a virtual private network (VPN) connection between your VPC and a private network, such as an on-premises data center or internal corporate network','allows traffic into the VPC only if it is coming from an approved network']),
            ('internet gateway',['a connection between a VPC and the internet','allows public traffic from the internet to access a VPC']),
            (['Amazon Virtual Private Cloud', 'Amazon VPC'], ['establish boundaries around your AWS resources','enables you to provision an isolated section of the AWS Cloud','launch resources in a virtual network that you define']),
            ('subnet','section of a VPC that can contain resources such as Amazon EC2 instances'),

        ),
        'fillers': ()
    },
    'Networking_on_AWS': {
        'question_with_0':'Which best describes "PLACEHOLDER"?',
        'question_with_1':'"PLACEHOLDER" best describes:',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('Public subnets','contain resources that need to be accessible by the public, such as an online store\'s website'),
            ('Private subnets','contain resources that should be accessible only through your private network, such as a database that contains customers\' personal information and order histories'),
            ('virtual private gateway',['enables you to establish a virtual private network (VPN) connection between your VPC and a private network, such as an on-premises data center or internal corporate network','allows traffic into the VPC only if it is coming from an approved network']),
            (['Amazon Virtual Private Cloud', 'Amazon VPC'], ['where subnets can communicate with each other','establish boundaries around your AWS resources','enables you to provision an isolated section of the AWS Cloud','launch resources in a virtual network that you define']),
            ('subnet','section of a VPC that can contain resources such as Amazon EC2 instances'),
            ('packet','unit of data sent over the internet or a network'),
            (['Network access control list','ACL'],['perform stateless packet filtering','have an explicit deny rule','a virtual firewall that controls inbound and outbound traffic at the subnet level','included by default in each AWS account'])

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
    'Networking':{
        'type':'auto_correct_incorrect',
        'verbs':('are', 'can', 'does', 'is'),
        'negator':'not',
        'correct':(
            'Public subnets are accessible to the public',
            'Private subnets are not accessible to the public',
            'Resources on private subnets are only accessible though your private network',
            'Resources on a VPC can communicate with each other by default',
            'Each AWS account does include a default network ACL',
            'By default, an account\'s default network ACL does allow all inbound and outbound traffic',
            'A default network ACL can be modified with custom rules',
            'A custom network does not allow inbound or outbound traffic by default',
            'There is an explicit deny rule by default for all network ACLS',
            'Stateless packet filtering is performed by Network ACLs',
            'Network ACLs are stateless',
            'Security Groups are not stateless',
            'Network ACLs are not stateful',
            'Security Groups are stateful',
            'Security Groups can be associated with multiple Amazon EC2 instances'
        )
    },
    'Network_security': {
        'question_with_0':'Which best describes PLACEHOLDER?',
        'question_with_1':'PLACEHOLDER best describes:',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('Public subnets','contain resources that need to be accessible by the public, such as an online store\'s website'),
            ('Private subnets','contain resources that should be accessible only through your private network, such as a database that contains customers\' personal information and order histories'),
            ('virtual private gateway',['enables you to establish a virtual private network (VPN) connection between your VPC and a private network, such as an on-premises data center or internal corporate network','allows traffic into the VPC only if it is coming from an approved network']),
            (['Amazon Virtual Private Cloud', 'Amazon VPC'], ['where subnets can communicate with each other','establish boundaries around your AWS resources','enables you to provision an isolated section of the AWS Cloud','launch resources in a virtual network that you define']),
            ('Default Network access control list',['allows all inbound and outbound traffic by default','a virtual firewall that controls inbound and outbound traffic at the subnet level','included by default in each AWS account']),
            ('Custom Network access control list','deny all inbound and outbound traffic by default'),
            ('Security groups', ['virtual firewall which controlls inbound and outbound traffic for an Amazon EC2 instance', 'denies all inbound traffic', 'allows all outbound traffic', 'can be associated with mutliple Amazon EC2 instances', 'performs stateful packet filtering'])
        ),
        'fillers': ()
    },
    'Security_groups':{
        'type':'auto_correct_incorrect',
        'verbs':('are', 'can', 'does', 'is'),
        'negator':'not',
        'correct':(
            'A security group is a virtual firewall which controlls inbound and outbound traffic for an Amazon EC2 instance',
            'A security group is not the same as a an ACL',
            'By default, a security group does deny all inbound traffic', 
            'By default, a security group does not allow all inbound traffic', 
            'By default, a security group does not deny all outbound traffic', 
            'By default, a security group does allow all outbound traffic', 
            'A security group can be associated with mutliple Amazon EC2 instances', 
            'A security group does perform stateful packet filtering',
            'A security group does not perform stateless packet filtering',
        )
    },
    'VPC_components': {
        'question_with_0':'What is done by PLACEHOLDER?',
        'question_with_1':'Which VPC component would perform the following: PLACEHOLDER',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            ('AWS Direct Connect','Establish a dedicated connection between the on-premises data center and the VPC'),
            ('Public subnet','Support the customer-facing website'),
            ('Private subnet','Isolate databases containing customers\' personal information'),
            ('virtual private gateway','Create a VPN connection between the VPC and the internal corporate network'),
        ),
        'fillers': ()
    },
    'Global_networking_terms': {
        'question_with_0':'What is done by PLACEHOLDER?',
        'question_with_1':'Which VPC component would perform the following:',
        'type':['new_pairs'],
        'course_code':'',
        'pairs':(
            (['Domain Name System','DNS'],'reloves a domain name to an IP address'),
            ('Amazon Route 53',['Connect user requests to infrastructure in AWS and outside of AWS','Manage DNS records for domain names']),
            ('Private subnet','Isolate databases containing customers\' personal information'),
            ('virtual private gateway','Create a VPN connection between the VPC and the internal corporate network'),
            
        ),
        'fillers': ()
    },

    





}


"""
Your company has an application that uses Amazon EC2 instances to run the customer-facing website and Amazon RDS database instances to store customers’ personal information. How should the developer configure the VPC according to best practices?

Place the Amazon EC2 instances in a private subnet and the Amazon RDS database instances in a public subnet.

Incorrectly selected
Place the Amazon EC2 instances in a public subnet and the Amazon RDS database instances in a private subnet.

Incorrectly unselected
Place the Amazon EC2 instances and the Amazon RDS database instances in a public subnet.

Correctly unselected
Place the Amazon EC2 instances and the Amazon RDS database instances in a private subnet.




"""