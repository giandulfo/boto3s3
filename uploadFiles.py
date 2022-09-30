import boto3

#example variable with a bucket name
BUCKET_NAME = "thebestbucketever2022"

s3 = boto3.client("s3")

#burger.png has to be in the same directory as script
#ACL sets it to public read
with open("./burger.jpg", "rb") as f:
    print(f.name)
    s3.upload_fileobj(f, BUCKET_NAME, "burger.jpg", ExtraArgs={"ACL": "public-read"})