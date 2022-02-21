from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def sci_to_cat(s):
    if "Pinus" in s:
        return 'Pines'
    if "Quercus" in s:
        return 'Oaks'
    if "Lagerstroemia" in s:
        return 'Crepe myrtles'
    if "Ilex" in s:
        return 'Hollies'
    if "Acer" in s:
        return 'Maples'
    if "Liquidambar" in s:
        return 'Sweetgums'
    if "Carya" in s:
        return 'Pecans'
    else:
        return 'Skip'


dis_list = []
browser = webdriver.Chrome()
browser.get('https://localhost:44367/trees/')
browser.refresh()
table_id = browser.find_element(By.TAG_NAME, 'tbody')
rows = table_id.find_elements(By.TAG_NAME, "tr")
for row in rows:
    tree_id = row.find_elements(By.TAG_NAME, "td")[0]
    sci_name = row.find_elements(By.TAG_NAME, "td")[9]
    if sci_to_cat(sci_name) == 'Skip':
        continue
    else:
        new = webdriver.Chrome()
        new.get('https://localhost:44367/Trees/Edit?id=' + tree_id.text)
        sel_spec = Select(new.find_element(By.ID, "SpecialtyTree_SpecialtyTitle"))
        spec = new.find_element(By.ID, "SpecialtyTree_SpecialtyTitle")
        count = 1
        for option in sel_spec.options:
            if option.text == sci_to_cat(sci_name.text):
                spec.send_keys(Keys.ENTER)
                break
            if count == len(sel_spec.options):
                dis_list.append(tree_id.text)
            else:
                ARROW_DOWN = u'\ue015'
                spec.send_keys(ARROW_DOWN)
                count += 1
        add_cat = new.find_element(By.ID, "add_cat")
        ActionChains(new).click(add_cat).perform()
        submit = new.find_element(By.ID, "final")
        ActionChains(new).click(submit).perform()
        new.close()
print(dis_list)
