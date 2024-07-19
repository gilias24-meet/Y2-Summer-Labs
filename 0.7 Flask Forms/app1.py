from flask import Flask, render_template, request
from flask import session as login_session

app = Flask(__name__,
template_folder='templates',
static_folder='static')


@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
       username = request.form['birth']
   return render_template("login.html")

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



	