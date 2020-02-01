from crime_club.conditions.element_conditions import ElementConditions
from crime_club.conditions.web_sleep import WebSleep


class Navigation:

    def basic_navigation(driver,target_link):
        if driver.current_url != target_link:
            driver.get(target_link)

    def navigate_using_xpath_element(driver,element):
        if ElementConditions.check_exists_by_xpath(driver,element):
            driver.find_element_by_xpath(element).click()
            WebSleep.wait_for_element_by_x_path(driver,element)
