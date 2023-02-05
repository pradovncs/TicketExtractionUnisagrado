from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    username_field = (By.CSS_SELECTOR, "input[name='username']")
    password_field = (By.CSS_SELECTOR, "input[name='password']")
    btn_login = (By.ID, "button-login")


class HomePageLocators(object):
    btn_financial = (By.CSS_SELECTOR, "a[class='new_navigation-item--link'] i[class='icon ion-cash iconfix placeholder-icon ']")
    btn_invoices_to_pay = (By.CSS_SELECTOR, "a[href='#/home/pgtocobrancas']")


class ChargesToPayLocators(object):
    btn_see_ticket = (By.CSS_SELECTOR, "a[class='link-item-boleto btn-payment-anexo cursor-pointer'] i[class='fa placeholder-icon fa-barcode']")
    