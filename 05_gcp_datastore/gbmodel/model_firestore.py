from .Model import Model
from datetime import datetime
from google.cloud import firestore

class model(Model):
    def __init__(self):
        self.client = firestore.Client()

    def select(self):
        revs = self.client.collection(u'Reviews').stream()
        entities = [ [r.get('name'), r.get('email'), r.get('date').strftime("%c"), r.get('message')] for r in revs]
        return entities

    def insert(self,name,email,message):
        review_ref = self.client.collection(u'Reviews').document()
        review_ref.set({
            'name': name,
            'email' : email,
            'date' : datetime.today(),
            'message' : message
        })
        return True
