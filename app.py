from flask import Flask
from twilio.twiml.voice_response import VoiceResponse, Dial, Play

app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("Välkommen upp till femte våningen", voice='alice', language='sv-SE')
    resp.play('', digits='w*')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)