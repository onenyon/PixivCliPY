from pixivpy3 import (PixivAPI, utils)
from urllib.parse import parse_qs, urlparse

class PixivClip:
	def __init__(self, _user, _pass):
		(self._user, self._pass) = _user, _pass
		self.validater = ('pixiv.net', '/member_illust.php', 'illust_id')
		self.pixiv = PixivAPI()

	def login(self):
		self.pixiv.login(self._user, self._pass)

	def is_pixiv_illust_url(self, url):
		return url.startswith(('http://','https://')) and all(x in url for x in self.validater)

	def parse_url_for_id(self, url):
		query = parse_qs(urlparse(url).query)
		illust_id = self.is_single_array(query['illust_id']).strip()

		if not (isinstance(illust_id, str) and illust_id.isdigit()):
			raise self.PixivClipError('Illust Id is not string integer.')
		return illust_id

	def get_illust(self, illust_id_or_url):
		if isinstance(illust_id_or_url, str):
			try:
				illust_id = int(illust_id_or_url)
			except ValueError:
				if not self.is_pixiv_illust_url(illust_id_or_url):
					raise Exception('String is not a url', illust_id_or_url)
				illust_id = self.parse_url_for_id(illust_id_or_url)

		return self.pixiv.works(illust_id)

	def is_single_array(self, arr):
		poped = arr.pop()
		length = len(arr)
		if length != 0:
			print('Abmormality detected. Length of arr is', length)
			print('returnig the first one')
			# todo save for inspection
		return poped