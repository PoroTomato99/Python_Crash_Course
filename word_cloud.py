#!/usr/bin/env python
file_contents = """This title is the first of its kind and will help you to secure all aspects of your Amazon Web
Services (AWS) infrastructure by means of penetration testing. It walks through the
processes of setting up test environments within AWS, performing reconnaissance to
identify vulnerable services using a variety of tools, finding misconfigurations and insecure
configurations for various components, and how vulnerabilities can be used to gain further
access.
Who this book is for
If you are a security analyst or a penetration tester who is interested in exploiting cloud
environments to establish vulnerable areas and then secure them, this book is for you. A
basic understanding of penetration testing, AWS, and its security concepts would be
necessary.
What this book covers
Chapter 1, Setting Up a Pentesting Lab on AWS, focuses on setting up a vulnerable Linux
virtual machine (VM) as well as a generic Windows VM on AWS and putting it on the
same network as the Kali instance.
Chapter 2, Setting Up a Kali Pentestbox on the Cloud, focuses on creating an Amazon EC2
instance, setting it up with a Kali Linux Amazon Machine Image (AMI), and configuring
remote access to this host through a variety of means.
Chapter 3, Exploitation on the Cloud Using Kali Linux, walks you through the process of
scanning for vulnerabilities in a vulnerable lab, exploiting these vulnerabilities using
Metasploit, gaining reverse shells, and various other exploitation techniques. This serves to
help budding pentesters practice on a cloud environment that simulates real-life networks.
Chapter 4, Setting Up Your First EC2 Instances, walks you through the concepts of EC2
instance sizes, different types of instances and their uses, AMIs and the creation of custom
AMIs, various storage types, the concept of input/output operations per second (IOPS),
Elastic Block Stores, security policies, and virtual private cloud configurations.
Chapter 5, Penetration Testing of EC2 Instances Using Kali Linux, focuses on the methods for
performing a security assessment on an EC2 instance.Preface
[ 2 ]
Chapter 6, Elastic Block Stores and Snapshots – Retrieving Deleted Data, introduces you to the
different types of storage options that are available through AWS, extending the
information covered in Chapter 3, Exploitation on the Cloud Using Kali Linux.
Chapter 7, Reconnaissance – Identifying Vulnerable S3 Buckets, explains the concept of AWS
S3 buckets, what they're used for, and how to set them up and access them.
Chapter 8, Exploiting Permissive S3 Buckets for Fun and Profit, goes through the process of
exploiting a vulnerable S3 bucket to identify JavaScript files that are being loaded by a web
application and backdooring them to gain a pan-user compromise. 
Chapter 9, Identity Access Management on AWS, focuses on one of the most important
concepts in AWS that is meant to manage user identity and access to various layers of
services within AWS. 
Chapter 10, Privilege Escalation of AWS Accounts Using Stolen Keys, Boto3, and Pacu, focuses
on using the Boto3 Python library and the Pacu framework to leverage AWS keys for a
wide range of attacks within an AWS environment. We go through the processes of
enumerating access validity, identity information, and complete account information as
well as enumerating information such as that pertaining to S3 buckets and EC2 instance
metadata. This will also cover the process of automating some of the steps that we covered
in earlier chapters. Finally, the steps to change and set administrator roles for a given user
or group are also covered.
Chapter 11, Using Boto3 and Pacu to Maintain AWS Persistence, deals with permission
enumeration and privilege escalation, which are integral to AWS pentests. 
Chapter 12, Security and Pentesting of AWS Lambda, focuses on creating vulnerable Lambda
applications and executing them within a code sandbox. Once the architecture has been set
up, we focus on pivoting to connected application services, and achieving code execution
within a Lambda sandbox as well as achieving ephemeral persistence. To further simulate
an actual pentest, there is a walk-through of running a vulnerable Lambda application and
achieving subsequent compromise.
Chapter 13, Pentesting and Securing AWS RDS, focuses on explaining the process of setting
up a sample Relational Database Service (RDS) instance and connecting it to a WordPress
instance in a secure, as well as an insecure, way.
Chapter 14, Targeting Other Services, is designed to show some attacks on some less
common AWS APIs. This chapter deals with misconfigurations and attack vectors available
in Route53, SES, CloudFormation, and Key Management Service (KMS).Preface
[ 3 ]
Chapter 15, Pentesting CloudTrail, helps us deal with one of the most detailed sources of
information within an AWS environment, which is CloudTrail. CloudTrail logs can be a
treasure trove of information to a potential attacker regarding the internal operations of
various AWS services, virtual machines, and users, alongside significant amounts of other
useful information.
Chapter 16, GuardDuty, introduces you to GuardDuty, the dedicated intrusion detection
system for AWS. You will be exposed to the range of GuardDuty alerting capabilities and
how it relies on the CloudTrails listed in the previous chapter. After covering the
monitoring and alerting capabilities of GuardDuty, we'll explore GuardDuty as an attacker
and how to bypass AWS security monitoring capabilities.
Chapter 17, Using Scout Suite and Security Monkey, introduces you to another automated
tool, Scout Suite, which performs an audit on the attack surface within an AWS
infrastructure and reports a list of findings that can be viewed on a web browser. It also
deals with Security Monkey, which, on the other hand, monitors AWS accounts for policy
changes as well as continuously monitoring for insecurity configurations. 
Chapter 18, Using Pacu for AWS Pentesting, puts together many of the Pacu concepts given
throughout the previous chapters, walking you through the full capabilities of the AWS
attack framework, Pacu. Modular and easily extendable, we'll walk through the structure of
Pacu, how to build new enumeration and attack services, and leverage the existing
framework for complex AWS pentests.
Chapter 19, Putting it All Together – Real-World AWS Pentesting, brings together the various
concepts to walk you through a real-world AWS penetration test, starting with the
enumeration of permissions, the escalation of privileges, the backdooring of accounts, the
compromising EC2 instances, and the exfiltration of data."""

uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
"we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
"their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
"have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
"all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

# LEARNER CODE START HERE
#reference code
# file_contents = "".join((char if char.isalpha() else " ") for char in file_contents).lower().split()
# resultWords  = [word for word in file_contents if word not in uninteresting_words]
# freqDict = {word: file_contents.count(word) for word in resultWords}


#create empty word dictionary 
wordDict = {}

#processed text (punctuation is removed)
new_text = ""

characters = [char.lower() for char in file_contents]
#check is alpa 
for char in characters:
    if char.isalpha():
        new_text += char
    else:
        new_text += " "

#check if in uninteresting word
for word in new_text.split():
    if word not in uninteresting_words:
        #check if in wordDict
        if word in wordDict:
            wordDict[word] += 1
        wordDict[word] =1

wordDict = sorted(wordDict.items(), reverse=True)
for key, value in wordDict:
    print("{:>20} | {:>3} occurance".format(key,value))