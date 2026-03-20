from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/signup")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys("Azad")

driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("azadsr15@gmail.com")
print("Email entered")
driver.find_element(By.XPATH, "//button[text()='Signup']").click()
wait.until(EC.visibility_of_element_located((By.ID, "id_gender1")))
driver.find_element(By.ID, "id_gender1").click()
newsletter = driver.find_element(By.ID, "newsletter")
offers = driver.find_element(By.ID, "optin")
newsletter.click()
offers.click()
print("Checkboxes selected")

print("Newsletter checked:", newsletter.get_attribute("checked"))
print("Offers checked:", offers.get_attribute("checked"))
