import pytest
from selenium import webdriver

from Action.Base_Page import BaseTest, AddToCartPage
from config.configuration import Config


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
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
    driver = login.driver
    cart_page = AddToCartPage(driver)

    #ADD TO CART
    cart_page.click_test_all_the_thing_shirt()
    cart_page.click_sauce_labs_backpack()
    cart_page.click_sauce_labs_bike_light()
    cart_page.click_sauce_labs_fleece_jacket()
    cart_page.click_sauce_labs_bolt_tshirt()
    cart_page.click_sauce_labs_onesie()

    #lOGOUT
    cart_page.click_hamburger_menu()
    cart_page.click_log_out()









