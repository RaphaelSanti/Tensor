from Pages.Base_Page import BasePage
from locators.sbis_ru.main import MainPageLocators as main


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_sbisru(self):
        self.go_to_url(main.url)

    def main_page__contacts_button__click(self):
        return self.find_clickble(main.contacts_link_button).click()



