from flask import render_template
from flask.views import MethodView
import gbmodel
import giphy_client
from giphy_client.rest import ApiException
import os
import random

API_KEY = os.environ['GIPHY_KEY']
api_instance = giphy_client.DefaultApi()

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(name=row[0], email=row[1], signed_on=row[2], message=row[3] ) for row in model.select()]
        offset = random.randint(0,50)
        try:
            api_response = api_instance.gifs_search_get(API_KEY, 'welcome', limit=1, offset=offset, rating='g', lang='en', fmt='json')
            if len(api_response.data) > 0:
                embed_url = api_response.data[0].embed_url
        except ApiException as e:
            embed_url = ''

        return render_template('index.html',entries=entries,embed_url=embed_url)