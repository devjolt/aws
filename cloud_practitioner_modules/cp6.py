from random import choice

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

    "Responsibilites_of_customers_and_AWS":{
        'question':'Which of the following is the responsibility of PLACEHOLDER?',
        'type':['multi_option_from_correct_incorrect', 'make_items_question_from_correct_incorrect'],
        'positive':'the customer',
        'negative':'AWS',
        'course_code':'',
        'correct':(
            "customer data",
            "platform",
            'applications',
            'identity and access management',
            "patching software",
            "operating system configuration",
            "network configuration",
            "firewall configuration",
            'client-side data encryption',
            'server-side encryption',
            "configuring security groups",
            'networking traffic protection',
            'setting permission for Amazon S3 objects',     
        ),
        'incorrect': (
            "physical security at data centers",
            "maintaining serves that run EC2 instances",
            "software",
            "compute",
            "security of the cloud",
            "storage",
            "database",
            "the network",
            'hardware',
            'global infrastructure',
            'virtualization infrastructure',
            'regions',
            'availability zones',
            'edge locations',
        )
    },
    'User_permission_and_access': {
        'question_with_0':'Which isPOSNEG a description of PLACEHOLDER?',
        'question_with_1':'Which of the following is described by this: PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            (['AWS Identity and Access Management', 'IAM'],['enables you to manage access to AWS services and resources securely','gives you the flexibility to configure access based on your company’s specific operational and security needs']),
            ('AWS accound root user',['should not be used for every day tasks','has complete access to all the AWS services and resources in the account','accessed by signing in with the email address and password that you used to create your AWS account','when you first create an AWS account, you begin with this','']),
            ('IAM user',['an identity that you create in AWS','represents the person or application that interacts with AWS services and resources','consists of a name and credentials','has no permissions associated with it by default','must be granted necessary permissions to perform specific actions', 'one should be created for each person who needs AWS access', 'each should have a unique set of security credentials']),
            ('IAM policy',['a document that allows or denies permissions to AWS services and resources','principle of least privilege should be followed']),
            ('IAM groups',['a collection of IAM users','can be assigned an IAM policy','']),
            ('IAM roles',['an identity that you can assume to gain temporary access to permissions','an IAM user, application or service can have this','permission is required for an entity to change this','when this changes, previous permissions are abandoned', 'used when access to services or resources needs to be granted temporarily, instead of long-term']),
            (['MFA','Multi-factor authentication'],['provides an extra layer of security for an AWS account', 'involves providing a password and a second form of authentication']),
            ('AWS Organizations',['features consolidated billing','consolidate and manage multiple AWS accounts within a central location','automatically creates a root when one is creates']),
            (['service control policies','SCPs'],['enable you to place restrictions on the AWS services, resources, and individual API actions that users and roles in each account can access','can be applied to individual member accounts and organizational units','control permissions for the accounts in your organization']),
            ('Organizational units', ['make it easier to manage accounts with similar business or security requirements','accounts in this inherit applied policies','more easily isolate workloads or applications that have specific security requirements'])
        ),
        'fillers': ()
    },
    'Compliance': {
        'question_with_0':'Which isPOSNEG a description of PLACEHOLDER?',
        'question_with_1':'Which of the following is described by this: PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            ('AWS Artefact',['access documentation proving AWS follows best practices for security and compliance','gain access to compliance reports done by third parties who have validated a wide range of compliance standards, which you should read to ensure that you understand security and compliance with AWS','a service that provides on-demand access to AWS security and compliance reports and select online agreements','consists of two main sections']),
            ('AWS Artefact Agreements',['sign an agreement with AWS regarding your use of certain types of information throughout AWS services','you can review, accept, and manage agreements for an individual account and for all your accounts in AWS Organizations','types are offered to address the needs of customers who are subject to specific regulations, such as the Health Insurance Portability and Accountability Act (HIPAA)']),
            ('AWS Artefact Reports',['get more information about their responsibility for complying with certain regulatory standards','provide compliance reports from third-party auditors','remains up to date with the latest information released','can be provided to auditors or regulators as evidence of AWS security controls']),
            ('Customer Compliance Center',['contains resources to help you learn more about AWS compliance','read customer compliance stories to discover how companies in regulated industries have solved various compliance, governance, and audit challenges',f"access compliance whitepapers and documentation on {choice(['AWS answers to key compliance questions','an overview of AWS risk and compliance','an auditing security checklist'])}","includes an auditor learning path designed for individuals in auditing, compliance, and legal roles who want to learn more about how their internal operations can demonstrate compliance using the AWS Cloud"]),
        ),
        'fillers': ()
    },
    'Additional_defence': {
        'question_with_0':'Which isPOSNEG a description of PLACEHOLDER?',
        'question_with_1':'Which of the following is described by this: PLACEHOLDER?',
        'positive_negative':('',' not'),
        'type':['posneg_pairs', 'new_pairs'],
        'course_code':'',
        'pairs':(
            ('Denial of service attacks',['accessa deliberate attempt to make a website or application unavailable to users','attacker flooding a website or application with excessive network traffic until the targeted website or application becomes overloaded and is no longer able to respond']),
            ('Distributed denial of service attacks',['use multiple infected computers (also known as “bots”) to send excessive traffic to a website or application','multiple sources are used to start an attack that aims to make a website or application unavailable']),
            ('AWS Shield','a service that protects applications against DDoS attacks'),
            ('AWS Shield Standard',['automatically protects all AWS customers at no cost','protects your AWS resources from the most common, frequently occurring types of DDoS attacks','AWS Shield Standard uses a variety of analysis techniques to detect malicious traffic in real time and automatically mitigates it']),
            ('AWS Shield Advanced',['a paid service that provides detailed attack diagnostics and the ability to detect and mitigate sophisticated DDoS attacks',"integrates with Amazon CloudFront, Amazon Route 53, and Elastic Load Balancing",'integrates with AWS WAF by writing custom rules to mitigate complex DDoS attacks']),
            (['AWS Key Management Service','AWS KMS'],['enables you to perform encryption operations through the use of cryptographic keys','create, manage, and use cryptographic keys','control the use of keys across a wide range of services and in your applications','choose the specific levels of access control that you need for cryptographic keys','specify which IAM users and roles are able to manage keys','temporarily disable keys so that they are no longer in use by anyone','keys never leave here']),
            ('cryptographic key','random string of digits used for locking (encrypting) and unlocking (decrypting) data'),
            (['AWS Web Application Firewall','AWS WAF'],['lets you monitor network requests that come into your web applications','works together with Amazon CloudFront and an Application Load Balancer','blocks or allows traffic in a similar way to an ACL','uses a web access control list (ACL) to protect your AWS resources']),
            (['AWS Web Access Control List','ACL'],'contains a list of IP addresses to block', 'a list of rules describing permitted traffic'),
            ('Amazon Inspector',['helps to improve the security and compliance of applications by running automated security assessments','checks applications for security vulnerabilities and deviations from security best practices, such as open access to Amazon EC2 instances and installations of vulnerable software versions','provides you with a list of security findings','prioritizes security findings by severity level, including a detailed description of each security issue and a recommendation for how to fix it']),
            ('Amazon GuardDuty',['a service that provides intelligent threat detection for your AWS infrastructure and resources','identifies threats by continuously monitoring the network activity and account behavior within your AWS environment','monitors your network and account activity','after enabling, does not require deploying or managing any additional security software','continuously analyzes data from multiple AWS sources, including VPC Flow Logs and DNS logs','if any threats are detected, you can review detailed findings about them from the AWS Management Console','provides recommended steps for remediation','AWS Lambda functions can be configures to take remediation steps automatically in response to findings']),
        ),
        'fillers': ()
    },
}