import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

data1 = pd.read_excel(r"C:\Users\Kaden's Laptop\PycharmProjects\DataEntry\Tree_Data.xlsx", sheet_name='1-1150')
df = pd.DataFrame(data1, columns=['ID', 'Location', 'Latitude', 'Longitude', 'Common name', 'Scientific name', 'Ht', 'HAZ ', 'Target', 'Defects', 'Cond.', 'Maintenance', '???', 'Comments'])

# data2 = pd.read_excel(r"C:\Users\Kaden's Laptop\PycharmProjects\DataEntry\Tree_Data.xlsx", sheet_name='3000-5000')
# df2 = pd.DataFrame(data2, columns=['ID', 'Location', 'Latitude', 'Longitude', 'Common name', 'Scientific name', 'Ht', 'HAZ ', 'Target', 'Defects', 'Cond.', 'Maintenance', '???', 'Comments', 'Planted', 'Photo', 'Icon', 'No.'])

# getitem() separates the index from the series

browser = webdriver.Chrome()
browser.get('https://localhost:44367/Trees/Create')

for i in df.iterrows():
    dat_list = i.__getitem__(1)
    dis = dat_list[0]
    browser.find_element(By.TAG_NAME, "input").below({By.ID: "TreeID"}).send_keys(dis)
    print(dis)
    if dis == 1:
        break


# Need to fill in specialties & scientific categories before making a tree
# (Check IF data column for that tree matches df)
#
# browser.get('https://localhost:44367/Scientifics/Create')
# browser.get('https://localhost:44367/Specialties')
