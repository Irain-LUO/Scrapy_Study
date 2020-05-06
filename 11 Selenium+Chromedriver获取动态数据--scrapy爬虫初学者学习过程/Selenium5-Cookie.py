# ================= Cookie操作 ========================
from selenium import webdriver
driber_path = r'D:\Information\Working\pycharm\ChromeDriver\chromedriver.exe'# Chromedriver的绝对路径
driver = webdriver.Chrome(executable_path=driber_path)# 初始化一个driver驱动，并且制定Chromedriver的路径
driver.get("https://www.baidu.com")# 请求网页
print('================= 打印Cookie ========================')
for cookie in driver.get_cookies(): # 只能获取该网页下的cookie
    print(cookie)
print('================= 打印 BD_HOME Cookie ========================')
print(driver.get_cookie('BD_HOME'))
print('================= 删除 BD_HOME Cookie ========================')
driver.delete_cookie('BD_HOME')
print(driver.get_cookie('BD_HOME'))
print('================= 删除 所有 Cookie，在浏览器中查看 ========================')
# driver.delete_all_cookies()