import wx

class Frame(wx.Frame):
	pass

class MyApp(wx.App):

	def OnInit(self):
		self.frame = Frame(parent=None, title='Spare')
		self.frame.Show(True)
		self.SetTopWindow(self.frame) //设置顶级窗口
		return True


if __name__=='__main__':
	app = MyApp()
	app.MainLoop()