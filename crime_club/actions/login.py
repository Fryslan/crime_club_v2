from crime_club.conditions.element_conditions import ElementConditions
from crime_club.conditions.web_sleep import WebSleep
from crime_club.values import Values


class Login:

    def login(driver,user,passw):
        if driver.current_url == Values.login_page:
            if ElementConditions.check_exists_by_name(driver,'username'):
                driver.find_element_by_name('username').send_keys(user)

            if ElementConditions.check_exists_by_name(driver,'password'):
                driver.find_element_by_name('password').send_keys(passw)

            if ElementConditions.check_exists_by_name(driver,'submit_login'):
                driver.find_element_by_name('submit_login').click()

            WebSleep.wait_for_element_by_x_path(driver,Values.timer_gym_x_path)