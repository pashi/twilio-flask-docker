Introduction
============

This provide simple as possible method to send sms messages through twilio api.
Application hide all authentication params from requestor. 


RUN
===

docker run -d -e account=<twilio_account_here> -e token=<twilio_token_here> -e from=<twilio_phone_number_here> -p 8080:8080 pashi/twilio-flask



