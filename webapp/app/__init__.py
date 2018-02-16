# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from twilio.rest import Client
import os

app = Flask(__name__)
api = Api(app)
CORS(app)

ACCOUNT = os.environ['account']
TOKEN = os.environ['token']
FROM = os.environ['from']

counter = 0

def send_message(msg,to):
    try:
      client = Client(ACCOUNT, TOKEN)
      message = client.messages.create(to=to, from_=FROM, body=msg)
      return message
    except:
      return None

class SendSMS(Resource):
    def get(self):
        global counter
        counter += 1
        msg = request.args.get('msg')
        to = request.args.get('to')
        ret = send_message(msg,to)
        if ret == None:
          return {'status': 'fail', 'ret': ret}
        else:
          return {'status': 'ok'}

class stats(Resource):
    def get(self):
        return {'counter': counter }

api.add_resource(SendSMS, '/', '/send/')
api.add_resource(stats, '/stats/')

if __name__ == '__main__':
    app.run(debug=True)

