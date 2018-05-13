# coding=utf-8

import requests
import re


class SinaBookSpider(object):

    url = "http://feed.mix.sina.com.cn/api/roll/get?callback=jsonp1526192761164&pageid=96&lid=541&num=20&page={0}"
    headers = {
        'Host': 'feed.mix.sina.com.cn',
        'Referer': 'http://book.sina.com.cn/excerpt/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
    }

    def __init__(self):
        self.total = 0
        self.count = 0
        self.first = True

    def run(self, page=1):

        print "正在获取第" + str(page) + "页数据"
        response = requests.get(self.url.format(page), headers=self.headers)

        if self.first:
            # 获取总数
            self.total = int(re.findall(r'"total":(.*?),', response.content)[0])
            # print self.total

        # 解析得到文章详情页地址
        pattern = re.compile(r'"url":"(.*?)",')
        links = pattern.findall(response.content)
        for link in links:
            self.count += 1
            print link

        # 判断是否结束
        if self.count < self.total:
            page += 1
            return self.run(page)

        print "一共{0}条数据，抓取到{1}条".format(self.total, self.count)


if __name__ == '__main__':
    s = SinaBookSpider()
    s.run()
