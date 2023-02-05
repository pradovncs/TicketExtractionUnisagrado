from .BasePage import PageElement
from locators.Locators import *


class HomePage(PageElement):
    
    def click_on_financial(self) -> dict:
        """
        Click on "Financial" button.

        Args:
        Return:
            dict.
        """
        try:
            self.do_click(HomePageLocators.btn_financial)
        except Exception as e:
            return {"error": True, "message": "Financial button error", "data": f"{e}"}
        
        return {"error": False, "message": "Financial button ok", "data": ""}
    
    def click_on_invoices_to_pay(self) -> dict:
        """
        Click on "Invoices to Pay" button.
        
        Args:
        Return:
            dict.
        """
        try:
            self.do_click(HomePageLocators.btn_invoices_to_pay)
        except Exception as e:
            return {"error": True, "message": "Invoices button error", "data": f"{e}"}
        
        return {"error": False, "message": "Invoices button ok.", "data": ""}
    
