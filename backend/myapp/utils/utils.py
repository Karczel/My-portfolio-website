from mysite.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_REGION_NAME, AWS_STORAGE_BUCKET_NAME
import boto3


NAME = 50
ROLE = 20

def get_s3_client():
    """Get S3 client for authentication to access S3 storage."""
    return boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_S3_REGION_NAME
    )


s3_client = get_s3_client()
BUCKET_NAME = AWS_STORAGE_BUCKET_NAME
