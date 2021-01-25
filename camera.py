from time import sleep
import glob
from base_camera import BaseCamera
import os
import cv2


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    imgs = [cv2.imread(img) for img in glob.glob("{}/*".format(os.environ['VOLUME_PATH']))]
    imgs_bytes = [cv2.imencode('.jpg', img)[1].tobytes() for img in imgs]
    @staticmethod
    def frames():
        while True:
            for img in Camera.imgs_bytes:
                sleep(1)
                yield img
