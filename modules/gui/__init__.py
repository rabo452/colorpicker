from kivy.clock import Clock
from kivy.config import Config
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window
import pyperclip


class InterfaceObserver(BoxLayout):
    # it'll receive from out of this class
    pixel_hex_color = ""
    pixel_rgb_color = ""
    rgb_color = [0, 0, 0]

    _canvasWidget = ObjectProperty(None)
    _rgbLabel = ObjectProperty(None)
    _hexLabel = ObjectProperty(None)

    def rgbBtnOnClick(self, btn):
        pyperclip.copy(self.pixel_rgb_color)

    def hexBtnOnClick(self, btn):
        pyperclip.copy(self.pixel_hex_color)

    # update text in rgb and hex labels
    def updateLabels(self):
        self._rgbLabel.text = f"color as rgb {self.pixel_rgb_color}"
        self._hexLabel.text = f"color as hex {self.pixel_hex_color}"

    # draw the color in rectangle every 0.5 sec
    def showColor(self, p):
        with self._canvasWidget.canvas:
            rgb_color = [(value / 255) for value in self.rgb_color]
            Color(rgb_color[0], rgb_color[1], rgb_color[2])
            Rectangle(size=self._canvasWidget.size, pos=self._canvasWidget.pos)

        # call it again after some time
        Clock.schedule_once(self.showColor, .5)


class GuiApp(App):
    observer_obj = None

    def build(self):
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
        Window.size = (640, 370)
        Window.minimum_width, Window.minimum_height = Window.size

        GuiApp.observer_obj = InterfaceObserver()
        GuiApp.observer_obj.showColor([255, 0, 0])

        Clock.schedule_once(GuiApp.observer_obj.showColor, .5)

        return GuiApp.observer_obj