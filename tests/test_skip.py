from selene import browser
import pytest


@pytest.mark.skip
def test_mobile(desktop_window):
    browser.open("https://github.com/")
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.skip
def test_mobile(mobile_window):
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()
