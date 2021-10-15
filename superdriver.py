from selenium.webdriver.support.ui import WebDriverWait # timeout 
from selenium.webdriver.support import expected_conditions as EC # conditions for search
from selenium.webdriver.common.by import By # method of search

from lib import Terminal

class SuperDriver():

    __terminal = Terminal()

    def __init__ (self, driver):
        self.driver = driver

    def get(self, path):
        try:
            self.driver.get(path)
        except:
            self.__terminal.print_except()

    def click(self, el):
        try:
            el.click()
        except:
            self.__terminal.print_except()
            
    def element_by_xpath(self, path, time=3):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            element = self.driver.find_element_by_xpath(path)
            return element
        except:
            return None

    def elements_by_xpath(self, path, time=3):
        try:
            elements = WebDriverWait(self.driver, time).until(
                EC.presence_of_all_elements_located((By.XPATH, path))
            )
            elements = self.driver.find_elements_by_xpath(path)
            return elements
        except:
            return None

    def element_by_name(self, path, time=3):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.NAME, path))
            )
            element = self.driver.find_element_by_name(path)
            return element
        except:
            return None

    def elements_by_name(self, path, time=3):
        try:
            elements = WebDriverWait(self.driver, time).until(
                EC.presence_of_all_elements_located((By.NAME, path))
            )
            elements = self.driver.find_elements_by_name(path)
            return elements
        except:
            return None