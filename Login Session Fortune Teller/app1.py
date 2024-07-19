from flask import Flask, render_template, request, url_for, redirect, session as login_session
import random
app = Flask(__name__,
template_folder='templates',
static_folder='static')

app.config['SECRET_KEY'] = "secret_key"

@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return render_template("login.html")
	else:
		birth = request.form['birth']
		username = request.form['username']
		return redirect(url_for('fortune',
            b = birth))



# @app.route('/fortune/<string:b>')
# def fortune(b):
# 	fortunes = ["You  will never submit the lab on time", "you will only have du until the end of the week", "you will lose your water bottle", "you will not be on time for complementary", "you will eat IASA food forever", "Your computer will die,", "you will win the entrp contest", "you wiil have no free time,", "your pet will die,", "tomorrow you will discover something shocking"]
# 	l =len(b)


# 	if len(b) <= 9:
# 		f = fortunes[l]
		
# 	else:
# 		f = "You  will never submit the lab on time"
		
# 	return render_template("fortune.html", f = f)

# if __name__ == '__main__':
# 	app.run(debug = True, port='3000')



# 	