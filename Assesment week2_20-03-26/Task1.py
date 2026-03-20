from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep

driver=webdriver.Chrome()
driver.get('https://www.amazon.com')
sleep(2)

assert 'Amazon.com' in driver.title,'title not present'
assert 'https://www.amazon.com' in driver.current_url,'current_url not present'

wait=WebDriverWait(driver,10)
all_button=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='nav-search-scope nav-sprite']")))
all_button.click()

select=Select(wait.until(EC.presence_of_element_located((By.XPATH,"//select[@id='searchDropdownBox']"))))
select.select_by_index(5)

book=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
book.send_keys("Harry Potter",Keys.ENTER)

wait.until(EC.presence_of_element_located((By.XPATH,'//span[text()="1-16 of over 10,000 results for"]')))

elements=driver.find_elements(By.XPATH,"//div[@data-cy='title-recipe'][1]/descendant::span[1]")
i=0
for element in elements:
    i+=1
    if(i>=6):
        break
    print(element.text)

click_first=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@data-cy='title-recipe'][1]/descendant::span[1]")))
click_first.click()
sleep(2)
