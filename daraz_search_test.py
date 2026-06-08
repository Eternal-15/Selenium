from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

driver = webdriver.Chrome(options=options)
driver.get("https://www.daraz.com.np")

time.sleep(3)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Nike shoes")
search_box.submit()

time.sleep(3)

print("Page title is:", driver.title)
assert "Nike" in driver.title or "nike" in driver.title.lower()

print("TEST PASSED — Search works correctly.")

driver.quit()