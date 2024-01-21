'''
    bs4进行数据解析：
        数据解析原理：
            1. 标签定位
            2. 提取标签，标签属性中存储的数据值

        bs4数据解析的原理：
            1. 实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
            2. 通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取

        环境安装：
            pip install bs4
            pip install lxml

        如何实例化BeautifulSoup对象：
            from bs4 import BeautifulSoup

            对象的实例化：
                1. 将本地的html文档中的数据加载到该对象中
                    with open('./test.html', 'r', encoding='utf-8') as fp:
                        soup = BeautifulSoup(fp, 'lxml')
                2. 将互联网上获取的页面源码加载到该对象中
                    page_text = response.text
                    soup = BeautifulSoup(page_text, 'lxml')

            提供的用于数据解析的方法和属性:
                soup.tagname：返回文档中第一次出现的tagname
                soup.find(): 
                    1. (soup.div= soup.find('div'))
                    2. 属性定位：soup.find('div', class_(或其他属性)='song')    class_是为了区别class类和class_变量
                soup.find_all(): 找到符合要求的所有标签（列表）
                soup.select(选择器)
                    选择器包括id，class，标签等，返回一个列表
                    层级选择器
                        soup.select('.tang > ul > li > a'): >表示一个层级
                        soup.select('.tang > ul a'): 空格表示多个层级
        
            获取标签之间的文本数据：
                soup.a.text/string/get_text()
                    text/get_text(): 可以获取某一个标签中所有的文本内容
                    string：只能获取该标签下直系的文本内容

            获取标签中的属性
                soup.a['href']

'''

'''
    爬取三国演义所有章节和内容
'''


import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    # 对首页数据进行爬取
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }
    page_text = requests.get(url=url, headers=headers).content

    # 在首页中解析出章节的标题和详情页的url
    # 1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')
    # 解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')

    fp = open('./sanguo3.txt', 'w', encoding='utf-8')

    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(
            url=detail_url, headers=headers).content                    # 将text方法改为content就不会乱码

        # 解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        # 解析到章节内容
        content = div_tag.text

        fp.write(title + ':' + content + '\n')
        print(title, '爬取成功！')
