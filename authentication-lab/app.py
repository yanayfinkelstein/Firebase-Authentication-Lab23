from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
config = {
    "apiKey": "AIzaSyBl_uoeLcBeD5AkpLdgAw-PuXNp49HS6qk",
    "authDomain": "fir-lab-d3e7b.firebaseapp.com",
    "projectId": "fir-lab-d3e7b",
    "storageBucket": "fir-lab-d3e7b.appspot.com",
    "messagingSenderId": "403423018058",
    "appId": "1:403423018058:web:50cf569b17ac4411797ab3",
    "measurementId": "G-QE1P8B068F",
    "databaseURL":"https://console.firebase.google.com/project/fir-lab-d3e7b/database/fir-lab-d3e7b-default-rtdb/data/~2F"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       bio = request.form['bio']
       try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            user = {"email":"email", "password":"password", "bio":"bio"}
            db.child("Users").child(UID).set(user)
            return redirect(url_for('add_tweet'))
       except:
            error = "AUTH FAILED"
            return render_template("signin.html")
    else:
        return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        

        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            
            return redirect(url_for('signin'))
        except: 
            return render_template("signup.html")

    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")





if __name__ == '__main__':
    app.run(debug=True)