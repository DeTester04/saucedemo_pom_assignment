import time


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Locators.Login_Page import LoginLocators, LogoutLocators
from Locators.Add_To_Cart_Page import  AddToCartLocators
from Locators.Payment_Process_Page import PaymentProcessLocators


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
    def test_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.USERNAME))
        enter_username.send_keys(username)
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.SUBMIT_BUTTON))
        click_submit_button.click()
        time.sleep(DEFAULT_SLEEP_TIME)

        #HOMEPAGE/ ADD TO CART
class AddToCartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_sauce_labs_backpack(self):
        click_sauce_labs_backpack = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.SAUCE_LABS_BACKPACK))
        click_sauce_labs_backpack.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_sauce_labs_bike_light(self):
        click_sauce_labs_bike_light = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.SAUCE_LABS_BIKE_LIGHT))
        click_sauce_labs_bike_light.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_sauce_labs_bolt_tshirt(self):
        click_sauce_labs_bolt_tshirt = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.SAUCE_LABS_BOLT_TSHIRT))
        click_sauce_labs_bolt_tshirt.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_sauce_labs_fleece_jacket(self):
        click_sauce_labs_fleece_jacket = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.SAUCE_LABS_FLEECE_JACKET))
        click_sauce_labs_fleece_jacket.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_sauce_labs_onesie(self):
        click_sauce_labs_onesie = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.SAUCE_LABS_ONESIE))
        click_sauce_labs_onesie.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_test_all_the_thing_shirt(self):
        click_test_all_the_thing_shirt = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.TEST_ALL_THE_THING_SHIRT))
        click_test_all_the_thing_shirt.click()
        time.sleep(DEFAULT_SLEEP_TIME)


#Payment Process
class PaymentProcessPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_cart_icon(self):
        click_add_cart_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PaymentProcessLocators.ADD_CART_ICON))
        click_add_cart_icon.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_check_out_button(self):
        click_check_out_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PaymentProcessLocators.CHECK_OUT_BUTTON))
        click_check_out_button.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    # CHECK_OUT_INFORMATION
    def enter_name(self, enter_name):
        name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PaymentProcessLocators.NAME))
        name.send_keys(enter_name)
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_last_name(self, enter_last_name):
        last_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PaymentProcessLocators.LAST_NAME))
        last_name.send_keys(enter_last_name)
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_zip_postal_code(self, postal_code):
        zip_postal_code = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PaymentProcessLocators.ZIP_POSTAL_CODE))
        zip_postal_code.send_keys(postal_code)
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_continue_button(self):
        click_continue_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PaymentProcessLocators.CONTINUE_BUTTON))
        click_continue_button.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_finish_button(self):
        click_finish_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PaymentProcessLocators.FINISH_BUTTON))
        click_finish_button.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_back_home_button(self):
        click_back_home_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PaymentProcessLocators.BACK_HOME_BUTTON))
        click_back_home_button.click()
        time.sleep(DEFAULT_SLEEP_TIME)


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

#
    def click_hamburger_menu(self):
        click_hamburger_menu = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LogoutLocators.HAMBURGER_MENU))
        click_hamburger_menu.click()
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_log_out(self):
        click_log_out = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LogoutLocators.LOG_OUT))
        click_log_out.click()
        time.sleep(DEFAULT_SLEEP_TIME)





