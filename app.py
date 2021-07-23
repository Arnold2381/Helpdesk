from flask import Flask, render_template, request
app = Flask(__name__, static_folder="./static")
@app.route('/', methods=['POST', 'GET'])
def home():
    print("hello")
    return render_template('login.html')
@app.route('/homepage', methods=['POST', 'GET'])
def dashboard():
    return render_template('homepage.html')

@app.route('/postmethod', methods=['POST', 'GET'])
def r():
    jsdata = request.form['javascript_data']
    print(jsdata)
    return jsdata

app.run('0.0.0.0', 5000, debug=True)