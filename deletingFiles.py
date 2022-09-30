import boto3

bucket_name = str(input("Please state which bucket you are deleting objects from: "))
ObjName = str(input("Please state which object you are deleting: "))


s3 = boto3.resource('s3')
s3.Object(bucket_name, ObjName).delete()

print("Your object has now been deleted!")