import wx
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示汉字的操作
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号的操作
mpl.rcParams['font.family']='sans-serif'
# mpl.style.use('ggplot')
plt.rc('font', family='SimHei', size=15)
pylab.rcParams['figure.figsize'] = 8, 5


class MyFrame(wx.Frame):

	def __init__(self, parent=None, id=-1, ):
		wx.Frame.__init__(self, parent, id, "简易折线图工具",size=(400,300))
		self.SetMaxSize((400,300))
		self.SetMinSize((400,300))
		panel = wx.Panel(self, -1)
		font = wx.Font(10,wx.DEFAULT,wx.NORMAL,wx.NORMAL,False)
		Label1 = wx.StaticText(panel, -1, "横坐标（逗号分隔）", pos=(15,35))
		Label2 = wx.StaticText(panel, -1, "纵坐标（逗号分隔）", pos=(15,85))
		Label1.SetFont(font)
		Label2.SetFont(font)

		self.inputText1 = wx.TextCtrl(panel, -1, pos=(140,30),size=(220,25))
		self.inputText1.SetInsertionPoint(0)
		self.inputText2 = wx.TextCtrl(panel, -1, pos=(140,80),size=(220,25))
		self.inputText2.SetInsertionPoint(0)

		self.button_draw = wx.Button(panel, -1, "绘图", pos=(210,130), size=(150,100))
		self.button_draw.SetFont(font)
		self.button_draw.Bind(wx.EVT_BUTTON, self.OnClickDraw)

		self.button_clearh = wx.Button(panel, -1, "清空横坐标", pos=(20,130), size=(150,50))
		self.button_clearh.SetFont(font)
		self.button_clearh.Bind(wx.EVT_BUTTON, self.OnClickClearH)
		
		self.button_clearz = wx.Button(panel, -1, "清空纵坐标", pos=(20,180), size=(150,50))
		self.button_clearz.SetFont(font)
		self.button_clearz.Bind(wx.EVT_BUTTON, self.OnClickClearZ)
		
		self.inputText2.Bind(wx.EVT_TEXT_ENTER,self.OnClickDraw)
		# self.inputText1.Bind(wx.EVT_TEXT_ENTER,self.OnClickDraw)


	def OnClickDraw(self, event):
		x = self.inputText1.GetValue().split(',')
		y = self.inputText2.GetValue().split(',')
		x = [eval(i) for i in x]
		y = [eval(i) for i in y]

		try:
			self.LinePlot(x, y)
		except:
			self.PlotError()
		event.Skip()

	def OnClickClearH(self, event):
		self.inputText1.Clear()
		event.Skip()

	def OnClickClearZ(self, event):
		self.inputText2.Clear()
		event.Skip()

	def LinePlot(self, x, y):
		plt.cla()
		plt.title("y-x关系图")
		plt.plot(x, y, label="line", marker='o')
		plt.grid(color='grey',linestyle='--', alpha=0.5)
		plt.xlabel('x')
		plt.ylabel('y')
		plt.legend()
		plt.show()

	def PlotError(self):
		wx.MessageBox("输入有误，请重新输入！")


if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()