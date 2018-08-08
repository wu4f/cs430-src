# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .Model import Model
from datetime import datetime
from flask import current_app
from google.cloud import datastore

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        {id: id, prop: val, ...}
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['name'],entity['email'],entity['date'],entity['message']]

class model(Model):
    def __init__(self):
        #self.client = datastore.Client(current_app.config['PROJECT_ID'])
        self.client = datastore.Client('cs410c-wuchang-201515')

    def select(self):
        query = self.client.query(kind = 'Review')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    def insert(self,name,email,message):
        key = self.client.key('Review')
        rev = datastore.Entity(key)
        rev.update( {
            'name': name,
            'email' : email,
            'date' : datetime.today(),
            'message' : message
            })
        self.client.put(rev)
        return True
