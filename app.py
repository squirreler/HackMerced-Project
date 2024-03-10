from flask import Flask, render_template

app = Flask(__name__, template_folder= 'templates')

#app.config['SEVER_NAME'] = 'domain.com'

@app.route('/')

def home():
    return render_template("st.html")
    return render_template("structure.html") 

@app.route('/chat')
def chat():
    
    

    
if __name__ == '__main__':
    app.run(debug = True)

print("hello")












