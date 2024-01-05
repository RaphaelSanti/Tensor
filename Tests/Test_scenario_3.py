from Pages.sbis_ru.main import MainPage as SbisMain
from Pages.sbis_ru.download import DownloadPage as SbisDwld
from conftest import browser


def test_three(browser):

    test_3 = SbisMain(browser)
    test_3.open_sbisru()
    test_3 = SbisDwld(browser)
    test_3.sbis_download_and_size_check()
