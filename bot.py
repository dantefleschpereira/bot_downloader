from selenium import webdriver
import time

from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://covid.saude.gov.br/')
element = driver.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[1]/div[2]/ion-button')
time.sleep(7)
element.click()