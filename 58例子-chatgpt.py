from lxml import etree
import requests

if __name__ == '__main__':
    # 爬取页面源码数据
    url = 'https://xm.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
    page_text = requests.get(url=url, headers=headers).text

    # 数据解析
    tree = etree.HTML(page_text)
    div_list = tree.xpath(
        '//div[@class="property"]')

    fp = open('58.txt', 'w', encoding='utf-8')
    for div in div_list:
        title_list = div.xpath('.//div/h3/text()')
        if title_list:
            title = title_list[0]
            print(title)
            fp.write(title + '\n')

    fp.close()
