import allure

from Pages.Base_Page import BasePage
from locators.sbis_ru.download import DownloadPageLocators as DLlocators
from locators.sbis_ru.main import MainPageLocators as locators



class DownloadPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://sbis.ru/download'

    @allure.step('Кликаем "Скачать СБИС" в Footer')
    def open_sbis_download(self):
        self.go_to_url(self.find_element(locators.Footer.footer_download_sbis).get_attribute('href'))

    @allure.step('Выбираем "СБИС Плагин" в Controls')
    def select_plagin_category(self):
        self.action__move_and_click(self.find_element(DLlocators.Controls.sbis_plagin_category))

    @allure.step('Находим кнопку "Скачать (Exe...)')
    def find_download_button(self):
        return self.find_element(DLlocators.Downloads.sbis_download_link)

    @allure.step('Получаем атрибут "href" из кнопки "Скачать (Exe...)')
    def get_link_from_download_button(self):
        return DownloadPage.find_download_button(self).get_attribute('href')

    @allure.step('Получаем размер загрузки из текста ссылки') # Посмотреть есть ли размер загрузки в заголовках реквеста
    def get_download_size(self):
        return DownloadPage.find_download_button(self).text.split('Exe ')[-1].replace(')', '')

    @allure.step('Получаем имя файла для загрузки')
    def get_download_file_name(self):
        return self.file_name_from_url(DownloadPage.get_link_from_download_button(self))

    @allure.step('Скачиваем файл')
    def download_plugin(self):
        self.download_file(DownloadPage.get_link_from_download_button(self), DownloadPage.get_download_file_name(self))

    @allure.step('Получаем размер скачанного файла')
    def downloaded_file_size(self):
        return self.get_file_size(DownloadPage.get_download_file_name(self))

    @allure.step('Сравниваем размер скачанного файла и указаный на странице загрузки')
    def check_file_size(self):
        assert DownloadPage.downloaded_file_size(self) == DownloadPage.get_download_size(self),\
            f"Скачанный файл весит: {DownloadPage.downloaded_file_size(self)}, а файл по сссылке: {DownloadPage.get_download_size(self)}"

    @allure.step('Проверяем скачался ли файл')
    def downloaded_plugin_check(self):
        assert DownloadPage.downloaded_file_check(self, DownloadPage.get_download_file_name(self))
