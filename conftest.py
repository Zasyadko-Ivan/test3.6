import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#chrome_link = "/Users/ivanzasadko/PycharmProjects/pythonProject/chromedriver/chromedriver"


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language == "ar" or user_language == "ca" or user_language == "cs" or user_language == "da" or user_language == "de" or user_language == "en-gb" or user_language == "el" or user_language == "es" or user_language == "fi" or user_language == "fr" or user_language == "it" or user_language == "ko" or user_language == "nl" or user_language == "pl" or user_language == "pt" or user_language == "pt-br" or user_language == "ro" or user_language == "ru" or user_language == "sk" or user_language == "uk" or user_language == "zh-hans":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        #browser = webdriver.Chrome(options=options, executable_path=chrome_link)
    else:
        raise pytest.UsageError(f"This {user_language} language does not exist")

    yield browser
    print("\nquit browser..")
    browser.quit()