from selenium import webdriver

chrome_driver = webdriver.Chrome(executable_path="C:/Users/DESKTOP/Desktop/Compiler/Pythonfiles/chromedriver_win32/chromedriver.exe")
chrome_driver.maximize_window()

chrome_driver.get('https://login.salesforce.com/')
chrome_driver.find_element_by_css_selector("#username").send_keys("This is Username")
chrome_driver.find_element_by_css_selector(".password").send_keys("This is Password")
chrome_driver.find_element_by_css_selector('#rememberUn').click()
chrome_driver.find_element_by_css_selector('.password').clear()
chrome_driver.find_element_by_link_text('Forgot Your Password?').click()
