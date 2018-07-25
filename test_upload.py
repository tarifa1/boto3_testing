import os
import boto3
import sys
from boto3.s3.key import Key


def upload_to_s3(aws_access_key_id, aws_secret_access_key, file, bucket, key,
                 callback=None, md5=None, reduced_redundancy=False,
                 content_type=None):
    '''
    Method to upload a given file into an AWS S3 bucket
    '''
    try:
        size = os.fstat(file.fileno()).st_size
    except:
        # Not all file objects implement fileno(),
        # so we fall back on this
        file.seek(0, os.SEEK_END)
        size = file.tell()

    conn = boto3.connect_s3(aws_access_key_id, aws_secret_access_key)
    bucket = conn.get_bucket(bucket, validate=True)
    k = Key(bucket)
    k.key = key
    if content_type:
        k.set_metadata('Content-Type', content_type)
    sent = k.set_contents_from_file(file, cb=callback, md5=md5,
                                    reduced_redundancy=reduced_redundancy,
                                    rewind=True)
    file.seek(0)

    if sent == size:
        return True
    return False


def main():

    if len(sys.argv[0:]) < 5:
        exit("Need 4 inputs: Access Key, Secret Key, File, Bucket")

    AWS_ACCESS_KEY = sys.argv[1]
    AWS_ACCESS_SECRET_KEY = sys.argv[2]

    file = open(sys.argv[3], "r+")

    key = file.name
    bucket = sys.argv[4]

    if upload_to_s3(AWS_ACCESS_KEY, AWS_ACCESS_SECRET_KEY, file, bucket, key):
        print("Success!")
    else:
        print("Upload failed")


if __name__ == '__main__':
    main()
