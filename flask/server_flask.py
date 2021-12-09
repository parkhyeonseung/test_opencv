from flask import Flask
from flask import request
from flask import Response
from flask import render_template
import cv2
from camera import gstreamer_pipeline

app = Flask(__name__)
# cap = cv2.VideoCapture(gstreamer_pipeline(),cv2.CAP_GSTREAMER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/video_feed")
def video_feed():
    return Response(stream_gen(cv2.VideoCapture(0)), mimetype='multipart/x-mixed-replace; boundary=frame')

def stream_gen(cap):
    while True:
        success, frame = cap.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('turtle.png', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 8000)