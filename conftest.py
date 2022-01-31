import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="ru, es")

# executable_path="c:/webdrive/chromedriver.exe"
# executable_path="c:/webdrive/geckodriver.exe"

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(executable_path="c:/webdrive/chromedriver.exe", options=options)
    yield browser
    browser.quit()