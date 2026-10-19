
import boto3
from botocore.exceptions import BotoCoreError, ClientError

bucket_name = "your-bucket-name"
file_name = "sample.txt"

s3 = boto3.client("s3")

try:
    s3.upload_file(file_name, bucket_name, file_name)
    print("File uploaded successfully!")
except (BotoCoreError, ClientError, OSError) as error:
    print(f"Upload failed: {error}")
  
