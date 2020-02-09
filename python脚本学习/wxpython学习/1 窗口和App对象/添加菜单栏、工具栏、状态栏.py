import wx
import wx.py.images as images


class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars', size=(300,200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour("White") # 背景调成白色
        statusBar = self.CreateStatusBar() # 创建状态栏
        toolbar = self.CreateToolBar() # 创建工具栏
        # 给工具栏添加一个工具
        toolbar.AddSimpleTool(wx.NewId(), images.getPyBitmap(), "New", "Long help for New")
        toolbar.Realize() # 显示工具栏
        menuBar = wx.MenuBar() # 创建菜单栏
        
        # 创建两个菜单栏
        menu1 = wx.Menu() 
        menuBar.Append(menu1, " 1")# 在菜单栏上添加菜单
        menu2 = wx.Menu()
        
        # 菜单内添加选项
        # 参数分别是（ID，选项的文本，鼠标停留时显示在状态栏的文本）
        menu2.Append(wx.NewId(),"ahah ","Copy in status bar")
        menu2.Append(wx.NewId(),"C","123")
        menu2.Append(wx.NewId(),"Paste","456")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(),"okay","Display Options")
        menuBar.Append(menu2, " 2")
        self.SetMenuBar(menuBar)
        
if __name__=='__main__':
    app=wx.App()
    frame=ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()