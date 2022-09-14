from typing import Union

from PIL import Image
import pyscreenshot


class WindowScreenWorker:
    # return screenshot as jpg
    # need to indicate the box inside that will be made screenshot
    def getWindowScreenshot(self) -> Union[None, type(Image)]:
        image = pyscreenshot.grab()
        return image