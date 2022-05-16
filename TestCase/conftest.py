import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome("F:\\Python\\Driver\\chromedriver.exe")
    if browser=='firfox':
        driver=webdriver.ie("F:\\Python\\Driver\\internetexplorer.exe")
    else:
        driver=webdriver.Chrome("F:\\Python\\Driver\\chromedriver.exe")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

############### pyTest html Report ###############
#it is Hook for adding environment info to html report

def pytest_configure(config):
    config._metadata['Project Name']='Commerce'
    config._metadata['Module Name']='Customer'
    config._metadata['Tester']='Dhananjay'

@pytest.mark.optionalHook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
    metadata.pop("Packages",None)

