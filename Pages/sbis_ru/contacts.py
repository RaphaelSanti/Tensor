from Pages.Base_Page import BasePage
from locators.sbis_ru.contacts import ContactsPageLocators as cont
from locators.sbis_ru.main import MainPageLocators as main
from time import sleep


class ContactsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def tensor_logo__click(self):
        return self.find_element(cont.tensor_logo).click()

    def default_region__check(self):
        assert self.find_element(cont.region).text == main.my_region

    def partners_list__displayed(self):
        partners = self.find_elements(cont.partners_list)
        assert len(partners) >= 1

    def partners_list(self):
        return self.find_elements(cont.partners_list)

    def region_change(self):
        self.find_element(cont.region).click()
        self.find_element(cont.choice_41_region).click()
        sleep(2)  # Придумать проверку обновления страницы

    def region_changed__check(self):
        assert self.find_element(cont.region).text == main.region_for_choise.split(' ', 1)[-1]
        assert main.region_for_choise.split(' ', 1)[-1] in self.tab_title() and \
               main.region_for_choise.split(' ')[0] == self.current_url().split('/')[-1].split('-')[0]    # Лишь номер региона

    