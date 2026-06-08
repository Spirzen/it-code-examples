
import boto3

from datetime import datetime

def upload_to_s3(bucket_name, file_path):
    s3_client = boto3.client('s3')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    object_key = f'backup/{timestamp}.tar.gz'
    
    s3_client.upload_file(file_path, bucket_name, object_key)
    print(f'Файл {file_path} загружен в бакет {bucket_name}')
    
    return object_key

upload_to_s3('my-backup-bucket', '/home/user/document.tar.gz')
