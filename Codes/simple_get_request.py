from flask import Flask, jsonify

app= Flask(__name__)

db=["Apple","Mango","Banana"]

@app.route("/")
def index():
	return jsonify({"message":"Hello World!"})

@app.route("/fruits", methods=['GET'])
def get_fruits():
	return jsonify({"fruits":db})

@app.route("/fruits/<int:fruitID>", methods=['GET'])
def get_specific_fruit(fruitID):
	if fruitID>0 and fruitID<=len(db):
		return jsonify({"fruit":db[fruitID-1]})
	else:
		return jsonify({"fruit":""})

if __name__ =="__main__":
	app.run(debug=True)