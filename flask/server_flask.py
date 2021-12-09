from flask import Flask
import cv2
from camera import gstreamer_pipeline

app = Flask(__name__)
@app.route("/")
def helloworld():
    str = "Hello World! park"
    return str

if __name__ == '__main__':
    # cap = cv2.VideoCapture(gstreamer_pipeline(),cv2.CAP_GSTREAMER)
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret,frame = cap.read()
        cv2.imshow('web',frame)
        cv2.waitKey(1)
        pass

    app.run(host = '0.0.0.0',port = 8000)