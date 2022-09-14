import unittest

from modules.window_screen_worker import WindowScreenWorker


class MyTestCase(unittest.TestCase):
    def test_screenshot_grab(self):
        img = WindowScreenWorker().getWindowScreenshot((100, 1000, 200, 1780))
        img.show()


if __name__ == '__main__':
    unittest.main()
