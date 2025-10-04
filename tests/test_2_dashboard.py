import allure
from pages.login import LoginPages
from pages.dashboard import DashboardPages, SortPages, AddtoCartPages, RemoveProductsPage
from pages.burger import BurgerMenuPages


@allure.story('4 Click burger menu')
def test_burger_menu(browser):
    login = LoginPages(browser)
    dashboard = DashboardPages(browser)
    burger = BurgerMenuPages(browser)

    login.check_open_saucedemo()
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_btn()

    with allure.step('Verify burger menu'):
        dashboard.click_burger_menu()
        assert dashboard.check_burger_menu()

    with allure.step('Close burger menu'):
        burger.click_close_burger()
        assert dashboard.check_login_dashboard()

@allure.story('5 Sort by selected dropdown')
def test_sort_products(browser):
    login = LoginPages(browser)
    dashboard = SortPages(browser)

    login.check_open_saucedemo()
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_btn()

    with allure.step('Tap dropdown'):
        dashboard.tap_select_dropdown()

    with allure.step('Sort product by Name (Z to A)'):
        dashboard.select_sort('za')

    with allure.step('Verify sort by name Z to A'):
        assert dashboard.verify_sort_select('za')

    with allure.step('Sort product by Name (A to Z)'):
        dashboard.select_sort('az')

    with allure.step('Verify sort by name A to Z'):
        assert dashboard.verify_sort_select('az')

    with allure.step('Sort product by Price (high to low)'):
        dashboard.verify_sort_select('hilo')

    with allure.step('Verify sort by Price High to Low'):
        assert dashboard.verify_sort_select('hilo')

    with allure.step('Sort product by Price (low to high)'):
        dashboard.select_sort('lohi')

    with allure.step('Verify sort by Price Low to High'):
        assert dashboard.verify_sort_select('lohi')

@allure.story('6 Add 2 Cart')
def test_add_to_carts(browser):
    login = LoginPages(browser)
    addtocart = AddtoCartPages(browser)

    login.check_open_saucedemo()
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_btn()
    
    with allure.step('Add to cart backpack'):
        addtocart.add_to_cart_backpack()

    with allure.step('Add to cart Jacket'):
        addtocart.add_to_cart_jacket()

    with allure.step('Verify view badge'):
        assert addtocart.check_view_badge()
    
@allure.story('7 Remove 2 Cart')
def test_remove_carts_product(browser):
    login = LoginPages(browser)
    addtocart = AddtoCartPages(browser)
    removecart = RemoveProductsPage(browser)

    login.check_open_saucedemo()
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_btn()
    
    with allure.step('Add 2 cart product'):
        addtocart.add_to_cart_backpack()
        addtocart.add_to_cart_jacket()

    with allure.step('Remove 2 cart product'):
        removecart.remove_cart_backpack()
        removecart.remove_cart_jacket()

    with allure.step('Verify view badge'):
        assert removecart.check_view_badge()