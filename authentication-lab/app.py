from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
config = {
    apiKey: "AIzaSyBl_uoeLcBeD5AkpLdgAw-PuXNp49HS6qk",
    authDomain: "fir-lab-d3e7b.firebaseapp.com",
    projectId: "fir-lab-d3e7b",
    storageBucket: "fir-lab-d3e7b.appspot.com",
    messagingSenderId: "403423018058",
    appId: "1:403423018058:web:50cf569b17ac4411797ab3",
    measurementId: "G-QE1P8B068F"
}
firebase = pyrebase.initialize_app(config)
auth = pyrebase.auth()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")





if __name__ == '__main__':
    app.run(debug=True)