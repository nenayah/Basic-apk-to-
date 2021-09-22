# my pop up app

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.textinput import TextInput

#Builder.load_file("pop.kv")

class OurApk(GridLayout):
    def __init__(self, **kwargs):
        super(OurApk, self).__init__()
        self.cols = 2
        self.rows = 4

        self.add_widget(Label(text = "Student Name", color= (0.0, 0.4, 0.4,1), font_size = 20))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text = "Student Age", color= (3.0, 5.4, 0.4,1), font_size = 20))
        self.s_age= TextInput()
        self.add_widget(self.s_age)

        self.add_widget(Label(text = "Student Marks", color= (0.0, 10.4, 100.4, 71), font_size = 20))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.press = Button(text = "Enter", color= (1.0, 1, 1, 1), font_size = 20)
        self.press.bind(on_press = self.okay)
        self.add_widget(self.press)


    def okay(self, instance):
        self.box = FloatLayout()

        self.lab = (Label(text = f" Student name: {self.s_name.text} \n Student age: {self.s_age.text} \n Student marks: {self.s_marks.text}",
                          font_size=15, size_hint=(None, None), pos_hint={'x': .25, 'y': .6}))
        self.box.add_widget(self.lab)

        self.main_pop = Popup(title="pop up", content=self.box,
                              size_hint=(None, None), size=(450, 300), auto_dismiss=False, title_size=15)

        self.but = (Button(text="close", size_hint=(None, None),
                           width=200, height=50, pos_hint={'x': 0, 'y': 0}))
        self.box.add_widget(self.but)

        self.but.bind(on_press=self.main_pop.dismiss)

        self.main_pop.open()

class DemoApp(App):
    def build(self):
        return OurApk()

DemoApp().run()



