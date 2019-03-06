from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from twilio.twiml.voice_response import VoiceResponse, Dial, Play

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////light.db'
db = SQLAlchemy(app)

# Lets user toggle if away or home
@app.route('/')
def hello_world():
	cur = get_db().cursor()
	return render_template('home.html', is_home = home)

# handles toggle
@app.route('/get_toggled_status') 
def toggled_status():
	current_status = request.args.get('status')
	if current_status == 'Away':
		home = True
	else:
		home = False
	print(home)
	return 'Home' if current_status == 'Away' else 'Away'


# Respond to incoming phone calls with a brief message.
@app.route('/answer', methods=['GET', 'POST'])
def answer_call():
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    if home:
	    resp.say('Welcome. Proceed to the fifth floor', voice='alice', language='en-EN')
	    resp.play('', digits='w*')
    else:
    	resp.say('Hello. Dahl is not home right now. Please call Johan on 0. 7. 0. 7. 4. 4. 7. 4. 1. 3. if you need to be let inside. Thank you', voice='alice', language='en-EN')
    return str(resp)

if __name__ == '__main__':
    app.run()
