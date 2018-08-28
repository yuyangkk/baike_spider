from urllib import request
import ssl


# 如果访问的是https，会自动校验，此句停止自动校验
ssl._create_default_https_context = ssl._create_unverified_context


# 类定义上面必须要空两行，方法定义上面必须要空一行
class HtmlDownloader(object):

    @staticmethod
    def download(url):
        # 下载URL中的数据
        if url is None:
            return

        with request.urlopen(url) as f:
            if f.getcode() != 200:
                print('请求失败')
                return None
            return f.read().decode('utf-8')
