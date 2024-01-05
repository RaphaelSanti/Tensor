from selenium.webdriver.common.by import By


class ContactsPageLocators:
   
    tensor_logo = (By.XPATH, "//a[@title='tensor.ru']")
    region = (By.XPATH, "//*[(text()='Контакты') and contains(@class, 'h2')]/parent::div/following::*[contains(@class, 'Region-Chooser') and contains(@class, 'link')]")


    choice_41_region = (By. XPATH, "//span[@title='Камчатский край']")
    partners_list = (By. XPATH, "//*[contains(@class, 'Contacts-List')]//*[@data-qa='item']")
