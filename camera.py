import time
import glob
from base_camera import BaseCamera


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    imgs = set_imgs("volume")

    def set_imgs(path):
        return [img for img in glob.glob("{}/*".format(path))]

    @staticmethod
    def frames():
        while True:
            for img in Camera.imgs:
                time.sleep(1)
                yield img
