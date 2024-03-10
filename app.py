from flask import Flask, render_template, request
import client
import random as rand
import subprocess

app = Flask(__name__, template_folder='/Users/kevinwu/Desktop/Hackaton/')

MESSAGES = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    msg = request.form['Message']
    out = ""
    client.client_f("Arc", msg, 1)
    print(msg)
    with open(file_path,'a') as f:
        f.write("|" + msg + "|\n")
    with open(file_path, 'r') as f:
        out = f.read()
    return render_template('index.html', msg=out)

@app.route('/chat')
def chat():
    return render_template("chat.html")

@app.route('/send_message', methods=['POST'])
def send_message():
    user = request.form['user']
    text_msg = request.form['text_msg']
    # Call your client_f function to send the message
    client_f(user, text_msg)
    return 'Message sent successfully'

if __name__ == '__main__':
    app.run(debug=True)
