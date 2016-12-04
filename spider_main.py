# coding:utf8
from baike_python import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HTMLDownloader()
        self.parser = html_parser.HTMLParser()
        self.outputer = html_outputer.HTMLOutputer()

    def craw(self, root_url):
        try:
            count = 1
            self.urls.add_new_url(root_url)
            while self.urls.has_new_url():
                new_url = self.urls.get_new_url()
                print "craw %d: %s" % (count, new_url)
                html_cont = self.downloader.download(new_url)
                if html_cont is None:
                    continue
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                self.outputer.output_html()
                if count == 1000:
                    break
                count = count + 1
        except:
            print "craw failed"
        self.outputer.output_html()
if __name__ == "__main__":
    root_url = "http://baike.baidu.com/link?url=aeSo1UxscIIjbIPV-yltkVssbd7cKoJmUW3IV87SNqWkULzPau9lA_VsMhQNdj7DX0GqeR8UWkKS06xiiAUzj_"
    # root_url = "http://baike.baidu.com/view/53593.htm?force=1"
    # root_url = "http://baike.baidu.com/view/100904.htm"
    # root_url = "http://baike.baidu.com/view/129545.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
