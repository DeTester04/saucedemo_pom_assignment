import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Locators.Login_Page import LoginLocators
from Locators.Add_To_Cart_Page import  AddToCartLocators


class BaseTest:
    #Initializing our browser
    def __init__(self, driver):
        self.driver = driver

#calling our URL
    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.USERNAME))
        enter_username.send_keys(username)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.SUBMIT_BUTTON))
        click_submit_button.click()
        time.sleep(5)

        #homepage/ ADD TO CART
class AddToCartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_sauce_labs_backpack(self):
        click_sauce_labs_backpack = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.SAUCE_LABS_BACKPACK))
        click_sauce_labs_backpack.click()
        time.sleep(5)

    def click_sauce_labs_bike_light(self):
        click_sauce_labs_bike_light = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.SAUCE_LABS_BIKE_LIGHT))
        click_sauce_labs_bike_light.click()
        time.sleep(5)

    def click_sauce_labs_bolt_tshirt(self):
        click_sauce_labs_bolt_tshirt = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.SAUCE_LABS_BOLT_TSHIRT))
        click_sauce_labs_bolt_tshirt.click()
        time.sleep(5)

    def click_sauce_labs_fleece_jacket(self):
        click_sauce_labs_fleece_jacket = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.SAUCE_LABS_FLEECE_JACKET))
        click_sauce_labs_fleece_jacket.click()
        time.sleep(5)

    def click_sauce_labs_onesie(self):
        click_sauce_labs_onesie = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.SAUCE_LABS_ONESIE))
        click_sauce_labs_onesie.click()
        time.sleep(5)

    def click_test_all_the_thing_shirt(self):
        click_test_all_the_thing_shirt = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.TEST_ALL_THE_THING_SHIRT))
        click_test_all_the_thing_shirt.click()
        time.sleep(5)

    def click_hamburger_menu(self):
        click_hamburger_menu = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.HAMBURGER_MENU))
        click_hamburger_menu.click()
        time.sleep(5)

    def click_log_out(self):
        click_log_out = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocators.LOG_OUT))
        click_log_out.click()
        time.sleep(5)








