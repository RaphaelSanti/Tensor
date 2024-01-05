from Pages.Base_Page import BasePage
from locators.tensor_ru.about import AboutPageLocators as about



class AboutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def current_url_is_about_page(self):
        assert self.current_url() == about.url

    def about_page__work_block__exist(self):
        assert self.find_element(about.work_block__title)

    def about_page__work_block__pictures_sizes_is_equal(self):
        images = self.find_elements(about.work_block__images)
        width, height = [], []
        for image in images:
            width.append(image.get_attribute('width'))
            height.append(image.get_attribute('height'))
        assert sorted(width) == sorted(width, reverse=True) and sorted(height) == sorted(height, reverse=True)





