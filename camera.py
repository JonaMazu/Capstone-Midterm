from flask import Response
from flask import Flask
from flask import render_template, request
import cv2

main = Flask(__name__)

vid = cv2.VideoCapture(1)

def generateFrames():
    while True:
        ret, frame = vid.read()
        if not ret:
            break
        else:
            cv2.imwrite('place.jpg',frame)
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + open('place.jpg', 'rb').read() + b'\r\n')

@main.route('/', methods = ['POST'])
def input():
    if request.method == "POST":
        print("DO SOMETHING")
    return render_template("index.html")

@main.route('/')
def index():
    return render_template('index.html') 

@main.route('/video_feed')
def video_feed():
    return Response(generateFrames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    main.run(debug=True, use_reloader=False)
