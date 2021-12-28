import boto3
from src.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY


class S3(object):
    def __init__(self):
        self._client = None
        self._region = {}
        self._buckets = {}
        self.connect()

    def connect(self):
        self._client = boto3.client(
            service_name='s3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_KEY,
        )
        self._buckets = {}

        bucket_list = self._client.list_buckets().get('Buckets')

        for bucket_obj in bucket_list:
            bucket_name = bucket_obj.get('Name')
            module_name = self.make_module_name(bucket_name)
            self._buckets[module_name] = bucket_name

    def make_module_name(self, bucket_name):
        module_name = ''
        modules = bucket_name.replace('soulinno-ems-log-', '').split('-')

        for idx, name in enumerate(modules):
            if idx != 0:
                name = name.capitalize()
            module_name += name

        return module_name

    def get_bucket_name(self, module_name):
        bucket_name = self._buckets.get(module_name)

        return bucket_name

    def get_client(self):
        return self._client
# S3.connect()