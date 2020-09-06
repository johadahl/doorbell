import datetime
import smtplib, ssl
import os
from flask import Flask, request, render_template, jsonify
from twilio.twiml.voice_response import VoiceResponse, Dial, Play, Gather


app = Flask(__name__)

# landing page
@app.route('/')
def hello_world():
	return render_template('home.html', is_home = is_home())

# handles toggle
@app.route('/toggle') 
def toggle_status():
	toggle_home()
	log("toggled. Home is now: " + str(is_home()))
	return render_template('home.html', is_home = is_home())


# Handles IFTTT activate - Turn on automatic opening
@app.route('/api/ifttt/v1/actions/activate')
def activate():
	log("activate")
	if not is_home():
		toggle_home()
#	return jsonify({"status_code" : 200, "data" : [{"id" : 1,},]}) 

# Handles IFTTT deactivate - Turn off automatic opening
@app.route('/api/ifttt/v1/actions/deactivate')
def deactivate():
	log("deactivate")
	if is_home():
		toggle_home()
#	return jsonify({"status_code" : 200, "data" : [{"id" : 1,},]})



# Respond to incoming phone calls with a brief message.
@app.route('/answer', methods=['GET', 'POST'])
def answer_call():
	log("answered call, home is now: " + str(is_home()))
	# Start our TwiML response
	resp = VoiceResponse()
	# Read a message aloud to the caller
	if is_home():
		resp.say('Hi. state your name to enter', voice='alice', language='en-EN')
		resp.gather(timeout=3)
		resp.play('Welcome. Proceed to the fifth floor', digits='w*')
		send_email(resp)
	else:
		resp.say('Hello. Automatic entry is not activated. Please call Johan if you need to be let inside. Thank you.', voice='alice', language='en-EN')
	return str(resp)

# Toggles status and updates persistant storage
def toggle_home():
	f = open("status.txt", "r+")
	previous = f.read()
	f.close()
	# Overwrites new value based on prev
	f = open("status.txt", "w")
	if previous == "home":
		f.write("away")
	else:
		f.write("home")
	f.close()

# Read file and get status
def is_home():
	f = open("status.txt", "r")
	saved = f.read()
	f.close()
	if saved == "home":
		return True
	else:
		return False

# Adds message with timestamp to log
def log(message):
	f = open("log.txt", "a")
	s = "\n" + str(datetime.datetime.now()) + ", " + message
	f.write(s)
	f.close()

def send_email(message):
	port = 465
	password = os.environ['GMAIL_PASSWORD']
	mail_sender = os.environ['GMAIL_SENDER']
	mail_reciever = os.environ['GMAIL_RECIEVER']

	context = ssl.create_default_context()

	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login(mail_sender, password)
		server.sendmail(mail_sender, mail_reciever, "%s is on their way up!" % message)

if __name__ == '__main__':
    app.run()


