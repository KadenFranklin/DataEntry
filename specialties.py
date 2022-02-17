import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# categories:
# Oaks
# Ashes
# Crepe Myrtles
# Oldest and Rarest Trees (maybe also scan for comment)
# Trees with Plaques (comments contain 'PLQ')

browser = webdriver.Chrome()
browser.get('https://localhost:44367/Trees/')
browser.refresh()
rows = browser.find_elements(By.TAG_NAME, "tr")

# for every row (maybe select element by index)
# check scientific name
# open a new tab, & edit the trees data

# for category in specialties
# choose the correct cat

# enter = browser.find_element(By.ID, "ENTER")
# ActionChains(browser).click(enter).perform()
