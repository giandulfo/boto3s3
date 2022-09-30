import boto3


BUCKET_NAME = str(input('Please input bucket name to be deleted: '))


s3 = boto3.client("s3")

reponse = s3.delete_bucket(Bucket=BUCKET_NAME)

print('\n\n\nYour bucket has now been deleted!\n\n\n')