from selenium import webdriver
import time
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from pynput.mouse import Listener
from pynput import keyboard
#import keyboard

b = webdriver.Chrome(executable_path=r'chromedriver.exe')
b.maximize_window()


class EventListeners(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        print("before_navigate_to %s" % url)

    def after_navigate_to(self, url, driver):
        print("after_navigate_to %s" % url)

    def before_click(self, element, driver):
        print("before_click %s" % element)

    def after_click(self, element, driver):
        print("after_click %s" % element)

    def after_navigate_forward(self, driver):
        print("after_navigate_forward")

    def before_navigate_forward(self, driver):
        print("before_navigate_forward")

    def after_navigate_back(self, driver):
        print("after_navigate_back")

    def before_navigate_back(self, driver):
        print("before_navigate_back")

    def before_change_value_of(self, element, driver):
        print("before_change_value_of")


d = EventFiringWebDriver(b, EventListeners())

spisok = []


def on_click(x, y, button, pressed):
    print(button, x, y, pressed)
    if pressed:
        print('Mouse clicked')
        try:
            print(b.current_url)
            if b.current_url == 'https://vk.com/':
                while b.current_url == 'https://vk.com/':
                    keyboard.Listener(on_press=on_press).join()
        except:
            b.switch_to.window(d.window_handles[0])


with Listener(on_click=on_click) as listener:
    listener.join()
