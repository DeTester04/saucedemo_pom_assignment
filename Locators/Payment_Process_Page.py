from selenium.webdriver.common.by import By

class PaymentProcessLocators:
    ADD_CART_ICON = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    CHECK_OUT_BUTTON = (By.ID, "checkout")
    #CHECK_OUT_INFORMATION
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

