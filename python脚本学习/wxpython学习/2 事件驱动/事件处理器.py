


# 利用Bind方法
# 使用预定义的事件绑定器对象wx.EVT_BUTTON将aButton和self.OnClick相关联
# self.Bind(wx.EVT_BUTTON, self.OnClick, aButton)


# 先从触发对象中开始找匹配事件类型的被绑定的处理器函数
# 找到则执行，找不到就到上一级

import wx

class MouseEventFrame(wx.Frame):

	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Frame With Button', size=(300,100))
		self.panel = wx.Panel(self)
		self.button = wx.Button(self.panel, label="Not Over", pos=(100,15))
		
		'''注意下面三行'''
		# 框架本身上绑定事件（因为按钮在框架上）
		self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)
		
		# 在按钮上绑定事件（因为Label在按钮上）
		self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
		self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)

	def OnButtonClick(self,event):
		self.panel.SetBackgroundColour("Green")
		self.panel.Refresh()

	def OnEnterWindow(self,event):
		self.button.SetLabel("鼠标进入！")
		event.Skip() #如果后面还有要处理的函数，需要调用该方法
		# print("666")

	def OnLeaveWindow(self,event):
		self.button.SetLabel("鼠标出去")
		event.Skip()
		# print("777")

if __name__ == '__main__':
	app=wx.App();
	frame=MouseEventFrame(parent=None,id=-1)
	frame.Show()
	app.MainLoop()