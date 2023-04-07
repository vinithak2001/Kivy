import os
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.filemanager import MDFileManager
from kivy.lang import Builder

Builder.load_string("""
<MenuScreen>:
    MDBoxLayout:
        adaptive_height: True
        orientation: "vertical"
        spacing: "100dp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
        MDLabel:
            text: "Oral Cancer Detection"
            halign: 'center'
            theme_text_color: "Primary"
            text_color: 'black'
            font_style: 'H3'
            font_size: '25sp'
            
        MDRaisedButton:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            text: "Goto Settings"
            on_press: root.manager.current = 'settings'
            
<SettingsScreen>:
    MDBoxLayout:
        spacing: "10dp"
        orientation: 'vertical'
        
        MDRaisedButton:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            text: "Choose Image"
            on_press: root.file_manager_open()
        
        FitImage:
            id: my_image
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: 0.5, 1
            source: ''
            
""")


class MenuScreen(MDScreen):
    pass


class SettingsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True
        )

    def file_manager_open(self):
        # for windows
        # self.file_manager.show(".")

        # for linux
        self.file_manager.show(os.path.expanduser("~"))
        self.manager_open = True

    def select_path(self, path: str):
        self.exit_manager()
        self.ids.my_image.source = path

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()


class CancerDetectionApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        # create the screen manager
        sm = MDScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(SettingsScreen(name="settings"))

        return sm


if __name__ == '__main__':
    CancerDetectionApp().run()
