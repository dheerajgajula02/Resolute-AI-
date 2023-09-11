from flask import Flask,Response
import cv2

app = Flask(__name__)


def another_try():
    camera = cv2.VideoCapture(0)
    print(camera.isOpened())
    count = 0
    while True:
        success, frame = camera.read()
        print(success)

        # ret, buffer = cv2.imencode('.jpg', frame)
        # frame = buffer.tobytes()
        # yield (b'--frame\r\n'
        #         b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        count += 1
        print(count)
        if count > 10000:
            break
    camera.release()

# def gen_frames():
#     print("gen_frames")
#     while True:
#         success, frame = camera.read()
#         print(success)

#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                 b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return "Hello World!"

@app.route('/video_feed')
def video():
    camera = cv2.VideoCapture(0)
    count = 0
    while True:
        success, frame = camera.read()
        print(success)

        # ret, buffer = cv2.imencode('.jpg', frame)
        # frame = buffer.tobytes()
        # yield (b'--frame\r\n'
        #         b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        count += 1
        print(count)
        if count > 10000:
            break
    camera.release()
    
    return {"hello":"world"}

@app.route('/video_feed2')
def video2():
    another_try()

    return {"hello":"world"}

if __name__ == '__main__':
    app.run(debug=True, port=8000)


