from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


class HtmlParser(object):

    @staticmethod
    def _get_new_urls(soup, page_url):
        # /item/Python/407313
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item/\w+/\d+'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            print('page_url: %s, link: %s, new_url: %s, full_url: %s' % (page_url, link, new_url, new_full_url))
        return new_urls

    @staticmethod
    def _get_new_data(soup, page_url):

        res_data = {'url': page_url}

        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        # title_node = <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        # summary
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):

        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        # 提取网页中的其他URL
        new_urls = self._get_new_urls(soup, page_url)
        new_data = self._get_new_data(soup, page_url)
        return new_urls, new_data
