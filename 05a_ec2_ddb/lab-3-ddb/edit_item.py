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

DDB_RESOURCE = boto3.resource("dynamodb", region_name="us-east-1")

table = DDB_RESOURCE.Table("lostcats")

petname = "Hosepipe"

table.update_item(
    Key={
        'petname': petname
    },
    UpdateExpression="set breed = :b",
    ExpressionAttributeValues={
        ":b": "British Shorthair"
    },
    ReturnValues="UPDATED_NEW"
)
