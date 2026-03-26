# #Extra Linebreak Remover

# a=r"""
# Analytics

# Application Integration

# AWS Cost Management

# Compute

# Containers

# Database

# Developer Tools

# Front-End Web and Mobile

# Machine Learning

# Management and Governance

# Media Services

# Migration and Transfer

# Networking and Content Delivery

# Security, Identity, and Compliance

# Serverless

# Storage

# Analytics

# Amazon Athena

# AWS Data Exchange

# Amazon Data Firehose

# Amazon EMR

# AWS Glue

# Amazon Kinesis

# AWS Lake Formation

# Amazon Managed Streaming for Apache Kafka (Amazon MSK)

# Amazon OpenSearch Service

# Amazon QuickSuite

# Amazon Redshift

# Application Integration

# Amazon AppFlow

# AWS AppSync

# Amazon EventBridge

# Amazon MQ

# Amazon SNS

# Amazon SQS

# AWS Step Functions

# AWS Cost Management

# AWS Budgets

# AWS Cost and Usage Report

# AWS Cost Explorer

# Savings Plans

# Compute

# AWS Batch

# Amazon EC2

# Amazon EC2 Auto Scaling

# AWS Elastic Beanstalk

# AWS Outposts

# AWS Serverless Application Repository

# VMware Cloud on AWS

# AWS Wavelength

# Containers

# Amazon ECR

# Amazon ECS

# Amazon ECS Anywhere

# Amazon EKS

# Amazon EKS Anywhere

# Amazon EKS Distro

# Database

# Amazon Aurora

# Amazon Aurora Serverless

# Amazon Document DB

# Amazon DynamoDB

# Amazon Elastic Cache

# Amazon Key spaces

# Amazon Neptune

# Amazon RDS

# Amazon Redshift

# Developer Tools

# AWS X-Ray

# Front-End Web and Mobile

# AWS Amplify

# Amazon API Gateway

# AWS Device Farm

# Machine Learning

# Amazon Comprehend

# Amazon Kendra

# Amazon Lex

# Amazon Polly

# Amazon Rekognition

# Amazon Sage Maker AI

# Amazon Textract

# Amazon Transcribe

# Amazon Translate

# Management and Governance

# AWS Auto Scaling

# AWS CLI

# AWS CloudFormation

# AWS CloudTrail

# Amazon CloudWatch

# AWS Compute Optimizer

# AWS Config

# AWS Control Tower

# AWS Health Dashboard

# AWS License Manager

# Amazon Managed Grafana

# Amazon Managed Service for Prometheus

# AWS Management Console

# AWS Organizations

# AWS Service Catalog

# AWS Systems Manager

# AWS Trusted Advisor

# AWS Well-Architected Tool

# Media Services

# Amazon Elastic Transcoder

# Amazon Kinesis Video Streams

# Migration and Transfer

# AWS Application Migration Service

# AWS Data Sync

# AWS DMS

# AWS Snow Family

# AWS Transfer Family

# Networking and Content Delivery

# AWS Client VPN

# Amazon CloudFront

# AWS Direct Connect

# Elastic Load Balancing (ELB)

# AWS Global Accelerator

# AWS Private Link

# Amazon Route 53

# AWS Site-to-Site VPN

# AWS Transit Gateway

# Amazon VPC

# Security, Identity, and Compliance

# AWS Artifact

# AWS Audit Manager

# AWS Certificate Manager (ACM)

# AWS Cloud HSM

# Amazon Cognito

# Amazon Detective

# AWS Directory Service

# AWS Firewall Manager

# Amazon Guard Duty

# AWS IAM Identity Center

# Amazon Inspector

# AWS KMS

# Amazon Macie

# AWS Network Firewall

# AWS Resource Access Manager (AWS RAM)

# AWS Secrets Manager

# AWS Security Hub

# AWS Shield

# AWS WAF

# IAM

# Serverless

# AWS AppSync

# AWS Far gate

# AWS Lambda

# Storage

# AWS Backup

# Amazon EBS

# Amazon EFS

# Amazon FSx (for all types)

# Amazon S3

# Amazon S3 Glacier

# AWS Storage Gateway
# """

# a=a.split("\n")
# # print(a)
# temp=""
# for i in range(0,len(a)):
#     if a[i]!="":
#         temp=temp+"\n"+a[i]

