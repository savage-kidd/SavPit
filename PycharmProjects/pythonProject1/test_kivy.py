#Color
#
# from kivy.lang import Builder
#
# from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel
#
# KV = '''
# MDScreen:
#
#     MDBoxLayout:
#         id: box
#         orientation: "vertical"
#
#         MDTopAppBar:
#             title: "MDLabel"
# '''
#
#
# class Test(MDApp):
#     def build(self):
#         screen = Builder.load_string(KV)
#         # Names of standard color themes.
#         for name_theme in [
#             "Primary",
#             "Secondary",
#             "Hint",
#             "Error",
#             "ContrastParentBackground",
#         ]:
#             screen.ids.box.add_widget(
#                 MDLabel(
#                     text=name_theme,
#                     halign="center",
#                     theme_text_color=name_theme,
#                 )
#             )
#         return screen


# Test().run()

#Labels

# from kivy.lang import Builder
#
# from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel
# from kivymd.font_definitions import theme_font_styles
#
#
# KV = '''
# MDScreen:
#
#     MDBoxLayout:
#         orientation: "vertical"
#
#         MDTopAppBar:
#             title: "MDLabel"
#
#         ScrollView:
#
#             MDList:
#                 id: box
# '''
#
#
# class Test(MDApp):
#     def build(self):
#         screen = Builder.load_string(KV)
#         # Names of standard font styles.
#         for name_style in theme_font_styles[:-1]:
#             screen.ids.box.add_widget(
#                 MDLabel(
#                     text=f"{name_style} style",
#                     halign="center",
#                     font_style=name_style,
#                 )
#             )
#         return screen
#
#
# Test().run()

#Icon

# MDIcon:
#     icon: "gmail"
#     pos_hint: {"center_x": .5, "center_y": .5}