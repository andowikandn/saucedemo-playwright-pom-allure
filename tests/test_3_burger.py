import allure
from pages.burger import BurgerMenuPages
from pages.login import LoginPages
from pages.dashboard import DashboardPages


@allure.story('8 Click logout of burger menu')
def test_click_logout(browser):    
    login = LoginPages(browser)
    dashboard = DashboardPages(browser)
    burger = BurgerMenuPages(browser)    

    login.check_open_saucedemo()
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_btn()

    dashboard.click_burger_menu()

    with allure.step('Verify on click logout'):
        burger.click_logout_menu()
        assert burger.check_click_logout()

@allure.story('9 Click About link and Verify direct url')
def test_click_about_link(browser):
    login = LoginPages(browser)
    dashboard = DashboardPages(browser)
    burger = BurgerMenuPages(browser)    

    login.check_open_saucedemo()
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_btn()

    dashboard.click_burger_menu()
    burger.click_about()

    with allure.step('Verify on clik About redirect url'):
        assert burger.verify_about_link()
