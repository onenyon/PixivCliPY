from ClipWatcher import ClipWatcher
from lib import PixivUtils
from queue import Queue

class PixivClip:
	def __init__(self, _user, _pass, default_path=r'F:/PIXIV'):
		self.pastes = Queue() 
		self.pixiv_utils = PixivUtils()
		self.default_path = default_path

		self.local_pixiv_ids = []

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

if __name__ == '__main__':
	p = PixivClip('', '')
	# p.begin()
	o= p.refresh_local_pixiv_ids()
	# print(o)