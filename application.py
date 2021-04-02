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

		clf = RandomForestClassifier(random_state=0)
		X = [[ 1,  2,  3],  # 2 samples, 3 features
		     [11, 12, 13]]
		y = [0, 1]  # classes of each sample
		clf.fit(X, y)
		res=clf.predict(X)
		d={}
		d["res"]=res.tolist()s
		return d

@app.route("/ping",methods =[ 'GET'])
def ping():
	return "check function"



if __name__ == "__main__":
	app.run()	
