import wx 


class MyFrame(wx.Frame):

	def __init__(self, parent=None, id=-1):
		wx.Frame.__init__(self, parent, id, "文本输入框", size=(300,150))
		panel = wx.Panel(self,-1)
		Label1 = wx.StaticText(panel,-1,"姓名：",pos=(10,10))
		self.inputText = wx.TextCtrl(panel,-1,"",pos=(80,10),size=(150,-1))
		self.inputText.SetInsertionPoint(0)

		Label2 = wx.StaticText(panel,-1,"密码：",pos=(10,50))
		self.pwdText = wx.TextCtrl(panel,-1,"",pos=(80,50),size=(150,-1),style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
		self.pwdText.Bind(wx.EVT_TEXT_ENTER,self.OnLostFocus)

	def OnLostFocus(self, event):
		wx.MessageBox("%s %s"%(self.inputText.GetValue(),self.pwdText.GetValue()))


if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()