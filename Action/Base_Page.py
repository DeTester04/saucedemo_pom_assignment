import time



from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from Locators.Add_To_Cart_Page import  AddToCartLocators
from Locators.Log_In_Page import LogOutLocators, LoginLocators
from Locators.Payment_Process_Page import PaymentProcessLocators
from selenium.common.exceptions import TimeoutException




#Time Variable
DEFAULT_SLEEP_TIME = 5

class BaseTest:
    #Initializing our browser
    def __init__(self, driver):
        self.driver = driver

#calling our URL
    def open_login_page(self, url):
        self.driver.get(url)

#lOGIN PAGE
    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(LoginLocators.USERNAME))
        enter_username.send_keys(username)
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(LoginLocators.SUBMIT_BUTTON))
        click_submit_button.click()
        time.sleep(DEFAULT_SLEEP_TIME)

        #HOMEPAGE/ ADD TO CART
class AddToCartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_product(self, locator):
         WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
            ).click()

    def click_sauce_labs_backpack(self):
        self.click_product(AddToCartLocators.SAUCE_LABS_BACKPACK)

    def click_sauce_labs_bike_light(self):
        self.click_product(AddToCartLocators.SAUCE_LABS_BIKE_LIGHT)

    def click_sauce_labs_bolt_tshirt(self):
        self.click_product(AddToCartLocators.SAUCE_LABS_BOLT_TSHIRT)

    def click_sauce_labs_fleece_jacket(self):
        self.click_product(AddToCartLocators.SAUCE_LABS_FLEECE_JACKET)

    def click_sauce_labs_onesie(self):
        self.click_product(AddToCartLocators.SAUCE_LABS_ONESIE)

    def click_test_all_the_thing_shirt(self):
        self.click_product(AddToCartLocators.TEST_ALL_THE_THING_SHIRT)


class PaymentProcessPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def wait_and_type(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).send_keys(text)

    def click_add_cart_icon(self):
        self.wait_and_click(PaymentProcessLocators.ADD_CART_ICON)

    def click_check_out_button(self):
        self.wait_and_click(PaymentProcessLocators.CHECK_OUT_BUTTON)

    def enter_first_name(self, first_name):
        self.wait_and_type(PaymentProcessLocators.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.wait_and_type(PaymentProcessLocators.LAST_NAME, last_name)

    def enter_zip_postal_code(self, zip_postal_code):
        self.wait_and_type(PaymentProcessLocators.ZIP_POSTAL_CODE, zip_postal_code)

    def click_continue_button(self):
        self.wait_and_click(PaymentProcessLocators.CONTINUE_BUTTON)

#Checkout: Overview
    def click_finish_button(self):
        self.wait_and_click(PaymentProcessLocators.FINISH_BUTTON)

#Checkout: Complete!
    def click_back_home_button(self):
        self.wait_and_click(PaymentProcessLocators.BACK_HOME_BUTTON)

#click hamburger menu select logout
class LogInPage:
    def __init__(self, driver):
        self.driver = driver

    def click_hamburger_menu_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LogOutLocators.HAMBURGER_MENU)
        ).click()

    def click_log_out_button(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(LogOutLocators.LOG_OUT)
            ).click()
        except TimeoutException as e:
            self.driver.save_screenshot("logout_button_failure.png")
            print(f"TimeoutException: Logout button not clickable. Current URL: {self.driver.current_url}")
            with open("page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise e

