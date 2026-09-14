import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
import pytest

USERS = {
    'goodUser': {
        'email': 'hiwasi1765@wisnick.com',
        'password': 'tesztelek2021'
    }
}


class TestHootel(object):
    def setup_method(self):
        URL = 'http://hotel-v3.progmasters.hu/'
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--guest')
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        print(self.browser.get_window_size())
        self.browser.set_window_size(1024, 768)
        print(self.browser.get_window_size())

    def teardown_method(self):
        # self.browser.quit()
        pass

    @allure.title("Hootel Login")
    @allure.description("A belépés tesztelése")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("login", 'Hootel', 'happy-path')
    def test_login(self):
        login_btn = self.browser.find_element(By.XPATH, '//a[@class="nav-link"]')
        # time.sleep(1)
        login_btn.click()

        email_input = self.browser.find_element(By.ID, 'email')
        email_input.send_keys(USERS['goodUser']['email'])
        password_input = self.browser.find_element(By.ID, 'password')

        password_input.send_keys(USERS['goodUser']['password'])

        submit_btn = self.browser.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(1)

        logout_btn = self.browser.find_element(By.ID, 'logout-link')
        allure.dynamic.description(f"email: {USERS['goodUser']['email']}; password: {USERS['goodUser']['password']}")

        assert logout_btn.text == "Kilépés"

    @allure.title("Szallashelyek listazasa")
    @allure.description("Egy oldalon megjelenitett szallashelyek szama")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("szallashelyek", "Hootel", "happy-path")
    def test_hotel_list(self):
        hotel_list_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
        hotel_list_btn.click()
        time.sleep(1)

        hotel_list = self.browser.find_elements(By.XPATH, '//h4[@style="cursor: pointer"]')
        assert len(hotel_list) != 0
        assert len(hotel_list) == 10