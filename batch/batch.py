import boto3

def getmessage():
    return "Sample AWS Batch application"

def printmessage():
    msg = getmessage()
    print(msg)

printmessage()