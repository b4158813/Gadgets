import wx


# 父类构造函数
# wx.frame(parent, id=-1, title="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_SYTLE, name="frame")

# parent：父窗口
# id：wxPython的ID号，传-1则随机
# title：标题
# pos：窗口左上角在屏幕中的位置，(0,0)是左上角，(-1,-1)默认让系统决定
# size：尺寸，(-1,-1)默认让系统决定
# style：窗口的类型
# name：框架的内在名字，用于寻找该窗口

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,"my friendly window",(100,100),(100,100))

app = wx.PySimpleApp()
frame = MyFrame()
id = frame.GetId()
print(id)
