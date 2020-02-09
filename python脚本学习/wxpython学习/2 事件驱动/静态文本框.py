
import wx

class MyFrame(wx.Frame):
	def __init__(self, parent=None):
		wx.Frame.__init__(self, parent, id=-1, size=(100,75))
		panel = wx.Panel(self, -1)
		text = wx.StaticText(panel,-1,"Hello World", (10,10),(80,25),wx.ALIGN_CENTER)
		text.SetForegroundColour("blue") # 设置字体颜色
		text.SetBackgroundColour("green") # 设置字的背景色
		# 设置字体样式：意大利斜体
		font = wx.Font(12,wx.DEFAULT,wx.ITALIC,wx.NORMAL,True)
		text.SetFont(font)


if __name__ == '__main__':
	app = wx.App()
	frame=MyFrame()
	frame.Show()
	app.MainLoop()