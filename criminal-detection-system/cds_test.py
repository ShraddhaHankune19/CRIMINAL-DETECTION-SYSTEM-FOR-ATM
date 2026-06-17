from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Set up the WebDriver
driver = webdriver.Chrome()

# Step 2: Open a website
driver.get("https://example.com")

# Step 3: Interact with page content
heading = driver.find_element(By.TAG_NAME, "h1")
print("Page heading is:", heading.text)

# Step 4: Wait and close the browser
time.sleep(3)
driver.quit()
