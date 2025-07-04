import bs4
import requests
import os
import time
import pandas as pd

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

while True:
    try:
        view_more = driver.find_element(By.XPATH, "//button[.//span[text()='View More']]")  
        time.sleep(2)
        view_more.click()
        print("Clicked 'View More'")
        time.sleep(2)
    except:
        break
    
tickets_data = []
# (Get names of lottery present in current page)
elements = driver.find_elements(By.TAG_NAME, "li")
for el in elements:
    try:
        name = el.find_element(By.CLASS_NAME, "inline-block.focus-pink").text
        top_prize = el.find_element(By.CLASS_NAME, "text-lg").text
        ticket_price = el.find_element(By.XPATH, ".//dt[text()='Price']/following-sibling::dd[1]").text
        ticket_info = {
            "Name": name,
            "Top Prize": top_prize,
            "Ticket Price": ticket_price
        }
        tickets_data.append(ticket_info)

    except:
        continue
df = pd.DataFrame(tickets_data)

# Optional: Save to CSV
df.to_csv("lottery_tickets_data.csv", index=False)

# Print preview
print(df.head())
# 🎯 Find all scratch-off ticket cards


# <dd class="text-lg">$5,000,000</dd>   Price money
# <dt class="sr-only">Price</dt> Price of ticket
# <span class="block bg-center bg-cover rounded-t-lg bg-beige-300 ratio ratio-4:3 lazyloaded" data-bg="/content/dam/flalottery-web/images/games/scratch-offs/$5,000,000-cash-money/fl-1594-$5000000-cash-money-teaser@2x.png/jcr:content/renditions/cq5dam.web.1280.1280.jpeg" style="background-image: url(&quot;/content/dam/flalottery-web/images/games/scratch-offs/$5,000,000-cash-money/fl-1594-$5000000-cash-money-teaser@2x.png/jcr:content/renditions/cq5dam.web.1280.1280.jpeg&quot;);"></span>
# //*[@id="scratchoffsearch-6c58e32c1d-vc-results"]/li[1]/article/div/div/dl/div[2]/dd


# elements = driver.find_elements(By.TAG_NAME, "li")
# elements = driver.find_elements(By.CSS_SELECTOR, "li.game-item")

# for element in elements:
#     name = element.find_element(By.CSS_SELECTOR, ".inline-block.focus-pink").text
#     top_prize = element.find_element(By.CLASS_NAME, "text-lg").text
#     ticket_price = element.find_element(By.XPATH, ".//dt[text()='Price']/following-sibling::dd[1]").text
#     tickets_data = []

#     print(top_prize)

# for el in elements:
#     try:
#         name = el.find_element(By.CSS_SELECTOR, ".inline-block.focus-pink").text
#         top_prize = el.find_element(By.CLASS_NAME, "text-lg").text
#         ticket_price = el.find_element(By.XPATH, ".//dt[text()='Price']/following-sibling::dd[1]").text

#         ticket_info = {
#             "Name": name,
#             "Top Prize": top_prize,
#             "Ticket Price": ticket_price
#         }
#         tickets_data.append(ticket_info)
#         print(ticket_info)

#     except Exception as e:
#         print(f"❌ Error: {e}")
#         continue

#print(tickets_data)
# df = pd.DataFrame(tickets_data)

# # Optional: Save to CSV
# df.to_csv("lottery_tickets_data.csv", index=False)

# # Print preview
# print(df.head())