import time

import pytest
from selenium import webdriver
from pytest_testconfig import config

web_driver = None
from Infrastructure.WebDriverWrapper import Wrapper
from Infrastructure.BasicTest import BasicTestClass

@pytest.fixture(scope="function")
def driver_init(request, env):

    # from selenium import webdriver
    desired_caps = {'platform': 'Linux', 'browserName': 'chrome'}

    global web_driver

    if web_driver is None:

        web_driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_caps)
        Wrapper.driver = web_driver
        BasicTestClass.env = env

    elif web_driver is not None:

        web_driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_caps)
        Wrapper.driver = web_driver
        BasicTestClass.env = env

    web_driver.maximize_window()

    if env == 'test':
        web_driver.get(config['SUT']['TEST'])

    if env == 'sand':
        web_driver.get(config['SUT']['SAND'])

    if env == 'prod':
        web_driver.get(config['SUT']['PROD'])

    request.cls.driver = web_driver

    yield

    web_driver.quit()


def pytest_addoption(parser):
    parser.addoption("--env", action="store")
    parser.addoption("--platform", action="store")


@pytest.fixture(scope='session')
def env(request):
    name_value = request.config.option.env
    if name_value is None:
        pytest.skip()
    return name_value


@pytest.fixture(scope='session')
def platform(request):
    name_value = request.config.option.platform
    if name_value is None:
        pytest.skip()
    return name_value


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            time.sleep(1)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    web_driver.get_screenshot_as_file(name)


