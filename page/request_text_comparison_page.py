from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure


class Assert_requests_text_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    request_value = "//span[@data-key='url']"

    # Getters
    def get_requests_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.request_value)))

    # Actions
    def check_requests_value(self):
        value = self.get_requests_value()
        return value.text

    # Method
    def requests_value(self):
        with allure.step("Selection requests"):
            return self.check_requests_value()
