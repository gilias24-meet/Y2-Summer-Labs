from flask import Flask, render_template, request, url_for
import random
app = Flask(__name__,
template_folder='templates',
static_folder='static')

@app .route('/home', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template("hello.html")
	else:
		birth = request.form['birth month']
		return redirect(url_for('fortune',
            b = birth))



@app .route('/fortune/<string:b>')
def fortune(b):
	fortunes = ["You  will never submit the lab on time", "you will only have du until the end of the week", "you will lose your water bottle", "you will not be on time for complementary", "you will eat IASA food forever", "Your computer will die,", "you will win the entrp contest", "you wiil have no free time,", "your pet will die,", "tomorrow you will discover something shocking"]
	l =len(b)
	f = fortunes[l]

	return render_template("fortune.html", f = f)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000)
	