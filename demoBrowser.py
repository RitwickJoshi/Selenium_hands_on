from selenium import webdriver

chrome_driver = webdriver.Chrome(executable_path="C:/Users/DESKTOP/Desktop/Compiler/Pythonfiles/chromedriver_win32/chromedriver.exe")

chrome_driver.get("https://www.youtube.com/")
chrome_driver.maximize_window() # * maximizes window 

print(chrome_driver.title, chrome_driver.current_url)
# chrome_driver.close() # * only current window will close

chrome_driver.get("https://www.google.com/")
print(chrome_driver.title, chrome_driver.current_url)

chrome_driver.back() #* the back button to go back to previous page
chrome_driver.minimize_window()# * minimizes window 

print(chrome_driver.title, chrome_driver.current_url)
chrome_driver.refresh() #* the refresh button to refresh the browser

chrome_driver.quit() # * all window will close