from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.get("https://duckduckgo.com/")
sleep(1)
logo = driver.find_element(By.CSS_SELECTOR, '#content_homepage > div.cw--c > div.logo-wrap--home')
assert logo.is_displayed() is True
sleep(2)
driversearchBar = search_input = driver.find_element(By.ID, "search_form_input_homepage")
sleep(1)
search_input.send_keys('python')
sleep(1)
search_input.send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, "div#r1-0 a.result__a.js-result-title-link")
search_input = driver.find_element(By.CSS_SELECTOR, "#search_form_input")
search_input.clear()
sleep(1)
search_input.send_keys('dog')
sleep(1)
search_input.send_keys(Keys.ENTER)
driver.close()
