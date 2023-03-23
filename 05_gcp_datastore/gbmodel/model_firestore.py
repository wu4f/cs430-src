from .model import Model
from datetime import datetime
from google.cloud import firestore

class ModelFirestore(Model):
    def __init__(self):
        self.client = firestore.Client()

    def select(self):
        revs = self.client.collection(u'Reviews').stream()
        entities = [ [r.get('name'), r.get('email'), r.get('signed_on'), r.get('message'), r.id] for r in revs]
        return entities

    def insert(self,name,email,message):
        review_ref = self.client.collection(u'Reviews').document()
        review_ref.set({
            'name': name,
            'email' : email,
            'signed_on' : datetime.now(),
            'message' : message
        })
        return True
