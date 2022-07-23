from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://covid.saude.gov.br/')
elemento = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[1]/div[2]/ion-button')
time.sleep(7)  
elemento.click()

