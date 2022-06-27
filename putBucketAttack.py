#!/usr/bin/env python

import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f' {bucket["Name"]}')

bucket_name=input('what bucket would you like to check? : ')

# Retrieve the policy of the specified bucket
s3 = boto3.client('s3')
result = s3.get_bucket_policy(Bucket=bucket_name)
print(result['Policy'])

#list objects
s3 = boto3.client('s3')

def get_s3_keys(bucket):

    """Get a list of keys in an S3 bucket."""
    resp = s3.list_objects_v2(Bucket=bucket)
    for obj in resp['Contents']:
      files = obj['Key']
    return files
filename = get_s3_keys(bucket_name)

print(filename)

#List Objects of Bucket
s3 = boto3.resource('s3')
object = s3.Object(bucket_name,'key')

question1=input("Does the bucket allow you to put a new bucket policy? Please type yes or no : ")


if question1 == 'yes' or 'YES':
    print('The policy can be bypassed!')
else:
    print('Keep digging')
    
#Upload New Policy

#Upload Lulz.txt
upload = input('Would you like to upload proof.txt? : ')
if upload == 'yes' or 'YES':
    s3.meta.client.upload_file(Filename='lulzProof.txt', Bucket=bucket_name, Key='lulzProof.txt')
else:
   print("Ok, we won't upload anything then...")
