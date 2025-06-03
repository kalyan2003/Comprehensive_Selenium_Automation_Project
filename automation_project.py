from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import  ActionChains
import requests
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Pavan")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("vnsdjvbw@gmail.com")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9876543212")
driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("lvmkfnvof dkfv dfn kvmdobnd")


male_radio_but = driver.find_element(By.XPATH, "//input[@id='male']")
if not male_radio_but.is_selected():
    male_radio_but.click()


days_checkbox = driver.find_elements(By.XPATH, "//input[@class='form-check-input' and @type='checkbox']")
for day in days_checkbox:
    if not day.is_selected():
        day.click()


dropdown_country = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
dropdown_country.select_by_visible_text("India")


dropdown_colors = Select(driver.find_element(By.XPATH, "//select[@id='colors']"))
dropdown_colors.select_by_visible_text("Green")


dropdown_animals = Select(driver.find_element(By.XPATH, "//select[@id='animals']"))
dropdown_animals.select_by_visible_text("Fox")


date_input1 = driver.find_element(By.XPATH, "//input[@id='datepicker']")
date_input1.click()
date_year = "2026"
date_month = "June"
date_day = "25"

while True:
    month = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']/span[@class='ui-datepicker-month']").text
    year = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']/span[@class='ui-datepicker-year']").text
    if month == date_month and year == date_year:
        break
    driver.find_element(By.XPATH, "//a[@title='Next' and @data-handler='next']").click()

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")
for ele in dates:
    if ele.text == date_day:
        ele.click()
        break




date_input2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='txtDate' and @name='SelectedDate']")))
date_input2.click()

month_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@class='ui-datepicker-month']")))
month_drops = Select(month_dropdown)

for option in month_drops.options:
    if option.text == date_month:
        option.click()
        break


year_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@class='ui-datepicker-year']")))
year_drops = Select(year_dropdown)
for option in year_drops.options:
    if option.text == date_year:
        option.click()
        break


dates = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")))
for d in dates:
    if d.text == date_day:
        d.click()
        break

time.sleep(5)

start_date = driver.find_element(By.XPATH,"//input[@id='start-date']").send_keys("02-02-2024")
end_date = driver.find_element(By.XPATH,"//input[@id='end-date']").send_keys("04-04-2027")
submit_button = driver.find_element(By.XPATH,"//button[@class='submit-btn']").click()
time.sleep(2)

search_input = driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("GE vernova")
search_but = driver.find_element(By.XPATH,"//input[@class='wikipedia-search-button']")
search_but.submit()
time.sleep(2)

alert_button = driver.find_element(By.XPATH,"//button[@id='alertBtn']").click()
time.sleep(3)
js_alert = driver.switch_to.alert
js_alert.accept()

confirm_alert = driver.find_element(By.XPATH,"//button[@id='confirmBtn']").click()
time.sleep(3)
js_alert = driver.switch_to.alert
print(js_alert.text)
js_alert.accept()

prompt_alert = driver.find_element(By.XPATH,"//button[@id='promptBtn']").click()
time.sleep(3)
js_alert = driver.switch_to.alert
js_alert.send_keys("Pavan kalyan")
js_alert.accept()

hover_but = driver.find_element(By.XPATH,"//button[@class='dropbtn']")
laptops_click = driver.find_element(By.XPATH,"//div[@class='dropdown-content']/a[text()='Laptops']")

mous_actions = ActionChains(driver)
mous_actions.move_to_element(hover_but).move_to_element(laptops_click).click().perform()

double_click_but = driver.find_element(By.XPATH,"//button[text()='Copy Text']")
mous_actions.double_click(double_click_but).perform()

source_ele = driver.find_element(By.XPATH,"//div[@id='draggable']")
desti_ele = driver.find_element(By.XPATH,"//div[@id='droppable']")

mous_actions.drag_and_drop(source_ele,desti_ele).perform()

min_value = driver.find_element(By.XPATH,"//div[@id='slider-range']/span[1]")
max_value = driver.find_element(By.XPATH,"//div[@id='slider-range']/span[2]")

mous_actions.drag_and_drop_by_offset(min_value,50,0).perform()
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(max_value,-90,0).perform()


scroll_drop_down = driver.find_element(By.XPATH,"//input[@type = 'text' and @id='comboBox']")
scroll_drop_down.click()

wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='dropdown']")))

scroll_options = driver.find_elements(By.XPATH,"//div[@id='dropdown']/div")

my_option = "Item 19"

for ele in scroll_options:
    if ele.text == my_option:
        ele.click()
        break

#handling links

