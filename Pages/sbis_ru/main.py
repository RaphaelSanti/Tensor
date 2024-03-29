import allure

from Pages.Base_Page import BasePage
from locators.sbis_ru.main import MainPageLocators as locators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://sbis.ru/"

    @allure.step('Открываем https://sbis.ru/')
    def open_sbisru(self):
        self.go_to_url(self.url)

    @allure.step('Кликнуть "Контакты" в Header ')
    def main_page__contacts_button__click(self):
        return self.find_clickble(locators.Header.contacts_link_button).click()



