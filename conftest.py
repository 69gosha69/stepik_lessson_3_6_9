import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default= "ru",
                     help="Choose language: 'ru' or 'es'")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser = None
    if user_language:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        print("\nstart browser for test..")
    else:
        raise pytest.UsageError('--language should be for example: "es" or "fr"')
    yield browser
    print("\nquit browser..")
    browser.quit()
    