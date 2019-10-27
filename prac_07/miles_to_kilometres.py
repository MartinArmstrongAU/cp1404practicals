from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKilometresApp(App):
    output_distance = StringProperty()

    def build(self):
        self.title = "Miles in Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_calculate(self, value):
        self.root.ids.output_label.text = str(value * MILES_TO_KM)

    def handle_increment(self, value, change):
        self.root.ids.input_number.text = str(value + change)


MilesToKilometresApp().run()
