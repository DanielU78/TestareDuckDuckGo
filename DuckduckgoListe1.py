from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.get("https://duckduckgo.com/")
sleep(1)
searchBar = search_input = driver.find_element(By.ID, "search_form_input_homepage")
sleep(1)
search_input.send_keys('python')
sleep(1)
search_input.send_keys(Keys.ENTER)
sleep(1)
list1 = driver.find_element(By.CSS_SELECTOR, "[data-testid='result-title-a']").is_displayed()
print(list1)
main_page = page.MainPage(self.driver)
