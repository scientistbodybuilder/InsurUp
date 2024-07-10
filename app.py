from selenium import webdriver
import os
PATH = os.getenv('PATH')
driver = webdriver.Chrome(PATH)


driver.get("https://techwithtim.net")
driver.quit()