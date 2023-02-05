from .BasePage import PageElement
from locators.Locators import *


class ChargesToPayPage(PageElement):
    
    def click_on_see_ticket(self) -> dict:
        """
        Click on "See Ticket" button.

        Args:
        Return:
            dict.
        """
        try:
            self.do_click(ChargesToPayLocators.btn_see_ticket)
        except Exception as e:
            return {"error": True, "message": "Button see ticket error", "data": f"{e}"}
        
        return {"error": False, "message": "Button see ticket ok", "data": ""}
    
    
