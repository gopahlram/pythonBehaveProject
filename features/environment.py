import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import ConfigReader


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile_default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--incognito")
        context.driver = webdriver.Chrome(options=chrome_options)
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))


def after_feature(context, driver):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      , name="failed_screenshot"
                      , attachment_type=AttachmentType.PNG)
