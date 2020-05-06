from selenium import webdriver
import time
# Chromedriver的绝对路径
driber_path = r'D:\Information\Working\pycharm\ChromeDriver\chromedriver.exe'
# 初始化一个driver驱动，并且制定Chromedriver的路径
driver = webdriver.Chrome(executable_path=driber_path)
# 请求网页
driver.get("http://www.baidu.com")
# 通过id获取元素
inputTag =driver.find_element_by_id('kw')
inputTag.send_keys('python')
# 通过name获取元素
inputTag =driver.find_element_by_name('wd')
inputTag.send_keys('python')
# 通过class_name获取元素
inputTag =driver.find_element_by_class_name('s_ipt')
inputTag.send_keys('python')
# 通过xpath获取元素
inputTag =driver.find_element_by_xpath("//input[@id='kw']")
inputTag.send_keys('python')
# 通过css获取元素
inputTag =driver.find_element_by_css_selector(".quickdelete-wrap > input")
inputTag.send_keys('python')
