from selenium import webdriver
from selenium.webdriver.common.by import By
import time


a = webdriver.Chrome()
a.maximize_window()
a.implicitly_wait(10)
a.get("https://sqatools.in/")
a.implicitly_wait(5)
time.sleep(10)
