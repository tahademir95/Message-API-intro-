import json
from http import client
from models.user import User
from flask import request
import random

headers = {"Content-type": "application/json"}
isAsked = False
Responses =  {0: " I'm fine.",
              1: "I'm not fine."}
Questions =  {0: " How are you? ",
              1: " What happened?"}
Situations = {1: " My car crashed",
              2: " My computer is not working",
              3: " I stuck at traffic for 2 hours",
              4: " I'm fired"}
def hello_post(body):
    global isAsked
    userIP = request.environ['REMOTE_ADDR']
    user = User(body['name'], body['fine'])
    data = {'name': user.name, 'fine': user.fine}
    conn = client.HTTPConnection(userIP, 5000)
    if isAsked is False:
        conn.request("POST", "/how", json.dumps(data), headers)
        how_response = conn.getresponse().read().decode()
        isAsked = True
        hello_response = "Hi " + user.name + how_response
        return hello_response
def how_post(body):
    user = User(body['name'], body['fine'])
    rand = random.randrange(1, 5)
    if user.fine is True:
        return Questions[0] + Responses[0]
    elif user.fine is False:
        return Questions[0] + Responses[1] + Questions[1] + Situations[rand]
