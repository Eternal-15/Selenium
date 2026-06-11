import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

def setup():
    options = Options()
    options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    return driver

user = {"name": "Shinji", "email": "shinji@email.com", "password": "Password", "confirmPass": "Password", "role":"Admin", "depart": "Finance"}

def register(driver):
    driver.get("https://eternal-15.github.io/Mero-Kharcha/index.html")
    driver.find_element(By.XPATH, "//a[@onclick='showRegisterForm()']").click()
    time.sleep(1)

    fullName = driver.find_element(By.ID, "registerName")
    fullName.send_keys(user["name"])

    email = driver.find_element(By.ID, "registerEmail")
    email.send_keys(user["email"])

    password = driver.find_element(By.ID, "registerPassword")
    password.send_keys(user["password"])

    confPass = driver.find_element(By.ID, "confirmPassword")
    confPass.send_keys(user["confirmPass"])

    role_dropdown = driver.find_element(By.ID, "userRole")
    select_role = Select(role_dropdown)
    select_role.select_by_visible_text(user["role"])

    depart_drop = driver.find_element(By.ID, "userDepartment")
    select_depart = Select(depart_drop)
    select_depart.select_by_visible_text(user["depart"])
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[text()='Register']").click()
    time.sleep(2)

def login(driver):
    driver.get("https://eternal-15.github.io/Mero-Kharcha/index.html")
    time.sleep(3)
    logEmail =driver.find_element(By.ID, "loginEmail")
    logEmail.send_keys(user["email"])

    logPass = driver.find_element(By.ID, "loginPassword")
    logPass.send_keys(user["password"])
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(3)

def test_login(driver):
    login(driver)
    
    assert "home.html" in driver.current_url
    print(f"Current URL: {driver.current_url}")
    print("Registration Test successfully executed")

def test_add_expenses(driver):
    # login(driver)
    driver.get("https://eternal-15.github.io/Mero-Kharcha/add-expenses.html")
    time.sleep(3)
    
    category = driver.find_element(By.ID, "category")
    select_category = Select(category)
    select_category.select_by_visible_text("Accommodation")

    amount = driver.find_element(By.ID, "amount")
    amount.send_keys(1500)

    date = driver.find_element(By.ID, "date")
    date.send_keys("06/08/2026")

    depart = driver.find_element(By.ID, "department")
    select_dept = Select(depart)
    select_dept.select_by_visible_text("Information Technology (IT)")

    emp_name = driver.find_element(By.ID, "employeeName")
    emp_name.send_keys(user["name"])

    notes = driver.find_element(By.ID, "notes")
    notes.send_keys("Purchased office lunch by IT department @Rs.1500.00")
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()='Add Expense']").click()
    time.sleep(3)

def test_view_expenses(driver):
    # login(driver)
    driver.get("https://eternal-15.github.io/Mero-Kharcha/view-expenses.html")
    
    table = driver.find_element(By.ID, "expensesList")
    assert "Accommodation" in table.text
    print("Test passed successfully")

def teardown(driver):
    driver.quit()
    print("Browser closed.")

driver = setup()
try:
    register(driver)
    test_login(driver)
    test_add_expenses(driver)
    test_view_expenses(driver)
finally:
    teardown(driver)