import allure
from locators.login import LoginLocators
from playwright.sync_api import expect

class LoginPages:
    def __init__(self, page):
        self.page = page

    @allure.step('Get open web page')
    def check_open_saucedemo(self):
        expect(self.page.locator(LoginLocators.login_swaglabs_logo)).to_be_visible()
        return True
  
    @allure.step('Input username with {username}')
    def input_username(self, username: str):
        self.page.fill(LoginLocators.login_input_username, username)

    @allure.step('Input password with {password}')
    def input_password(self, password: str):
        self.page.fill(LoginLocators.login_input_password, password)

    @allure.step('Click login button')
    def click_login_btn(self):
        self.page.click(LoginLocators.login_btn)

    @allure.step('Click close error message button')
    def click_close__msg_btn(self):
        self.page.click(LoginLocators.login_btn)

    @allure.step('Get login error message')
    def check_login_error_msg(self):
        expect(self.page.locator(LoginLocators.login_error_message)).to_be_visible()
        return True