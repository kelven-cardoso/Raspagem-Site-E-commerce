from selenium import webdriver

#abrir navegador
navegador = webdriver.Chrome()
#abrindo site
navegador.get('https://www.google.com/')
#localizar elemento, a partir do path dele (inspecionando e copiando
navegador.find_element_by_xpath('//*[@id="gb"]/div/div[1]/div/div[1]/a').click()   #adicionar-> .click() -< para clicar 
