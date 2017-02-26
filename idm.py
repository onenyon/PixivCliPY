from comtypes.client import (GetModule, CreateObject)

def get_idm_object():
	try:
		from comtypes.gen import IDManLib
	except ImportError as e:
		GetModule(('{ECF21EAB-3AA8-4355-82BE-F777990001DD}', 1, 0))
		return self.load_idm_lib()		
	except Exception as e:
		print(e, type(e))
	else:
		return CreateObject('IDMan.CIDMLinkTransmitter', None, None, IDManLib.ICIDMLinkTransmitter2)

class IDM:
	def __init__(self, path=None):
		self.idm = get_idm_object()
		self.path = path
		self.flags = 2

	def dl(self, url, file_name=None, flags=2, refer=None, cookies=None, post=None, _user=None, _pass=None):
		return self.idm.SendLinkToIDM(url, refer, cookies, post, _user, _pass, self.path, file_name, flags)