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
options.add_experimental_option("detach", True)
#options.add_argument("--headless")
#options.add_argument("--window-size=1920,1080")

# ✅ Use service and options in Chrome() constructor
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.flalottery.com/scratch-offs")
time.sleep(2)  # Wait for page to fully load

# <span class="cmp-button__text">View More</span>
# //*[@id="scratchoffsearch-6c58e32c1d"]/div[2]/button
# <button class="cmp-button spacing-t-none spacing-b-none min-w-[12rem] justify-center bg-beige-200 text-black" type="button"><!----><span class="cmp-button__text">View More</span></button>
while True:
    try:
        view_more = driver.find_element(By.XPATH, "//button[.//span[text()='View More']]")  
        time.sleep(2)
        view_more.click()
        print("Clicked 'View More'")
        time.sleep(2)
    except:
        break
    

# (Get names of lottery present in current page)
elements = driver.find_elements(By.TAG_NAME, "li")
for el in elements:
    try:
        name = el.find_element(By.CLASS_NAME, "inline-block.focus-pink").text
        print(name)
    except:
        continue


