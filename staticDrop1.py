from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
static_drop = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
static_drop.select_by_visible_text("Female")
# static_drop.select_by_index(1)




