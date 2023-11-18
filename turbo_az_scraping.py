import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('./chromedriver.exe')
# driver = webdriver.Chrome(service=service)
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://turbo.az/')

# Function to slowly scroll down the page
def slow_scroll_down(driver):
    SCROLL_HEIGHT = 300    # Distance to scroll in each step (pixels)

    while True:
        # Scroll the page down by a certain amount
        driver.execute_script(f"window.scrollBy(0, {SCROLL_HEIGHT});")

        # Waiting time (Optional, can be adjusted)
        time.sleep(1)

        # # If the bottom of the page is reached, exit the loop
        # if driver.execute_script("return window.innerHeight + window.scrollY >= document.body.scrollHeight"):
        #     break

        # If the scroll position surpasses 10,000 pixels, exit the loop to stop scrolling.
        if driver.execute_script("return window.innerHeight + window.scrollY >= 10000"):
            break

#--------------------------------------------------------------------------
# Slowly scroll down the page
slow_scroll_down(driver)

# Allow time for other actions (e.g., wait for 5 seconds)
time.sleep(5)

car_prices = driver.find_elements(By.CLASS_NAME, 'product-price')
car_names = driver.find_elements(By.CLASS_NAME, 'products-i__name')
car_years = driver.find_elements(By.CLASS_NAME, 'products-i__attributes')

car_list = []

for i in range(len(car_prices)):
    car = {
        "Name": car_names[i].text,
        "Price": car_prices[i].text,
        "Year": car_years[i].text
    }
    car_list.append(car)
    # if i == 500:
    #     break

with open('PREMIUM_ADS_cars.json', 'w', encoding='utf-8') as json_file:
    json.dump(car_list, json_file, ensure_ascii=False, indent=4)

print('Successfully finished')
# Close the browser
driver.quit()
