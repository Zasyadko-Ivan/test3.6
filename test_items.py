import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

    browser.find_element(By.XPATH, '//ul[@data-navigation="dropdown-menu"]/li[1]/a').click()
    browser.find_element(By.XPATH, '//img[@alt="The Girl Who Played with Non-Fire"]').click()

    time.sleep(5)

    assert browser.find_element(By.XPATH, '//a[@class="btn btn-default"]')



