from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
    REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "input#id_registration-redirect_url+button.btn")

class ProductPageLocators():
    BASKET_BUTTON_LINK = (By.CSS_SELECTOR, "form#add_to_basket_form > button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "h1 + .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong ")
    PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, "div.row h1")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:first-child")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_PRODUCTS = (By.CSS_SELECTOR, "form.basket_summary")
    BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner > p")
    BASKET_EMPTY_LINK_A = (By.CSS_SELECTOR, "div#content_inner > p >a")