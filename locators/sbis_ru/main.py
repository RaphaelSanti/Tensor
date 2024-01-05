from selenium.webdriver.common.by import By


class MainPageLocators:

    class Header:

        contacts_link_button = (By. CSS_SELECTOR, "a[href*='contacts'")

    class Footer:

        footer_download_sbis = (By.XPATH, "//*[contains(@class, 'Footer')]/a[text()='Скачать СБИС']")
