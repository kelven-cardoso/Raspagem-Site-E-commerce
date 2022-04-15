from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://google.com")

#Restante do código

driver.quit()