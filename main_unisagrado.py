from selenium.webdriver.chrome.service import Service as ChromeService
from urls import login_page_url, home_page_url, charges_to_pay_url
from credentials import username_credentials, password_credentials
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.ChargesToPayPage import ChargesToPayPage
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from selenium import webdriver
from utils.Utils import Utils
from datetime import datetime
import os


def start_unisagrado():
    DOWNLOAD_DIR = os.path.join(os.environ["USERPROFILE"], "Desktop", "RPA", "TicketExtractionUnisagrado", "downloads")
    today = datetime.now()
    month = today.month
    name_prefix_archive = f"{month}_VINICIUS_UNISAGRADO.pdf"
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    login_page = LoginPage(driver, login_page_url)
    home_page = HomePage(driver, home_page_url)
    charges_to_pay = ChargesToPayPage(driver, charges_to_pay_url)
    utils = Utils()
    login_page.open()

    username = login_page.send_username(username_credentials)
    if username["error"]:
        print(username["data"])
        return username
    
    password = login_page.send_password(password_credentials)
    if password["error"]:
        print(password["data"])
        return password
    
    send_login_form = login_page.submit_login_form()
    if send_login_form["error"]:
        print(send_login_form["data"])
        return send_login_form

    financial_click = home_page.click_on_financial()
    if financial_click["error"]:
        print(financial_click["data"])
        return financial_click

    invoices_to_pay = home_page.click_on_invoices_to_pay()
    if invoices_to_pay["error"]:
        print(invoices_to_pay["data"])
        return invoices_to_pay
    
    download_ticket = charges_to_pay.click_on_see_ticket()
    if download_ticket["error"]:
        print(download_ticket["data"])
        return charges_to_pay
    
    validate_download = utils.validate_download(DOWNLOAD_DIR)
    if validate_download["error"]:
        print(validate_download["data"])
        return validate_download

    rename_file = utils.rename_file(DOWNLOAD_DIR, name_prefix_archive)
    if rename_file["error"]:
        print(rename_file["data"])
        return rename_file

    return {"error": False, "message": "Finished", "data": ""}

if __name__ == "__main__":
    unisagrado = start_unisagrado()
    print(unisagrado)