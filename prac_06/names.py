
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class NameDisplayApp(App):
    """ Main program - Kivy app to demo dynamic widget creation """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        # basic data example - dictionary of names
        self.names = ("Bob Brown", "Cat Cyan", "Oren Ochre", "Joshua Stanley")

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Names List"
        self.root = Builder.load_file('names.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        :return: None
        """
        for name in self.names:
            temp_label = Label(text=name)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_label)


NameDisplayApp().run()


