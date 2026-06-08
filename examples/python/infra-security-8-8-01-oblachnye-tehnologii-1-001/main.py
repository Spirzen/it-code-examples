
import boto3

# MinIO локально — endpoint_url="http://127.0.0.1:9000"
s3 = boto3.client(
    "s3",
    endpoint_url="https://s3.amazonaws.com",
    region_name="eu-central-1",
)

bucket = "my-company-demo-logs-2025"
key = "reports/2025/report.pdf"

s3.upload_file("report.pdf", bucket, key)
# url = s3.generate_presigned_url(
#     "get_object",
#     Params={"Bucket": bucket, "Key": key},
#     ExpiresIn=3600,
# )
