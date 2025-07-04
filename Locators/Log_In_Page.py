from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "login-button")

class LogOutLocators:
    HAMBURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOG_OUT = (By.ID, "logout_sidebar_link")




