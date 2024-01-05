from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.core.text import LabelBase
import os

Window.size = (310, 580)

class LoginScreen(Screen):
    pass

class DiguoApp(MDApp):
    def build(self):
        main_screen_manager = ScreenManager()
        main_screen = Builder.load_file("main.kv")
        login_screen = Builder.load_file("login.kv")
        signup_screen = Builder.load_file("signup.kv")


        main_screen_manager.add_widget(main_screen)
        main_screen_manager.add_widget(login_screen)
        main_screen_manager.add_widget(signup_screen)
        return main_screen_manager

if __name__ == "__main__":
    # Get the absolute path to the Poppins folder
    poppins_folder = os.path.join("/home", "barryodoro", "PycharmProjects", "diguo_1", "Poppins")
    # Register the font files using the absolute paths
    LabelBase.register(name="MPoppins", fn_regular=os.path.join(poppins_folder, "Poppins-Medium.ttf"))
    LabelBase.register(name="BPoppins", fn_regular=os.path.join(poppins_folder, "Poppins-SemiBold.ttf"))

    DiguoApp().run()
