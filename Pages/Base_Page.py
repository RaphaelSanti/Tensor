from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests
import os


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url):
        return self.driver.get(url)

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Элемент по локатору {locator} не найден")

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Элементы по локатору {locator}не найдены")

    def find_clickble(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((locator)), message=f"Кликабельный элемент по локатору {locator} не найдены")

    def current_url(self):
        return self.driver.current_url

    def tab_title(self):
        return self.driver.title

    def switch_tab(self, title):
        tabs = self.driver.window_handles
        for tab in tabs:
            if self.driver.title != title:
                self.driver.switch_to.window(tab)

    def action__move_and_click(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        sleep(0.1) # Так стабильней))
        action.click(element)
        action.perform()

    def create_new_tab(self):
        self.driver.switch_to.new_window('tab')

    def download_file(self, url, file_name):
        r = requests.get(url, allow_redirects=True)
        open(file_name, 'wb').write(r.content)

    def file_name_from_url(self, url):
        if url.find('/'):
            return url.rsplit('/', 1)[1]
        else:
            return 'download.file'

    def get_file_size(self, file_name):
        path = os.getcwd()
        file_size = os.path.getsize(path + '/' + file_name)
        # Определение еденицы измерения
        measure, n = 'Б', 0
        while int(file_size) > 1024:
            file_size /= 1024
            n += 1
        file_size = round(file_size, 2)
        if n == 1: measure = 'КБ'
        elif n == 2: measure = 'МБ'
        elif n == 3: measure = 'ГБ'
        elif n == 4: measure = 'ТБ'
        return f"{file_size} {measure}"

    def downloaded_file_check(self, file_name):
        path = os.getcwd()
        return os.path.isfile(path + '/' + file_name)
