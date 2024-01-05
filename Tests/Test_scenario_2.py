from Pages.sbis_ru.main import MainPage as SbisMain
from Pages.sbis_ru.contacts import  ContactsPage as SbisCont
from conftest import browser
from time import sleep


def test_two(browser):

    # 1) Перейти на https://sbis.ru/ в раздел "Контакты"
    test_2 = SbisMain(browser)
    test_2.open_sbisru()
    sleep(1) # Придумать ожидание
    test_2.main_page__contacts_button__click()

    # 2) Проверить, что определился ваш регион и есть список партнеров.
    test_2 = SbisCont(browser)
    test_2.default_region__check()
    test_2.partners_list__displayed()
    partners = test_2.partners_list() # Сохраняем список партнёров для сравнения

    # 3) Изменить регион на Камчатский край
    test_2.region_change()
    new_partners =  test_2.partners_list() # Сохраняем список партнёров для сравнения

    # 4) Проверить, что подставился выбранный регион, список партнеров
    #    изменился, url и title содержат информацию выбранного региона
    assert partners != new_partners
    test_2.region_changed__check()