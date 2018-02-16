#!/usr/bin/env python

# simple wrapper for nagios/check_mk to send messages to docker
# pashi/twilio-flask
# https://hub.docker.com/r/pashi/twilio-flask/

import requests
import sys

url = 'http://localhost:8080/'

if __name__ == '__main__':

    to = sys.argv[1]
    msg = sys.argv[2]
    payload = { 'to': to, 'msg': msg }
    r = requests.get(url, params=payload)
sys.exit (0)

