import requests
from bs4 import BeautifulSoup
headers = {
        'Usr-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'cookie':'__guid=240418321.2698196731532421000.1585372730409.6943; sid=654461e8-539a-4ec3-a2c6-a2ecd5adab8d; Hm_lvt_2c8ad67df9e787ad29dbd54ee608f5d2=1585372731; monitor_count=4; Hm_lpvt_2c8ad67df9e787ad29dbd54ee608f5d2=1585372875',        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive'
    }
url = "https://cn.bing.com/" # 微软版的国内谷歌
response = requests.get(url=url, headers=headers) # 访问网址
html = response.text
soup = BeautifulSoup(html, 'lxml')  #BeautifulSoup4解析网页


# 1 获取所有div标签
print('='*30, "1 获取所有div标签", '='*30)
divs = soup.find_all('div')
i = 1
for div in divs:
    print("第{}个div标签：".format(i),div)
    print('='*88)
    i += 1



print("")
print("")
print("")
# 2 获取第2个div标签
print('='*30, "2 获取第2个div标签", '='*30)
div = soup.find_all('div', limit=2)[1] # limit=2：只获得两个div标签
print("获取第2个div标签：",div)
print('='*88)

print("")
print("")
print("")
# 3 获取所有class等于oml_img的div标签
print('='*30, "3 获取所有class等于oml_img的div标签方法一", '='*30)
divs = soup.find_all('div', class_='oml_img')
i = 1
for div in divs:
    print("第{}个div标签：".format(i),div)
    print('='*88)
    i += 1

print("")
print("")
print("")
# 3 获取所有class等于oml_img的div标签
print('='*30, "3 获取所有class等于oml_img的div标签方法二", '='*30)
divs = soup.find_all('div', attrs={'class':'oml_img'})
i = 1
for div in divs:
    print("第{}个div标签：".format(i),div)
    print('='*88)
    i += 1


print("")
print("")
print("")
# 4 获取所有class等于oml_img且id=officemenu_people_img的div标签
print('='*30, "4 获取所有class等于oml_img且id=officemenu_people_img的div标签方法一", '='*30)
divs = soup.find_all('div', attrs={'class':'oml_img', 'id':'officemenu_people_img'})
i = 1
for div in divs:
    print("第{}个div标签：".format(i),div)
    print('='*88)
    i += 1


print("")
print("")
print("")
# 4 获取所有class等于oml_img且id=officemenu_people_img的div标签
print('='*30, "4 获取所有class等于oml_img且id=officemenu_people_img的div标签方法二", '='*30)
divs = soup.find_all('div', class_='oml_img', id='officemenu_people_img')
i = 0
for div in divs:
    print("第{}个div标签：".format(i),div)
    print('='*88)
    i += 1
print("")
print("")
print("")



# 5 获得所有a标签的href属性
print('='*30, "5 获得所有a标签的href属性方法一", '='*30)
aLists = soup.find_all('a')
for a in aLists:
    href = a['href']
    print(href)
print("")
print("")
print("")



# 5 获得所有a标签的href属性
print('='*30, "5 获得所有a标签的href属性方法二", '='*30)
aLists = soup.find_all('a')
for a in aLists:
    href = a.attrs['href']
    print(href)
print("")
print("")
print("")



# 6 获得class=sc_hl1 hp_head_nav的ul标签中所有li标签中的a标签的字符串
print('='*30, "6 获得class=sc_hl1 hp_head_nav的ul标签中所有li标签的a标签的字符串方法一", '='*30)
lis = soup.find_all('ul',class_='sc_hl1 hp_head_nav')[0]
for li in lis:
    try:  # 存在一个li标签中没有a标签
        a = li.find_all('a')  #  获取a标签
        str = a[0].string #  获取a标签的字符
        print(str)
    except:
        str = li.string  # 获取li标签的字符
        print(str)
print("")
print("")
print("")



# 6 获得class=sc_hl1 hp_head_nav的ul标签中所有li标签中的a标签的字符串
print('='*30, "6 获得class=sc_hl1 hp_head_nav的ul标签中所有li标签的a标签的字符串方法二", '='*30)
lis = soup.find_all('ul',class_='sc_hl1 hp_head_nav')[0]
for li in lis:
    # 在这里：li.strings与li.stripped_strings效果一样。bing.com网页暂无发现合适元素作为示例。
    str = list(li.stripped_strings)[0] # stripped_strings：去除空字符（只有换行符'\n'，也算是空字符）
    print(str)
print("")
print("")
print("")


# 7 获得class=sc_hl1 hp_head_nav的ul标签中所有的字符串
print('='*30, "7 获得class=sc_hl1 hp_head_nav的ul标签所有的字符串", '='*30)
lis = soup.find_all('ul',class_='sc_hl1 hp_head_nav')[0]
str = lis.get_text()
print(type(str))
print(str)