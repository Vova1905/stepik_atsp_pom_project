from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini>span>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD2 = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_TITLE = (By.TAG_NAME, "h1")
    PRICE_TEXT = (By.CSS_SELECTOR, ".product_main>p.price_color")
    BOUGHT_TITLE = (By.CSS_SELECTOR, ".alert:nth-child(1)>div>strong")
    BASKET_COST = (By.CSS_SELECTOR, ".alert:nth-child(3)>div>p>strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")

class BasketPageLocators():
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner>p")
