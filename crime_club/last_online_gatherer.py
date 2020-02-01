import xlrd
import xlutils
import xlwt
from selenium import webdriver

from crime_club.actions.login import Login
from crime_club.actions.navigation import Navigation
from crime_club.conditions.web_sleep import WebSleep
from crime_club.values import Values

print('creating excel file')
workbook = xlrd.open_workbook('data.xlsx')
worksheet = workbook.sheet_by_name('1')

wt_workbook = xlwt.Workbook('data.xlsx')
wt_worksheet = wt_workbook.get_sheet('1')

print('loading client')
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
        for x in range(1,250):
            if worksheet.cell(x,6).value != '0%':
                if worksheet.cell(x,3).value == 'Scum':

                    print('gathering data for '+worksheet.cell(x,1).value)
                    driver.get('https://www.crime-club.nl/nav.php?p=profile&x='+worksheet.cell(x,1).value)
                    WebSleep.wait_for_element_by_x_path(driver,'/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[15]/td[2]')
                    wt_worksheet.write('H'+worksheet.cell(x,1),driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[15]/td[2]').text)
        break