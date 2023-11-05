# import boto3
import tempfile

# from cloudinary.uploader import upload, add_tag, remove_tag
# from cloudinary.api import resources, delete_resources
# from cloudinary.search import Search

from actions.base import BaseAction
from utilities.helper import Utility
import utilities.constant as constants
from schemas.core_provider.media import media_list_upload_response_schema, MediaResourceSchema


# from utilities.constant import get_s3_bucket, get_s3_secret, get_s3_key, get_s3_location


class MediaAction(BaseAction):
    def upload_file_to_s3(self, files, is_private=False):
        # s3 = boto3.client(
        #     "s3",
        #     aws_access_key_id=get_s3_key(),
        #     aws_secret_access_key=get_s3_secret()
        # )
        # try:
        #     rv = []
        #     for name, file in files.items():
        #         public_id = Utility.uuid()
        #         extra_args = {
        #             "ContentType": file.content_type
        #         } if is_private else {
        #             "ACL": "public-read",
        #             "ContentType": file.content_type
        #         }
        #         s3.upload_fileobj(
        #             file,
        #             get_s3_bucket(),
        #             public_id,
        #             ExtraArgs=extra_args
        #         )
        #         rv.append({
        #             'public_id': "{}/{}".format(get_s3_bucket(), public_id)
        #         })

        return media_list_upload_response_schema.dump([])
        # except Exception as e:
        #     return e

    def download_file_from_s3(self, public_id):
        temp = tempfile.NamedTemporaryFile(prefix="sia_", suffix="_pub", mode="w+b", delete=False)
        # s3 = boto3.client(
        #     "s3",
        #     aws_access_key_id=get_s3_key(),
        #     aws_secret_access_key=get_s3_secret()
        # )
        # try:
        #     s3.download_fileobj(
        #         get_s3_bucket(),
        #         public_id,
        #         temp.file
        #     )
        # except Exception as e:
        #     return e

        return temp.name


media_action = MediaAction()
