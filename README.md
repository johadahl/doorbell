# Automatic door-answering machine

# Goal

This project automatically opens the main entrance to the door in my apartment building whenever I am at home.
The guests call a number connected to Twilio. Twilio then connects to the /answer API which depending on if is_home() == True automatically responds with the required signal to open the door or not. I use IFTTT to trigger the server into a state of me being home or not. There is also a lightweight UI to toggle the status indepenently of my location.

It is built to easily deploy as a heroku app.

Persistant storage is achieved throught the status.txt file.

# Add-ons

## Twilio

To route incomming calls to this lightweight server and respond to the caller

## IFTTT

You need to set up your own service and connect two actions ("activate" & "deactivate") to your service.
Once that is done you can use the IFTTT app with a location service to toggle the servers is_home state based on your cellphones location.

# Acknowledgment

```
https://github.com/leah/hello-flask-heroku
```
