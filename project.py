import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "PythonAutomationFramework_1-master"))
from pages.HomePage import locators
import selenium
from selenium.webdriver.common.by import By
from pages.EventsPage.widgets.searchWidget import *
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome(
            executable_path="C:\\Users\\Dror\\Desktop\\Automation\\Automation+Devops\\chromedriver.exe")
            
driver.get("https://www.google.com")
