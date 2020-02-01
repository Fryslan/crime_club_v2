import time
from crime_club.actions.captcha import Captcha
from crime_club.conditions.element_conditions import ElementConditions
from crime_club.values import Values


class WeaponTraining:

    def completed_weapon_training(driver):
        if ElementConditions.check_exists_by_class_name(driver,'balk_empty'):
            return False
        return True

    def exchange_weapon_training(driver):
        if ElementConditions.check_exists_by_name(driver, 'change'):
            print('clicking echange button')
            driver.find_element_by_name('change').click()
            time.sleep(1)

        if ElementConditions.check_exists_by_name(driver, 'changeSure'):
            print('clicking echange sure button')
            driver.find_element_by_name('changeSure').click()
            time.sleep(0.5)

        driver.refresh()

    def commit_and_update_weapon_training(driver):
        if driver.current_url.startswith(Values.weapon_training_page):

            Captcha.detect_and_solve_captcha(driver)

            if WeaponTraining.completed_weapon_training(driver):
                print('we are done training')
                Values.finished_weapon_training = True

            if ElementConditions.check_exists_by_name(driver,'change') and Values.trade_in_weapon_experience == True:
                WeaponTraining.exchange_weapon_training(driver)
            else:
                if ElementConditions.check_exists_by_name(driver,'trainen'):
                    driver.find_element_by_name('trainen').click()
                    time.sleep(1)
                    driver.refresh()





