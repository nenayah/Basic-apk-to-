
import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
#
# class PageLayoutDemo(PageLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         # self.b1 = Button(
#         #     text='1',
#         #     background_color= (0.0, 0.4, 0.4,1),
#         #     color = (1, 1, 1, 1),
#         #     font_size = 195,
#         #     # font_weight =
#         # )
#         # self.add_widget(self.b1)
#
#         self.l1 = Label(
#         text='Hola!',
#         font_size = 16,
#             # size_hint = (.2, .2),
#         )
#         self.add_widget(self.l1)
#
#         self.b2 = Button(
#             text='2',
#             background_color=(2, 4, 1, 2),
#             font_size=155,
#             color = (0, 0, 0, 1)
#         )
#         self.add_widget(self.b2)
#
#
# class AdaApp(App):
#         def build(self):
#             return PageLayoutDemo()
#
# AdaApp().run()

class GridLayoutDemo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.cols = 1
        self.l1 = Label(
        text='Hola!',
        font_size = 16,
            # size_hint = (.2, .2),
        )
        self.add_widget(self.l1)

        self.b1 = Button(
            text='Click me',
            # size_hint=(.2, .2),
            background_color="green",
            color=(1, 1, 1, 1)
        )

        self.add_widget(self.b1)


class AdaApp(App):
        def build(self):
            return GridLayoutDemo()

AdaApp().run()