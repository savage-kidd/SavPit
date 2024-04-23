from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import  Window

Window.size = (300,530)

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Demo'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state('toggle')]]
                        elevation: 2.5
                        
                    Widget:
                    
        MDNavigationDrawer:
            id: nav_drawer
"""

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


DemoApp().run()