import requests
from lxml import etree
import time
import re
import pandas as pd
import os
import pymysql
from sqlalchemy import create_engine
# 设置头文件
headers = {
        'referer': 'https: // www.lagou.com / jobs / list_Java / p - city_0? & cl = false & fromSearch = true & labelWords = & suginput =',
        'sec - fetch - dest': 'empty',
        'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'x-anit-forge-code': '0',
        'x-anit-forge-code': '0',
        'x-anit-forge-token': None,
        'cookie':'user_trace_token=20200321131413-8ddfc34a-aa52-4262-9096-d9d05da3fd5a; _ga=GA1.2.542181339.1584767653; LGUID=20200321131416-b45c1477-a981-4087-b131-a7b9974b5600; JSESSIONID=ABAAABAABFIAAAC35F27D5B4D5AE1C5F2C9F333E9BBCCF4; WEBTJ-ID=20200321131422-170fb837a3113d-030b63af31512b-5d1f391c-1049088-170fb837a326cf; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22170fb83bf0b209-0245070180f324-5d1f391c-1049088-170fb83bf0c16d%22%2C%22%24device_id%22%3A%22170fb83bf0b209-0245070180f324-5d1f391c-1049088-170fb83bf0c16d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; X_MIDDLE_TOKEN=3ff5a12012ebfd67a30924ca6d31c84e; _putrc=4EF91627A84C9BD4123F89F2B170EADC; login=true; unick=%E7%BD%97%E4%BC%9F%E6%98%8E; LG_LOGIN_USER_ID=7e1df141aefd772eaccf6aebd297375c9de7ab50fa2a947b5f2da2737a55fd6a; LG_HAS_LOGIN=1; _gid=GA1.2.593238733.1588814276; gate_login_token=9ad2b13c5356891d10a151c6a4e98f1624cc225476cf2d8a45fa860da49f565c; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; privacyPolicyPopup=false; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1588814469; hasDeliver=9; TG-TRACK-CODE=index_search; SEARCH_ID=1f60a80b4dd34e76b07c7be3127da27b; X_HTTP_TOKEN=9ea9eb5a8fddf22666701988513d84c5d39321ba5e; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1588911281; LGRID=20200508121443-eaeb9b7d-79a1-4032-b14f-f24c5fc48cbc'
}
positions= [] # 存储岗位信息
def request_list_page(): # 爬取岗位url
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'# java的url
    data = { # 数据包
        'fisrt':'false',
        'pn':1,
        'kd':'java'
    }
    for x in range(1,10): # 访问页数
        data['pn'] = x
        response = requests.post(url, headers=headers, data=data)
        while re.findall(r"操作太频繁",response.text) :  # 拉勾网反爬虫，没有使用IP池，短时间不能多次访问
            response = requests.post(url, headers=headers, data=data)
            print("被拦截")
            time.sleep(1)
        print(response)
        result = response.json()          # json方法：如果返回是json数据，那么该方法自动的load成字典
        print(result)
        positions = result['content']['positionResult']['result'] # 获取Ajax文件中岗位信息
        for position in positions:
            positionId = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html' % positionId  # 获取岗位详情页面url
            parse_position_detail(position_url)  #  爬取岗位详情页面
        time.sleep(1)
       # break  # 只爬取第一页，删除break


def parse_position_detail(url):  #  爬取岗位详情页面
    response = requests.get(url, headers=headers)
    while re.findall(r"操作太频繁", response.text):  # 拉勾网反爬虫，没有使用IP池，短时间不能多次访问
        response = requests.get(url, headers=headers)
        time.sleep(1)
    text =response.text
    print(response.status_code)
    html = etree.HTML(text)
    position_name = html.xpath("//h1[@class='name']/text()")[0] #  获取岗位名称
    job_request_spans = html.xpath("//dd[@class='job_request']//span")
    salary = job_request_spans[0].xpath('.//text()')[0].strip() #  获取工资
    city = job_request_spans[1].xpath('.//text()')[0].strip() #  获取工作城市
    city =  re.sub(r"[\s/]","",city)
    work_year = job_request_spans[2].xpath('.//text()')[0].strip() #  获取工作年龄
    work_year = re.sub(r"[\s/]", "", work_year)
    education = job_request_spans[3].xpath('.//text()')[0].strip() #  获取学习
    education = re.sub(r"[\s/]", "", education)
    desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip() #  获取岗位描述
    company_name = html.xpath("//em[@class='fl-cn']/text()")[0].strip()# 获取招聘企业
    position = {
        'name': position_name,
        'company_name': company_name,
        'salary': salary,
        'city': city,
        'work_year': work_year,
        'education': education,
        'desc': desc,
    }
    positions.append(position)
    print('-' * 88)
    print(position)

def save():
    if (os.path.exists('positions.xlsx')): # 删除已存在的Excel文件
        os.remove('positions.xlsx')
    data = pd.DataFrame(positions)
    data.to_excel('positions.xlsx')  # 保存到Excel
    data = pd.read_excel('positions.xlsx', index_col=0)
    conn = pymysql.connect(host='127.0.0.1',  # 数据库地址
                                port=3366,  # 访问端口
                                user='root',  # 登录名
                                passwd='123',  # 登录密码
                                db='scrapy'  # 访问数据库名
                                )  # 连接数据库
    cur = conn.cursor()  # 创建操作游标
    cur.execute('drop table if exists lgw_positions')  # 删除已存在的表
    New_Table = """CREATE TABLE lgw_positions(
                              `index` int(2) ,
                              `name` VARCHAR (16),
                              company_name VARCHAR (16),
                              salary VARCHAR (16),
                              city VARCHAR (16),
                              education  VARCHAR (16),
                              work_year VARCHAR (16),
                              `desc` Text)"""
    cur.execute(New_Table) # 创建新表
    # create_engine('mysql+pymysql://用户名:密码@主机/库名?charset=utf8')
    engine = create_engine('mysql+pymysql://root:123@localhost:3366/scrapy?charset=utf8')
    data.to_sql('lgw_positions', con=engine, if_exists='append')  # 数据写入数据库
    pass

def main():
    request_list_page()
    save()

if __name__ == '__main__':
    main()

