aratýlýr.   -> class ExpandedTaskBar(ui.ScriptWindow):

alt kýsma eklenir   

BUTTON_OTOMATIK_AV = 3


aratýlýr : self.expandedTaskBarBoard = self.GetChild("ExpanedTaskBar_Board")

alt kýsýmda self.toggleButtonDict = {}  altýna eklenir 


self.toggleButtonDict[ExpandedTaskBar.BUTTON_OTOMATIK_AV] = self.GetChild("AutoButton")
self.toggleButtonDict[ExpandedTaskBar.BUTTON_OTOMATIK_AV].SetParent(self)