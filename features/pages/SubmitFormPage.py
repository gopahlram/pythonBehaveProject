from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.pages.BasePage import BasePage


class SubmitFormPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    submit_button = '//button[@data-test-id="position-apply-button"]'
    toast_message = '//p[@class="toast-message"]'

    def click_submit_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.submit_button)))
        self.element_click("xpath", self.submit_button)

    def verify_mandatory_error_message(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.toast_message)))
        return self.get_text("xpath", self.toast_message)
