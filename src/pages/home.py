"""Page object of git home page"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class GitHomePage:
    #Locators
    GIT_AVATAR = (By.XPATH,"//*[@class = 'Header-link' and @href='https://github.com/']")


    #Initializer
    def __init__(self, browser):
        self.browser = browser

    def gitLogo(self):
        try:
            Git_logo = self.browser.find_element(*self.GIT_AVATAR)
            Git_logo.click()
        except NoSuchElementException:
            print('No Such Element Found')





