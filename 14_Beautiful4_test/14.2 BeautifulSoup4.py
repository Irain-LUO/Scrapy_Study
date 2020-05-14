# =============================== select方法==============================================
print("=============================== select方法==============================================")
html = """<html>
<head>
<title>css设置标签颜色</title>
<style type="text/css">/*css设置标签颜色*/
p{ 			/*1 标签名选择：所有p标签为红色*/
	background-color: red;
}
.line1{		/*2 类名选择：class="line1"的p标签为蓝色*/
	background-color: blue;
}
#line3{		/*3 id选择：id="line3"的p标签为绿色*/
	background-color: green;
}
.desk p{	/*4 子孙元素（所有）：div class="desk"的p标签为黄色*/
	background-color: yellow;
}
.desk > div >p{		/*5 子元素（一个）：div class="desk"的div的p标签为灰色*/
	background-color: gray;
}
input[name="username"]{ /*6 属性名字：input标签为粉红色*/
	background-color: pink;
}
div.line1{ /*7 属性名字过滤：class="line1"的div标签为白色*/
	background: white
}
p#line1{  /*7 属性名字过滤：id="line1"的p标签为白色*/
	background: white
}
</style>
</head>
<body>
	<div class="box">
	<p>1 所有p标签为红色</p>
	<p class="line1">2 class="line1"的p标签为蓝色</p>
	<p class="line1">2 class="line1"的p标签为蓝色</p>
	<p id="line3">3 id="line3"为的p标签绿色</p></div>
	<div class="desk">
	<p>4 div class="desk"的p标签为黄色</p>
	<p>4 div class="desk"的p标签为黄色</p>
	<div>
	<p>5 div class="desk"的div的p标签为灰色</p></div></div>
	<form>6 属性名字：input标签为粉红色
	<input type="text" name="username"></form>
	<div class="line1">7 属性名字过滤：class="line1"的div标签为白色 </div>
	<p id="line1">7 属性名字过滤：id="line1"的p标签为白色</p>
</body></html>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
title = soup.select("title")[0]
print("1 标签名查找：",title.get_text())
line1s = soup.select(".line1",limit=2) # 只获得两个
for line1 in line1s:
    print("2 类名查找：",line1.get_text())
line3 = soup.select("#line3")[0]
print("3 id查找：",line3.get_text())
div_desk_ps = soup.select("div.desk > p")
for div_desk_p in div_desk_ps:
    print("4 组合（div标签 + p标签）查找：",div_desk_p.get_text())
id_line1 = soup.select("p#line1")[0]
print("4 组合（p标签 + id=line1）查找：",id_line1.get_text())
input = soup.select('input[type="text"]')[0]
print("5 属性查找：",input)




# ======================= contents与children方法 ========================
print("======================= contents与children方法 ========================")
print("contents类型：list",type(soup.body.contents))
print(soup.body.contents)

print("children类型：迭代器",type(soup.body.children))
for child in soup.body.children:
    print(child)


# ==========================   Tag、NavigableString、BeautifulSoup 类型=====================
print(" ==========================   Tag、NavigableString、BeautifulSoup 类型=====================")
html = """<title>css设置标签颜色</title>"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print("Tag类型：",type(soup.title))
print(soup.title)
print("NavigableString类型：",type(soup.title.string))
print(soup.title.string)
print("BeautifulSoup类型：",type(soup))
print(soup.name)




# ======================= string与contents方法 ========================
print("======================= string与contents方法 ========================")
html = """
<p><!--我是注释字符串--></p>
<p>
<!--我是注释字符串-->
</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print("---------------提取元素：<p><!--我是注释字符串--></p>--------------")
p = soup.find_all('p')[0]
print("string方法:",p.string)
print("")

print("---------------提取元素：-------------------\n<p>\n<!--我是注释字符串-->\n</p>\n--------------------------------------------")
p = soup.find_all('p')[1]
print("string方法:",p.string)
print("contents方法:",p.contents)