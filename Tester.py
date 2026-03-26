#Randomization and Test Generation
import random
Categories=['Analytics', 'Application Integration', 'AWS Cost Management', 'Compute', 'Containers', 'Database', 'Developer Tools', 'Front-End Web and Mobile', 'Machine Learning', 'Management and Governance', 'Media Services', 'Migration and Transfer', 'Networking and Content Delivery', 'Security, Identity, and Compliance', 'Serverless', 'Storage']
Services=['Amazon Athena', 'AWS Data Exchange', 'Amazon Data Firehose', 'Amazon EMR', 'AWS Glue', 'Amazon Kinesis', 'AWS Lake Formation', 'Amazon Managed Streaming for Apache Kafka (Amazon MSK)', 'Amazon OpenSearch Service', 'Amazon QuickSuite', 'Amazon Redshift', '', 'Amazon AppFlow', 'AWS AppSync', 'Amazon EventBridge', 'Amazon MQ', 'Amazon SNS', 'Amazon SQS', 'AWS Step Functions', '', 'AWS Budgets', 'AWS Cost and Usage Report', 'AWS Cost Explorer', 'Savings Plans', '', 'AWS Batch', 'Amazon EC2', 'Amazon EC2 Auto Scaling', 'AWS Elastic Beanstalk', 'AWS Outposts', 'AWS Serverless Application Repository', 'VMware Cloud on AWS', 'AWS Wavelength', '', 'Amazon ECR', 'Amazon ECS', 'Amazon ECS Anywhere', 'Amazon EKS', 'Amazon EKS Anywhere', 'Amazon EKS Distro', '', 'Amazon Aurora', 'Amazon Aurora Serverless', 'Amazon Document DB', 'Amazon DynamoDB', 'Amazon Elastic Cache', 'Amazon Key spaces', 'Amazon Neptune', 'Amazon RDS', 'Amazon Redshift', '', 'AWS X-Ray', '', 'AWS Amplify', 'Amazon API Gateway', 'AWS Device Farm', '', 'Amazon Comprehend', 'Amazon Kendra', 'Amazon Lex', 'Amazon Polly', 'Amazon Rekognition', 'Amazon Sage Maker AI', 'Amazon Textract', 'Amazon Transcribe', 'Amazon Translate', '', 'AWS Auto Scaling', 'AWS CLI', 'AWS CloudFormation', 'AWS CloudTrail', 'Amazon CloudWatch', 'AWS Compute Optimizer', 'AWS Config', 'AWS Control Tower', 'AWS Health Dashboard', 'AWS License Manager', 'Amazon Managed Grafana', 'Amazon Managed Service for Prometheus', 'AWS Management Console', 'AWS Organizations', 'AWS Service Catalog', 'AWS Systems Manager', 'AWS Trusted Advisor', 'AWS Well-Architected Tool', '', 'Amazon Elastic Transcoder', 'Amazon Kinesis Video Streams', '', 'AWS Application Migration Service', 'AWS Data Sync', 'AWS DMS', 'AWS Snow Family', 'AWS Transfer Family', '', 'AWS Client VPN', 'Amazon CloudFront', 'AWS Direct Connect', 'Elastic Load Balancing (ELB)', 'AWS Global Accelerator', 'AWS Private Link', 'Amazon Route 53', 'AWS Site-to-Site VPN', 'AWS Transit Gateway', 'Amazon VPC', '', 'AWS Artifact', 'AWS Audit Manager', 'AWS Certificate Manager (ACM)', 'AWS Cloud HSM', 'Amazon Cognito', 'Amazon Detective', 'AWS Directory Service', 'AWS Firewall Manager', 'Amazon Guard Duty', 'AWS IAM Identity Center', 'Amazon Inspector', 'AWS KMS', 'Amazon Macie', 'AWS Network Firewall', 'AWS Resource Access Manager (AWS RAM)', 'AWS Secrets Manager', 'AWS Security Hub', 'AWS Shield', 'AWS WAF', 'IAM', '', 'AWS AppSync', 'AWS Far gate', 'AWS Lambda', '', 'AWS Backup', 'Amazon EBS', 'Amazon EFS', 'Amazon FSx (for all types)', 'Amazon S3']
Keys=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 15, 15, 15, 15, 15]


print("Length of Services List: "+str(len(Services)))
print("Length of Keys List: "+str(len(Keys)))

#Generate order of Questions (old)
# for i in range(0,len(Categories)):
#     flag=0
#     temp2=random.randint(1,15)
#     if i==0:
#         order.append(temp2)
#         flag=1
#     else :
#         for j in range(0,len(order)):
#             if temp2==order[j]:
#                 flag=1
#     if flag==0:
#         order.append(temp2)




#Generate order for Shuffled Questions and Shuffled Answers list
order=[]
for i in range(0,len(Services)):
    order.append(i)

print("Serial Generation Successful")

random.shuffle(order)

print("Order Generation Successful")


#Create Shuffled Questions Shuffled Answer list Based on order
Shuffled_Questions=[]
Shuffled_Answer=[]
for i in range(0,len(order)):
    index=order[i]
    Shuffled_Questions.append(Services[index])
    Shuffled_Answer.append(Keys[index])

print("Questions Shuffling Successful")
print("Answer Shuffling Successful")


#Create Unique Random Numbers and Shuffle to generate index for keys
display_list=[]
for i in range(0,len(order)):
    temp1=[]
    temp1.append(Shuffled_Questions[i])
    temp2=[]
    temp2.append(Shuffled_Answer[i])
    for j in range(0,10):
        if len(temp2)<=4:
            flag=0
            temp3=random.randint(1,len(Keys))
            for k in range(0,len(temp2)):
                if temp2[k]==temp3:
                    flag=1
                if flag==0:
                    print("Extra Random Answer Order:  "+str(temp3))
                    print("Length of Shuffled Answer: "+str(len(Shuffled_Answer)))

                    temp2.append(Shuffled_Answer[temp3-1])
random.shuffle(temp2)
display_list.append(temp1+temp2)




score=0
#from Single display iteratively Create, Present, Take input for MCQ
for i in range(0,len(display_list)):
    single_display=display_list[i]
    for j in range(0,len(single_display)):
        if j==0:
            temp4="Select the option most closest to the following Service: "+single_display[i]+"\n"+"\n"+"\n"+"\n"
        if j>0:
            # for k in range(1,len(single_display)):
            temp5=chr(65+j)+") " +"   "+single_display(i)
            temp4=temp4+"\n"+temp5
        #Insert Extra Options Here

    Given_answer=input(temp4)
    #Make answer case insensitive and convert into number
    Given_answer=Given_answer.casefold()
    Index=ord(Given_answer)+1
    #Compare answer and change Score
    if single_display[index]==Shuffled_Answer[i]:
        score=score+1




#Present Score
print("Your score is :"+str(score))
print("Your Percentage is :"+str(score/len(single_display)))


#Log Score