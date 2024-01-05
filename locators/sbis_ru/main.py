from selenium.webdriver.common.by import By


class MainPageLocators:

    url = "https://sbis.ru/"
    my_region = 'Республика Башкортостан'
    region_for_choise = '41 Камчатский край'

    contacts_link_button = (By. CSS_SELECTOR, "a[href*='contacts'")
    footer_download_sbis = (By.XPATH, "//*[contains(@class, 'Footer')]/a[text()='Скачать СБИС']")
