from time import sleep
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Firefox options
# https://wiki.mozilla.org/Firefox/CommandLineOptions

# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

ROOT_FOLDER = Path(__file__).parent
FIREFOX_DRIVER_EXE = ROOT_FOLDER / 'drivers' /  'geckodriver.exe'

def make_firefox_browser(*options: str) -> webdriver.Firefox:
    firefox_options = webdriver.FirefoxOptions()

    # firefox_options.add_argument('--headless')
    if options is not None:
        for option in options:
            firefox_options.add_argument(option)  # type: ignore

    firefox_service = Service(
        executable_path=str(FIREFOX_DRIVER_EXE),
    )

    browser = webdriver.Firefox(
        service=firefox_service,
        options=firefox_options
    )

    return browser

if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_firefox_browser(*options)

    browser.get('https://www.google.com')

    # Wait to find input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_input.send_keys('Hello, world!')
    search_input.send_keys(Keys.ENTER)

    # sleep(4)

    # results = browser.find_element(By.ID, "rhs")
    # print(results)
    # links = browser.find_elements(By.TAG_NAME, 'a')
    # print(f'Founded {len(links)} links.')
    # links[0].click()
    # print(links)

    sleep(TIME_TO_WAIT)

""" firefox_options = webdriver.FirefoxOptions()
firefox_service = Service(executable_path=FIREFO_XDRIVER_EXE)
firefox_browser = webdriver.Firefox(
    service=firefox_service,
    options=firefox_options,
)
#firefox_options.add_argument('--headless')

firefox_browser.get('https://www.google.com.br/')
time.sleep(5) """