from selenium import webdriver
#take screenshot from site
driver = webdriver.Chrome('C:\\Users\\PC\\AppData\\Local\\Programs\\Python\\Python310\\Chromium\\chromedriver.exe')
driver.get("http://www.python.org")
driver.save_screenshot('ss.png')
'''

#get window size
s = driver.get_window_size()
#obtain browser height and width
w = driver.execute_script('return document.body.parentNode.scrollWidth')
h = driver.execute_script('return document.body.parentNode.scrollHeight')
#set to new window size
driver.set_window_size(w, h)
#obtain screenshot of page within body tag
driver.find_element('body').screenshot("tutorialspoint.png")
driver.set_window_size(s['width'], s['height'])
'''
driver.close()