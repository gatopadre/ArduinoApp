from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from python.controllers import Arduino



class mainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(mainScreen, self).__init__(**kwargs)
        self.rows = 3
        self.add_widget(Label(text='Seleccione una accion:'))
        self.action = TextInput(multiline=False)
        self.add_widget(self.action)
        self.on_led_btn = Button(text='Led On')
        self.add_widget(self.on_led_btn)


    def on_led_action(self):
        Arduino.connect()
        message_to_arduino = '1'
        Arduino.send_order(message_to_arduino)
        Arduino.disconnect()
