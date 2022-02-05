import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


data2 = pd.read_excel(r"C:\Users\Kaden's Laptop\PycharmProjects\DataEntry\Tree_Data.xlsx", sheet_name='3000-5000')
df = pd.DataFrame(data2, columns=['ID', 'Location', 'Latitude', 'Longitude', 'Common name', 'Scientific name', 'DBH', 'Ht', 'HAZ ', 'Cond.', 'Comments'])

# data1 = pd.read_excel(r"C:\Users\Kaden's Laptop\PycharmProjects\DataEntry\Tree_Data.xlsx", sheet_name='1-1150')
# df = pd.DataFrame(data1, columns=['ID', 'Location', 'Latitude', 'Longitude', 'Common name', 'Scientific name', 'DBH', 'Ht', 'HAZ ', 'Cond.', 'Comments'])

browser = webdriver.Chrome()

for i in df.iterrows():
    browser.get('https://localhost:44367/Trees/Create')
    browser.refresh()
    dis = i.__getitem__(1)
    if (not isinstance(dis[1], float)) & (not isinstance(dis[2], float)) & (not isinstance(dis[3], float)):
        continue
    else:
        tree_id = browser.find_element(By.ID, "Tree_TreeID")
        tree_id.send_keys(dis[0])
        tree_lat = browser.find_element(By.ID, "Tree_Latitude")
        tree_lat.send_keys(dis[2])
        tree_long = browser.find_element(By.ID, "Tree_Longitude")
        tree_long.send_keys(dis[3])
        sel_loc = Select(browser.find_element(By.ID, "Tree_LocationName"))
        location = browser.find_element(By.ID, "Tree_LocationName")
        count = 1

        for option in sel_loc.options:
            if option.text == dis[1]:
                location.send_keys(Keys.ENTER)
                break
            if count == len(sel_loc.options):
                browser.get('https://localhost:44367/Locations/Create')
                new_loc = browser.find_element(By.ID, "Location_LocationName")
                new_loc.send_keys(dis[1])
                enter1 = browser.find_element(By.ID, "ENTER")
                ActionChains(browser).click(enter1).perform()
                browser.get('https://localhost:44367/Trees/Create')
                tree_id = browser.find_element(By.ID, "Tree_TreeID")
                tree_id.send_keys(dis[0])
                tree_lat = browser.find_element(By.ID, "Tree_Latitude")
                tree_lat.send_keys(dis[2])
                tree_long = browser.find_element(By.ID, "Tree_Longitude")
                tree_long.send_keys(dis[3])
                sel_loc = Select(browser.find_element(By.ID, "Tree_LocationName"))
                location = browser.find_element(By.ID, "Tree_LocationName")
                for opt in sel_loc.options:
                    if opt.text == dis[1]:
                        location.send_keys(Keys.ENTER)
                        break
                    else:
                        ARROW_DOWN = u'\ue015'
                        location.send_keys(ARROW_DOWN)
            else:
                ARROW_DOWN = u'\ue015'
                location.send_keys(ARROW_DOWN)
                count += 1
        sel_name = Select(browser.find_element(By.ID, "Tree_ScientificName"))
        name = browser.find_element(By.ID, "Tree_ScientificName")
        count2 = 1

        for option in sel_name.options:
            if option.text == dis[5]:
                name.send_keys(Keys.ENTER)
                break
            if count2 == len(sel_name.options):
                browser.get('https://localhost:44367/Scientifics/Create')
                new_name = browser.find_element(By.ID, "Scientific_ScientificName")
                new_name.send_keys(dis[5])
                enter1_2 = browser.find_element(By.ID, "add_common")
                ActionChains(browser).click(enter1_2).perform()
                common = browser.find_element(By.ID, "CommonNames[0]_Name")
                common.send_keys(dis[4])
                enter2 = browser.find_element(By.ID, "ENTER")
                ActionChains(browser).click(enter2).perform()
                browser.get('https://localhost:44367/Trees/Create')
                tree_id = browser.find_element(By.ID, "Tree_TreeID")
                tree_id.send_keys(dis[0])
                tree_lat = browser.find_element(By.ID, "Tree_Latitude")
                tree_lat.send_keys(dis[2])
                tree_long = browser.find_element(By.ID, "Tree_Longitude")
                tree_long.send_keys(dis[3])
                sel_loc = Select(browser.find_element(By.ID, "Tree_LocationName"))
                location = browser.find_element(By.ID, "Tree_LocationName")
                for opt in sel_loc.options:
                    if opt.text == dis[1]:
                        location.send_keys(Keys.ENTER)
                        break
                    else:
                        ARROW_DOWN = u'\ue015'
                        location.send_keys(ARROW_DOWN)
                sel_name = Select(browser.find_element(By.ID, "Tree_ScientificName"))
                name = browser.find_element(By.ID, "Tree_ScientificName")
                count2 = 1
                for op in sel_name.options:
                    if op.text == dis[5]:
                        name.send_keys(Keys.ENTER)
                        break
                    else:
                        ARROW_DOWN = u'\ue015'
                        name.send_keys(ARROW_DOWN)
            else:
                ARROW_DOWN = u'\ue015'
                name.send_keys(ARROW_DOWN)
                count2 += 1
        if not isinstance(dis[6], float):
            tree_dbh = browser.find_element(By.ID, "Tree_DBH")
            tree_dbh.send_keys(dis[6])
        if not isinstance(dis[7], float):
            tree_hgt = browser.find_element(By.ID, "Tree_Height")
            tree_hgt.send_keys(dis[7])
        if not isinstance(dis[8], float):
            tree_haz = browser.find_element(By.ID, "Tree_Hazard")
            tree_haz.send_keys(dis[8])
        if not isinstance(dis[9], float):
            tree_cond = browser.find_element(By.ID, "Tree_Condition")
            tree_cond.send_keys(dis[9])
        if not isinstance(dis[10], float):
            tree_com = browser.find_element(By.ID, "Tree_Comment")
            tree_com.send_keys(dis[10])
        enter = browser.find_element(By.ID, "ENTER")
        ActionChains(browser).click(enter).perform()
