from selene import browser
import pytest


@pytest.fixture(params=[(1680, 1050), (1920, 1080)], scope='function')
def desktop_window(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield
    browser.quit()


@pytest.fixture(params=[(390, 844), (414, 896)], scope='function')
def mobile_window(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield
    browser.quit()
