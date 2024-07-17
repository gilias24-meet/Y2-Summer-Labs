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
	fortunes = ["Death", "wealth", "happiness", "joy", "sadness", "love", "hate", "anger", "boredom", "stress"]
	index_f = random.randint(0, 9)
	f = fortunes(index_f)



	return render_template("fortune.html")

if __name__ == '__main__':
	app.run(debug=True)
	