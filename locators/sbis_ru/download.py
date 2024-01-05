from selenium.webdriver.common.by import By


class DownloadPageLocators:

    sbis_plagin_category = (By.XPATH, "//div[text()='СБИС Плагин']/parent::div/parent::div/parent::div")
    sbis_download_link = (By. XPATH, "//a[contains(text(),'Скачать (Exe')]")
