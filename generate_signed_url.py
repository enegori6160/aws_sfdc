import boto3
from botocore.config import Config

# AWS設定
bucket_name = ''
object_key = ''
region_name = ''  # バケットのリージョンを指定
expires_in = 3600  # URLの有効期限（秒）

# アクセスキーの設定
aws_access_key_id = ''
aws_secret_access_key = ''

# S3クライアントの作成
s3_client = boto3.client(
    's3',
    region_name=region_name,
    config=Config(signature_version='s3v4'),
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# 署名付きURLの生成
signed_url = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': object_key}, ExpiresIn=expires_in)

print('Signed URL:', signed_url)
