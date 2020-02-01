from crime_club.conditions.element_conditions import ElementConditions


class TimerStatus:

    def timer_is_finished(driver,xpath):
        try:
            if ElementConditions.check_exists_by_xpath(driver,xpath):
                text = driver.find_element_by_xpath(xpath).text
                if text == 'Nu' or text == '0':
                    return True
                else:
                    if text == '':
                        print('timer is empty')
                    return False
            else:
                print('timer element not found')
        except Exception:
            print('error checking if the timer is finished')