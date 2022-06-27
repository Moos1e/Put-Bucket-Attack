# Put-Bucket-Attack READ ME

## General Information
* Author: Jon Helmus
* Date 06/25/2022
* Description: A script that will allow you to check for any buckets that allow GET and PUT on bucket policies. These are a major concern when assessing AWS environments and can lead to impactful situations such as DoS on the S3 bucket.

## Installing
Ensure you install the following from `requirements.txt`:

```
pip3 install awspolicy 
pip3 install boto3 
pip3 install python3

