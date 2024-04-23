from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 520)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Demo'
            left_action_items: [["menu",lambda x: app.navigation_draw()]]
            right_action_items: [["rocket",lambda x: app.navigation_draw()]]
            elevation: 2.5
        MDLabel:
            text: 'New Release'
            halign: 'center'
            
        MDBottomAppBar:
        
            MDTopAppBar:
                type: "bottom"
                icon: 'language-python'
                left_action_items: [["coffee",lambda x: app.navigation_draw()]]
                elevation: 2.5
                mode: 'end'
                on_action_button: app.navigation_draw()
"""


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("Navigation")


DemoApp().run()
