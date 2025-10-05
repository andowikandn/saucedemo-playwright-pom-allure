import allure
from locators.dashboard import DashboardLocators
from locators.burger import BurgerMenuLocators
from playwright.sync_api import expect

class DashboardPages:
    def __init__(self, page):
        self.page = page
        
    @allure.step('Login success direct to Dashboard')
    def check_login_dashboard(self):
        expect(self.page.locator(DashboardLocators.direct_dashboard)).to_be_visible()
        return True
    
    @allure.step('Click burger menu')
    def click_burger_menu(self):
        self.page.click(DashboardLocators.burger_menu)

    @allure.step('Check on click burger menu')
    def check_burger_menu(self):
        expect(self.page.locator(BurgerMenuLocators.burger_menu_about)).to_be_visible()
        return True
    
class SortPages:
    def __init__(self, page):
        self.page = page
        self.sort_dropdown = page.locator(DashboardLocators.product_sorting)
        self.verify_sort = page.locator(DashboardLocators.product_sorting)

    @allure.step('Tap select dropdown')
    def tap_select_dropdown(self):
        expect(self.sort_dropdown).to_be_visible()
        self.sort_dropdown.click()
        return True

    @allure.step('Select product sort: {option}')
    def select_sort(self, option: str):
        """
        Pilih option di dropdown sort.
        Parameter `option` bisa:
        - 'az'    -> Name (A to Z)
        - 'za'    -> Name (Z to A)
        - 'lohi'  -> Price (low to high)
        - 'hilo'  -> Price (high to low)
        """
        expect(self.sort_dropdown).to_be_visible()
        self.sort_dropdown.select_option(option)
        return True
    
    @allure.step('Verify sort by: {option}')
    def verify_sort_select(self, option: str):
        """
        Verify sort by selected.
        - 'az'     -> 'option[value="az"]'      
        - 'za'     -> 'option[value="za"]'      
        - 'lohi'   -> 'option[value="lohi"]'    
        - 'hilo'   -> 'option[value="hilo"]'    
        """
        expect(self.verify_sort).to_be_visible()
        self.verify_sort.select_option(option)
        return True

class AddtoCartPages:
    def __init__(self, page):
        self.page = page

    @allure.step('Add to Cart Backpack')
    def add_to_cart_backpack(self):
        self.page.click(DashboardLocators.add_to_cart_backpack)

    @allure.step('Add to Cart Jacket')
    def add_to_cart_jacket(self):
        self.page.click(DashboardLocators.add_to_cart_jacket)

    @allure.step('View badge cart')
    def check_view_badge(self):
        expect(self.page.locator(DashboardLocators.view_badge)).to_be_visible()
        return True
    
class RemoveProductsPage:
    def __init__(self, page):
        self.page = page

    @allure.step('Remove cart backpack')
    def remove_cart_backpack(self):
        self.page.click(DashboardLocators.remove_cart_backpack)

    @allure.step('Remove cart Jacket')
    def remove_cart_jacket(self):
        self.page.click(DashboardLocators.remove_cart_jacket)

    @allure.step('View badge cart')
    def check_view_badge(self):
        expect(self.page.locator(DashboardLocators.view_badge)).not_to_be_visible()
        return True
