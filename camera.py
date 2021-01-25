from time import sleep
import glob
from base_camera import BaseCamera
import os


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    imgs = [open(img, 'rb').read() for img in glob.glob("{}/*".format(os.environ['VOLUME_PATH']))]

    @staticmethod
    def frames():
        while True:
            for img in Camera.imgs:
                sleep(1)
                yield img
