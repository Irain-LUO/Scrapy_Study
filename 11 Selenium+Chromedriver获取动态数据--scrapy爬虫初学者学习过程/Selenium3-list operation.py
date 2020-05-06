#  常见的表单元素：
# input:type=''
# button:input[tpye='submit']
from selenium import webdriver
import time
driber_path = r'D:\Information\Working\pycharm\ChromeDriver\chromedriver.exe'# Chromedriver的绝对路径
driver = webdriver.Chrome(executable_path=driber_path)# 初始化一个driver驱动，并且制定Chromedriver的路径
# ========================   输入框输入和清空输入框 =================
# driver.get("http://www.baidu.com")# 请求网页
# inputTag =driver.find_element_by_id('kw')# 通过id获取元素
# inputTag.send_keys('python')# 输入框输入'python'
# time.sleep(3)# 3秒后，清空输入框
# inputTag.clear()

# ========================   点击复选框 =================
# driver.get("https://www.douban.com")# 请求网页
# time.sleep(3)
# rememberb = driver.find_elements_by_name('remember')
# rememberb.click()

# ========================   鼠标点击 =================
driver.get("https://www.baidu.com")# 请求网页
inputTag =driver.find_element_by_id('kw')# 通过id获取输入框元素
inputTag.send_keys('python')# 输入框输入'python'
inputTag =driver.find_element_by_id('su')# 通过id获取按钮元素
inputTag.click() # 点击按钮