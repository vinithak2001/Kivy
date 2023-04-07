from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation:"vertical"
        Label:
            text:"oral cancer daignosis"
            pos_hint:{'center_x':0.5, 'center_y':0.9}
            theme_text_color: "Primary"
            text_color:'black'
            font_style:'H3'
            font_size:'25sp'
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'

<SettingsScreen>:
    BoxLayout:
        size:root.width,root.height
        FileChooserIconView: 
            id: filechooser
            filters: ['*.png', '*.jpg']
            on_selection: selected(filechooser.selection)
        Image:
            id:"my_image"
            source:""

            
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    def selected(self,filename):
        try:
            self.ids.my_image.source=filename[0]
        except:
            pass
    
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

if __name__ == '__main__':
    TestApp().run()