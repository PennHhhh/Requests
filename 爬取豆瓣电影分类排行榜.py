import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    params = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',               # 从库中的第几部电影开始取
        'limit': '20'               # 一次取出的个数
    }

    response = requests.get(url=url, params=params, headers=headers)

    list_data = response.json()

    filename = './douban.json'
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(list_data, fp=fp, ensure_ascii=False)

    print('over..')
