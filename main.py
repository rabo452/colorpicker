from pynput import mouse

from modules.gui import GuiApp
from modules.mouse_monitoring import MouseMonitoringSingleton
# inside this box the will be made screenshot
# cursor inside this box will be in center
from modules.window_screen_worker import WindowScreenWorker


# mouse onclick handler
def on_click_handler(x, y, button, pressed):
    if pressed and button == mouse.Button.right:
        screenshot_img = WindowScreenWorker().getWindowScreenshot()
        r, g, b = screenshot_img.getpixel((x, y))

        rgb_str = f"{r}, {g}, {b}"
        hex_str = "#{:02x}{:02x}{:02x}".format(r, g, b)

        GuiApp.observer_obj.pixel_hex_color = hex_str
        GuiApp.observer_obj.pixel_rgb_color = rgb_str
        GuiApp.observer_obj.updateLabels()
        GuiApp.observer_obj.rgb_color = [r, g, b]


def main():
    gui_obj = GuiApp()

    # start monitoring the mouse
    mouse_obj = MouseMonitoringSingleton()
    mouse_obj.startMonitoring(on_click_handler)

    gui_obj.run()


if __name__ == "__main__":
    main()
