from Pages.sbis_ru.main import MainPage as SBIS_Main_Page
from Pages.sbis_ru.contacts import ContactsPage as SBIS_Contacts_Page
from Pages.tensor_ru.main import MainPage as Tensor_Main_Page
from Pages.tensor_ru.about import AboutPage as Tensor_About_Page
from conftest import browser
from time import sleep
import allure


def test_one(browser):

    # 1) Перейти на https://sbis.ru/ в раздел "Контакты"
    test_1 = SBIS_Main_Page(browser)
    test_1.open_sbisru()
    test_1.main_page__contacts_button__click()
    sleep(2)

    # 2) Найти баннер Тензор, кликнуть по нему
    test_1 = SBIS_Contacts_Page(browser)
    test_1.tensor_logo__click()

    # 3) Перейти на https://tensor.ru/
    test_1 = Tensor_Main_Page(browser)
    test_1.switch_tab_to_tensor()

    # 4) Проверить, что есть блок "Сила в людях"
    test_1.main_page__power_in_people_block__exist()

    # 5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается
    #    https://tensor.ru/about
    test_1.main_page__power_in_people_block__more_open()
    test_1 = Tensor_About_Page(browser)
    test_1.current_url_is_about_page()

    # 6) Находим раздел Работаем и проверяем, что у всех фотографии
    #    хронологии одинаковые высота (height) и ширина (width)
    test_1.about_page__work_block__exist()
    test_1.about_page__work_block__pictures_sizes_is_equal()