from selenium.webdriver.common.by import By

class PaymentProcessLocators:
    ADD_CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CHECK_OUT_BUTTON = (By.ID, "checkout")
    #CHECK_OUT_INFORMATION
    NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

