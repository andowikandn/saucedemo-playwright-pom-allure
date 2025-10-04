import allure
from pages.login import LoginPages
from pages.dashboard import AddtoCartPages, RemoveProductsPage, DashboardPages
from pages.view_cart import ViewCartPages, CheckoutInformationPages

from pages.burger import BurgerMenuPages
from playwright.sync_api import expect

@allure.story('10 View Cart Page')
def test_E2E(browser):
    login = LoginPages(browser)
    addtocart = AddtoCartPages(browser)
    removecart = RemoveProductsPage(browser)
    view_cart = ViewCartPages(browser)
    overview = CheckoutInformationPages(browser)
    dashboard = DashboardPages(browser)
    burger = BurgerMenuPages(browser)

    login.check_open_saucedemo()
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_btn()
    
    with allure.step('Add 2 cart product'):
        addtocart.add_to_cart_backpack()
        addtocart.add_to_cart_jacket()

    with allure.step('Click view cart page'):
        view_cart.view_cart_page()

    with allure.step('Remove 1 cart backpack'):
        removecart.remove_cart_backpack()

    with allure.step('Verify view badge count'):
        assert view_cart.check_view_badge_count('1')

    with allure.step('Continue shopping'):
        view_cart.click_continue_shopping()

    with allure.step('Continue shopping on click direct to Dashboard'):
        assert dashboard.check_login_dashboard()
    
        view_cart.view_cart_page()

    with allure.step('Click Checkout'):
        view_cart.click_checkout()

    with allure.step('Verify checkout page'):
        assert view_cart.check_checkout_page()

    with allure.step('Fill checkout information'):
        overview.input_first_name('asd')
        overview.input_last_name('asd')
        overview.input_zip_code('asd')

    with allure.step('Click continue'):
        overview.click_continue()

    with allure.step('Verify checkout overview'):
        assert overview.checkout_overview_finish()

    with allure.step('Click finish'):
        overview.click_finish_button()

    with allure.step('Verify completed'):
        assert overview.check_completed()

    with allure.step('Click back home'):
        overview.click_back_home()
        assert dashboard.check_login_dashboard()

    with allure.step('User logout'):
        dashboard.click_burger_menu()
        burger.click_logout_menu()
        assert burger.check_click_logout()
        # sleep(2)

@allure.story('11 Click checkout then cancel button')
def test_view_cart_then_cancel(browser):
    login = LoginPages(browser)
    addtocart = AddtoCartPages(browser)
    view_cart = ViewCartPages(browser)

    login.check_open_saucedemo()
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_btn()

    addtocart.add_to_cart_backpack()
    view_cart.view_cart_page()
    
    view_cart.click_checkout()
    
    with allure.step('Click cancel button'):
        view_cart.click_cancel_btn()

    with allure.step('Back to your cart page'):
        assert view_cart.direct_to_view_cart_page()

@allure.story('12 Click continue then cancel button')
def test_checkout_then_cancel(browser):
    login = LoginPages(browser)
    addtocart = AddtoCartPages(browser)
    dashboard = DashboardPages(browser)
    view_cart = ViewCartPages(browser)
    overview = CheckoutInformationPages(browser)

    login.check_open_saucedemo()
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_btn()

    addtocart.add_to_cart_backpack()
    view_cart.view_cart_page()
    
    view_cart.click_checkout()
    overview.click_continue()

    with allure.step('Verify field required'):
        assert overview.verify_field_required()

        overview.close_error_message_checkout()

    with allure.step('Fill checkout information'):
        overview.input_first_name('1st')
        overview.input_last_name('2nd')
        overview.input_zip_code('12345')

    overview.click_continue()
    overview.overview_then_cancel_button()

    with allure.step('Verify back to dashboard'):
        assert dashboard.check_login_dashboard()
