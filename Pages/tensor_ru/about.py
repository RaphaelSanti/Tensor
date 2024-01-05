import allure

from Pages.Base_Page import BasePage
from locators.tensor_ru.about import AboutPageLocators as locators



class AboutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://tensor.ru/about'

    @allure.step('Проверяем, что текущая страница https://tensor.ru/about')
    def current_url_is_about_page(self):
        assert self.current_url() == self.url

    @allure.step('Ищем блок "Работаем"')
    def about_page__work_block__exist(self):
        assert self.find_element(locators.work_block__title)

    @allure.step('Проверяем что картинки блока "Работаем" имеют одинаковый размер')
    def about_page__work_block__pictures_sizes_is_equal(self):
        images = self.find_elements(locators.work_block__images)
        width, height = [], []
        for image in images:
            width.append(image.get_attribute('width'))
            height.append(image.get_attribute('height'))
        assert sorted(width) == sorted(width, reverse=True) and sorted(height) == sorted(height, reverse=True)





