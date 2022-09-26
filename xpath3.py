from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://mypage.rediff.com/login/dologin")
# driver.find_element(By.XPATH, "//input[@id='txtlogin']").send_keys("Athithya6")
# driver.find_element(By.XPATH, "//input[@id='pass_box']").send_keys("Athithya$1997")
# driver.find_element(By.XPATH, "//input[@value='Login']").click()

driver.find_element(By.XPATH, "//div[@id='leftcontainer']/div/form/div/input").send_keys("Athithya6")
driver.find_element(By.XPATH, "//div[@id='leftcontainer']/div/form/div[2]/input").send_keys("Athithya$1997")
driver.find_element(By.XPATH, "//div[@id='pass_div']/input[3]").click()
driver.find_element(By.XPATH, "//a[text()='Forgot password?']").click()
