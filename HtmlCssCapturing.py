from selenium import webdriver
chrome_driver = webdriver.Chrome(executable_path="C:/Users/DESKTOP/Desktop/Compiler/Pythonfiles/chromedriver_win32/chromedriver.exe")
chrome_driver.get('https://rahulshettyacademy.com/angularpractice/')
chrome_driver.maximize_window()

#chrome_driver.find_element_by_name('name').send_keys('Rj test') #* selecting name using name

chrome_driver.find_element_by_css_selector("input[name='name']").send_keys('Rj test') #* selecting name using css_selector

chrome_driver.find_element_by_name('email').send_keys('rj@gg.com') #* selecting name using name

chrome_driver.find_element_by_id('exampleCheck1').click() #* selecting checkbox using id

#chrome_driver.find_element_by_xpath("//input[@type = 'submit']").click() #* selecting button using xpath

chrome_driver.find_element_by_css_selector("input[value='Submit']").click()

print(chrome_driver.find_element_by_class_name("alert-success").text) #* selecting success message using class name
