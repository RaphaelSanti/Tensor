from Pages.Base_Page import BasePage
from locators.sbis_ru.contacts import ContactsPageLocators as locators
from time import sleep
from Data.Scenario_1 import Prequials


class ContactsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://sbis.ru/contacts'

    def tensor_logo__click(self):
        return self.find_element(locators.tensor_logo).click()

    def default_region__check(self):
        assert self.find_element(locators.region).text == Prequials.my_region

    def partners_list__displayed(self):
        partners = self.find_elements(locators.partners_list)
        assert len(partners) >= 1

    def partners_list(self):
        return self.find_elements(locators.partners_list)

    def region_change(self):
        self.find_element(locators.region).click()
        self.find_element(locators.choice_41_region).click()
        sleep(2)  # Придумать проверку обновления страницы

    def region_changed__check(self):
        assert self.find_element(locators.region).text == Prequials.region_for_choise.split(' ', 1)[-1]
        assert Prequials.region_for_choise.split(' ', 1)[-1] in self.tab_title() and \
               Prequials.region_for_choise.split(' ')[0] == self.current_url().split('/')[-1].split('-')[0]    # Лишь номер региона

    