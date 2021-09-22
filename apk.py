import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class OurApk(GridLayout):
    def __init__(self, **kwargs):
        super(OurApk, self).__init__()
        self.cols = 2

        self.add_widget(Label(text = "Student Name", color= (0.0, 0.4, 0.4,1), font_size = 20
            )
        )
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text = "Student Age", color= (3.0, 5.4, 0.4,1), font_size = 20))
        self.s_age= TextInput()
        self.add_widget(self.s_age)

        self.add_widget(Label(text = "Student Gender", color= (0.0, 10.4, 100.4, 71), font_size = 20))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text = "Enter", color= (1.0, 1, 1, 1), font_size = 20)
        self.press.bind(on_press = self.okay)
        self.add_widget(self.press)

    def okay(self, instance):
        print(f"Student name: {self.s_name.text}")
        print(f"Student age: {self.s_age.text}")
        print(f"Student gender: {self.s_gender.text}")
        print(" ")

class DemoApp(App):
    def build(self):
        return OurApk()

DemoApp().run()


