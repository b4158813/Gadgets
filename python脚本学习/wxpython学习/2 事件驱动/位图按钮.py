import wx

class MyFrame(wx.Frame):
	def __init__(self,parent=None,id=-1):
		wx.Frame.__init__(self,parent,id,"文本框",size=(300,350))

		panel = wx.Panel(self,-1)

		bmp = wx.Image("1.jpg",wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
		self.button = wx.BitmapButton(panel,-1,bmp,pos=(20,50),size=(200,250))
		self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
		self.inputText = wx.TextCtrl(panel,-1,"",pos=(10,10),size=(150,-1),style=wx.TE_READONLY)

	def OnClick(self,event):
		self.inputText.Value = "Hello World"

if __name__ == '__main__':
	app=wx.App()
	frame=MyFrame()
	frame.Show()
	app.MainLoop()