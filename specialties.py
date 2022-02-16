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
browser.get('https://localhost:44367/trees/')
browser.refresh()


table_id = browser.find_element(By.TAG_NAME, 'tbody')
rows = table_id.find_elements(By.TAG_NAME, "tr")
for row in rows:
    tree_id = row.find_elements(By.TAG_NAME, "td")[0]
    comment = row.find_elements(By.TAG_NAME, "td")[7]
    sci_name = row.find_elements(By.TAG_NAME, "td")[9]
    crud_row = row.find_elements(By.TAG_NAME, "td")[10]
    edit = crud_row.find_elements(By.TAG_NAME, "a")[0]

    new = webdriver.Chrome()
    new.get('https://localhost:44367/Trees/Edit?id=' + tree_id.text)
    sel_spec = Select(browser.find_element(By.ID, "SpecialtyTree_SpecialtyTitle"))
    spec = browser.find_element(By.ID, "SpecialtyTree_SpecialtyTitle")
    count = 1

    for option in sel_spec.options:
        # do some comparison with scientific name
        # maybe write a function
        if option.text == dis[1]:
            spec.send_keys(Keys.ENTER)
            break
        # if count == len(sel_spec.options):
            # if run out of options
            # shouldnt happen
        else:
            ARROW_DOWN = u'\ue015'
            spec.send_keys(ARROW_DOWN)
            count += 1
    # after selecting correct category,
    # add category button
    # maybe a refresh button
    # save button
