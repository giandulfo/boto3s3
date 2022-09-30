import boto3

#example variable with a bucket name
BUCKET_NAME = "cf-templates-15esisdhwosya-eu-west-2"

s3 = boto3.client("s3")


# Presigned URL to give limited access to an unauthorized user
url = s3.generate_presigned_url(
    "get_object", Params={"Bucket": BUCKET_NAME, "Key": "burger.jpg"}, ExpiresIn=30
)
print(url)