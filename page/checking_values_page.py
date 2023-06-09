import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure



class Checking_values_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    response_body_page = "//pre[@data-key = 'output-response']"
    status_code = "//span[@data-key='response-code']"

    # Getters
    def get_body_responce(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.response_body_page)))

    def get_status_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.status_code)))

    # Actions
    def value_body_responce_page(self):
        value_body = self.get_body_responce()
        text_value_body = value_body.text
        dict_value_body = json.loads(text_value_body)
        return dict_value_body

    def getting_status_code(self):
        status_code_element = self.get_status_code()
        status_code_text = status_code_element.text
        print("Status Code:", status_code_text)
        return status_code_text


    # METOD
    def checking_values(self):
        with allure.step("Selection requests"):
            return self.value_body_responce_page()


