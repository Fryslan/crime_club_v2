import time

from selenium.webdriver import ActionChains

from crime_club.conditions.element_conditions import ElementConditions


class Captcha:

    def detect_and_solve_captcha(driver):
        if (ElementConditions.check_exists_by_class_name(driver, 'ui-draggable')):
            print('captcha found')
            source_element = driver.find_element_by_class_name('ui-draggable')
            dest_element = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[3]/form/table/tbody/tr[21]/td')
            ActionChains(driver).drag_and_drop(source_element, dest_element).perform()

            print('captcha should be solved')
            time.sleep(0.25)

    def captcha_present(driver):
        if (ElementConditions.check_exists_by_class_name(driver, 'ui-draggable')):
            return True
        return False