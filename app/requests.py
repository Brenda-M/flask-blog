import requests, json
from .models import Quotes

def get_quotes():
  response = requests.get('API_URL')
  if response.status_code == 200:
    quote = response.json()
    return quote