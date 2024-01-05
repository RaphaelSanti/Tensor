from Pages.sbis_ru.main import MainPage as Page
from Pages.sbis_ru.contacts import  ContactsPage as CTPage
from conftest import browser
from time import sleep
import allure


@allure.suite('Второй сценарий')
def test_two(browser):


    with allure.step('1) Перейти на https://sbis.ru/ в раздел "Контакты"'):
        test_2 = Page(browser)
        test_2.open_sbisru()
        test_2.main_page__contacts_button__click()

    with allure.step('2) Проверить, что определился ваш регион и есть список партнеров.'):    #
        test_2 = CTPage(browser)
        test_2.default_region__check()
        test_2.partners_list__displayed()
        partners = test_2.partners_list() # Сохраняем список партнёров для сравнения

    with allure.step('3) Изменить регион на Камчатский край'):
        test_2.region_change()
        new_partners = test_2.partners_list() # Сохраняем список партнёров для сравнения

    with allure.step('4) Проверить, что подставился выбранный регион, список партнеров изменился, url и title содержат информацию выбранного региона'):
        assert partners != new_partners
        test_2.region_changed__check()