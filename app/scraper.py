import bs4
import requests
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 🔧 Define your ChromeDriver path correctly
chromeDriverPath = r"C:\Users\smeet\OneDrive\Desktop\Project_Lottery_DLS\chromedriver-win64\chromedriver.exe"

# ✅ Create a Service object
service = Service(executable_path=chromeDriverPath)

# ✅ Optional: Set Chrome to headless mode
options = Options()
#options.add_argument("--headless")
#options.add_argument("--window-size=1920,1080")

# ✅ Use service and options in Chrome() constructor
driver = webdriver.Chrome(service=service, options=options)

#driver.get("https://floridalottery.com/games/scratch-offs")


