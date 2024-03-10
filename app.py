from flask import Flask, render_template, request
import client

app = Flask(__name__, template_folder='templates')

# app.config['SEVER_NAME'] = 'domain.com'

@app.route('/')
def home():
    return render_template("structure.html") 

@app.route('/process_form', methods=['POST'])
def process_form():
    file_path = "messages.txt"
    msg = request.form.get('Message', '')  # Using get() to avoid IndexError
    out = ""

    if msg:  # Checking if msg is not empty
        client.client_f("Arc", msg, 1)
        print(msg)

        with open(file_path, 'a') as f:
            f.write("|" + msg + "|\n")

    with open(file_path, 'r') as f:
        out = f.read()
        
    return render_template('index.html', msg=out)

if __name__ == '__main__':
    app.run(debug=True)

print("hello")
