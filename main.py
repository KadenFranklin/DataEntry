import pandas as pd
from selenium import webdriver

data1 = pd.read_excel(r"C:\Users\Kaden's Laptop\PycharmProjects\DataEntry\Tree_Data.xlsx", sheet_name='1-1150')
df = pd.DataFrame(data1, columns=['ID', 'Location', 'Latitude', 'Longitude', 'Common name', 'Scientific name', 'Ht', 'HAZ ', 'Target', 'Defects', 'Cond.', 'Maintenance', '???', 'Comments'])

# data2 = pd.read_excel(r"C:\Users\Kaden's Laptop\PycharmProjects\DataEntry\Tree_Data.xlsx", sheet_name='3000-5000')
# df2 = pd.DataFrame(data2, columns=['ID', 'Location', 'Latitude', 'Longitude', 'Common name', 'Scientific name', 'Ht', 'HAZ ', 'Target', 'Defects', 'Cond.', 'Maintenance', '???', 'Comments', 'Planted', 'Photo', 'Icon', 'No.'])

# imports columns^ the loop through rows
for i in df.iterrows():
    print(i)
    
# browser = webdriver.Chrome()
# Need to fill in specialties & scientific categories before making a tree
# (Check IF data column for that tree matches df)
# browser.get('https://localhost:44367/Trees/Create')
# browser.get('https://localhost:44367/Scientifics/Create')
# browser.get('https://localhost:44367/Specialties')
