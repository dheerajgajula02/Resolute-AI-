from flask import Flask, jsonify, request
import werkzeug
import os
from deepface import DeepFace
import matplotlib.pyplot as plt

app = Flask(__name__)




@app.route("/register", methods=["POST"])
def register():
    images = request.files['image']
    filename = werkzeug.utils.secure_filename(images.filename)
    path = "buffer/" + filename
    images.save("./buffer/" + filename)

    path = "buffer/" + filename
    face_path = "face_db/"+filename
    face_objs = DeepFace.extract_faces(img_path=path,target_size=(244,244), detector_backend='opencv')
    print(face_objs)

    plt.imsave(face_path,face_objs[0]['face'])


    

    for files in os.listdir("./buffer"):
        # remove files in this directory
        os.remove("./buffer/" + files)

    return jsonify({
        "message": "success",
        "path": path
    })

@app.route("/register_test", methods=['POST'])
def register_test():
    images = request.files['image']
    print(images)
    return "read"

@app.route("/verify", methods=['POST'])
def verify():
    images = request.files['image']
    filename = werkzeug.utils.secure_filename(images.filename)
    path = "buffer/" + filename
    images.save("./buffer/" + filename)
    path = "buffer/" + filename
    

    dfs = DeepFace.find(img_path = path,db_path="face_db")

    for files in os.listdir("./buffer"):
    # remove files in this directory
        os.remove("./buffer/" + files)

    if dfs[0].shape[0] == 0:
        return jsonify({
            "message": "failed to verify, make sure you registered"
        })
    else:
        return jsonify({
            "message": "success",
            "distance": dfs[0]['identity'][0]
        })
    pass





@app.route("/test", methods=['GET'])
def test():
    return jsonify({
        "message": "success"
    })

@app.route("/")
def home():
    return jsonify({
        "message": "hello world"
    })

if __name__ == "__main__":
    app.run(port=3000, host="0.0.0.0")



