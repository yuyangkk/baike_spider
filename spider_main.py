import url_mananger
import html_download
import html_parser
import html_output


class SpiderMain(object):

    def __init__(self):
        # 实例化属性
        self.urls = url_mananger.UrlManager()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutputer()

    def craw(self, root_url):
        if root_url is None:
            return

        count = 1
        # 向URL管理器中添加root_url
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                # 获取要爬去数据的URL
                new_url = self.urls.get_new_url()
                # 下载URL对应的html
                html_cont = self.downloader.download(new_url)
                # 解析下载的数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 将解析出来的相关urls添加到urls.new_urls中
                self.urls.add_new_urls(new_urls)
                # 将解析出来的数据保存到outputer中
                self.outputer.collect_data(new_data)

                # 只爬取100条数据
                if count == 100:
                    break
                count = count + 1
            except ValueError:
                print('aaa,failed')

        # 输出一个html页面
        self.outputer.output_html()


def main():
    # 设置入口URL
    root_url = 'https://baike.baidu.com/item/Python/407313'
    # 实例化一个爬虫对象
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)


if __name__ == '__main__':
    main()
