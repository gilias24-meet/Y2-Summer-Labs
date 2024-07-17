from flask import Flask, render_template
import random
app = Flask(__name__,
template_folder='templates',
static_folder='static')

@app .route('/home')
def home():
	return render_template("hello.html")


@app .route('/fortune')
def fortune():
	fortunes = ["You  will never submit the lab on time", "you will only have du until the end of the week", "you will lose your water bottle", "you will not be on time for complementary", "you will eat IASA food forever", "Your computer will die,", "you will win the entrp contest", "you wiil have no free time,", "your pet will die,", "tomorrow you will discover something shocking"]
	i = random.randint(0, 9)
	f = fortunes[i]

	return render_template("fortune.html", f = f)

if __name__ == '__main__':
	app.run(debug=True)
	