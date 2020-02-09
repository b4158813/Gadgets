import wx

class InsertFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Frame with Button',size=(300,100))
        panel = wx.Panel(self) # 创建画板
        # 创建按钮
        button = wx.Button(panel, label='Close', pos=(125,10), size=(50,50))
        # 绑定按钮的点击事件
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        # 绑定按钮的关闭事件
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        
    def OnCloseMe(self,event):
        self.Close(True)
        
    def OnCloseWindow(self,event):
        self.Destroy()
        
if __name__=='__main__':
    app = wx.App()
    frame = InsertFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()