import time
import glob
from base_camera import BaseCamera
import os
import cv2
class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    # imgs = [open(img, 'rb').read() for img in glob.glob("{}/*".format(os.environ['VOLUME_PATH']))]
    videos = [video for video in glob.glob("{}/*".format(os.environ['VOLUME_PATH']))]
    print(videos[0])
    @staticmethod
    def frames():
        cam = cv2.VideoCapture("/flask-image-video-file-streaming/files/Friends.mp4")
        while True:
            success, img = cam.read()
            print(img)
            print(success)
            print("SUCCESS")
            img_encoded = cv2.imencode('.jpg', img)[1]
            img_bytes = img_encoded.tobytes()
            yield img_bytes
