from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.Locators import *
from abc import ABC


class PageElement(ABC):
    def __init__(self, driver, url: str=''):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.url = url


    def find_element(self, locator: tuple, timeout: int=15):
        """
        Find element in the page.

        Args:
            locator: tuple containing the locator.
            timeout: maximum wait time in seconds.

        Return:
            element
        """
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.visibility_of_element_located(locator))
        return element
    
    def find_elements(self, locator: tuple, timeout: int=15):
        """
        Find all elements in the page.

        Args:
            locator: tuple containing the locator.
            timeout: maximum wait time in seconds.
        Return:
            elements
        """
        wait = WebDriverWait(self.driver, timeout)
        elements = wait.until(ec.visibility_of_all_elements_located(locator))
        return elements
    
    def do_click(self, locator: tuple, timeout: int=15) -> None:
        """
        Click on element from past locator.

        Args:
            locator: tuple containing the locator.
            timeout: maximum wait time in seconds.
        Return:
            None.
        """
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.element_to_be_clickable(locator))
        return element.click()
    
    def do_send_keys(self, locator: tuple, text_to_send, timeout: int=15) -> None:
        """
        Send text to the element.

        Args:
            locator: tuple containing the locator.
            text_to_send: string to send to the element
            timeout: maximum wait time in seconds.
        Return:
            None.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(ec.visibility_of_element_located(locator), message='Element not found!').send_keys(text_to_send)
    
    def get_text_of_element(self, locator: tuple, timeout: int=15):
        """
        Get the text of the element.

        Args:
            locator: tuple containing the locator.
            timeout: maximum wait time in seconds.

        Return:
            None.
        """
        wait = WebDriverWait(self.driver, timeout)
        element = str(wait.until(ec.visibility_of_element_located(locator)).text)
        return element
    
    def open(self) -> None:
        """
        open the page.

        Return:
            None.
        """
        self.driver.get(self.url)
        return None
