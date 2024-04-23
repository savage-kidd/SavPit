from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.button import MDRectangleFlatButton


class App(MDApp):
    def build(self):
        label = MDLabel(text="Lets Take A Trip", halign="center", theme_text_color="Error",
                        font_style="H6")
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style ="Dark"
        screen = Screen()

        screen.add_widget(label)
        return screen


App().run()
