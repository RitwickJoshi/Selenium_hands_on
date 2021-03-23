from selenium import webdriver
from time import sleep

chrome_driver = webdriver.Chrome(executable_path="C:/Users/DESKTOP/Desktop/Compiler/Pythonfiles/chromedriver_win32/chromedriver.exe")
chrome_driver.maximize_window()
chrome_driver.get('https://www.youtube.com/')
chrome_driver.find_element_by_id("search").send_keys('garmi')
chrome_driver.find_element_by_id('search-icon-legacy').click()
chrome_driver.find_element_by_tag_name('ytd-video-renderer').click()
sleep(10)
try:
    chrome_driver.find_element_by_css_selector('.ytp-ad-skip-button').click()
except Exception:
    print('no skipable or some error')
    