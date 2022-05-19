from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://www.gatry.com")

items = driver.find_elements(By.XPATH, 
'//div[@class="description"]//h3//a')
for item in items:
    print(item.text)
