import time

import requests
from selenium import webdriver

from crime_club.actions.login import Login
from crime_club.actions.navigation import Navigation
from crime_club.conditions.element_conditions import ElementConditions
from crime_club.conditions.web_sleep import WebSleep
from crime_club.values import Values

try:
    driver = webdriver.Chrome('./driver/chromedriver.exe')
    driver.get('https://www.crime-club.nl/login.php');
    driver.maximize_window()
    WebSleep.wait_for_element_by_name(driver, 'submit_login')
except Exception:
    print("error while loading driver")

while True:

    if driver.current_url == Values.login_page:
        print('logging in')
        Login.login(driver, 'Fryslan', 'tc6m4e')

    elif driver.current_url == Values.index_page or driver.current_url == Values.base_page:
        print('navigatin to login page')
        Navigation.basic_navigation(driver, Values.login_page)

    else:
        if not driver.current_url.startswith('https://www.crime-club.nl/nav.php?p=wheeloffortune'):
            if ElementConditions.check_exists_by_xpath(driver,'/html/body/table/tbody/tr/td[1]/table/tbody/tr[39]/td/a'):
                driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/table/tbody/tr[39]/td/a').click()
                time.sleep(1)

        else:
            r = requests.post(
                'https://www.crime-club.nl/ajax/wheeloffortune.php',
                data='start_spin:true',
                headers={'content-type': 'json',
                }
            )

            print(r.content)
            time.sleep(5)
