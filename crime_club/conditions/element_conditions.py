from selenium.common.exceptions import NoSuchElementException


class ElementConditions:
    def check_exists_by_xpath(driver,xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_class_name(driver, name):
        try:
            driver.find_element_by_class_name(name)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_id(driver, id):
        try:
            driver.find_element_by_id(id)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_name(driver, name):
        try:
            driver.find_element_by_name(name)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_tag(driver, tag):
        try:
            driver.find_element_by_tag_name(tag)
        except NoSuchElementException:
            return False
        return True