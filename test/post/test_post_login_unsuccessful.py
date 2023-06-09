import pytest
import conftest
from base.base_class import Base
import allure
from body_requests import body_requests
from body_response import body_response
from page.login_page import Login_page
from page.requests_selection_page import Selection_requests_page
from page.request_text_comparison_page import Assert_requests_text_page
from page.checking_values_page import Checking_values_page

# Позитивные API тесты
@allure.description("Test api positive")
def test_api_positive(api_request, set_up):
    url = "https://reqres.in/api/login"
    data = body_requests.request_post_login_unsuccessful
    response = api_request(url, method="POST", data=data)

    assert response.status_code == 400
    assert all(item in response.json().items() for item in body_response.response_post_login_unsuccessful.items())
    print("test_api_positive - PASSED")

# Негативные API тесты
def test_api_negative(api_request):
    url = "https://reqres.in/appi/register"
    response = api_request(url, method="POST", data={})

    assert response.status_code == 404


def test_api_negative_invalid_url(api_request):
    url = "https://reqres.in/api/unknown-endpoint"
    response = api_request(url, method="POST", data={})

    assert response.status_code == 201
    not_word = Base(conftest.driver)
    not_word.check_word_not_in_json(response, "Буду укладываться в дедлайны")
    print("test_api_negative_2 - PASSED")


def test_web(driver):
    button_locator = "//li[@data-id='login-unsuccessful']"  #ЛОКАТОР ДЛЯ ID АЖДОГО ТЕСТА
    key_url = "/api/login"
    status = "400"

    """LOGIN PAGE"""
    login = Login_page(driver)
    login.authorization()

    """REQUESTS SELECTION PAGE"""
    rs = Selection_requests_page(driver, button_locator)
    rs.selection_requests()

    """REQUESTS TEXT PAGE"""
    vr = Assert_requests_text_page(driver)
    value_requests = vr.requests_value()

    """CHECKING VALUE PAGE"""
    cv = Checking_values_page(driver)  #
    value_cv = cv.checking_values()
    code = cv.getting_status_code()

    assert code == status
    assert value_requests == key_url
    assert all(item in value_cv.items() for item in body_response.response_post_login_unsuccessful.items())
    print("test WEB - PASSED")


if __name__ == "__main__":
    pytest.main()
