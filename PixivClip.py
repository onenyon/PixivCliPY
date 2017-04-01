from ClipWatcher import ClipWatcher
from lib import PixivUtils
from queue import Queue

from pixivpy3 import (PixivAPI, utils)
from urllib.parse import (urlparse, parse_qs)

class PixivClip:
	def __init__(self, _user, _pass, default_path=r'F:/PIXIV'):
		self._user, self._pass = (_user, _pass)

		self.api = PixivAPI()
		self.pixiv_utils = PixivUtils()

		self.pastes = Queue() 
		self.default_path = default_path

		self.local_pixiv_ids = []

	def login(self):
		self.api.login(self._user, self._pass)

	def get_illust(self, illust_id):
		if not self.api.access_token:
			self.login()
		try:
			json_result = self.api.works(illust_id)
			json_result = json_result.response
		except AttributeError:
			raise AttributeError(json_result)
		except utils.PixivError as e:
			self.login()
			print(e, self.api.access_token, json_result)
			return self.get_illust(illust_id)
		else:			
			json_result = self.pixiv_utils.is_single_array(json_result)
			return json_result

	def work(self, illust_id):
		try:
			illust = self.get_illust(illust_id)
		except AttributeError as json_result:
			# print(json_result.has_error)
			# print(json_result.status)
			print(json_result)
			print(dir(json_result))
			return
		else:
			pass
		illust_type = illust.type
		print(illust)


	def refresh_local_pixiv_ids(self):
		for i in self.pixiv_utils.list_imgs_pixiv_ids_in_dir(self.default_path):
			self.local_pixiv_ids.append(i)

	def callback(self, url):
		illust_id = self.pixiv_utils.parse_url_for_id(url)
		if illust_id in self.pastes.queue:
			print(illust_id, "Already In Queue!")
			return
		self.pastes.put(illust_id)

	def watch(self):
		watcher = ClipWatcher(self.pixiv_utils.is_pixiv_illust_url, self.callback)
		try:
			for i in watcher.start():
				print('PIXIV LINKS:', self.pastes.qsize(), i, flush=True, end='\r')
		except (KeyboardInterrupt, Exception) as e:
			watcher.stop()
		return watcher

	def print_pastes_queue(self):
		while not self.pastes.empty():
			illust_id = self.pastes.get()
			print(illust_id)

		input("PAUSED!!!")

	def begin(self):
		watcher = self.watch()
		self.print_pastes_queue()