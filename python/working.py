import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from views import mainScreen as mainScreen


class ArduinoApp(App):

    def build(self):
        return mainScreen.mainScreen()


if __name__ == '__main__':
    ArduinoApp().run()