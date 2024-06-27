from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp
import os
import sqlite3

# importing custom modules
from user_data import create_user
from user_stock_data import access_inventory

from client import data_sender

Window.size = (310, 580)

class LoginScreen(Screen):
    pass

class Content(MDFloatLayout):
    pass


conn = sqlite3.connect("Userdata.db")
class DiguoApp(MDApp):
    def build(self):
        self.main_screen_manager = ScreenManager()
        main_screen = Builder.load_file("main.kv")
        home_screen = Builder.load_file("home.kv")
        login_screen = Builder.load_file("login.kv")
        signup_screen = Builder.load_file("signup.kv")
        # definitions of different sub widgets
        define = Builder.load_file("definitions.kv")


        self.main_screen_manager.add_widget(main_screen)
        self.main_screen_manager.add_widget(home_screen)
        self.main_screen_manager.add_widget(login_screen)
        self.main_screen_manager.add_widget(signup_screen)
        return self.main_screen_manager

    def add_user(self,username,password,email):
        create_user(username,password,email)
    def check_user(self,username,password):
        """checks the login if valid"""
        if data_sender(username,password) == "Login successful!":
            self.main_screen_manager.current = "home"
        else :
            print("f you")

    def fill_inventory(self,*args):
        """refresh rows and add items"""
        items_dialog = MDDialog(title="Enter new item",
                                type = "custom",
                               content_cls = Content() )

        items_dialog.open()

    def create_stock_list(self,screen):
        """will create stock list to be intergrated into the application."""
        stock_list = access_inventory(conn)
        Inventory_layout = MDFloatLayout()
        Inventory_list = MDDataTable(
            size_hint = (.9,.9),
            pos_hint = {"center_x":.5,"center_y":.45},
            check = True,
            column_data=[("NO.",dp(20)),("Name",dp(30)),("No_available",dp(20)),("sales",dp(10)),("price",dp(20)),("usage",dp(20)),("type",dp(20))],
            row_data = [item for item in stock_list],
        )
        self.add_button = MDIconButton(icon="plus",on_release = self.fill_inventory)

        Inventory_layout.add_widget(Inventory_list)
        Inventory_layout.add_widget(self.add_button)
        screen.add_widget(Inventory_layout)



if __name__ == "__main__":
    # Get the absolute path to the Poppins folder
    poppins_folder = os.path.join("/home", "barryodoro", "PycharmProjects", "diguo_1", "Poppins")
    # Register the font files using the absolute paths
    LabelBase.register(name="MPoppins", fn_regular=os.path.join(poppins_folder, "Poppins-Medium.ttf"))
    LabelBase.register(name="BPoppins", fn_regular=os.path.join(poppins_folder, "Poppins-SemiBold.ttf"))

    DiguoApp().run()

