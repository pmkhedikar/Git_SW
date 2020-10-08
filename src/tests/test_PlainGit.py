from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import pytest

path = r"C:\Users\paragk1\PycharmProjects\Git_SW\chromedriver.exe"
driver = Chrome(executable_path=path)


def test_test1():
    driver.get("https://github.com")
    driver.find_element_by_xpath("//*[@class='d-lg-flex mb-3 mb-lg-0']//following-sibling::a[@href='/login']").click()
    driver.find_element_by_xpath("//*[@id='login_field']").send_keys('ppqe')
    driver.find_element_by_xpath("//*[@id='password']").send_keys("az123@az123")
    driver.find_element_by_xpath( "//*[@value='Sign in']" ).send_keys(Keys.RETURN)
    driver.find_element_by_xpath("//*[@class='avatar avatar-user ']").click()
    driver.find_element_by_xpath("//*[@class='logout-form']").click()


