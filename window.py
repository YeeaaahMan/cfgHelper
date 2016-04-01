import wx
import wx.xrc
import xml.etree.ElementTree as ET
from confg import *

CFG = read_config()  # JSON object

def WoTVersion(text):
    version = dict( CFG["wot"]["versions"] )

    for item in text:
        if item.split('=')[0] in version:
            version[item.split('=')[0]] = item.split('=')[-1]

    if version["hdcontent_ver"] != "unknown":
        version["selected_target"] = "hd"
    else:
        version["selected_target"] = "sd"

    return version


def WoWPVersion(text):
    version = dict( CFG["wowp"]["versions"] )

    for item in text:
        if item.split('=')[0] in version:
            version[item.split('=')[0]] = item.split('=')[-1]

    if version["hdcontent_ver"] != "unknown":
        version["selected_target"] = "hd"
    else:
        version["selected_target"] = "sd"

    return version


def WoWSVersion(text):
    version = dict( CFG["wows"]["versions"] )

    for item in text:
        if item.split('=')[0] in version:
            version[item.split('=')[0]] = item.split('=')[-1]
    return version


def CreateCFG(filePath, Versions):
    filePath.replace("/", "\\")
    cfg_file = filePath.split('\\')[-1]
    try:
        tree = ET.parse(filePath)
    except:
        return "\nERROR! Can't open " + filePath + ".  =(\n"
    root = tree.getroot()

    for item in root:
        if item.tag in Versions:
            # print item.tag, item.text, Versions[item.tag]
            item.text = Versions[item.tag]

    tree.write(CFG["output"] + cfg_file, xml_declaration=True, encoding="utf-8")
    return "\n" + CFG["output"] + cfg_file + ' has been created.'


