import wx

app = wx.App()

### 用户输入文本
# wx.TextEntryDialog()
# 参数按顺序说明是，父窗口，显示在窗口中的文本标签，窗口的标题（默认是“Please enter text”），输入域中的默认值
dlg1 = wx.TextEntryDialog(None, "Who is buried in Grant's tomb?",'A question', 'Cary Grant')

if dlg1.ShowModal()==wx.ID_OK: # 如果ShowModal返回值是ID_OK
	response = dlg1.GetValue() # GetValue方法的到输入的值
	print(response)




### 从一个列表中选择
dlg2 = wx.SingleChoiceDialog(None, 'What vesion of Python are you using?', 'Single Choice', ['1.5.2','2.0','2.1.3','2.2','2.3.1'])

if dlg2.ShowModal()==wx.ID_OK:
	# GetStringSelection方法返回所选的字符串
	response1 = dlg2.GetStringSelection()
	print(response1)