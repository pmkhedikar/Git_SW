import json
import pytest
import selenium.webdriver

#
# @pytest.fixture
# def config(scope='session'):
#     # Read the file
#     with open(r"C:\Users\paragk1\PycharmProjects\Git_SW\config.json") as config_file:
#         config = json.load(config_file)
#
#     # Assert values are acceptable
#     assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
#     assert isinstance( config['implicit_wait'], int )
#     assert config['implicit_wait'] > 0
#
#     # Return config so it can be used
#     return config
#
#
# @pytest.fixture
# def browser(config):
#     Chrome_path = r"C:\Users\paragk1\PycharmProjects\Git_SW\chromedriver.exe"
#     Firefox_path = r"C:\Users\paragk1\PycharmProjects\Git_SW\geckodriver.exe"
#
#     # Initialize the WebDriver instance
#     if config['browser'] == 'Firefox':
#         b = selenium.webdriver.Firefox(executable_path=Firefox_path)
#     elif config['browser'] == 'Chrome':
#         b = selenium.webdriver.Chrome(executable_path=Chrome_path)
#     elif config['browser'] == 'Headless Chrome':
#         opts = selenium.webdriver.ChromeOptions()
#         opts.add_argument( 'headless' )
#         b = selenium.webdriver.Chrome( executable_path=Chrome_path,options=opts )
#     else:
#         raise Exception( f'Browser "{config["browser"]}" is not supported' )
#
#     # Make its calls wait for elements to appear
#     b.implicitly_wait( config['implicit_wait'] )
#
#     # Return the WebDriver instance for the setup
#     yield b
#
#     # Quit the WebDriver instance for the cleanup
#     b.quit()

#if __name__ == '__main__':

@pytest.fixture
def browser():

  # Initialize the ChromeDriver instance
  Chrome_path = r"C:\Users\paragk1\PycharmProjects\Git_SW\chromedriver.exe"
  b = selenium.webdriver.Chrome(executable_path=Chrome_path)

  # Make its calls wait up to 10 seconds for elements to appear
  b.implicitly_wait(10)

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()