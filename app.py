from flask import Flask


app = Flask(__name__)


@app.route('/')  ## decorator to identy what addres we are loking for
def home():
	return "Hello, World!"

app.run(port=5000)