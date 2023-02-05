from .BasePage import PageElement
from locators.Locators import *


class LoginPage(PageElement):
    
    def send_username(self, username: str) -> dict:
        """
        Send the username.
        
        Args:
            username: str containing the username.

        Return:
            dict.
        """
        try:
            self.do_send_keys(LoginPageLocators.username_field, username)

        except Exception as e:
            return {"error": True, "message": "Error in login field", "data": f"{e}"}
        
        return {"error": False, "message": "Useraname ok", "data": ""}
    
    def send_password(self, password: str) -> dict:
        """
        Send the password.
        
        Args:
            password: str containing the password.

        Return:
            dict.
        """
        try:
            self.do_send_keys(LoginPageLocators.password_field, password)

        except Exception as e:
            return {"error": True, "message": "Error in password field", "data": f"{e}"}
        
        return {"error": False, "message": "Password ok", "data": ""}
    
    def submit_login_form(self) -> dict:
        """
        Submit the login form.

        Args:
        Return:
            None.
        """
        try:
            self.do_click(LoginPageLocators.btn_login)
        except Exception as e:
            return {"error": True, "message": "Error to submit the login form", "data": f"{e}"}
        
        return {"error": False, "message": "Login success", "data": f""}
