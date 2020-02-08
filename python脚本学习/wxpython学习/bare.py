import wx

class App(wx.App):

	#def __init__(self):
	#	wx.App.__init__(self)

	def OnInit(self):
		frame = wx.Frame(parent=None,id=-1)
		frame.Show(True)
		return True

app = App()
app.MainLoop()