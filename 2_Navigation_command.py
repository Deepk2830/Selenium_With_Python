import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://newlinkautomaton.com/") # FR
print(driver.title) #FR
driver.get("https://www.selenium.dev/downloads/")
time.sleep(5)
print(driver.title) #tt
driver.back()
time.sleep(5)
print(driver.title) #FR
driver.forward()
time.sleep(5)
print(driver.title) #tt
