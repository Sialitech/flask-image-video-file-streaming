import os
import cv2
from base_camera import BaseCamera
import glob

class Camera(BaseCamera):
    videos_cap = [cv2.VideoCapture(video) for video in glob.glob("{}/*".format(os.environ['VOLUME_PATH']))]

    @staticmethod
    def frames():
        while True:
            for idx, cap in enumerate(Camera.videos_cap):
                while(cap.isOpened()):
                    ret, img = cap.read()
                    if ret:
                        # read current frame
                        # encode as a jpeg image and return it
                        yield cv2.imencode('.jpg', img)[1].tobytes()
                    else:
                        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
