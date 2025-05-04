# sauced emo_pom_assignment

A **step-by-step guide** 
to set up the **Page Object Model (POM)** in **PyCharm**
---

## ✅ Step 1: Set Up Your Project in PyCharm

1. **Open PyCharm**
2. **Create a New Project**  
   - File > New Project  
   - Choose a directory and name your project, e.g., `automation_project`
3. **Set up a Virtual Environment**  
   PyCharm will prompt you to create a virtual environment. Make sure it's checked and Python interpreter is selected.

---

## ✅ Step 2: Project Directory Structure (POM-Friendly)

Create the following folder structure:

```
automation_project/
│
├── config/                # For configuration files
│   └── config.yaml
│
├── pages/                 # Page classes for UI elements
│   └── login_page.py
│
├── tests/                 # Your test scripts
│   └── test_login.py
│
├── utils/                 # Helper functions or common actions
│   └── base_page.py
│
├── requirements.txt       # Dependencies
└── conftest.py            # Pytest setup (optional)
```

---

## ✅ Step 3: Install Required Packages

Go to the PyCharm Terminal and install:

```bash
pip install selenium pytest pyyaml
```

Also, save them in `requirements.txt`:

```txt
selenium
pytest
pyyaml
```

To save manually:
```bash
pip freeze > requirements.txt
```

---

## ✅ Step 4: Create a config File

In `config file

base_url: "https://example.com"
username: "tester"
password: "secure password"
browser: "chrome"


## ✅ Step 6: Base Page Setup 

python

Action page 
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text


## ✅ Step 7: Example of Locator (pages/login_page.py)


class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginBtn")


## ✅ Step 8: Example Test Case (`tests/test_login.py`)


import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import load_config

config = load_config()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(config['base_url'])
    yield driver
    driver.quit()

def test_login(driver):
    page = LoginPage(driver)
    page.login(config['username'], config['password'])
    assert "Dashboard" in driver.Title


## ✅ Step 9: Run the Test in PyCharm

Right-click `test_login.py` > Run ‘pytest in test_login.py’


pytest --html=report.html -p no:warnings - to run and generate test report