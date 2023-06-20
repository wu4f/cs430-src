import os
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
token_url = 'https://accounts.google.com/o/oauth2/token'

if not (redirect_callback := os.environ.get('REDIRECT_CALLBACK'):
  redirect_callback = 'http://localhost:8000/callback'
