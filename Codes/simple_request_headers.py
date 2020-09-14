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

@app.route("/fruits/<string:fruitName>", methods=['POST'])
def add_fruit(fruitName):
	userName = request.headers.get('userName')
	if userName and userName==USER_NAME:
		db.append(fruitName)
		return jsonify({"fruits":db})
	else:
		return jsonify({"message":"Unauthorized"})

@app.route("/fruits/<int:fruitID>", methods=['GET'])
def get_specific_fruit(fruitID):
	if fruitID>0 and fruitID<=len(db):
		return jsonify({"fruit":db[fruitID-1]})
	else:
		return jsonify({"fruit":""})

if __name__ =="__main__":
	app.run(debug=True)