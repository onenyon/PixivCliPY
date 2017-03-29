try:
	from comtypes.gen import IDManLib
except ImportError as e:
	GetModule(('{ECF21EAB-3AA8-4355-82BE-F777990001DD}', 1, 0))
	from comtypes.gen import IDManLib

class IDM:
	def __init__(self, path=None):
		self.idm = CreateObject('IDMan.CIDMLinkTransmitter', None, None, IDManLib.ICIDMLinkTransmitter2)
		self.path = path
		self.flags = 2

	def dl(self, url, file_name=None, flags=2, refer=None, cookies=None, post=None, _user=None, _pass=None):
		return self.idm.SendLinkToIDM(url, refer, cookies, post, _user, _pass, self.path, file_name, flags)
