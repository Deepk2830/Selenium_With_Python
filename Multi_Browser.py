from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver=webdriver.Ie(executable_path="C:\Python\drivers\IEDriverServer_x64_4.2.0\IEDriverServer.exe")
driver.get("http://newtours.demoaut.com/")
print(driver.title)  # title of page
print(driver.current_url) #return url
print(driver.page_source) # HTML code for the page
driver.close() #
