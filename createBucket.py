import boto3

bucket_name = str(input('Please input bucket name to be created: '))
regions3 = str(input("Please state which region: "))
s3_location = {
    'LocationConstraint' : regions3
}

s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)

print('\n\n\nYour bucket has now been created!\n\n\n')