import gutil
import misc
import util

import wx

class SCDictDlg(wx.Dialog):
    def __init__(self, parent, scDict, isGlobal):
        wx.Dialog.__init__(self, parent, -1, "Spell Checker Dictionary",
                           style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.scDict = scDict

        vsizer = wx.BoxSizer(wx.VERTICAL)

        if isGlobal:
            s = "Global Words"
        else:
            s = "Script-specific Words"

        vsizer.Add(wx.StaticText(self, -1, s))

        self.itemsEntry = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE |
                                     wx.TE_DONTWRAP, size=(300, 300))
        vsizer.Add(self.itemsEntry, 1, wx.EXPAND)

        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        hsizer.Add((1, 1), 1)

        cancelBtn = gutil.createStockButton(self, "Cancel")
        hsizer.Add(cancelBtn, 0, wx.LEFT, 10)

        okBtn = gutil.createStockButton(self, "OK")
        hsizer.Add(okBtn, 0, wx.LEFT, 10)

        vsizer.Add(hsizer, 0, wx.EXPAND | wx.TOP, 10)

        self.cfg2gui()

        util.finishWindow(self, vsizer)

        wx.EVT_TEXT(self, self.itemsEntry.GetId(), self.OnMisc)
        wx.EVT_BUTTON(self, cancelBtn.GetId(), self.OnCancel)
        wx.EVT_BUTTON(self, okBtn.GetId(), self.OnOK)

    def OnOK(self, event):
        self.scDict.refresh()
        self.EndModal(wx.ID_OK)

    def OnCancel(self, event):
        self.EndModal(wx.ID_CANCEL)

    def OnMisc(self, event):
        self.scDict.set(misc.fromGUI(self.itemsEntry.GetValue()).split("\n"))

    def cfg2gui(self):
        self.itemsEntry.SetValue("\n".join(self.scDict.get()))
