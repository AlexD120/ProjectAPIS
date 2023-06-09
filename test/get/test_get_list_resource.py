import pytest
import conftest
from base.base_class import Base
import allure
from body_response import body_response
from page.login_page import Login_page
from page.requests_selection_page import Selection_requests_page
from page.request_text_comparison_page import Assert_requests_text_page
from page.checking_values_page import Checking_values_page


# Позитивные API тесты
@allure.description("Test api positive")
def test_api_positive(api_request, set_up):
    url = "https://reqres.in/api/unknown"
    response = api_request(url)

    body = body_response.response_get_list_resource

    assert response.status_code == 200
    assert response.json() == body
    print("test_api_positive - PASSED")


 # Негативные API тесты
def test_api_negative(api_request, set_up):
     url = "https://reqres.in/apis/nonexistent-endpoint"
     response = api_request(url)

     assert response.status_code == 404
#
#
def test_api_negative_2(api_request, set_up):
    url = "https://reqres.in/api/unknown?param=value"
    response = api_request(url)

    assert response.status_code == 200
    not_word = Base(conftest.driver)
    not_word.check_word_not_in_json(response, "pages1")
    print("test_api_negative_2 - PASSED")


def test_web(driver):
    button_locator = "//li[@data-id='unknown']"  #ЛОКАТОР ДЛЯ ID АЖДОГО ТЕСТА
    key_url = "/api/unknown"
    status = "200"

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
    assert value_cv == body_response.response_get_list_resource
    print("test WEB - PASSED")

if __name__ == "__main__":
    pytest.main()

