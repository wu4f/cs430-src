#
#	Copyright @2019 [Amazon Web Services] [AWS]
#
#	Licensed under the Apache License, Version 2.0 (the "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#	    http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable law or agreed to in writing, software
#	distributed under the License is distributed on an "AS IS" BASIS,
#	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#	See the License for the specific language governing permissions and
#	limitations under the License.
#
import boto3

client = boto3.client("dynamodb", region_name="us-east-1")

res = client.update_table(
    AttributeDefinitions=[
        {
                "AttributeName": "breed",
                "AttributeType": "S"
        },
    ], 
    TableName="lostcats",
    GlobalSecondaryIndexUpdates=[
        {
            'Create': {
                'IndexName': 'breed_index',
                'KeySchema': [
                    {
                        'AttributeName': 'breed',
                        'KeyType': 'HASH'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            }
        }
    ],
)
print(res)
