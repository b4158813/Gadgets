import wx
import random

class MyFrame(wx.Frame):
	def __init__(self,parent=None):
		wx.Frame.__init__(self,parent,-1,"吃饭决策器",size=(800,500))
		panel = wx.Panel(self,-1)
		self.button1 = wx.Button(panel,-1,"不知道",pos=(600,350),size=(100,100))
		self.Bind(wx.EVT_BUTTON,self.OnClick3,self.button1)
		self.button2 = wx.Button(panel,-1,"吃面",pos=(100,350),size=(100,100))
		self.Bind(wx.EVT_BUTTON,self.OnClick2,self.button2)
		self.button3 = wx.Button(panel,-1,"吃食堂",pos=(350,350),size=(100,100))
		self.Bind(wx.EVT_BUTTON,self.OnClick1,self.button3)
		
		self.button1.SetDefault()
		self.button2.SetDefault()
		self.button3.SetDefault()
		self.inputText = wx.TextCtrl(panel,-1,"",pos=(100,10),size=(600,300),style=wx.TE_MULTILINE)
		

	def decision(self,cnm):
		res = ""
		choose = ['吃面','吃食堂']
		noodle = ['螺蛳粉','刀削面','荞麦面','乌冬面']
		canteen = ['五食堂','五食堂二楼','一食堂','新世纪','二食堂','mini餐厅']
		random.shuffle(noodle)
		random.shuffle(canteen)
		if cnm == '2':
			res += '我们选择:' + '\n\n' + '、'.join(noodle[:2])
		elif cnm == '1':
			res += '我们选择:' + '\n\n' + '、'.join(canteen[:2])
		else:
			random.shuffle(choose)
			if choose[0] == '吃面':
				res += '我们选择:' + '\n\n' + '、'.join(noodle[:2])
			else:
				res += '我们选择:' + '\n\n' + '、'.join(canteen[:2])
		# print(res)
		return res

	def OnClick1(self,event):
		font = wx.Font(25,wx.SCRIPT,wx.NORMAL,wx.NORMAL)
		self.inputText.SetFont(font)
		self.inputText.Value = self.decision('1')
		event.Skip()

	def OnClick2(self,event):
		font = wx.Font(25,wx.SCRIPT,wx.NORMAL,wx.NORMAL)
		self.inputText.SetFont(font)
		self.inputText.Value = self.decision('2')
		event.Skip()

	def OnClick3(self,event):
		font = wx.Font(25,wx.SCRIPT,wx.NORMAL,wx.NORMAL)
		self.inputText.SetFont(font)
		self.inputText.Value = self.decision('3')
		event.Skip()


if __name__ == '__main__':
	app=wx.App()
	frame=MyFrame()
	frame.Show()
	app.MainLoop()