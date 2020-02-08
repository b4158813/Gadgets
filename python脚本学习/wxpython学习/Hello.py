import wx

class Frame(wx.Frame):
	def __init__(self, image, parent=None, id=-1, pos=wx.DefaultPosition, title='Hello, wxPython!'):
		temp = image.ConvertToBitmap()
		size = temp.GetWidth(), temp.GetHeight()
		wx.Frame.__init__(self,parent,id,title,pos,size)
		# 父类方法StaticBitmap用来显示图像（要求一个位图）
		self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)

class App(wx.App):

	def OnInit(self):
		image = wx.Image('wxPython.jpg',wx.BITMAP_TYPE_JPEG)
		self.frame = Frame(image)

		self.frame.Show(True)
		self.SetTopWindow(self.frame)
		return True

def main():
	app = App()
	app.MainLoop()

if __name__=="__main__":
	main()