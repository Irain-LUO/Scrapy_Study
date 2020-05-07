## 6 Selenium-Ajax.py
from selenium import webdriver
driber_path = r'D:\Information\Working\pycharm\ChromeDriver\chromedriver.exe'# Chromedriver的绝对路径
driver = webdriver.Chrome(executable_path=driber_path)# 初始化一个driver驱动，并且制定Chromedriver的路径
driver.get("https://www.baidu.com")# 请求网页
# ================= 隐式等待 ========================
driver.implicitly_wait(10) #  等待10秒
element = driver.find_element_by_id('kw')
print('='*100)
print(element)
# ================= 显示等待 ========================
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
element = WebDriverWait(driver,10).until(  #  等待10秒
    EC.presence_of_all_elements_located((By.ID,'su'))
)
print('='*100)
print(element)