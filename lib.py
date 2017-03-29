from os import walk
from urllib.parse import (urlparse, parse_qs)

class PixivUtils:
    def __init__(self):
        self.validater = ('pixiv.net', '/member_illust.php', 'illust_id')

    def is_pixiv_illust_url(self, url):
        return url.startswith(('http://','https://')) and all(x in url for x in self.validater)

    def is_single_array(self, arr):
        poped = arr.pop()
        length = len(arr)
        if length != 0:
            print('Abnormality detected. Length of array is', length, arr)
            print('RETURNIG THE FIRST ONE')
            # todo save for inspection
        return poped

    def parse_url_for_id(self, url):
        query = parse_qs(urlparse(url).query)
        illust_id = query['illust_id']
        illust_id = self.is_single_array(illust_id).strip()
        illust_id = int(illust_id)
        return illust_id

    def list_imgs_pixiv_ids_in_dir(self, dir_path, tup=tuple()):
        for path, subdirs, files in walk(dir_path):
            for name in files:
                if name.endswith('.zip') or name.startswith('.'):continue
                tup += (name, )
        return tup

if __name__ == '__main__':
    p = PixivUtils()
    o = p.list_imgs_pixiv_ids_in_dir(r'Z:/Pixiv')
    print(len(o))
    # print(o)