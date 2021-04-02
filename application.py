from flask import Flask,request
application=app = Flask(__name__)
from sklearn.ensemble import RandomForestClassifier
# Create a Random forest Classifier

@app.route("/",methods = ['POST', 'GET'])
def hello():
	if request.method == 'POST':
		user_id = request.form['id']
		return f"hello--{user_id}"
	else:
		clf = RandomForestClassifier(n_estimators = 100)

		return f"Hello World!{clf}"

@app.route("/ping",methods =[ 'GET'])
def hello():

	return 200,"Ok"


if __name__ == "__main__":
	app.run()	
