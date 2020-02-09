import wx

# 构造函数
# wx.MessageDialog(parent, message, caption="Message box",  style=wx.OK|wx.CANCEL, pos=wx.DefaultPosition)
# message：显示在对话框中的字符串
# caption：显示在对话框标题栏上的字符串
# style：按钮样式
# pos：对话框位置



app = wx.App()
dlg = wx.MessageDialog(None, 'Is this the coolest thing ever!', 'MessageDialog', wx.YES_NO|wx.ICON_QUESTION)

# ShowModal：以模式框架的方式显示，在对话框关闭之前别的窗口不能影响用户事件
# 返回按下按钮的ID：有ID_YES ID_NO ID_CANCEL ID_OK
result = dlg.ShowModal()
dlg.Destroy()