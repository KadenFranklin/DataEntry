import pandas as pd
from selenium import webdriver

data = pd.read_excel(r"C:\Users\Kaden's Laptop\PycharmProjects\DataEntry\Tree_Data.xlsx", sheet_name='1-1150')
# df = pd.read_excel(r"C:\Users\Kaden's Laptop\PycharmProjects\DataEntry\Tree_Data.xlsx", sheet_name='3000-5000')
df = df = pd.DataFrame(data, columns=['ID', 'Location', 'Latitude', 'Longitude', 'Common name', 'Scientific name', 'Ht', 'HAZ ', 'Target', 'Defects', 'Cond.', 'Maintenance', '???', 'Comments'])
# imports columns^ the loop through rows
for i in df.iterrows():
    print(i)
    
# browser = webdriver.Chrome()
# Need to fill in specialties & scientific categories before making a tree
# (Check IF data column for that tree matches df)
# browser.get('https://localhost:44367/Trees/Create')
# browser.get('https://localhost:44367/Scientifics/Create')
# browser.get('https://localhost:44367/Specialties')
