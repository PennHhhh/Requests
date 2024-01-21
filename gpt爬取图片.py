import requests

if __name__ == '__main__':
    url = 'https://ts1.cn.mm.bing.net/th/id/R-C.6e6dbd5fa142442f5512530a5af0f5ff?rik=%2bGvbMv4Ct1goA&riu=http%3a%2f%2fimg.zcool.cn%2fcommunity%2f01f3c75548ad2b0000019ae9f2a4a8.jpg%401280w_1l_2o_100sh.jpg&ehk=A29P6BnrDHm8PdsiqkEYgyXOL2R74fjCWUBQhHm0v1A=&risl=&pid=ImgRaw&r=0'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        image_data = response.content
        with open('./tu.jpg', 'wb') as fp:
            fp.write(image_data)
        print('Image downloaded successfully.')
    else:
        print(f'Failed to download image. Status code: {response.status_code}')
