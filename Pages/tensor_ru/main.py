from Pages.Base_Page import BasePage
from locators.tensor_ru.main import MainPageLocators as locators
import allure

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://tensor.ru/"
        self.title = "Тензор — IT-компания"

    @allure.step('Открыть https://tensor.ru/')
    def open_tensorru(self):
        self.go_to_url(self.url)

    @allure.step('Переключиться на окно с сайтом Тензора')
    def switch_tab_to_tensor(self):
        self.switch_tab(self.title)

    @allure.step('Проверка существования блока с заголовком "Сила в людях"')
    def main_page__power_in_people_block__exist(self):
        assert self.find_element(locators.power_in_people__title)

    @allure.step('Кликнуть "Подробнее" в блоке "Сила в людях"')
    def main_page__power_in_people_block__more_open(self):
        more = self.find_element(locators.power_in_people__more).get_attribute('href')
        self.go_to_url(more)