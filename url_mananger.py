class UrlManager(object):
    
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    # 添加单个URL
    def add_new_url(self, url):
        # 检查
        if url is None:
            return
        if url in self.new_urls and url in self.old_urls:
            return
        else:
            self.new_urls.add(url)

    # 添加多个url
    def add_new_urls(self, urls):
        if urls is None:
            return
        for url in urls:
            self.add_new_url(url)
            
    # 是否还有未爬取数据的URL
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取一个待爬取数据的URL
    def get_new_url(self):
        # 在未爬去数据的URL中获取将要爬去数据的URL，并在new_urls中删除
        new_url = self.new_urls.pop()
        # 将new_url添加到已经使用的URL中
        self.old_urls.add(new_url)
        # 返回将要爬去数据的URL
        return new_url