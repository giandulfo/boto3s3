import boto3


BUCKET_NAME = "boto-tutorial-bucket"

s3 = boto3.client("s3")

buckets_resp = s3.list_buckets()
for bucket in buckets_resp["Buckets"]:
    print(bucket)



