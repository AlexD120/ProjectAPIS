from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure


class Login_page(Base):
    url = 'https://reqres.in/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    main_word = "//ya-tr-span[contains(text(), '  Test your front-end against a real API  ')]"

    #Getters
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    #Actions


    #METOD
    def authorization(self):
        with allure.step("Authorization"):
            self.driver.get(self.url)