import boto3
from botocore.exceptions import ClientError
import os


def send_email(body):
    client = boto3.client("ses")
    message = {"Subject": {"Data": "Daily job links"}, "Body": {"Html": {"Data": body}}}
    sender = os.environ['SENDER_EMAIL']
    recipient = os.environ['RECIPIENT_EMAIL']
    try:    
        response = client.send_email(
            Source=sender,
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message = message
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])