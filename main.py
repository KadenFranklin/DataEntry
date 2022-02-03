import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

data1 = pd.read_excel(r"C:\Users\Kaden's Laptop\PycharmProjects\DataEntry\Tree_Data.xlsx", sheet_name='1-1150')
df = pd.DataFrame(data1, columns=['ID', 'Location', 'Latitude', 'Longitude', 'Common name', 'Scientific name', 'DBH', 'Ht', 'HAZ ', 'Cond.', 'Comments'])

# data2 = pd.read_excel(r"C:\Users\Kaden's Laptop\PycharmProjects\DataEntry\Tree_Data.xlsx", sheet_name='3000-5000')
# df2 = pd.DataFrame(data2, columns=['ID', 'Location', 'Latitude', 'Longitude', 'Common name', 'Scientific name', 'Ht', 'HAZ ', 'Target', 'Defects', 'Cond.', 'Maintenance', '???', 'Comments', 'Planted', 'Photo', 'Icon', 'No.'])

browser = webdriver.Chrome()
browser.get('https://localhost:44367/Trees/Create')

for i in df.iterrows():
    # check if it is in the database somehow
    # maybe dont, just gonna get an error page if it is
    dis = i.__getitem__(1)
    if (dis[1] == 'nan') & (dis[2] == 'nan') & (dis[3] == 'nan'):
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
        count = 0
        for option in sel_loc.options:
            if option.text == dis[1]:
                location.send_keys(Keys.ENTER)
                break
            elif count == len(sel_loc.options):
                browser.get('https://localhost:44367/Locations/Create')
                new_loc = browser.find_element(By.ID, "Location_LocationName")
                new_loc.send_keys(dis[1])
                enter = browser.find_element(By.ID, "ENTER")
                enter.send_keys(Keys.ENTER)
                browser.get('https://localhost:44367/Trees/Create')
            else:
                ARROW_DOWN = u'\ue015'
                location.send_keys(ARROW_DOWN)
                count += 1

        sel_name = Select(browser.find_element(By.ID, "Tree_ScientificName"))
        name = browser.find_element(By.ID, "Tree_ScientificName")
        count2 = 0
        for option in sel_name.options:
            if option.text == dis[5]:
                name.send_keys(Keys.ENTER)
                break
            elif count2 == len(sel_name.options):
                browser.get('https://localhost:44367/Scientific/Create')
                new_name = browser.find_element(By.ID, "Scientific_ScientificName")
                new_name.send_keys(dis[5])
                enter = browser.find_element(By.ID, "ENTER")
                enter.send_keys(Keys.ENTER)
                browser.get('https://localhost:44367/Trees/Create')
            else:
                ARROW_DOWN = u'\ue015'
                name.send_keys(ARROW_DOWN)
                count += 1

        if dis[6] != 'nan':
            tree_dbh = browser.find_element(By.ID, "Tree_DBH")
            tree_dbh.send_keys(dis[6])

        if dis[7] != 'nan':
            tree_hgt = browser.find_element(By.ID, "Tree_Height")
            tree_hgt.send_keys(dis[7])

        if dis[8] != 'nan':
            tree_haz = browser.find_element(By.ID, "Tree_Hazard")
            tree_haz.send_keys(dis[8])

        if dis[9] != 'nan':
            tree_cond = browser.find_element(By.ID, "Tree_Condition")
            tree_cond.send_keys(dis[9])

        if dis[10] != 'nan':
            tree_com = browser.find_element(By.ID, "Tree_Comment")
            tree_com.send_keys(dis[10])

        enter = browser.find_element(By.ID, "ENTER")
        ActionChains(browser).click(enter).perform()

        if dis[0] == 1:
            break