allLinks = driver.find_elements(By.XPATH,"//div[@id='laptops']/a")

good_links = 0

for link in allLinks:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code<400:
        good_links += 1

allBrokenLinks = driver.find_elements(By.XPATH,"//div[@id='broken-links']/a")

brokenLinks = 0

for link in allBrokenLinks:
    url = link.get_attribute("href")

    try:
        res = requests.head(url)
    except:
        None


    if res.status_code>=400:
        brokenLinks += 1

print("Good links:",good_links)
print("Broken links:",brokenLinks)

#uploading files

file_input = driver.find_element(By.XPATH,"//input[@id='singleFileInput']")
file_input.send_keys(r"C:\Users\pavan\Downloads\file_example_XLS_10.xlsx")

driver.find_element(By.XPATH,"//button[text()='Upload Single File']").click()

mul_file_input = driver.find_element(By.XPATH,"//input[@id = 'multipleFilesInput']")
file1 = r"C:\Users\pavan\Downloads\file_example_XLS_10.xlsx"
file2 = r"C:\Users\pavan\Downloads\que_3.pdf"
file3 = r"C:\Users\pavan\Downloads\Manual Testing Notes (1).pdf"
mul_file_input.send_keys(f"{file1}\n{file2}\n{file3}")
driver.find_element(By.XPATH,"//button[text() = 'Upload Multiple Files']").click()


#handling static tables

nrows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print("No of rows:",nrows)

ncols = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print("No of cols:",ncols)

for r in range(2,nrows+1):
    for c in range(1,ncols+1):
        data = driver.find_element(By.XPATH,f"//table[@name='BookTable']//tr[{r}]/td[{c}]")
        print(data.text,end='    ')

    print()


# handling dynamic tables

noofrows = len(driver.find_elements(By.XPATH,"//table[@id='taskTable']//tr"))
noofcols = len(driver.find_elements(By.XPATH,"//table[@id='taskTable']//tr[1]/th"))
print("No of rows:",noofrows)
print("No of cols:",noofcols)

for r in range(1,noofrows):
    for c in range(1,noofcols+1):
        data = driver.find_element(By.XPATH,f"//table[@id='taskTable']//tbody/tr[{r}]/td[{c}]")
        print(data.text,end='    ')
    print()



##Pagination on web table

pages = driver.find_elements(By.XPATH,"//ul[@id='pagination']/li")

nrows = len(driver.find_elements(By.XPATH,"//table[@id='productTable']//tbody/tr"))
print("No of rows:",nrows)

ncols = len(driver.find_elements(By.XPATH,"//table[@id='productTable']//thead/tr/th"))
print("No of columns:",ncols)

for page in pages:
    page.click()

    for r in range(1,nrows+1):
        for c in range(1,ncols+1):
            data = driver.find_element(By.XPATH,f"//table[@id='productTable']//tbody/tr[{r}]/td[{c}]")
            if c==4:
                checkbox = driver.find_element(By.XPATH,f"//table[@id='productTable']//tbody/tr[{r}]/td[{c}]/input")
                checkbox.click()
            print(data.text,end='    ')
        print()


input_1 = driver.find_element(By.XPATH,"//input[@id='input1']").send_keys("VJBFV  JVNSKJFBGWVSV SGNRWRNVS VLWRNGSVWLR")
but_1 = driver.find_element(By.XPATH,"//button[@id='btn1']").click()

input_2 = driver.find_element(By.XPATH,"//input[@id='input2']").send_keys("Pcmdvf  vsdkvjbr")
but_2 = driver.find_element(By.XPATH,"//button[@id='btn2']").click()

input_3 = driver.find_element(By.XPATH,"//input[@id='input3']").send_keys("fnvln   fsnvfvbnwvnwripg v nvwrow")
but_3 = driver.find_element(By.XPATH,"//button[@id='btn3']").click()

##handling shadow dom

shadow_host = driver.find_element(By.ID,"shadow_host")
shadow_root = shadow_host.shadow_root

input1 = shadow_root.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("Pavan kalyan")
input2 = shadow_root.find_element(By.CSS_SELECTOR,"input[type='checkbox']")
input2.click()
input3 = shadow_root.find_element(By.CSS_SELECTOR,"input[type='file']").send_keys("C:\\Users\\pavan\\Downloads\\file_example_XLS_10.xlsx")

blog_link = shadow_root.find_element(By.CSS_SELECTOR,"a[href='https://www.pavantestingtools.com/']")
driver.execute_script("arguments[0].click();", blog_link)

driver.back()







time.sleep(10)
driver.quit()
