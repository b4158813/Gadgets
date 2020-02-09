import wx

class MyFrame(wx.Frame):

	def __init__(self,parent=None,id=-1):
		wx.Frame.__init__(self,parent,id,"文本框",size=(300,150))
		panel = wx.Panel(self, -1)

		#
		multiText = wx.TextCtrl(panel, -1, "", pos=(10,10),size=(180,80), style=wx.TE_MULTILINE|wx.TE_CENTER)
		multiText.SetBackgroundColour("pink")
		multiText.SetFocus()

if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame(None,-1)
	frame.Show()
	app.MainLoop()