from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKilometresApp(App):
    output_distance = StringProperty()

    def build(self):
        self.title = "Miles in Kilometres"
        self.root = Builder.load_file('miles_to_kilometres_2.kv')
        return self.root

    def handle_calculate(self, text):
        value = self.convert_to_number(text)
        # self.root.ids.output_label.text = str(value * MILES_TO_KM)
        self.output_distance = str(value * MILES_TO_KM)

    def handle_increment(self, text, change):
        value = self.convert_to_number(text)
        self.root.ids.input_number.text = str(value + change)

    @staticmethod
    def convert_to_number(text):
        try:
            value = float(text)
            return value
        except ValueError:
            return 0.0


MilesToKilometresApp().run()
