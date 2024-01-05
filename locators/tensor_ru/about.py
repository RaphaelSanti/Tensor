from selenium.webdriver.common.by import By


class AboutPageLocators:

    work_block__title = (By.XPATH, "//*[contains(@class, 'block-title')]//*[text()='Работаем']")
    work_block__images = (By.XPATH, "//*[contains(@class, 'block-title')]//*[text()='Работаем']/parent::div/parent::div//img[contains(@class, 'image')]")

