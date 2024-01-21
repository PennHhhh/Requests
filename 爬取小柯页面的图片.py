import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin  # Import urljoin function to handle relative URLs


def download_images(url, output_folder='./images'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        '''
        response.status_code 是 requests 库中的一个属性，表示服务器对 HTTP 请求的响应中返回的 HTTP 状态码。
        HTTP 状态码是互联网上的 Web 服务器给出的标准响应代码，它们指示了 HTTP 请求的结果，包括成功、错误或需要进一步处理等情况。

        以下是一些常见的 HTTP 状态码：
        200 OK: 请求成功。
        404 Not Found: 服务器无法找到请求的资源。
        500 Internal Server Error: 服务器遇到了意外的条件，阻止它完成请求。
        '''

        soup = BeautifulSoup(response.text, 'html.parser')
        # Modify this according to the actual HTML structure
        image_tags = soup.find_all('img')

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for i, image_tag in enumerate(image_tags):
            image_url = image_tag.get('src')
            if image_url:
                # Check if the URL is relative and construct the absolute URL
                if not image_url.startswith(('http://', 'https://')):
                    image_url = urljoin(url, image_url)

                image_data = requests.get(image_url).content
                image_filename = os.path.join(
                    output_folder, f'image_{i+1}.jpg')

                with open(image_filename, 'wb') as fp:
                    fp.write(image_data)

                print(f'Image {i+1} downloaded successfully.')
            else:
                print(f'Skipping image {i+1} - no source URL.')

    else:
        print(
            f'Failed to download webpage. Status code: {response.status_code}')


if __name__ == '__main__':
    url = 'https://tuchong.com/1711316/118412682/'
    download_images(url)


# 获取原画质图片——无效，应该是网页不允许

# import requests
# from bs4 import BeautifulSoup
# import os
# from urllib.parse import urljoin


# def download_images(url, output_folder='./images'):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
#         'Referer': url,  # Add a referer header to mimic a request from the original page
#     }

#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')

#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)

#         for i, image_tag in enumerate(soup.find_all('img', src=True)):
#             image_url = urljoin(url, image_tag['src'])

#             try:
#                 image_data = requests.get(image_url, headers=headers).content

#                 if image_data.startswith(b'\xFF\xD8\xFF'):  # JPEG magic number
#                     image_filename = os.path.join(
#                         output_folder, f'image_{i+1}.jpg')

#                     if os.path.exists(image_filename):
#                         print(f'Skipping image {i+1} - file already exists.')
#                     else:
#                         with open(image_filename, 'wb') as fp:
#                             fp.write(image_data)

#                         print(f'Image {i+1} downloaded successfully.')
#                 else:
#                     print(f'Skipping image {i+1} - not a valid image.')

#             except requests.RequestException as e:
#                 print(f'Error downloading image {i+1}: {e}')

#     else:
#         print(
#             f'Failed to download webpage. Status code: {response.status_code}')


# if __name__ == '__main__':
#     url = 'https://tuchong.com/1711316/118412682/'
#     download_images(url)
