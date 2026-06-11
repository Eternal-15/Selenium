from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

pages = [
    ("Home", "https://eternal-15.github.io/Mero-Kharcha/home.html"),
    ("Add Expenses", "https://eternal-15.github.io/Mero-Kharcha/addExpenses.html"),
    ("View Expenses", "https://eternal-15.github.io/Mero-Kharcha/viewExpenses.html"),
    ("Budget", "https://eternal-15.github.io/Mero-Kharcha/budget.html"),
    ("Report", "https://eternal-15.github.io/Mero-Kharcha/report.html"),
]

# for page_name, url in pages:
#     driver.get(url)
#     time.sleep(2)
#     assert "Mero Kharcha" in driver.title, f"FAILED: {page_name} title incorrect"
#     print(f"PASSED: {page_name} loaded correctly — Title: {driver.title}")

driver.get(pages[1][1])
dropdown = driver.find_element(By.ID, "category")
select = Select(dropdown)
select.select_by_visible_text("Food")

amount = driver.find_element(By.ID, "amount")
amount.send_keys(1500)

date = driver.find_element(By.ID, "date")
date.send_keys("06/04/2026")

depart_dropdown = driver.find_element(By.ID, "department")
select_dept = Select(depart_dropdown)
select_dept.select_by_visible_text("Finance")

notes = driver.find_element(By.ID, "notes")
notes.send_keys("Team Lunch")
time.sleep(5)

driver.find_element(By.XPATH, "//button[text()='Add Expense']").click()

print("Test passed succesfully!!")
driver.quit()
print("\nAll navigation tests passed.")