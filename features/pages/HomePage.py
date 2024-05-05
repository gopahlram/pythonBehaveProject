
from features.pages.BasePage import BasePage
from features.pages.CareerPage import CareerPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    career_tab_element = ("//div[contains(@class,'hover') and contains(@class,'cmp-tabs__list')]//a[contains(@class,"
                          "'cmp-tabs__link')]")

    def click_on_careers_tab(self):
        self.element_click("xpath", self.career_tab_element)
        return CareerPage(self.driver)