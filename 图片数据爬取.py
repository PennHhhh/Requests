import requests

if __name__ == '__main__':
    url = 'https://cn.bing.com/images/search?view=detailV2&ccid=bm29X6FC&id=7A8B9920EB324339A317A060DD0AF8CB6CAFB1F9&thid=OIP.bm29X6FCRC9VElMKWvD1_wHaEj&mediaurl=https%3a%2f%2fts1.cn.mm.bing.net%2fth%2fid%2fR-C.6e6dbd5fa142442f5512530a5af0f5ff%3frik%3d%252bbGvbMv4Ct1goA%26riu%3dhttp%253a%252f%252fimg.zcool.cn%252fcommunity%252f01f3c75548ad2b0000019ae9f2a4a8.jpg%25401280w_1l_2o_100sh.jpg%26ehk%3dA29P6BnrDHm8PdsiqkEYgyXOL2R74fjCWUBQhHm0v1A%253d%26risl%3d%26pid%3dImgRaw%26r%3d0&exph=787&expw=1280&q=%e5%9b%be%e8%99%ab&simid=608009559719636033&FORM=IRPRST&ck=9D57B9B9C99F28A20B4A5709A36C9A41&selectedIndex=2'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}

    # content返回的是二进制形式的图片数据
    image_data = requests.get(url=url, headers=headers).content

    with open('./t.jpg', 'wb') as fp:
        fp.write(image_data)

# 图片没有爬下来
