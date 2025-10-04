import allure
import pytest
from pages.login import LoginPages
from pages.dashboard import DashboardPages

@allure.story('1 Open web page')
def test_open_saucedemo(browser):
    login = LoginPages(browser)

    with allure.step('User open web page'):
        assert login.check_open_saucedemo()

input_invalid = [('',''),
                 ('','secret_sauce'),
                 ('standard_user',''),
                 ('wronguser','wrongpass')]

@allure.story('2 Input with invalid credentials')
@pytest.mark.parametrize('x,y', input_invalid)
def test_login_failed(browser,x,y):
    login = LoginPages(browser)
    
    login.check_open_saucedemo()

    with allure.step('Input invalid credentials'):
        login.input_username(x)
        login.input_password(y)

    with allure.step('Verify error message credentials'):
        login.click_login_btn()
        assert login.check_login_error_msg()

        login.click_close__msg_btn()

@allure.story('3 Input with valid credentials')
def test_login_success(browser):
    login = LoginPages(browser)
    dashboard = DashboardPages(browser)
    
    login.check_open_saucedemo()

    with allure.step('Input valid credentials'):
        login.input_username('standard_user')
        login.input_password('secret_sauce')

    with allure.step('Verify success login to dashboard'):
        login.click_login_btn()
        assert dashboard.check_login_dashboard()