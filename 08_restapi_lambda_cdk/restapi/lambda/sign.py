import os
import boto3
import json
from datetime import datetime

def handler(event, context):
    """Add an item to the guestbook table and scan for updated results. Return 
       updated results on success.
    """
    resource = boto3.resource("dynamodb")
    table = resource.Table(os.environ['TABLE'])

    try:
        entry = json.loads(event['body'])
        table.put_item(
            Item={
                    'name': entry['name'],
                    'email': entry['email'],
                    'date': str(datetime.today()),
                    'message': entry['message']
                }
        )
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