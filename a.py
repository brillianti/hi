#如何获取API KEY和Secret Key:https://blog.csdn.net/qq_37273544/article/details/104197205
# https://blog.csdn.net/ZackSock/article/details/106010757


import base64
import requests

def get_access_token():
    # 获取token的API
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    # 获取access_token需要的参数
    params = {
        # 固定参数
        'grant_type':'client_credentials',
        # 必选参数，传入你的API Key
        'client_id':'你的API Key',
        # 必选参数，传入你的Secret Key
        'client_secret':'你的Secret Key'
    }
    # 发送请求，获取响应数据
    response = requests.post(url, params)
    # 将响应的数据转成字典类型，然后取出access_token
    access_token = eval(response.text)['access_token']
    # 将access_token返回
    return access_token

def img2Cartoon(img):
    # 头像动漫化的API
    url = 'https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime'
    # 以二进制的方式读取原始图片
    origin_im = open(img, 'rb')
    # 将图片进行base64编码
    img = base64.b64encode(origin_im .read())
    # 关闭原图片
    origin_im.close()

    # 请求的headers信息，固定写法
    headers = {'content-type':'application/x-www-form-urlencoded'}

    # 请求的参数
    params = {
        # 开始获取的access_token
        'access_token':get_access_token(),
        # 图片的base64编码
        'image':img,
    }
    # 发送请求
    response = requests.post(url, data=params, headers=headers)
    # 对响应结果进行处理
    if response:
        # 打开一个文件
        f = open('result.jpg', 'wb')
        # 获取动漫头像
        anime = response.json()['image']
        # 对返回的头像进行解码
        anime = base64.b64decode(anime)
        # 将头像写入文件当中
        f.write(anime)
        f.close()

if __name__ == '__main__':
    img2Cartoon('origin12.jpg')
