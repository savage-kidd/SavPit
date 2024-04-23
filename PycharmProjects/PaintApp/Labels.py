from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (1, 1, 0, 1)


class MainApp(App):
    def build(self):
        label = Label(text="I'm Dark", font_size='28sp', bold=True,
                      color=(0, 0, 0, 1),
                      italic=True)
        return label


MainApp().run()
