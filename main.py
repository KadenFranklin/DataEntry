import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

data1 = pd.read_excel(r"C:\Users\Kaden's Laptop\PycharmProjects\DataEntry\Tree_Data.xlsx", sheet_name='1-1150')
df = pd.DataFrame(data1, columns=['ID', 'Location', 'Latitude', 'Longitude', 'Common name', 'Scientific name', 'Ht', 'HAZ ', 'Target', 'Defects', 'Cond.', 'Maintenance', '???', 'Comments'])

# data2 = pd.read_excel(r"C:\Users\Kaden's Laptop\PycharmProjects\DataEntry\Tree_Data.xlsx", sheet_name='3000-5000')
# df2 = pd.DataFrame(data2, columns=['ID', 'Location', 'Latitude', 'Longitude', 'Common name', 'Scientific name', 'Ht', 'HAZ ', 'Target', 'Defects', 'Cond.', 'Maintenance', '???', 'Comments', 'Planted', 'Photo', 'Icon', 'No.'])

browser = webdriver.Chrome()
browser.get('https://localhost:44367/Trees/Create')

for i in df.iterrows():
    # check if it is in the database somehow
    # maybe dont, just gonna get an error page if it is
    dis = i.__getitem__(1)
    if (dis[1] == 'Nan') & (dis[2] == 'Nan') & (dis[3] == 'Nan'):
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
                enter = browser.find_element(By.CLASS_NAME, "btn btn-primary")
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
                enter = browser.find_element(By.CLASS_NAME, "btn btn-primary")
                enter.send_keys(Keys.ENTER)
                browser.get('https://localhost:44367/Trees/Create')
            else:
                ARROW_DOWN = u'\ue015'
                name.send_keys(ARROW_DOWN)
                count += 1

        if dis[6] != 'Nan':
            tree_dbh = browser.find_element(By.ID, "Tree_DBH")
            tree_dbh.send_keys(dis[6])

        if dis[7] != 'Nan':
            tree_hgt = browser.find_element(By.ID, "Tree_Height")
            tree_hgt.send_keys(dis[7])

        if dis[8] != 'Nan':
            tree_haz = browser.find_element(By.ID, "Tree_Hazard")
            tree_haz.send_keys(dis[8])

        if dis[9] != 'Nan':
            tree_cond = browser.find_element(By.ID, "Tree_Condition")
            tree_cond.send_keys(dis[9])

        if dis[10] != 'Nan':
            tree_com = browser.find_element(By.ID, "Tree_Comment")
            tree_com.send_keys(dis[10])

        if dis[0] == 1:
            break

# browser.get('https://localhost:44367/Specialties')

# maybe come up with a way to do specialties

# Add cat:
# <input type="button" onclick="AddCat()" value="+">

# then becomes a dropdown
# <select class="form-control valid" id="SpecialtyTrees_0__SpecialtyTitle" name="SpecialtyTrees[0].SpecialtyTitle" aria-invalid="false"><option value=""></option><option value="Old">Old</option></select>

# Enter button:
# <input type="submit" value="Create" class="btn btn-primary">