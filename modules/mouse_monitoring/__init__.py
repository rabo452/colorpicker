from pynput import mouse


class MouseMonitoringSingleton:
    __mouse_coords = (0, 0)
    __obj_ref = None

    def __init__(self):
        if not self.__obj_ref:
            MouseMonitoringSingleton.__obj_ref = self
        else:
            raise Exception("this class is singleton, can't be created more than 1 instance")

    def startMonitoring(self, on_click_handler):
        def on_move(x, y):
            self.__mouse_coords = (x, y)

        listener = mouse.Listener(on_move=on_move, on_click=on_click_handler)
        listener.start()

    def getMouseCoords(self) -> tuple:
        return self.__mouse_coords
