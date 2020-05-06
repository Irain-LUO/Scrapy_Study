from selenium import webdriver
import time
# Chromedriver的绝对路径
driber_path = r'D:\Information\Working\pycharm\Chromediver\chromedriver.exe'
# 初始化一个driver驱动，并且制定Chromedriver的路径
driver = webdriver.Chrome(executable_path=driber_path)
# 请求网页
driver.get("http://www.baidu.com")
time.sleep(3)
driver.close()  #  关闭当前页面
time.sleep(3)
driver.quit()  # 关闭当前浏览器
