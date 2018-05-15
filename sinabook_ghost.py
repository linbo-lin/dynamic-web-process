# coding=utf-8

import re
import time

from ghost import Ghost, Session


class SinaBookSpider(object):

    # 初始化相关参数
    gh = Ghost()
    ss = Session(gh, display=True)  # 设置display为true, 方便调试

    total = 1526  # 预先计算的总数据量
    count = 0  # 已爬取的数据量

    # 记录解析以及翻页位置
    location = 0
    click_times = 0

    def run(self):
        """
        开始爬虫
        :return:
        """
        # 打开网页
        self.ss.open("http://book.sina.com.cn/excerpt/rwws/")
        # 等待数据加载完成
        self.ss.wait_for_selector('#subShowContent1_static > div:nth-child(20)')

        self.parselist()

        while self.count < self.total:
            if self.click_times is 0:
                # 点击加载更多
                self.ss.click('#subShowContent1_loadMore')
                # 每次翻页，或加载更多，要等待至加载完成
                self.ss.wait_for_selector('#subShowContent1_static > div:nth-child(21)')

                self.click_times += 1
                self.parselist()
            elif self.click_times is 1:
                self.ss.click('#subShowContent1_loadMore')
                self.ss.wait_for_selector('#subShowContent1_static > div:nth-child(41)')

                self.click_times += 1
                self.parselist()
            elif self.click_times is 2:
                self.ss.click('#subShowContent1_page .pagebox_next a')
                self.ss.sleep(2)

                self.click_times = 0
                self.location = 0
                self.parselist()

    def parselist(self):
        """
        解析列表页
        :return:
        """
        html = self.ss.content.encode('utf8')
        # print html

        pattern = re.compile(r'<div class="item"><h4><a href="(.*?)" target="_blank">', re.M)
        links = pattern.findall(html)

        for i in range(self.location, len(links)):
            print links[i]
            self.count += 1
            self.location += 1
        print self.count


if __name__ == '__main__':
    spider = SinaBookSpider()
    spider.run()

