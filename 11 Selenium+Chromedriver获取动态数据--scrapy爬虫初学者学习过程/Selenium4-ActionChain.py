# ================= 行为链 ========================
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driber_path = r'D:\Information\Working\pycharm\ChromeDriver\chromedriver.exe'# Chromedriver的绝对路径
driver = webdriver.Chrome(executable_path=driber_path)# 初始化一个driver驱动，并且制定Chromedriver的路径
driver.get("https://www.baidu.com")# 请求网页
inputTag =driver.find_element_by_id('kw')# 通过id获取输入框元素
submitTag =driver.find_element_by_id('su')# 通过id获取按钮元素
actions = ActionChains(driver)  # 启动行为链
actions.move_to_element(inputTag) # 鼠标移动到输入框元素
actions.send_keys_to_element(inputTag,'python') #  向输入框传入数据
actions.move_to_element(submitTag) # 鼠标移动到按钮元素
actions.click() # 鼠标点击按钮
actions.perform()  # 执行行为链