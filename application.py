from flask import Flask,request
application=app = Flask(__name__)
from sklearn.ensemble import RandomForestClassifier
# Create a Random forest Classifier
import json
@app.route("/",methods = ['POST', 'GET'])
def hello():
	if request.method == 'POST':
		user_id = request.form['id']
		return f"hello--{user_id}"
	else:
		clf = RandomForestClassifier(random_state=0)
		X = [[ 1,  2,  3],  # 2 samples, 3 features
		     [11, 12, 13]]
		y = [0, 1]  # classes of each sample
		clf.fit(X, y)
		res=clf.predict(X)
		d={}
		d["res"]=res.tolist()
		JSON_obj=json.dumps(d)

		return JSON_obj
		# return "hello"
@app.route("/ping",methods =[ 'GET'])
def ping():
	return "200 , Ok"
 
if __name__ == "__main__":
	app.run()	
