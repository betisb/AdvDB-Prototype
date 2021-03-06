# 3rd party
import boto3
from google.cloud import storage, exceptions


###############################################################################
# Cloud interface methods
#
# Google Cloud Storage
#   * https://cloud.google.com/storage/docs/how-to
#   We assume that the user has properly provided the required application
#   credentials (found defined on the EVN - GOOGLE_APPLICATION_CREDENTIALS)
#   The below links outline what is required to use the python library
#   along with the SDK (recommended to make setup easier)
#   * https://cloud.google.com/sdk/
#   * https://cloud.google.com/storage/docs/reference/libraries#client
#       -libraries-usage-python
#
# Amazon AWS S3
#   * https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html
#   We assume that the user has properly provided the required application
#   credentials (https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
#   Note, for access ID/key
#       1. http://aws.amazon.com/
#       2. Account menu -> Security Credentials
#       3. Access keys (access key ID and secret access key) -> Create New Access Key
###############################################################################


def gcloud_create_bucket(bucket_name):
    """Creates a new bucket (if not already present) """
    storage_client = storage.Client()
    try:
        bucket = storage_client.create_bucket(bucket_name)
        print('Bucket {} created'.format(bucket.name))
    except exceptions.Conflict:
        print('Bucket {} already exists'.format(bucket_name))


def gcloud_upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


def gcloud_download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))


def gcloud_delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()

    print('Blob {} deleted.'.format(blob_name))


def aws_create_bucket(bucket_name):
    """Creates a new bucket (if not already present) """
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)

    print('Bucket {} created'.format(bucket_name))


def aws_upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    s3 = boto3.client('s3')
    s3.upload_file(source_file_name, bucket_name, destination_blob_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


def aws_download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    s3 = boto3.resource('s3')
    s3.Bucket(bucket_name).download_file(source_blob_name, destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))


def aws_delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    s3 = boto3.resource('s3')
    s3.Object(bucket_name, blob_name).delete()

    print('Blob {} deleted.'.format(blob_name))