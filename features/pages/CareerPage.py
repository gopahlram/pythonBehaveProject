
from features.pages.BasePage import BasePage
from features.pages.JobListingPage import JobListingPage


class CareerPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    search_button = "//a[contains(@aria-label,'Search')]"

    def click_search_button(self):
        self.element_click("xpath", self.search_button)
        return JobListingPage(self.driver)