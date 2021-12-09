import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from controllers import Arduino

class mainScreen(App):
    def build(self):
        layout = FloatLayout()
        on_led_btn = Button(pos_hint={'x': 0, 'center_y': .1}, size_hint=(.1, .1), text= 'Turn Led On')
        on_led_btn.bind(on_press=self.turn_on)
        layout.add_widget(on_led_btn)
        off_led_btn = Button(pos_hint={'x': .1, 'center_y': .1}, size_hint=(.1, .1), text='Turn Led Off')
        off_led_btn.bind(on_press=self.turn_off)
        layout.add_widget(off_led_btn)
        return layout

    def turn_on(self, event):
        print("Turning Led On")
        message_to_arduino = '1'
        result = Arduino.send_order(message_to_arduino)
        print(result)

    def turn_off(self, event):
        print("Turning Led Off")
        message_to_arduino = '0'
        result = Arduino.send_order(message_to_arduino)
        print(result)


def ArduinoApp(App):
    Arduino.connect()
    mainScreen().run()
    Arduino.disconnect()
    return True


if __name__ == '__main__':
    ArduinoApp(App)
