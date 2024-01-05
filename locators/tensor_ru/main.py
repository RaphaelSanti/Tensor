from selenium.webdriver.common.by import By


class MainPageLocators:

    url = "https://tensor.ru/"
    site_title = "Тензор — IT-компания"
    power_in_people__title = (By. XPATH, "//*[text()='Сила в людях']")
    power_in_people__more = (By.XPATH, "//*[text()='Сила в людях']/parent::*//a[@href and text()='Подробнее']")
