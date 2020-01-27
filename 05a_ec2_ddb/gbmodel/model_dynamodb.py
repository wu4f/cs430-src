from .Model import Model
from datetime import datetime
import boto3

class model(Model):
    def __init__(self):
        self.resource = boto3.resource("dynamodb", region_name="us-west-2")
        self.table = self.resource.Table('guestbook')
        try:
            self.table.load()
        except:
            self.resource.create_table(
                TableName="guestbook",
                KeySchema=[
                    {
                        "AttributeName": "email",
                        "KeyType": "HASH"
                    },
                    {
                        "AttributeName": "date",
                        "KeyType": "RANGE"
                    }
                ],
                AttributeDefinitions=[
                    {
                        "AttributeName": "email",
                        "AttributeType": "S"              
                    },
                    {
                        "AttributeName": "date",
                        "AttributeType": "S"              
                    }
                ],
                ProvisionedThroughput={
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1
                }
            )

    def select(self):
        try:
            gbentries = self.table.scan()
        except Exception as e:
            return([['scan failed', '.', '.', '.']])
        
        return([ [f['name'], f['email'], f['date'], f['message']] for f in gbentries['Items']])

    def insert(self,name,email,message):
        gbitem = {
            'name' : name,
            'email' : email,
            'date' : str(datetime.today()),
            'message' : message
            }
            
        try:
            self.table.put_item(Item=gbitem)
        except:
            return False
        
        return True
