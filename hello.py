from flask import Flask
from twilio.twiml.voice_response import VoiceResponse, Dial, Play

app = Flask(__name__)
home = False

@app.route('/')
def hello_world():
    return 'Home:' + str(home)

# Respond to incoming phone calls with a brief message.
@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    if home:
	    resp.say("Welcome. Proceed to the fifth floor", voice='alice', language='en-EN')
	    resp.play('', digits='w*')
    else:
    	resp.say("Hello. Dahl is home right now. Please call 0. 7. 0. 7. 4. 4. 7. 4. 1. 3. if you need to be let inside. Thank you", voice='alice', language='en-EN')
    return str(resp)

if __name__ == '__main__':
    app.run()
