import boto3
import sys


def upload_to_s3(file, bucket, subdir):
    '''
    Method to upload a given file into an AWS S3 bucket
    '''

    key = "{}/{}".format(subdir, file)
    print(key)
    content = open(file, 'rb')
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=key, Body=content)


def main():

    if len(sys.argv[0:]) < 4:
        exit("Need 3 inputs: File, Bucket, Bucket Key")

    file = sys.argv[1]
    bucket = sys.argv[2]
    subdir = sys.argv[3]

    upload_to_s3(file, bucket, subdir)


if __name__ == '__main__':
    main()
