from urllib import response
import boto3

#example variable with a bucket name
BUCKET_NAME = "cf-templates-15esisdhwosya-eu-west-2"

s3 = boto3.client("s3")

response =s3.list_objects_v2(Bucket=BUCKET_NAME)
for obj in response["Contents"]:
    print('\n\n\n' + obj + '\n\n\n')