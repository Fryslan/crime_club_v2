import time

from crime_club.actions.captcha import Captcha
from crime_club.actions.navigation import Navigation
from crime_club.conditions.element_conditions import ElementConditions
from crime_club.conditions.web_sleep import WebSleep
from crime_club.values import Values


class Jail:

    # def get_first_break_out(driver):
    #     for element in driver.find_elements_by_tag_name('input'):
    #         if element.

    def break_out_players(driver):
        # try:
        if not driver.current_url.startswith('https://www.crime-club.nl/nav.php?p=prison'):
            Navigation.navigate_using_xpath_element(driver, Values.jail_x_path)
            WebSleep.wait_for_element_by_id(driver, 'ibox')
            print('navigating to prison')
        else:
            if Captcha.captcha_present(driver):
                Captcha.detect_and_solve_captcha(driver)
                driver.find_element_by_name('check').click()
                time.sleep(0.25)

            if ElementConditions.check_exists_by_class_name(driver, 'inhoud_c'):
                print('checking jail')
                for element in driver.find_elements_by_class_name('inhoud_c'):
                    if 'Breek' in element.text:
                        try:
                            element.find_element_by_tag_name('input').click()
                            # driver.find_element_by_xpath(Values.jail_all_x_path)
                            time.sleep(0.15)
                        except:
                            break
                            pass

    # except Exception :
    #     print('exeption in jail')
