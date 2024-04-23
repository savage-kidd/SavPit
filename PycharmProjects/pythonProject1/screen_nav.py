screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'Profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'Upload'

<ProfileScreen>:
    name: 'Profile'
    MDLabel:
        text: 'Welcome Trip'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'menu'

<UploadScreen>:
    name: 'Upload'
    MDLabel:
        text: 'Upload files'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'menu'

"""