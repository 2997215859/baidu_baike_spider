# coding:utf8
from bs4 import BeautifulSoup
import re
import urlparse
class HTMLParser():

	def _get_new_urls(self, page_url, soup):
		new_urls = set()
		links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url, new_url)
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self, page_url, soup):
		res_data = {}

		# url
		res_data['url'] = page_url
		# <dd class="lemmaWgt-lemmaTitle-title">
		# <h1>自由软件</h1>
		# <a href="javascript:;" class="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link" style="display: inline-block;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
		# <a class="lock-lemma" target="_blank" href="/view/10812319.htm" title="锁定"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lock-lemma"></em>锁定</a>
		# </dd>
		try:
			title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
			res_data['title'] = title_node.get_text()
		except:
			res_data['title'] = "title is null"

		# <div class="lemma-summary" label-module="lemmaSummary">
		# <div class="para" label-module="para">根据自由软件<a target="_blank" href="/view/21375.htm">基金会</a>的定义，<b>自由软件</b>是一种可以不受限制地自由使用、复制、研究、修改和分发的软件。可以买卖。这方面的不受限制正是自由软件最重要的本质。要将软件以自由软件的形式发表，通常是让软件以“自由软件授权协议”的方式被分配发布，以及公开的软件原始码。 自由软件对全世界的商业发展有巨大的贡献。自由软件使成千上万的人的日常工作更加便利，为了满足用户的各种应用需要，它以一种不可思议的速度发展。<a target="_blank" href="/view/20965.htm">自由软件</a>是信息社会下以开放创新、共同创新为特点的<a target="_blank" href="/view/1923326.htm">创新2.0</a>模式在软件开发与应用领域的典型体现。主要许可证有GPL和BSD许可证两种。</div>
		# </div>
		try:
			summary_node = soup.find('div', class_='lemma-summary')
			res_data['summary'] = summary_node.get_text()
		except:
			res_data['summary'] = "summary is null"

		return res_data

	def parse(self, page_url, html_cont):
		if page_url is None or html_cont is None:
			return None

		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding="utf-8")

		new_urls = self._get_new_urls(page_url, soup)
		new_data = self._get_new_data(page_url, soup)
		return new_urls, new_data