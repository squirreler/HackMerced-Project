from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# Define routes
@app.route('/')
def home():
    return render_template("structure.html")

@app.route('/chat')
def chat():
    return render_template("chat.html")

@app.route('/send_message', methods=['POST'])
def send_message():
    user = request.form['user']
    text_msg = request.form['text_msg']
    # Call your client_f function to send the message
    client.client_f(user, text_msg)  # Corrected the function call
    return 'Message sent successfully'

if __name__ == '__main__':
    app.run(debug=True)
