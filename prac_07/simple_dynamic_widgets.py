from kivy.app import App
from kivy.lang import Builder
# from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty


class SimpleDynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self):
        super().__init__()
        self.names = ["Martin Armstrong", "Zackary Wright", "Fletcher Hartley", "Phillip Cluff"]

    def build(self):
        self.title = "Simple Dynamic Widgets"
        self.root = Builder.load_file('simple_dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            # text = Label(text=name)
            text = Button(text=name)
            self.root.ids.output_label.add_widget(text)


SimpleDynamicWidgetsApp().run()
