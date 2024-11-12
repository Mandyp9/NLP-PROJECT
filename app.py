from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from better_profanity import profanity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Load default and custom cuss words
profanity.load_censor_words()
# Custom cuss words
custom_cuss_words = ["youtube", "facebook"]  
profanity.add_censor_words(custom_cuss_words)

# Abbreviations dictionary
abbreviations = {
    "brb": "be right back",
    "gtg": "got to go",
    "idk": "I don't know",
    "omw": "on my way",
    "btw": "by the way",
    "fam": "family",
    "yolo": "you only live once",
    "tbh": "to be honest",
    "goat": "greatest of all time"
}

def replace_abbreviations(message):
    words = message.split()
    # Replace each abbreviation with its full form
    replaced_words = [abbreviations.get(word.lower(), word) for word in words]
    return " ".join(replaced_words)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    message = data['message']
    # Replace abbreviations
    message = replace_abbreviations(message)
    # Censor cuss words
    cleaned_message = profanity.censor(message)
    emit('receive_message', {'message': cleaned_message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
