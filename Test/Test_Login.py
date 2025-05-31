import pytest

from selenium import webdriver

from Action.Base_Page import BaseTest, AddToCartPage, LogoutPage, PaymentProcessPage
from config.configuration import Config
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")      # Run in headless mode
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

# Test adding product to cart/Logout
def test_add_product_to_cart(login):

    cart_page = AddToCartPage(login.driver)

    #ADD TO CART
    cart_page.click_test_all_the_thing_shirt()
    cart_page.click_sauce_labs_backpack()
    cart_page.click_sauce_labs_bike_light()
    cart_page.click_sauce_labs_fleece_jacket()
    cart_page.click_sauce_labs_bolt_tshirt()
    cart_page.click_sauce_labs_onesie()

    #Test payment process
def test_payment_process(login):

    check_out_page = PaymentProcessPage(login.driver)
    check_out_page.click_add_cart_icon()
    check_out_page.click_check_out_button()
    check_out_page.enter_name(Config.NAME)
    check_out_page.enter_last_name(Config.LASTNAME)
    check_out_page.enter_zip_postal_code(Config.POSTAL_CODE)
    check_out_page.click_continue_button()
    check_out_page.click_finish_button()
    check_out_page.click_back_home_button()

def test_logout_page_on_sauce_demo_website(login):
    log_out = LogoutPage(login.driver)

    #CLICK HAMBURGER MENU
    log_out.click_hamburger_menu()

    #CLICK LOGOUT BUTTON
    log_out.click_log_out()