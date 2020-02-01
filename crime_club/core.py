import time
from threading import Thread

from selenium import webdriver
import keyboard

from crime_club.actions.basic_action import BasicAction
from crime_club.actions.jail import Jail
from crime_club.actions.login import Login
from crime_club.actions.navigation import Navigation
from crime_club.actions.weapon_training import WeaponTraining
from crime_club.conditions.element_conditions import ElementConditions
from crime_club.conditions.rank import Rank
from crime_club.conditions.timer_status import TimerStatus
from crime_club.conditions.web_sleep import WebSleep
from crime_club.values import Values


def keyboard_thread():
    while True:
        if keyboard.is_pressed('f11'):
            Values.running = False
            print('pausing the program')
        elif keyboard.is_pressed('f12'):
            Values.running = True
            print('running the program')


def main_thread():
    # loading the driver
    print('loading client')
    try:
        driver = webdriver.Chrome('./driver/chromedriver.exe')
        driver.get('https://www.crime-club.nl/login.php');
        driver.maximize_window()
        WebSleep.wait_for_element_by_name(driver, 'submit_login')
    except Exception:
        print("error while loading driver")

    # the main loop
    while True:
        if (Values.running):
            try:
                if driver.current_url == Values.login_page:
                    print('logging in')
                    Login.login(driver, 'koehoal', 'tc6m4e')

                elif driver.current_url == Values.index_page or driver.current_url == Values.base_page:
                    print('navigatin to login page')
                    Navigation.basic_navigation(driver, Values.login_page)

                # Gathering some data before starting to commit crimes
                # todo check if we got an crusher and the amount we can crush
                # todo check cars in garage
                # todo crush cars
                # todo check if we got an crusher and the amount we can crush

                else:

                    if (ElementConditions.check_exists_by_xpath(driver, Values.rank_status_x_path)):
                        Values.rank = driver.find_element_by_xpath(Values.rank_status_x_path).text

                    if Values.jail_breakout_only == True:
                        Navigation.navigate_using_xpath_element(driver, Values.jail_x_path)
                        Jail.break_out_players(driver)
                    else:
                        if TimerStatus.timer_is_finished(driver, Values.timer_hookers_x_path) and Rank.get_rank_id(Values.rank) > 2:
                            Navigation.navigate_using_xpath_element(driver, Values.timer_hookers_x_path)
                            BasicAction.commit_using_element_name(driver, Values.hookers_page, 'pimp')
                        elif TimerStatus.timer_is_finished(driver, Values.timer_gym_x_path):
                            Navigation.navigate_using_xpath_element(driver, Values.timer_gym_x_path)
                            BasicAction.commit_using_element_name(driver, Values.gym_page, 'train')
                        elif TimerStatus.timer_is_finished(driver, Values.timer_weapon_experience_x_path) and Values.finished_weapon_training == False:
                            Navigation.navigate_using_xpath_element(driver, Values.timer_weapon_experience_x_path)
                            WeaponTraining.commit_and_update_weapon_training(driver)
                        elif TimerStatus.timer_is_finished(driver, Values.timer_delivery_boy_x_path):
                            Navigation.navigate_using_xpath_element(driver, Values.timer_delivery_boy_x_path)
                            BasicAction.commit_using_element_name(driver, Values.delivery_boy_page, 'give_task')
                        elif TimerStatus.timer_is_finished(driver, Values.timer_light_crime_x_path):
                            Navigation.navigate_using_xpath_element(driver, Values.timer_light_crime_x_path)
                            BasicAction.commit_using_element_name(driver, Values.crime_page, 'uitvoeren_licht')
                        elif TimerStatus.timer_is_finished(driver, Values.timer_heavy_crime_x_path) and Rank.get_rank_id(Values.rank) > 4:
                            Navigation.navigate_using_xpath_element(driver, Values.timer_heavy_crime_x_path)
                            BasicAction.commit_using_element_name(driver, Values.crime_page, 'uitvoeren_zwaar')
                        elif TimerStatus.timer_is_finished(driver, Values.timer_light_carjack_x_path):
                            Navigation.navigate_using_xpath_element(driver, Values.timer_light_carjack_x_path)
                            BasicAction.commit_using_element_name(driver, Values.carjack_page, 'uitvoeren_licht')
                        elif TimerStatus.timer_is_finished(driver, Values.timer_heavy_carjack_x_path) and Rank.get_rank_id(Values.rank) > 4:
                            Navigation.navigate_using_xpath_element(driver, Values.timer_heavy_carjack_x_path)
                            BasicAction.commit_using_element_name(driver, Values.carjack_page, 'uitvoeren_zwaar')

                        else:
                            if Values.break_out_players_when_idle:
                                Navigation.navigate_using_xpath_element(driver, Values.jail_x_path)
                                Jail.break_out_players(driver)
                            else:
                                print('taking a rest')
                                time.sleep(0.25)
                    # time.sleep(0.25)

            except Exception:
                print('error in main loop')


def start_threads():
    keyboard_threading = Thread(target=keyboard_thread)
    main_threading = Thread(target=main_thread)

    main_threading.start()
    keyboard_threading.start()


start_threads()
