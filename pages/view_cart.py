import allure
from locators.dashboard import DashboardLocators
from locators.view_cart import ViewCartLocators, ViewCheckoutLocators, CheckoutOverviewLocators, CompletedLocators
from playwright.sync_api import expect

class ViewCartPages:
    def __init__(self, page):
        self.page = page

    @allure.step('User click view Cart')
    def view_cart_page(self):
        self.page.click(DashboardLocators.view_cart_link)

    @allure.step('Check direct to view Cart page')
    def direct_to_view_cart_page(self):
        expect(self.page.locator(ViewCartLocators.your_cart)).to_be_visible()
        return True
    
    @allure.step('View badge cart')
    def check_view_badge_count(self, expected_count):
        expect(self.page.locator(DashboardLocators.view_badge)).to_have_text(expected_count) #, timeout=5000)
        return True
    
    @allure.step('Continue shopping')
    def click_continue_shopping(self):
        self.page.click(ViewCartLocators.continue_shopping)

    @allure.step('User click Checkout')
    def click_checkout(self):
        self.page.click(ViewCartLocators.checkout)

    @allure.step('Verify direct checkout page')
    def check_checkout_page(self):
        expect(self.page.locator(ViewCheckoutLocators.checkout_info_page)).to_be_visible()
        return True
    
    @allure.step('Click Cancel button')
    def click_cancel_btn(self):
        expect(self.page.locator(ViewCheckoutLocators.cancel_btn)).to_be_visible()

class CheckoutInformationPages:
    def __init__(self, page):
        self.page = page

    @allure.step('Input first name')
    def input_first_name(self, first_name_field: str):
        self.page.fill(ViewCheckoutLocators.first_name, first_name_field)

    @allure.step('Input first name')
    def input_last_name(self, last_name_field: str):
        self.page.fill(ViewCheckoutLocators.last_name, last_name_field)

    @allure.step('Input first name')
    def input_zip_code(self, zip_code_field: str):
        self.page.fill(ViewCheckoutLocators.zip_code, zip_code_field)

    @allure.step('Click continue')
    def click_continue(self):
        self.page.click(ViewCheckoutLocators.continue_btn)

    @allure.step('Verify field required')
    def verify_field_required(self):
        expect(self.page.locator(ViewCheckoutLocators.field_required)).to_be_visible()
        return True
    
    @allure.step('Close message error requirement field')
    def close_error_message_checkout(self):
        self.page.click(ViewCheckoutLocators.close_error_checkout)

    @allure.step('Verify checkout overview')
    def checkout_overview_finish(self):
        expect(self.page.locator(CheckoutOverviewLocators.overview_page)).to_be_visible()
        return True
    
    @allure.step('Overview then click cancel button')
    def overview_then_cancel_button(self):
        self.page.click(CheckoutOverviewLocators.overview_cancel_btn)

    @allure.step('Click Finish button')
    def click_finish_button(self):
        self.page.click(CheckoutOverviewLocators.finish_btn)

    @allure.step('Verify finish completed order')
    def check_completed(self):
        expect(self.page.locator(CompletedLocators.overview_completed)).to_be_visible()
        return True
    
    @allure.step('Click back home')
    def click_back_home(self):
        self.page.click(CompletedLocators.back_home)