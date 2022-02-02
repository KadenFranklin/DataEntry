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
    # maybe dont, just gonna get an error if it is
    dis = i.__getitem__(1)
    if dis[0].notnull() & dis[1].notnull() & dis[2].notnull() & dis[3].notnull():
        tree_id = browser.find_element(By.ID, "Tree_TreeID")
        tree_id.send_keys(dis[0])

        tree_lat = browser.find_element(By.ID, "Tree_Latitude")
        tree_lat.send_keys(dis[2])

        tree_long = browser.find_element(By.ID, "Tree_Longitude")
        tree_long.send_keys(dis[3])

        # if location name does not exist, go to the page and create it
        if browser.find_element(By.ID, "Tree_LocationName").select_by_visible_text(dis[1]):
            x = 1
        else:
            select_loc = browser.find_element(By.ID, "Tree_LocationName")
            select_loc.select_by_visible_text(dis[1])
        # if scientific name does not exist, go to the page and create it
        select_name = browser.find_element(By.ID, "Tree_ScientificName")
        select_name.select_by_visible_text(dis[5])

        if dis[6].notnull():
            tree_dbh = browser.find_element(By.ID, "Tree_DBH")
            tree_dbh.send_keys(dis[6])

        if dis[7].notnull():
            tree_hgt = browser.find_element(By.ID, "Tree_Height")
            tree_hgt.send_keys(dis[7])

        if dis[8].notnull():
            tree_haz = browser.find_element(By.ID, "Tree_Hazard")
            tree_haz.send_keys(dis[8])

        if dis[9].notnull():
            tree_cond = browser.find_element(By.ID, "Tree_Condition")
            tree_cond.send_keys(dis[9])

        if dis[10].notnull():
            tree_com = browser.find_element(By.ID, "Tree_Comment")
            tree_com.send_keys(dis[10])

        # maybe come up with a way to do specialties

        # Add cat:
        # <input type="button" onclick="AddCat()" value="+">
        # then becomes a dropdown
        # <select class="form-control valid" id="SpecialtyTrees_0__SpecialtyTitle" name="SpecialtyTrees[0].SpecialtyTitle" aria-invalid="false"><option value=""></option><option value="Old">Old</option></select>
        # Enter button:
        # <input type="submit" value="Create" class="btn btn-primary">
        if dis[0] == 1:
            break



# Need to fill in specialties & scientific categories before making a tree
# (Check IF data column for that tree matches df)
#
# browser.get('https://localhost:44367/Scientifics/Create')
# browser.get('https://localhost:44367/Specialties')
