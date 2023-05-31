from PyQt5 import QtWidgets
import Log_in_form
import Sign_in_form
import U_profile_form
import Forgot_pass_form
import Change_pass_form
import Change_login_form
import Change_name_form
import json
import os
from db_handler import SqliteDB


class ControlWindow:
    
    def __init__(self):
        self.session_id = Log_in_form.session_id
        
        User_data, self.session_binary_avatar = SqliteDB.get_user_data(None, self.session_id)
        if User_data is None:
            self.session_login = None
            self.session_name = None
        else:
            self.session_login = User_data["P_email_adress"]
            self.session_name = User_data["P_name"]

    def show_login(self):
        self.login_window = Log_in_form.LoginWindow()
        self.login_window.show()
    
    def show_sign_in(self):
        self.sign_in_window = Sign_in_form.RegistrationWindow()
        self.sign_in_window.show()

    def show_profile(self):
        self.profile_window = U_profile_form.ProfileWindow()
        self.profile_window.show()

    def show_forgot_pass(self):
        self.forgot_pass = Forgot_pass_form.ForgotPassWindow()
        self.forgot_pass.show()

    def show_change_pass(self):
        self.change_pass = Change_pass_form.ChangePassWindow()
        self.change_pass.show()

    def show_change_login(self):
        self.change_login = Change_login_form.ChangeLoginWindow()
        self.change_login.show()

    def show_change_name(self):
        self.change_name = Change_name_form.ChangeNameWindow()
        self.change_name.show()

        
class ControlAPI:
    def __init__(self):
        self.new_group = None
        with open('C:\\Solar Control\\Solar-Control\\PY\\new_group.txt', 'r') as file:
            data = file.read()
            if not data:  
                self.new_group = None
            else:
                parsed_data = json.loads(data)
                self.new_group = parsed_data

    def update_new_data(self,added_group_id):
        existing_data = []
        file_path = 'C:\\Solar Control\\Solar-Control\\PY\\new_group.txt'
        if os.path.isfile(file_path) and os.stat(file_path).st_size != 0:
            with open(file_path, 'r') as file:
                existing_data = json.load(file)

        existing_data = [data for data in existing_data if data["id"] != added_group_id]
        updated_data = json.dump(existing_data)

        with open(file_path, 'w') as file:
            file.write(updated_data)



    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    control = ControlWindow()
    control.show_login()
    app.exec_()