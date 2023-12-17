from selene import browser
import pytest


@pytest.fixture(params=['desktop', 'mobile'])
def window_size(request):
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080

    if request.param == 'mobile':
        browser.config.window_width = 390
        browser.config.window_height = 844

    yield
    browser.quit()


@pytest.mark.parametrize("window_size", ["desktop"], indirect=True)
def test_desktop(window_size):
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize("window_size", ["mobile"], indirect=True)
def test_desktop(window_size):
    browser.open("https://github.com/")
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
