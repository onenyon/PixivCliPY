from pixivpy3 import (PixivAPI, utils)

class PixivClip:
	def __init__(self, _user, _pass):
		(self._user, self._pass) = _user, _pass
		self.validater = ('pixiv.net', '/member_illust.php', 'illust_id')
		self.pixiv = PixivAPI()

	def login(self):
		self.pixiv.login(self._user, self._pass)

	def is_pixiv_illust_url(self, url):
		return url.startswith(('http://','https://')) and all(x in url for x in self.validater)
