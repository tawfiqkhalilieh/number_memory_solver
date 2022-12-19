# the test: https://humanbenchmark.com/tests/number-memory
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def play_level(browser):
    try:
        number: str = WebDriverWait(browser, 1000000).until( EC.presence_of_element_located((By.CLASS_NAME,'big-number'))).text
        input: any = WebDriverWait(browser, 1000000).until( EC.presence_of_element_located((By.CSS_SELECTOR,"input[type='text']")))
        input.send_keys(number)
        for _ in range(2):
            submit: any = WebDriverWait(browser, 1000000).until( EC.presence_of_element_located((By.CLASS_NAME,'e19owgy710')))
            submit.click()
    except:
        pass

print("Please enter the level you want to reach (0 to play forever): ", end="")
level = int(input())

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://humanbenchmark.com/tests/number-memory")

start: any = WebDriverWait(browser, 10).until( EC.presence_of_element_located((By.CLASS_NAME,'css-de05nr')))
start.click()


if not level:
    while True: play_level(browser=browser)
else:
    for i in range(level-1): play_level(browser=browser)

input: any = WebDriverWait(browser, 1000000).until( EC.presence_of_element_located((By.CSS_SELECTOR,"input[type='text']")))
input.send_keys("Exit")
submit: any = WebDriverWait(browser, 1000000).until( EC.presence_of_element_located((By.CLASS_NAME,'e19owgy710')))
submit.click()

time.sleep(15)