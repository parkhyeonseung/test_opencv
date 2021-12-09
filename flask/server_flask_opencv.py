from flask import Flask
import cv2
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return
def stream(cap):
    while cap.isOpend():
        ret,frame = cap.read()
        if not ret:break
        cv2.imshow('a',frame)
        cv2.waitKey(1)

def run():
    app.run(host = '0.0.0.0',port = 8000)
    return


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cam = threading.Thread(target = stream,args=(cap,))
    cam.daemon = True
    cam.start()
    app.run(host = '0.0.0.0',port = 8000)
    
    pass