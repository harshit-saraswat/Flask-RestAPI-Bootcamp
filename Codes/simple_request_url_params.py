from flask import Flask, jsonify, request

app= Flask(__name__)

db=["Apple","Mango","Banana"]
USER_NAME="johndoe"

@app.route("/")
def index():
	return jsonify({"message":"Hello World!"})

@app.route("/fruits", methods=['GET'])
def get_fruits():
	userName = request.headers.get('userName')
	if userName and userName==USER_NAME:
		return jsonify({"fruits":db})
	else:
		return jsonify({"message":"Unauthorized"})

@app.route("/fruits", methods=['POST'])
def add_fruit():
	userName = request.headers.get('userName')
	fruitName = request.form.get('fruitName')
	# fruitName = request.get_json().get('fruitName')
	if userName and userName==USER_NAME:
		if fruitName:
			db.append(fruitName)
			return jsonify({"fruits":db})
		else:
			return jsonify({"message":"No Fruit Given"})
	else:
		return jsonify({"message":"Unauthorized"})

@app.route("/fruit", methods=['GET'])
def get_specific_fruit():
	fruitID=request.args.get("fruitID")
	if not fruitID:
		return jsonify({"message":"Send a valid fruitID"})
	elif int(fruitID)>0 and int(fruitID)<=len(db):
		return jsonify({"fruit":db[int(fruitID)-1]})
	else:
		return jsonify({"fruit":""})

if __name__ =="__main__":
	app.run(debug=True)