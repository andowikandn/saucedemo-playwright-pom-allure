import allure
from locators.burger import BurgerMenuLocators
from locators.dashboard import DashboardLocators
from locators.login import LoginLocators
from playwright.sync_api import expect

class BurgerMenuPages:
    def __init__(self, page):
        self.page = page

    @allure.step('Close button burger menu')
    def click_close_burger(self):
        self.page.click(BurgerMenuLocators.close_burger_menu)

    @allure.step('Buger menu Click About')
    def click_about(self):
        self.page.click(BurgerMenuLocators.burger_menu_about)

    @allure.step('Verify on clik About menu')
    def verify_about_link(self):
        expect(self.page).to_have_url(BurgerMenuLocators.about_link_url)
        return True

    @allure.step('Check on click close burger')
    def check_click_logout(self):
        expect(self.page.locator(DashboardLocators.direct_dashboard)).to_be_visible()
        return True

    @allure.step('Click logout menu')
    def click_logout_menu(self):
        self.page.click(BurgerMenuLocators.logout_btn)

    @allure.step('Check on click logout button')
    def check_click_logout(self):
        expect(self.page.locator(LoginLocators.login_swaglabs_logo)).to_be_visible()
        return True