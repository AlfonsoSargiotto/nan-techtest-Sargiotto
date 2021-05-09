from flask import Flask, request, jsonify, Blueprint
from app import  app
from app.utilities.get_items import get_boards, get_lists, get_labels
import requests
import json

key = app.config['TRELLO_API_KEY'] # we get the trello_api_key from our environment file
token = app.config['TRELLO_SECRET_KEY'] # we get the trello_secret_key from our environment file
cards = Blueprint('cards', __name__, url_prefix='/nanlabs/cards') # we create the Blueprint for cards


@cards.route('', methods=['POST'])  #route to create a new card
def new_card():
  board_id = get_boards()
  categories = get_lists(board_id)
  labels = get_labels(board_id)
  name = request.json['title']
  desc = request.json['description']
  card_category = request.json['category']
  card_type = request.json['type']
  label_id = None
  category_id = categories[0]['id']

  if card_type:
    for label in labels:
      if card_type.lower() == label['name'].lower():
        label_id = label['id']

  if card_category:
    for category in categories:
      if card_category.lower() == category['name'].lower():
        category_id = category['id']
  
  # we build the query to Trello API here
  url = "https://api.trello.com/1/cards" # base URL for Trello cards' API
  query ={        
    'key':key,
    'token':token,
    'idList': category_id,
    'name':name,
    'desc':desc,
    'idLabels':label_id
  }

  response = requests.request(
    "POST",
    url,
    params=query
  )

  return (response.json())



  