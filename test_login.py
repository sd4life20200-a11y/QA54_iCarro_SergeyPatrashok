import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from credentials import EMAIL, PASSWORD


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get("https://icarro-v1.netlify.app/login")
    yield browser
    browser.quit()


class TestLogin:

    def test_successful_login(self, driver):

        driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(EMAIL)

        driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(PASSWORD)

        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        driver.find_element(By.XPATH, "//a[text()='OK']").click()

        logout_button = driver.find_element(By.XPATH, "//button[text()='Log out']")

        assert logout_button.is_displayed()
