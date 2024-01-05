from Pages.Base_Page import BasePage
from locators.sbis_ru.download import DownloadPageLocators as download
from locators.sbis_ru.main import MainPageLocators as main



class DownloadPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def sbis_download_and_size_check(self): # Разбить на простые функции
        self.go_to_url(self.find_element(main.footer_download_sbis).get_attribute('href'))
        self.action__move_and_click(self.find_element(download.sbis_plagin_category))
        download_button = self.find_element(download.sbis_download_link)
        download_link = download_button.get_attribute('href')
        download_size = download_button.text.split('Exe ')[-1].replace(')', '')
        file_name = self.file_name_from_url(download_link)
        self.file_download(download_link, file_name)
        downloaded_file_size = self.get_file_size(file_name)
        assert downloaded_file_size == download_size, f"Скачанный файл весит: {downloaded_file_size}, а файл по сссылке: {download_size}"


