import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict',methods=['POST'])
def predict():
    experience = request.form.get("exp")
    testScore = request.form.get("testScore")
    interviewScore = request.form.get("interviewScore")

    int_features = [int(experience),int(testScore),int(interviewScore)]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return jsonify({"prediction":output})

@app.route('/predict_json',methods=['POST'])
def predict_json():
    experience = request.get_json().get("exp")
    testScore = request.get_json().get("testScore")
    interviewScore = request.get_json().get("interviewScore")

    int_features = [int(experience),int(testScore),int(interviewScore)]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return jsonify({"prediction":output})

if __name__ == "__main__":
    app.run(debug=True)