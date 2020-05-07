# 8 Selenium-IP.py
# ================= 代理IP ========================
from selenium import webdriver
driber_path = r'D:\Information\Working\pycharm\ChromeDriver\chromedriver.exe'# Chromedriver的绝对路径
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://163.204.247.186:9999")  # 添加代理IP
driver = webdriver.Chrome(executable_path=driber_path, chrome_options=options)# 初始化一个driver驱动，设置代理IP
driver.get("http://httpbin.org/ip")# 查看代理IP