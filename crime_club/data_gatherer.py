from selenium import webdriver
import xlsxwriter
from crime_club.actions.login import Login
from crime_club.actions.navigation import Navigation
from crime_club.conditions.element_conditions import ElementConditions
from crime_club.conditions.web_sleep import WebSleep
from crime_club.values import Values
from datetime import date

print('creating excel file')
workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet(str(date.today()))

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
        Login.login(driver, 'USERNAME', 'PASSWORD')

    elif driver.current_url == Values.index_page or driver.current_url == Values.base_page:
        print('navigatin to login page')
        Navigation.basic_navigation(driver, Values.login_page)

    else:
        try:
            print('gathering all players')
            for x in range(0, 244):
                print('scanning page ' + str(x))
                if driver.current_url != Values.player_list_page + str(x):
                    driver.get(Values.player_list_page + str(x))
                    WebSleep.wait_for_element_by_x_path(driver,'/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[3]/td/table[1]/tbody/tr[28]')

                if driver.current_url == Values.player_list_page + str(x):
                    for i in range(4, 29):
                        row = driver.find_element_by_xpath(
                            '/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[3]/td/table[1]/tbody/tr[' + str(
                                i) + ']')

                        id = row.find_elements_by_tag_name('td')[0].text
                        name = row.find_elements_by_tag_name('td')[1].text
                        score = row.find_elements_by_tag_name('td')[2].text
                        rank = row.find_elements_by_tag_name('td')[3].text
                        wealth = row.find_elements_by_tag_name('td')[4].text
                        family = row.find_elements_by_tag_name('td')[5].text
                        life = row.find_elements_by_tag_name('td')[6].text

                        print('gathering data for : '+name+'['+id+']')
                        worksheet.write('A' + id, id)
                        worksheet.write('B' + id, name)
                        worksheet.write('C' + id, score)
                        worksheet.write('D' + id, rank)
                        worksheet.write('E' + id, wealth)
                        worksheet.write('F' + id, family)
                        worksheet.write('G' + id, life)

            break
        except Exception as e:
            print('exeption: '+e)
            try:
                workbook.close()
            except Exception as e:
                print("Close the file: ", e)

try:
    workbook.close()
except Exception as e:
    print ("Close the file: ", e)



