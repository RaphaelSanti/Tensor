from Pages.sbis_ru.main import MainPage as Page
from Pages.sbis_ru.download import DownloadPage as DLPage
from conftest import browser
import allure


@allure.suite('Третий сценарий')
def test_three(browser):

    with allure.step('1) Перейти на https://sbis.ru/'):
        test_3 = Page(browser)
        test_3.open_sbisru()

    with allure.step("2) В Footer'e найти и перейти 'Скачать СБИС'"):
        test_3 = DLPage(browser)
        test_3.open_sbis_download()

    with allure.step('3) Скачать СБИС Плагин для вашей для windows, веб-установщик в папку с данным тестом'):
        test_3.select_plagin_category()
        test_3.download_plugin()

    with allure.step(('4) Убедиться, что плагин скачался')):
         test_3.downloaded_plugin_check()

    with allure.step('5) Сравнить размер скачанного файла в мегабайтах. Он должен совпадать с указанным на сайте.'):
        test_3.check_file_size()



