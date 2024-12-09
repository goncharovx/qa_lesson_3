import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def browser_setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--blink-settings=imagesEnabled=false")

    driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.window_width = 1980
    browser.config.window_height = 1080
    browser.config.timeout = 2

    yield
