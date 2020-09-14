from flask import Flask, jsonify

app= Flask(__name__)

db=["Apple","Mango","Banana"]

@app.route("/")
def index():
	return jsonify({"message":"Hello World!"})

@app.route("/fruits", methods=['GET'])
def get_fruits():
	return jsonify({"fruits":db})

@app.route("/fruits/<string:fruitName>", methods=['POST'])
def add_fruit(fruitName):
	db.append(fruitName)
	return jsonify({"fruits":db})

@app.route("/fruits/<int:fruitID>", methods=['GET'])
def get_specific_fruit(fruitID):
	if fruitID>0 and fruitID<=len(db):
		return jsonify({"fruit":db[fruitID-1]})
	else:
		return jsonify({"fruit":""})

@app.route("/fruits/<int:fruitID>", methods=['DELETE'])
def delete_fruit(fruitID):
	if fruitID>0 and fruitID<=len(db):
		del db[fruitID-1]
		return jsonify({"fruits":db,"message":"Item Deleted Successfully!"})
	else:
		return jsonify({"fruits":db,"message":"Invalid FruitID"})

@app.route("/fruits/<int:fruitID>/<string:fruitName>", methods=['PUT'])
def put_fruit(fruitID,fruitName):
	if fruitID>0 and fruitID<=len(db):
		db[fruitID-1]=fruitName
		return jsonify({"fruits":db,"message":"Item Replaced Successfully!"})
	else:
		return jsonify({"fruits":db,"message":"Invalid FruitID"})

if __name__ =="__main__":
	app.run(debug=True)