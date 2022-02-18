from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def sci_to_cat(s):
    if "Pinus" in s:
        s = 'Pines'
        print("new var: " + s)
    if "Quercus" in s:
        s = 'Oaks'
        print("new var: " + s)
    if "Lagerstroemia" in s:
        s = 'Crepe myrtles'
        print("new var: " + s)
    # dunno if we need hollies
    if "Ilex" in s:
        s = 'Hollies'
        print("new var: " + s)
    if "Acer" in s:
        s = 'Maples'
        print("new var: " + s)
    if "Liquidambar" in s:
        s = 'Sweetgums'
        print("new var: " + s)
    if "Carya" in s:
        s = 'Pecans'
        print("new var: " + s)
    else:
        print()
    return s


browser = webdriver.Chrome()
browser.get('https://localhost:44367/trees/')
browser.refresh()

table_id = browser.find_element(By.TAG_NAME, 'tbody')
rows = table_id.find_elements(By.TAG_NAME, "tr")
for row in rows:
    tree_id = row.find_elements(By.TAG_NAME, "td")[0]
    if row.find_elements(By.TAG_NAME, "td")[7]:
        comment = row.find_elements(By.TAG_NAME, "td")[7]
    sci_name = row.find_elements(By.TAG_NAME, "td")[9]
    # edit = row.find_elements(By.TAG_NAME, "td")[10].find_elements(By.TAG_NAME, "a")[0]
    new = webdriver.Chrome()
    new.get('https://localhost:44367/Trees/Edit?id=' + tree_id.text)
    sel_spec = Select(new.find_element(By.ID, "SpecialtyTree_SpecialtyTitle"))
    spec = new.find_element(By.ID, "SpecialtyTree_SpecialtyTitle")
    count = 1

    for option in sel_spec.options:
        if option.text == sci_to_cat(tree_id.text):
            spec.send_keys(Keys.ENTER)
            # only uncomment when everything else works

            # add_cat = crud_row.find_elements(By.CLASS_NAME, "btn-primary")[0]
            # ActionChains(new).click(add_cat).perform()
            # new.refresh()
            # add_cat = crud_row.find_elements(By.TAG_NAME, "btn btn-primary")[0]
            # ActionChains(new).click(add_cat).perform()
            # new.close()
            # close new and run next iteration of loop
            break
        if count == len(sel_spec.options):
            print("whoops messed something up @ " + tree_id.text)
            # if run out of options
            # shouldn't happen
        else:
            ARROW_DOWN = u'\ue015'
            spec.send_keys(ARROW_DOWN)
            count += 1
    print("did i do everything?")

