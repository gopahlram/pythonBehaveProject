from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_type, locator_value):
        element = None
        locator_type = locator_type.lower()
        if locator_type in "id":
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type in "name":
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type in "class":
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type in "tag":
            element = self.driver.find_element(By.TAG_NAME, locator_value)
        elif locator_type in "xpath":
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type in "css":
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def element_click(self, locator_type, locator_value):
        self.get_element(locator_type, locator_value).click()

    def type(self, locator_type, locator_value, text):
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def get_text(self, locator_type, locator_value):
        return self.get_element(locator_type, locator_value).text

    def element_status(self, locator_type, locator_value):
        return self.get_element(locator_type, locator_value).is_displayed()