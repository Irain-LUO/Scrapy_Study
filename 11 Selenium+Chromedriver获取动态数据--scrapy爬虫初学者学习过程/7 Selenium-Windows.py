## 7 Selenium-Windows.py
from selenium import webdriver
driber_path = r'D:\Information\Working\pycharm\ChromeDriver\chromedriver.exe'# Chromedriver的绝对路径
driver = webdriver.Chrome(executable_path=driber_path)# 初始化一个driver驱动，并且制定Chromedriver的路径
driver.get("https://www.baidu.com")# 请求网页
# ================= 新标签页打开豆瓣网址 ========================
driver.execute_script("window.open('https://www.douban.com/')") # 新标签页打开豆瓣网址
print(driver.current_url)  # 当前url
print(driver.window_handles) # 窗口中所有的标签页url
# ================= 标签页切换 ========================
driver.switch_to.window(driver.window_handles[2]) # 跳转到豆瓣标签页
print(driver.current_url)   # 当前url

# ================= WebElement ========================
DownloadB = driver.find_element_by_class_name('lnk-app') # 获取下载豆瓣APP元素
print(type(DownloadB))  #  查看类型WebElement
print(DownloadB.get_attribute('href')) # 获取下载豆瓣的链接
driver.save_screenshot('douban.png') #  截图