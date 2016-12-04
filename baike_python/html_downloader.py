import urllib2
class HTMLDownloader():

	def download(self, url):
		if url is None:
			return None
		# req = urllib2.Request(url)
		# debug_handler = urllib2.HTTPHandler(debuglevel = 1)
		# opener = urllib2.build_opener(debug_handler, RedirctHandler)
		# urllib2.install_opener(opener)
		response = urllib2.urlopen(url)
		# print response.getcode()
		if response.getcode() != 200:
			return None

		return response.read()
