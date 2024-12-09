from selene import browser, have, be
from selene.api import s


def test_google_open():
    browser.open("https://google.com/ncr")
    assert browser.driver.current_url.startswith("https://www.google.com/")


def test_google_search():
    browser.open("https://google.com/ncr")
    s('[name=q]').should(be.blank).type('pytest github')
    s('[name=btnK]').click()
    s('.MBeuO').should(have.text('The pytest framework makes it easy to write small tests, yet ...'))


def test_negative_google_search():
    browser.open("https://google.com/ncr")
    s('[name=q]').should(be.blank).type('1p23iwefu2i9fdkmdk123131').press_enter()
    s('#rcnt').should(have.text('did not match any documents.'))