# print(temp)


#Preprocessing for Broad Classification list

# a=r"""Analytics
# Amazon Athena
# AWS Data Exchange
# Amazon Data Firehose
# Amazon EMR
# AWS Glue
# Amazon Kinesis
# AWS Lake Formation
# Amazon Managed Streaming for Apache Kafka (Amazon MSK)
# Amazon OpenSearch Service
# Amazon QuickSuite
# Amazon Redshift

# Application Integration
# Amazon AppFlow
# AWS AppSync
# Amazon EventBridge
# Amazon MQ
# Amazon SNS
# Amazon SQS
# AWS Step Functions

# AWS Cost Management
# AWS Budgets
# AWS Cost and Usage Report
# AWS Cost Explorer
# Savings Plans

# Compute
# AWS Batch
# Amazon EC2
# Amazon EC2 Auto Scaling
# AWS Elastic Beanstalk
# AWS Outposts
# AWS Serverless Application Repository
# VMware Cloud on AWS
# AWS Wavelength

# Containers
# Amazon ECR
# Amazon ECS
# Amazon ECS Anywhere
# Amazon EKS
# Amazon EKS Anywhere
# Amazon EKS Distro

# Database
# Amazon Aurora
# Amazon Aurora Serverless
# Amazon Document DB
# Amazon DynamoDB
# Amazon Elastic Cache
# Amazon Key spaces
# Amazon Neptune
# Amazon RDS
# Amazon Redshift

# Developer Tools
# AWS X-Ray

# Front-End Web and Mobile
# AWS Amplify
# Amazon API Gateway
# AWS Device Farm

# Machine Learning
# Amazon Comprehend
# Amazon Kendra
# Amazon Lex
# Amazon Polly
# Amazon Rekognition
# Amazon Sage Maker AI
# Amazon Textract
# Amazon Transcribe
# Amazon Translate

# Management and Governance
# AWS Auto Scaling
# AWS CLI
# AWS CloudFormation
# AWS CloudTrail
# Amazon CloudWatch
# AWS Compute Optimizer
# AWS Config
# AWS Control Tower
# AWS Health Dashboard
# AWS License Manager
# Amazon Managed Grafana
# Amazon Managed Service for Prometheus
# AWS Management Console
# AWS Organizations
# AWS Service Catalog
# AWS Systems Manager
# AWS Trusted Advisor
# AWS Well-Architected Tool

# Media Services
# Amazon Elastic Transcoder
# Amazon Kinesis Video Streams

# Migration and Transfer
# AWS Application Migration Service
# AWS Data Sync
# AWS DMS
# AWS Snow Family
# AWS Transfer Family

# Networking and Content Delivery
# AWS Client VPN
# Amazon CloudFront
# AWS Direct Connect
# Elastic Load Balancing (ELB)
# AWS Global Accelerator
# AWS Private Link
# Amazon Route 53
# AWS Site-to-Site VPN
# AWS Transit Gateway
# Amazon VPC

# Security, Identity, and Compliance
# AWS Artifact
# AWS Audit Manager
# AWS Certificate Manager (ACM)
# AWS Cloud HSM
# Amazon Cognito
# Amazon Detective
# AWS Directory Service
# AWS Firewall Manager
# Amazon Guard Duty
# AWS IAM Identity Center
# Amazon Inspector
# AWS KMS
# Amazon Macie
# AWS Network Firewall
# AWS Resource Access Manager (AWS RAM)
# AWS Secrets Manager
# AWS Security Hub
# AWS Shield
# AWS WAF
# IAM

# Serverless
# AWS AppSync
# AWS Far gate
# AWS Lambda

# Storage
# AWS Backup
# Amazon EBS
# Amazon EFS
# Amazon FSx (for all types)
# Amazon S3
# Amazon S3 Glacier
# AWS Storage Gateway
# """

# temp=[]
# temp1=[]

# a=a.split("\n")
# # print(a)
# i=0

# while i < len(a)-3:
    

#     if a[i]!="":
#         temp.append(a[i])
#         i=i+1

#     elif a[i]=="":
#         temp.append(a[i])
#         temp1.append(a[i+1])
#         i=i+2

# print(temp1)
# print(temp)



#Key List Generator