def SelectGame(link):
    link = link.strip().replace('"', '')
    link = link.split('&')

    if "wot" in link[0].lower() or "tank" in link[0].lower():
        Versions = WoTVersion(link)
        filePath = CFG["wot"]["path"]
        return "WoT detected...", Versions, filePath

    elif "wowp" in link[0].lower() or "plane" in link[0].lower():
        Versions = WoWPVersion(link)
        filePath = CFG["wowp"]["path"]
        return "WoWP detected...", Versions, filePath

    elif "wows" in link[0].lower() or "ship" in link[0].lower():
        Versions = WoWSVersion(link)
        filePath = CFG["wows"]["path"]
        return "WoWS detected...", Versions, filePath

    else:
        return "Can't detect project.", {}, ""
        # raw_input("ERROR! Can't detect project.")
        # exit()


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"cfgHelper", pos=wx.DefaultPosition,
                          size=wx.Size(500, 270), style=(wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL) ^ (wx.MAXIMIZE_BOX | wx.RESIZE_BORDER))

        self.SetIcon(icon_32.GetIcon())


        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl1 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        bSizer3.Add(self.m_textCtrl1, 1, wx.ALL | wx.EXPAND, 5)

        bSizer2.Add(bSizer3, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_buttonSettings = wx.Button(self.m_panel1, wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_buttonSettings, 0, wx.ALL, 5)

        bSizer4.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.m_buttonCreateCFG = wx.ToggleButton(self.m_panel1, wx.ID_ANY, u"Create CFG!", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.m_buttonCreateCFG.SetValue(True)
        bSizer4.Add(self.m_buttonCreateCFG, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer2.Add(bSizer4, 0, wx.EXPAND, 5)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar(2, wx.ST_SIZEGRIP, wx.ID_ANY)
        self.SetStatusWidths([-2,-7])

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnExit)
        self.m_buttonSettings.Bind(wx.EVT_BUTTON, self.SettingsShow)
        self.m_buttonCreateCFG.Bind(wx.EVT_TOGGLEBUTTON, self.CreateCFG)
        self.m_textCtrl1.Bind( wx.EVT_TEXT, self.textAdded )

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnExit(self, event):
        myApp.Exit()

    def textAdded( self, event ):
        myApp.frame.m_buttonCreateCFG.Enable(True)
        result, _, _ = SelectGame( myApp.frame.m_textCtrl1.GetRange(0,-1) )
        myApp.frame.m_statusBar1.SetStatusText(result, 0)
        myApp.frame.m_statusBar1.SetStatusText('', 1)

    def SettingsShow(self, event):
        CFG = read_config()
        myApp.settings.m_filePicker_wot.SetPath(CFG["wot"]["path"])
        myApp.settings.m_filePicker_wowp.SetPath(CFG["wowp"]["path"])
        myApp.settings.m_filePicker_wows.SetPath(CFG["wows"]["path"])
        myApp.settings.m_dirPicker_output.SetPath(CFG["output"])
        myApp.settings.Show()


    def CreateCFG(self, event):
        link = myApp.frame.m_textCtrl1.GetRange(0, -1).replace('"','')   # norm!
        result, Versions, filePath = SelectGame(link)

        myApp.frame.m_textCtrl1.Clear()
        #myApp.frame.m_textCtrl1.AppendText( result + "\n")

        if 'ERROR' not in result:
            myApp.frame.m_statusBar1.SetStatusText( CreateCFG(filePath, Versions) , 1)
            myApp.frame.m_textCtrl1.AppendText( '\n'.join(link.split('&')) )

        myApp.frame.m_buttonCreateCFG.SetValue(0)
        myApp.frame.m_buttonCreateCFG.Enable(False)


class MyFrame2(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Settings", pos=wx.DefaultPosition, size=wx.Size(480, 250),
                          style=(wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP) ^ (wx.CAPTION | wx.CLOSE_BOX))

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        # self.config = read_config()

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticSettingsWindowText = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Launcher.cfg paths:",
                                                        wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticSettingsWindowText.Wrap(-1)
        bSizer6.Add(self.m_staticSettingsWindowText, 0, wx.ALL, 5)

        self.m_filePicker_wot = wx.FilePickerCtrl(self.m_panel2, wx.ID_ANY, CFG["wot"]["path"], u"Select a file",
                                                  u"WoTLauncher.cfg", wx.DefaultPosition, wx.DefaultSize,
                                                  wx.FLP_DEFAULT_STYLE)
        bSizer6.Add(self.m_filePicker_wot, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.m_filePicker_wowp = wx.FilePickerCtrl(self.m_panel2, wx.ID_ANY, CFG["wowp"]["path"], u"Select a file",
                                                   u"WoWPLauncher.cfg", wx.DefaultPosition, wx.DefaultSize,
                                                   wx.FLP_DEFAULT_STYLE)
        bSizer6.Add(self.m_filePicker_wowp, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.m_filePicker_wows = wx.FilePickerCtrl(self.m_panel2, wx.ID_ANY, CFG["wows"]["path"], u"Select a file",
                                                   u"WoWSLauncher.cfg", wx.DefaultPosition, wx.DefaultSize,
                                                   wx.FLP_DEFAULT_STYLE)
        bSizer6.Add(self.m_filePicker_wows, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        self.m_staticline1 = wx.StaticLine(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer6.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Output path:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer6.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_dirPicker_output = wx.DirPickerCtrl(self.m_panel2, wx.ID_ANY, CFG["output"], u"Select a folder",
                                                   wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        bSizer6.Add(self.m_dirPicker_output, 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 5)

        bSizer6.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        bSizer_buttons = wx.BoxSizer(wx.HORIZONTAL)

        bSizer_buttons.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.m_button_save = wx.Button(self.m_panel2, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_buttons.Add(self.m_button_save, 0, wx.ALL, 5)

        self.m_button_close = wx.Button(self.m_panel2, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_buttons.Add(self.m_button_close, 0, wx.ALL, 5)

        bSizer6.Add(bSizer_buttons, 0, wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer6)
        self.m_panel2.Layout()
        bSizer6.Fit(self.m_panel2)
        bSizer5.Add(self.m_panel2, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnExit)
        self.m_button_save.Bind(wx.EVT_BUTTON, self.SettingsSave)
        self.m_button_close.Bind(wx.EVT_BUTTON, self.SettingsHide)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnExit(self, event):
        myApp.settings.Hide()

    def SettingsSave(self, event):
        # save settings
        CFG["wot"]["path"] = self.m_filePicker_wot.GetPath()
        CFG["wowp"]["path"] = self.m_filePicker_wowp.GetPath()
        CFG["wows"]["path"] = self.m_filePicker_wows.GetPath()
        CFG["output"] = self.m_dirPicker_output.GetPath()
        if len(CFG["output"]) != 0 and CFG["output"][-1] != '\\':
            CFG["output"] += '\\'
        write_config(CFG)
        myApp.settings.Hide()

    def SettingsHide(self, event):
        myApp.settings.Hide()


class myApp(wx.App):
    """ app"""

    def __init__(self, redirect=True):
        wx.App.__init__(self, redirect)

    def OnInit(self):
        self.frame = MyFrame1(parent=None)
        self.frame.Show()
        self.settings = MyFrame2(parent=None)
        self.SetTopWindow(self.frame)
        return True


if __name__ == '__main__':
    # (1) Text redirection starts here
    myApp = myApp(redirect=True)
    # (2) The main event loop is entered here
    myApp.MainLoop()
