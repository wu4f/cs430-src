import os
import boto3
import json

def handler(event, context):
    """Scan the DynamoDB table for all guestbook entries return them on success
    """
    resource = boto3.resource("dynamodb")
    table = resource.Table(os.environ['TABLE'])

    try:
        ddb_entries = table.scan()
        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin" : "*"
            },
            'body': json.dumps(ddb_entries['Items'])
        }
    except Exception as ex:
        return {
            'statusCode': 500,
            'headers': {
                "Access-Control-Allow-Origin" : "*"
            },
            'body': "It's not you, it's us. :("
        }