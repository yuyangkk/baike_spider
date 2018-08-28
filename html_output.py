

class HtmlOutputer(object):

    def __init__(self):
        self.data = []

    # 将每一条解析出来的结果，存放到数组中，以便在HTML页面中输出
    def collect_data(self, data):
        self.data.append(data)

    def output_html(self):
        with open('resource.html', 'w') as file:
            file.write('<html>')
            file.write('<head>')
            file.write('<meta charset = "utf-8">')
            file.write('<title>')
            file.write('爬取结果')
            file.write('</title>')
            file.write('</head>')
            file.write('<body>')
            file.write('<table border = "1" cellspacing = "0">')
            file.write('<tr><td>标题</td><td>链接</td><td>描述简介</td></tr>')
            for data in self.data:
                print(data)
                string = "<tr><td>%s</td><td><a href=%s>%s</a></td><td>%s</td></tr>" % (data['title'], data['url'], data['url'], data['summary'])
                file.write(string)
            file.write('</table>')
            file.write('</body>')
            file.write('</html>')
        file.close()
