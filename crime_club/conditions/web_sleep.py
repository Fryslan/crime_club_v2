from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_cond


class WebSleep:

    def wait_for_element_by_x_path(driver, x_path):
        WebDriverWait(driver, 3).until(expected_cond.presence_of_element_located((By.XPATH, x_path)))

    def wait_for_element_by_class(driver, class_name):
        WebDriverWait(driver, 3).until(expected_cond.presence_of_element_located((By.CLASS_NAME, class_name)))

    def wait_for_element_by_name(driver, name):
        WebDriverWait(driver, 3).until(expected_cond.presence_of_element_located((By.NAME, name)))

    def wait_for_element_by_id(driver, id):
        WebDriverWait(driver, 3).until(expected_cond.presence_of_element_located((By.ID, id)))
