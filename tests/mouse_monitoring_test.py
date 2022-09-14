import unittest
import time

from modules.mouse_monitoring import MouseMonitoringSingleton


class MouseMonitoringTest(unittest.TestCase):
    # move the mouse while testing
    def test_get_mouse_coords(self):
        obj = MouseMonitoringSingleton()
        obj.startMonitoring()

        self.assertTrue(isinstance(obj.getMouseCoords(), tuple))
        time.sleep(.5)
        self.assertNotEqual((0, 0), obj.getMouseCoords())
        print(obj.getMouseCoords())

    def test_check_singleton(self):
        try:
            MouseMonitoringSingleton()
            MouseMonitoringSingleton()
        except:
            return

        return AssertionError("singleton not working")


if __name__ == '__main__':
    unittest.main()
