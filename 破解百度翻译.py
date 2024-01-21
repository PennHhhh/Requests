'''
    破解百度翻译
'''

import requests
import json

if __name__ == '__main__':

    # 1.指定url
    post_url = 'https://fanyi.baidu.com/sug'

    # 2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    # 3.post请求参数处理（同get一致）
    word = input('Please input a word:')
    data = {
        'kw': word
    }

    # 4.请求发送
    response = requests.post(url=post_url, data=data, headers=headers)

    # 5.获取响应数据，json()方法返回的是obj（如果确认响应数据是json类型才可以用）
    dic_obj = response.json()

    # 6.持久化存储
    filename = word + '.json'
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print('Over..')
