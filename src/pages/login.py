"""" page object on Git login page """

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class GitLoginPage():
    #URL
    URL = "https://github.com/login"


    #Locators
    USERNAME = (By.XPATH ,"//*[@id='login_field']")
    PASSWORD = (By.XPATH ,"//*[@id='password']")
    SUBMITBUTTON = (By.XPATH, "//*[@value='Sign in']")

    #Initializer
    def __init__(self,browser):
        self.browser = browser


    #Page Object Methods
    def load(self):
        self.browser.get(self.URL)       #get method to open url in browser
        #self.browser.windows().maximize()

    def gitUsername(self, userName):
        self.browser.find_element(*self.USERNAME).send_keys(userName)

    def gitPassword(self, passWord):
        self.browser.find_element(*self.PASSWORD).send_keys(passWord)

    def gitloginSubmit(self):
        self.browser.find_element(*self.SUBMITBUTTON).click()




