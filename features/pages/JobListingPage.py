from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.pages.BasePage import BasePage
from features.pages.SubmitFormPage import SubmitFormPage
from utilities import ConfigReader
from utilities.OsUtils import OsUtils
from utilities.DriverUtils import DriverUtils


class JobListingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver_utils = DriverUtils(self.driver)

    header_element = "//div[@class='header-wrapper']//h1"
    drag_drop_element = "//div[@class='dropzone']/input"
    confirm_element = "//button[@data-test-id='confirm-upload-resume']"
    file_element = "//h3[text()='{0}']"
    file_upload_completion_element = "//div[@class='dropzone']//h3"
    search_box = "//input[@id='main-search-box']"
    drop_down_element = "//div[@class='Select-menu']//span[contains(text(),'{0}')]"
    go_button = "//button[@class='go-button']"
    job_card = "//div[@class='position-full-card']//p[contains(@class,'position-id-text')]"
    req_element = "//div[@class='position-full-card']//p[contains(@class,'position-id-text')]"
    apply_button = "//button[@data-test-id='apply-button']"
    submit_header_text = "//div[@id='careers-apply-form']"

    def navigate_to_job_listing_page(self):
        parent_window = self.driver_utils.get_parent_windowHandle()
        handles = self.driver_utils.get_all_windows()
        self.driver_utils.switch_to_window(handles, parent_window)

    def verify_job_listing_page(self):
        return self.get_text("xpath", self.header_element)

    def upload_file(self, file_name):
        path = ConfigReader.read_configuration("basic info", "upload_path")
        full_file_path = OsUtils.get_file_path(path, file_name)
        element = self.driver.find_element(By.XPATH, self.drag_drop_element)

        element.send_keys(full_file_path)
        self.element_click("xpath", self.confirm_element)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.file_element.format(file_name))))
        return self.element_status("xpath", self.file_upload_completion_element)

    def search_job(self, search_text):
        self.element_click("xpath", self.search_box)
        self.type("xpath", self.search_box, search_text)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.drop_down_element.format(search_text))))
        self.element_click("xpath", self.drop_down_element.format(search_text))
        self.element_click("xpath", self.go_button)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.job_card)))

    def validate_requirement_id(self):
        return self.get_text("xpath", self.req_element)

    def apply_job(self):
        apply_button = self.driver.find_element(By.XPATH, self.apply_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", apply_button)
        self.element_click("xpath", self.apply_button)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.submit_header_text)))
        return SubmitFormPage(self.driver)