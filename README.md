# Automatic door-answering machine

# Goal

This project automatically opens the main entrance to the door in my apartment building whenever I am at home.
The guests call a number connected to Twilio. Twilio then calls the /answer API which depending on if I am home or not automatically responds with the required signal or not. I use IFTTT to trigger the server into a state of me being home or not. There is also a lightweight UI to trigger if the automatic door-answer service should be turned on or not indepenedtly of my location

## Requirements

# Twilio

To route incomming calls to this lightweight server and respond to the caller

# IFTTT

You need to set up your own service and connect two actions ("activate" & "deactivate") to your service.
Once that is done you can use the IFTTT app with a location service to toggle the servers is_home state based on your cellphones location. 