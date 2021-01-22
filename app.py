#!/usr/bin/env python
from importlib import import_module
import os
import sys
from flask import Flask, render_template, Response

# import camera driver
if os.environ('SRC') == 'video':
    # Camera = import_module('camera_' + os.environ['CAMERA']).Camera
    from camera_opencv import Camera
elif os.environ('SRC') == 'images':
    from camera import Camera
else:
    sys.exit()
# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)


@app.route('/webpage')
def webpage():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
