from flask import Flask, render_template, request, url_for, redirect, session as login_session
import random
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')

                                    
firebaseConfig = {'databaseURL': "https://authentication-lab-f4a56-default-rtdb.firebaseio.com/",'apiKey': "AIzaSyB41V1D7NnEzJ8T3Nm8ClHu7L2slYpcKCU",
  'authDomain': "authentication-lab-f4a56.firebaseapp.com",
  'projectId': "authentication-lab-f4a56",
  'storageBucket': "authentication-lab-f4a56.appspot.com",
  'messagingSenderId': "747400524819",
  'appId': "1:747400524819:web:89f8e3a0ff00f982d77be6",
  'measurementId': "G-B7PFEQ49M3"}

firebase = pyrebase.initialize_app(firebaseConfig) 
auth = firebase.auth()

app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST'])
def signup():
  if request.method == "GET": 
    return render_template("signup.html")
  else:
    try:
      email = request.form["username"]
      passwored = request.form['passwored']
      login_session["user"] = auth.create_user_with_email_and_password(email, passwored)
      login_session['quotes'] = []
      return render_template("home.html")
    except:
      return render_template("signup.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
  if request.method == "GET":
    return render_template("signin.html")

  try:
    email = request.form["username"]
    passwored = request.form['passwored']
    login_session["user"] = auth.sign_in_with_email_and_password(email, passwored)
    return redirect(url_for("home"))
  except:
    return render_template("signin.html")


@app.route('/home', methods=['GET', 'POST'])
def home():
  
  if request.method == "POST":
    quotes = request.form["quotes"]
    login_session['quotes'] = quotes`
    login_session.modified = True

    return redirect(url_for("thanks"))
  return render_template("home.html")

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():

   return render_template("thanks.html")

@app.route('/display' ,  methods=['GET', 'POST'])
def display():
  return render_template("display.html" , quotes = login_session['quotes'])


@app.route('/signout', methods=['GET', 'POST'])
def signout():
   return render_template("signin.html", )


if __name__ == '__main__':
  app.run(debug = True, port='2000')



