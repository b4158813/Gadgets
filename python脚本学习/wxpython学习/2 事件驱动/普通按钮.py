import wx

class MyFrame(wx.Frame):
	def __init__(self,parent=None):
		wx.Frame.__init__(self,parent,-1,"文本框",size=(300,150))

		panel = wx.Panel(self,-1)

		self.button = wx.Button(panel,-1,"确定",pos=(10,10))
		self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
		self.button.SetDefault()
		self.inputText = wx.TextCtrl(panel,-1,"",pos=(100,10),size=(150,-1),style=wx.TE_READONLY)

	def OnClick(self,event):
		self.inputText.Value = "Hello Wrold"
		#wx.MessageBox("%s"%(self.inputText.GetValue()))
		event.Skip()


if __name__ == '__main__':
	app=wx.App()
	frame=MyFrame()
	frame.Show()
	app.MainLoop()