from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure


class Selection_requests_page(Base):

    def __init__(self, driver, button_get_list_users):
        super().__init__(driver)
        self.driver = driver
        self.button_get_list_users = button_get_list_users


    #Locators
    button_get_list_users = "//li[@data-id='users']"

    #Getters
    def get_list_users(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_get_list_users)))

    #Actions
    def click_get_list_users(self):
        click_button_list = self.get_list_users()
        click_button_list.click()
        print(" CLICK GET_ LIST USERS - PASSED")

    #METOD
    def selection_requests(self):
        with allure.step("Selection requests"):
            self.click_get_list_users()