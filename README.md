# nanlabs-techtest
Repository intended to develop a technical test for a company. (Only for demo porpuses)

## Short description
The test consisted in a small API with the objective to create new cards in Trello through its API.

## Requirements
 - **Python** 3.8.0+
 - **Flask**
 - A virtual environment (Python3 ***venv*** recommended)
 - All **requirements** listed on ***requirements.txt*** file.
 - Get your developers credentials from **Trello** (https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/) and give it the right permissions in order to have access to the services.
 - Be sure to have a **board** created in your Trello account.
 
## Running The App

- Create a virtual environment: ```python3 -m venv venv```
- Activate the virtual environment: ```source venv/bin/activate```
- Install the requirements: ```pip3 install -r requirements.txt```
- Also you should set up your own ***'.env'*** file in order to make it work. You can see I uploaded an ***'.env.example'*** file to the repo so you can modify it with your own credentials and rename it to ***'.env'*** or, as an alternative, you can duplicate it and change its name to ***'.env'*** so it will be untracked by github in order to protect *private keys* and *tokens*.

- Now we can **run** our **Flask App** with  ```flask run``` (by *default* it will run in port **5000**)
  

- Finally, here is a short *guide* of how to consume the *endpoint*:

  - *URI*: ```http://127.0.0.1:5000/nanlabs/cards```
  - *Method*: ```POST```
  - *Content Type*: ```application/json```
  - *Body content*:   ```
                      {
                        "title":"Create Tests",
                        "description":"As developers we should create tests for our application",
                        "type": "task",
                        "category" : "To Do"
                      }
                    ```

        
  - Keys explanation:
     -Title: The name of the card.
     -Description: Short description of the card. 
     -Type: The type of card. It will set a label (task, issue, bug). Required key. Can be Null
     -Category: This indicates the list where the card will be appended. Required key.Can be Null


