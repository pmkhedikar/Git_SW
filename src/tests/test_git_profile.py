""""  Test login to git account ,go to profile ,fill the bio & upload the image .Verify & logout """
from src.pages.login import GitLoginPage
from src.pages.home import GitHomePage
from src.pages.profile import GitProfilePage


def test_git_profile_update(browser):

    #Variables
    userName ='pmkhedikar@gmail.com'
    passWord ='parag151287'
    profileBio = 'Test Profile for Automation'
    profileLocation = 'LA'

    #Class Objects
    loginPage = GitLoginPage( browser )
    homePage = GitHomePage( browser )
    profilePage = GitProfilePage( browser )

    #Test Steps
    #Given open the git URL
    loginPage.load()

    #When Enter username,password & click
    loginPage.gitUsername(userName)
    loginPage.gitPassword(passWord)
    loginPage.gitloginSubmit()

    # then - verify the login page
    homePage.gitLogo()

    #Click on profile,Add the attributes ,Click on pic & upload the pic & save
    #Verify the attributes that filled

    profilePage.gitProfileDropdown()
    profilePage.gitYourProfile()
    profilePage.gitProfilePicClick()
    #profilePage.gitProfilePicEdit()
    profilePage.gitProfileBio(profileBio)
    profilePage.gitProfileLocation(profileLocation)
    profilePage.gitProfileUpdate()




