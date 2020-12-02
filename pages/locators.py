from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_TITLE = (By.TAG_NAME, "h1")
    PRICE_TEXT = (By.CSS_SELECTOR, ".product_main>p.price_color")
    BOUGHT_TITLE = (By.CSS_SELECTOR, ".alert:nth-child(1)>div>strong")
    BASKET_COST = (By.CSS_SELECTOR, ".alert:nth-child(3)>div>p>strong")
