import wx

#app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
#frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
#frame.Show(True)
style = wx.FRAME_NO_TASKBAR & wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
#frame.SetWindowStyle(style)
#frame.ToggleWindowStyle(wx.STAY_ON_TOP)     # Show the frame.
#app.MainLoop()
import os
#import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A StatusBar in the bottom of the window
        self.SetWindowStyle(style)
        self.ToggleWindowStyle(wx.STAY_ON_TOP)
        # Setting up the menu.
        filemenu= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)


        self.Show(True)

    def OnAbout(self,e):
            # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

        def OnExit(self,e):
            self.Close(True)  # Close the frame.

app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()
