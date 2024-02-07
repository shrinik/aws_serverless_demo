from time import time, ctime
import boto3

def lambda_handler(event, context):
    now = ctime(time())
    print("Lambda invoked on", now, "with event", event)    