# python3.7.4
import requests
import json

url1 = "http://qt.qq.com/lua/lol_news/mcn_author_news?author_uuid=5828dce3-30c1-49a4-9e3d-fb3b745fdc16&page="
url2 = "&num=10&type=0&plat=android&version=9931"
url_list = []
url_data = []
result = []
# 获取到从古至今所有的json页面，先不考虑failed页面


def get_url():
    for i in range(1, 100):
        url = str(url1+str(i)+url2)
        # print(url)
        url_list.append(url)
    return url_list

# 截取每个json页面中的article_url


def get_article_url():

    for i in url_list:
        # print(i）

        break

# 下载每个article_url的图片
# 同时保存图片下面文字作为图片命名
# 考虑所有图片存在同一个文件夹或者分文件夹存储

# print(get_url())
# r=requests.get(url)
# t=r.text
# load_data = json.loads(t)
# data = load_data.get("list")
# for i in data:
#     result.append(i.get("article_url"))
# print(result)
# print(data)
# print(data['article_url'])
# print(t)
# print(r.text)
