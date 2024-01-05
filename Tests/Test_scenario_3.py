from Pages.sbis_ru.main import MainPage as Page
from Pages.sbis_ru.download import DownloadPage as DLPage
from conftest import browser


def test_three(browser):

    test_3 = Page(browser)
    test_3.open_sbisru()
    test_3 = DLPage(browser)
    test_3.sbis_download_and_size_check()
