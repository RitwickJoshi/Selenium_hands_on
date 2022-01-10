from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
def player(chrome_path, query_string):
    """this player takes in input as chrome driver path and a query and plays youtube automatically and skips ads for you,
    if ran into any error run the code 2 to 3 times.
    
    Args:
        chrome_path (string): input the chrome driver path.
        query_string (string): input the query you want to perform.
    """
    #* it is very important to write if you run from terminal as this line keeps the window open else it closes automatically
    chrome_opti = Options()
    chrome_opti.add_experimental_option("detach", True) 
    
    chrome_driver = webdriver.Chrome(chrome_options = chrome_opti, executable_path=chrome_path) #* driver path and extra config goes here
    chrome_driver.maximize_window()
    chrome_driver.get('https://www.youtube.com/')
    chrome_driver.find_element_by_id("search").send_keys(query_string) #* your search goes here
    
    #* below is the code for getting the element and clicking them one by one.
    chrome_driver.find_element_by_id('search-icon-legacy').click()
    chrome_driver.find_elements_by_id("content")[0].click() #* clicks the first video link
    sleep(10) #* sleep for 10 seconds for youtube skip add button to show up could also use implicitly_wait or explicitly
    #TODO: need to learn about implicit wait so that it waits for the css tag to appear then proceeds further
    try:
        chrome_driver.find_element_by_css_selector('.ytp-ad-skip-button').click()
    except Exception as e:
        print('no skipable or some error; \n', e)

if __name__ == '__main__':
    #chrome_path = input("Enter the web Driver path: ")
    chrome_path = "C:\\Users\\DESKTOP\\Desktop\\Compiler\\Pythonfiles\\chromedriver_win32\\chromedriver.exe"
    query_string = input("Enter the query string you want to search: ")
    player(chrome_path, query_string)
