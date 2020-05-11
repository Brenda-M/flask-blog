import os
import requests
from .models import Quotes

def get_quotes():
  response = requests.get(os.environ.get('API_URL'))
  if response.status_code == 200:
    quote = response.json()
    return quote