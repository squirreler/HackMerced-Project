from flask import Flask, render_template, request
import client

app = Flask(__name__, template_folder='/Users/kevinwu/Desktop/Hackaton/')
MESSAGES_FILE_PATH = "C:\\Users\\anbha\\OneDrive\\Documents\\Projects\\chatbot\\messages.txt"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    msg = request.form.get('Message', '')
    if msg:
        client.client_f("Arc", msg, 1)
        with open(MESSAGES_FILE_PATH, 'a') as f:
            f.write("|" + msg + "|\n")
    return render_template('index.html', msg=read_messages())

@app.route('/chat')
def chat():
    return render_template("chat.html")

@app.route('/send_message', methods=['POST'])
def send_message():
    user = request.form.get('user', '')
    text_msg = request.form.get('text_msg', '')
    if user and text_msg:
        client_f(user, text_msg)
    return 'Message sent successfully'

def read_messages():
    try:
        with open(MESSAGES_FILE_PATH, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return ''

if __name__ == '__main__':
    app.run(debug=True)
