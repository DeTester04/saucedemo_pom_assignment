import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from Action.Base_Page import BaseTest, AddToCartPage, PaymentProcessPage, LogInPage
from Locators.Add_To_Cart_Page import AddToCartLocators
from selenium.webdriver.support import expected_conditions as EC

from Locators.Log_In_Page import LogOutLocators, LoginLocators
from Locators.Payment_Process_Page import PaymentProcessLocators
from config.configuration import Config
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")      # Run in headless mode
    chrome_options.add_argument("--disable-gpu")   # Prevent GPU errors in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)                     # Wait implicitly up to 20s
    driver.maximize_window()                       # Maximize window (has no effect in headless, but harmless)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = BaseTest(driver)
    login_page.open_login_page(Config.BASE_URL)
    return login_page

#Log in page
def test_login_page_on_sauce_demo_website(login):
    login.enter_username(Config.USERNAME)
    login.enter_password(Config.PASSWORD)
    login.click_submit_button()

    # Wait for any element on the home page after login
    WebDriverWait(login.driver, 10).until(
        EC.visibility_of_element_located(AddToCartLocators.SAUCE_LABS_BACKPACK)
    )

# Test_Page adding product to cart/Logout
def test_add_product_to_cart(login):

    cart_page = AddToCartPage(login.driver)

    #ADD TO CART
    cart_page.click_test_all_the_thing_shirt()
    cart_page.click_sauce_labs_backpack()
    cart_page.click_sauce_labs_bike_light()
    cart_page.click_sauce_labs_fleece_jacket()
    cart_page.click_sauce_labs_bolt_tshirt()
    cart_page.click_sauce_labs_onesie()

    #Test_Page payment process
def test_payment_process(login):

    check_out_page = PaymentProcessPage(login.driver)

     #PAYMENT PROCESS
    check_out_page.click_add_cart_icon()
    WebDriverWait(login.driver, 10).until(
        EC.visibility_of_element_located(PaymentProcessLocators.CHECK_OUT_BUTTON)
    )
    check_out_page.click_check_out_button()

    WebDriverWait(login.driver, 10).until(
        EC.visibility_of_element_located(PaymentProcessLocators.FIRST_NAME)
    )

    check_out_page.enter_first_name(Config.FIRSTNAME)
    check_out_page.enter_last_name(Config.LASTNAME)
    check_out_page.enter_zip_postal_code(Config.ZIP_POSTAL_CODE)
    check_out_page.click_continue_button()

    WebDriverWait(login.driver, 10).until(
        EC.element_to_be_clickable(PaymentProcessLocators.FINISH_BUTTON)
    )

    check_out_page.click_finish_button()

    WebDriverWait(login.driver, 10).until(
        EC.element_to_be_clickable(PaymentProcessLocators.BACK_HOME_BUTTON)
    )

    check_out_page.click_back_home_button()

def test_logout_page_on_sauce_demo_website(login):

    log_out_page = LogInPage(login.driver)

    log_out_page.click_hamburger_menu_button()

    WebDriverWait(login.driver, 10).until(
        EC.element_to_be_clickable(LogOutLocators.LOG_OUT)
    )

    log_out_page.click_log_out_button()

    # Confirm redirected to login page
    WebDriverWait(login.driver, 10).until(
        EC.visibility_of_element_located(LoginLocators.USERNAME)
    )



