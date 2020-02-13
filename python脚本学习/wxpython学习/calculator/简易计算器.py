import wx


class MyFrame(wx.Frame):

	def __init__(self, parent=None, id=-1):
		wx.Frame.__init__(self, parent, id)

		panel = wx.Panel(self, -1)
		
