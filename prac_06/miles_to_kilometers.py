from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometers.kv')

        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) * 1.60934
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = '0.00'

    def handle_increment(self, value):
        try:
            if not self.root.ids.input_number.text:
                self.root.ids.input_number.text = str(0)
            else:
                result = int(self.root.ids.input_number.text) + value
                self.root.ids.input_number.text = str(result)
        except ValueError:
            self.root.ids.input_number.text = '0'



MilesConverterApp().run()