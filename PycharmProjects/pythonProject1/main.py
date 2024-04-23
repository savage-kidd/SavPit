from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDFloatingActionButton
# from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.list import MDList,OneLineListItem,ThreeLineListItem,ThreeLineAvatarListItem,IconLeftWidget,IconRightWidget,ImageLeftWidget,ImageRightWidget
from kivy.uix.scrollview import ScrollView
from helpers import username_helper


list_helper = """ 
Screen:
    ScrollView:
        MDList:
            id: container
"""
class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)
    #     self.theme_cls.primary_palette = "Indigo"
    #     self.theme_cls.primary_hue = "A200"
    #     self.theme_cls.theme_style = "Dark"
    #     screen = Screen()
    #     self.theme_cls.primary_palette = "Green"
        # username = MDTextField(text='Enter username',
        #                    pos_hint={'center_x':0.5,'center_y':0.5},
        #                     size_hint_x=None,width=300)
        # button = MDRectangleFlatButton(text='Show',pos_hint={'center_x':0.5,'center_y':0.4},
        #                                on_release=self.show_data)
        # self.username =  Builder.load_string(username_helper)
        # btn_flat = MDRectangleFlatButton(text='Hello King',
        #                                  pos_hint={'center_x': 0.5, 'center_y': 0.5})


        # icon_btn = MDFloatingActionButton(icon='meteor',pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # screen.add_widget(self.username)
        # screen.add_widget(button)
        return screen
        # label = MDLabel(text='Hello King',halign='center',theme_text_color='Custom',
        #                 text_color=(119/255.0,114/255.0,194/255.0,1),
        #                 font_style='Caption')
        #
        # icon_label = MDIcon(icon='microphone',pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # return icon_label

    # def show_data(self,obj):
    #     if self.username.text is "":
    #         check_string = 'Please enter a username'
    #     else:
    #         check_string = self.username.text + ' does not exist'
    #     close_button = MDFlatButton(text='Close',on_release=self.close_dialog)
    #     more_button = MDFlatButton(text='More')
    #     self.dialog = MDDialog(title='Username Check',text=check_string,
    #                       size_hint=(0.7,1),
    #                       buttons=[close_button,more_button])
    #     self.dialog.open()
    #
    # def close_dialog(self,obj):
    #     self.dialog.dismiss()

    def on_start(self):
        for i in range(20):
            items = OneLineListItem(text= 'New Release '+ str(i))
            self.root.ids.container.add_widget(items)

DemoApp().run()