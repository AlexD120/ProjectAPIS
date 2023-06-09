from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure


class Assert_query_name_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    query_name = "//ya-tr-span[@data-index='10-0']"

    # Getters
    def get_query_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.query_name)))

    # Actions
    def check_query_name(self):
        value_name = self.get_query_name()
        return value_name.text

    # Method
    def name_query(self):
        with allure.step("Name QUERY"):
            self.check_query_name()