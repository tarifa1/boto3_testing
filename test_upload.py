import boto3
import sys


def upload_to_s3(file, bucket, subdir):
    '''
    Method to upload a given file into an AWS S3 bucket
    '''
    try:
        key = "/{}/{}".format(subdir, file)
        content = open(file, 'rb')
        s3 = boto3.client('s3')
        s3.put_object(Bucket=bucket, Key=key, Body=content)

        success = True

    except Exception as e:
        raise e

    if not success:
        return True
    return False


def main():

    if len(sys.argv[0:]) < 4:
        exit("Need 3 inputs: File, Bucket, Bucket Key")

    file = sys.argv[1]
    bucket = sys.argv[2]
    subdir = sys.argv[3]

    if upload_to_s3(file, bucket, subdir):
        print("Success")
    else:
        print("Failed to upload")

    # AWS_ACCESS_KEY = sys.argv[1]
    # AWS_ACCESS_SECRET_KEY = sys.argv[2]

    # file = open(sys.argv[3], "r+")

    # key = file.name
    # bucket = sys.argv[4]


if __name__ == '__main__':
    main()
