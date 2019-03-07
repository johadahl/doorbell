from flask import Flask, request, render_template
from twilio.twiml.voice_response import VoiceResponse, Dial, Play

app = Flask(__name__)

# landing page
@app.route('/')
def hello_world():
	return render_template('home.html', is_home = is_home())

# handles toggle
@app.route('/toggle') 
def toggle_status():
	toggle_home()
	return render_template('home.html', is_home = is_home())


# Handles IFTTT activate - Turn on automatic opening
@app.route('/ifttt/v1/actions/activate')
def activate():
	if not is_home():
		toggle_home()

# Handles IFTTT deactivate - Turn off automatic opening
@app.route('/ifttt/v1/actions/deactivate')
def deactivate():
	if is_home():
		toggle_home()

# Respond to incoming phone calls with a brief message.
@app.route('/answer', methods=['GET', 'POST'])
def answer_call():
    # Start our TwiML response
    resp = VoiceResponse()
    # Read a message aloud to the caller
    if is_home():
	    resp.say('Welcome. Proceed to the fifth floor', voice='alice', language='en-EN')
	    resp.play('', digits='w*')
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

if __name__ == '__main__':
    app.run()
