from flask import Flask, jsonify, request
import cv2
import numpy as np

app= Flask(__name__)

@app.route("/",methods=['POST'])
def index():
	if request.files:
		# try:
		# 	filestr = request.files['file'].read()
		# 	npimg = np.frombuffer(filestr, np.uint8)
		# 	img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
		# 	_,_ = img.shape[:2]
		# except Exception as e:
		# 	return ({"message":"Invalid Image File","error":str(e)})
		# else:
		# 	img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
		# 	return({"message":"File Used"})
		file=request.files['file']
		file.save(file.filename)
		return({"message":"File Saved."})
	else:
		return jsonify({"message":"No file found!"})

if __name__ =="__main__":
	app.run(debug=True)