a=['Analytics', 'Application Integration', 'AWS Cost Management', 'Compute', 'Containers', 'Database', 'Developer Tools', 'Front-End Web and Mobile', 'Machine Learning', 'Management and Governance', 'Media Services', 'Migration and Transfer', 'Networking and Content Delivery', 'Security, Identity, and Compliance', 'Serverless', 'Storage']

b=['Amazon Athena', 'AWS Data Exchange', 'Amazon Data Firehose', 'Amazon EMR', 'AWS Glue', 'Amazon Kinesis', 'AWS Lake Formation', 'Amazon Managed Streaming for Apache Kafka (Amazon MSK)', 'Amazon OpenSearch Service', 'Amazon QuickSuite', 'Amazon Redshift', '', 'Amazon AppFlow', 'AWS AppSync', 'Amazon EventBridge', 'Amazon MQ', 'Amazon SNS', 'Amazon SQS', 'AWS Step Functions', '', 'AWS Budgets', 'AWS Cost and Usage Report', 'AWS Cost Explorer', 'Savings Plans', '', 'AWS Batch', 'Amazon EC2', 'Amazon EC2 Auto Scaling', 'AWS Elastic Beanstalk', 'AWS Outposts', 'AWS Serverless Application Repository', 'VMware Cloud on AWS', 'AWS Wavelength', '', 'Amazon ECR', 'Amazon ECS', 'Amazon ECS Anywhere', 'Amazon EKS', 'Amazon EKS Anywhere', 'Amazon EKS Distro', '', 'Amazon Aurora', 'Amazon Aurora Serverless', 'Amazon Document DB', 'Amazon DynamoDB', 'Amazon Elastic Cache', 'Amazon Key spaces', 'Amazon Neptune', 'Amazon RDS', 'Amazon Redshift', '', 'AWS X-Ray', '', 'AWS Amplify', 'Amazon API Gateway', 'AWS Device Farm', '', 'Amazon Comprehend', 'Amazon Kendra', 'Amazon Lex', 'Amazon Polly', 'Amazon Rekognition', 'Amazon Sage Maker AI', 'Amazon Textract', 'Amazon Transcribe', 'Amazon Translate', '', 'AWS Auto Scaling', 'AWS CLI', 'AWS CloudFormation', 'AWS CloudTrail', 'Amazon CloudWatch', 'AWS Compute Optimizer', 'AWS Config', 'AWS Control Tower', 'AWS Health Dashboard', 'AWS License Manager', 'Amazon Managed Grafana', 'Amazon Managed Service for Prometheus', 'AWS Management Console', 'AWS Organizations', 'AWS Service Catalog', 'AWS Systems Manager', 'AWS Trusted Advisor', 'AWS Well-Architected Tool', '', 'Amazon Elastic Transcoder', 'Amazon Kinesis Video Streams', '', 'AWS Application Migration Service', 'AWS Data Sync', 'AWS DMS', 'AWS Snow Family', 'AWS Transfer Family', '', 'AWS Client VPN', 'Amazon CloudFront', 'AWS Direct Connect', 'Elastic Load Balancing (ELB)', 'AWS Global Accelerator', 'AWS Private Link', 'Amazon Route 53', 'AWS Site-to-Site VPN', 'AWS Transit Gateway', 'Amazon VPC', '', 'AWS Artifact', 'AWS Audit Manager', 'AWS Certificate Manager (ACM)', 'AWS Cloud HSM', 'Amazon Cognito', 'Amazon Detective', 'AWS Directory Service', 'AWS Firewall Manager', 'Amazon Guard Duty', 'AWS IAM Identity Center', 'Amazon Inspector', 'AWS KMS', 'Amazon Macie', 'AWS Network Firewall', 'AWS Resource Access Manager (AWS RAM)', 'AWS Secrets Manager', 'AWS Security Hub', 'AWS Shield', 'AWS WAF', 'IAM', '', 'AWS AppSync', 'AWS Far gate', 'AWS Lambda', '', 'AWS Backup', 'Amazon EBS', 'Amazon EFS', 'Amazon FSx (for all types)', 'Amazon S3']

# counter=0
# for i in range(0,len(b)):
#     if b[i]=="":
#         counter=counter+1

# print(counter)
# print(len(a))

# counter=0
# temp=[]

# for i in range(0,len(b)):
#     if b[i]=="":
#         counter=counter+1
#     else :
#         temp.append(counter)

# print(a)
# print(temp)

