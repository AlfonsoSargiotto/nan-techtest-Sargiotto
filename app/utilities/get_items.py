from app import app
import requests
import json


key = app.config['TRELLO_API_KEY'] # we get the trello_api_key from our environment file
token = app.config['TRELLO_SECRET_KEY'] # we get the trello_secret_key from our environment file

headers_json = {"Accept": "application/json"}
base_query = {'key': key, 'token': token}

# First we need to get boards the person belongs to. For practical cases, we are using the first one of the list
def get_boards():
  url = "https://api.trello.com/1/members/me/boards"
  headers = headers_json
  query = base_query
  response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
  )

  return response.json()[0]['id']


# Then we need to get  lists IDs in order to know where to place them ["category" attribute]
def get_lists(id):
  url = f"https://api.trello.com/1/boards/{id}/lists"
  headers = headers_json
  query = base_query
  response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
  )

  return response.json()
  

# Finally we need to get labels  IDs in to order to put the right one on each card ["type" attribute]
def get_labels(id):
  url = f"https://api.trello.com/1/boards/{id}/labels"
  headers = headers_json
  query = base_query

  response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query
  )
  
  return response.json()