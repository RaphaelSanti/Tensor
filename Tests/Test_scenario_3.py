from Pages.sbis_ru.main import MainPage as Page
from Pages.sbis_ru.download import DownloadPage as DLPage
from conftest import browser
import allure


@allure.suite('Третий сценарий')
def test_three(browser):

    test_3 = Page(browser)
    test_3.open_sbisru()
    test_3 = DLPage(browser)
    test_3.open_sbis_download()
    test_3.select_plagin_category()
    test_3.download_file()
    test_3.check_file_size()

