from flask import Flask
from twilio.twiml.voice_response import VoiceResponse, Dial, Play

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

# Respond to incoming phone calls with a brief message.
@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("Welcome. Proceed to the fifth floor", voice='alice', language='en-EN')
    resp.play('', digits='w*')
    return str(resp)


if __name__ == '__main__':
    app.run()
