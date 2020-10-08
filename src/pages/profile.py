"""page object of profile page """
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GitProfilePage():

    #locators

    ProfileDropdown = (By.XPATH,"//*[@class='avatar avatar-user ']")
    YourProfile = (By.XPATH,"//*[contains(text(),'Your profile')]")
    ProfilePicClick =(By.XPATH,"//*[@aria-label='Change your avatar']")
    ProfilePicEdit =(By.XPATH,"//*[contains(text(),'Edit')]")
    ProfilePicEditUpload =(By.XPATH,"//*[@class ='dropdown-item text-normal']")
    ProfileLocation =(By.XPATH,"//*[@id='user_profile_location']")
    ProfileBio = (By.XPATH,"//*[@id='user_profile_bio']")
    ProfileUpdate =(By.XPATH,"//*[@class='btn btn-primary']")

    #Initializer
    def __init__(self,browser):
        self.browser = browser

    def gitProfileDropdown(self):
        self.browser.find_element( *self.ProfileDropdown ).click()


    def gitYourProfile(self):
        self.browser.find_element( *self.YourProfile ).click()


    def gitProfilePicClick(self):
        self.browser.find_element( self.ProfilePicClick ).click()


    def gitProfilePicEdit(self):
        self.browser.find_element( self.ProfilePicEdit ).click()
        self.browser.find_element( self.ProfilePicEditUpload )


    def gitProfileLocation(self,profileLocation):
        self.browser.find_element(self.ProfileLocation).send_keys(profileLocation)


    def gitProfileBio(self,profileBio):
        self.browser.find_element(self.ProfileBio).send_keys(profileBio)


    def gitProfileUpdate(self):
        self.browser.find_element(self.ProfileUpdate).click()

