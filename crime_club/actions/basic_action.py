import time

from selenium.webdriver import ActionChains

from crime_club.actions.captcha import Captcha
from crime_club.actions.navigation import Navigation
from crime_club.conditions.element_conditions import ElementConditions
from crime_club.conditions.web_sleep import WebSleep
from crime_club.values import Values


class BasicAction:

    def commit_using_element_name(driver,url,name):
        if driver.current_url.startswith(url):
            Captcha.detect_and_solve_captcha(driver)
            if ElementConditions.check_exists_by_name(driver,name):
                driver.find_element_by_name(name).click()
                time.sleep(0.25)
                driver.refresh()

