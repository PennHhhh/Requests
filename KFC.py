'''
    爬取肯德基餐厅位置信息
'''

import requests
import json
import os

if __name__ == '__main__':

    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    keyword = input('Please input a city:')
    data = {
        'cname': '',
        'pid': '',
        'keyword': keyword,
        'pageIndex': '1',
        'pageSize': '10'
    }
    response = requests.post(url=post_url, data=data, headers=headers)

    obj = response.text

    filename = keyword + '.json'
    with open(filename, 'w', encoding='utf-8') as fp:
        # Write the text directly instead of using json.dump
        fp.write(obj)

    print('over..')
