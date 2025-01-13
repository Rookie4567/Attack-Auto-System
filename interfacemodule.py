if uiTaskBar.TaskBar.IS_EXPANDED:  aratýlýr altýna 


self.wndExpandedTaskBar.SetToggleButtonEvent(uiTaskBar.ExpandedTaskBar.BUTTON_OTOMATIK_AV, ui.__mem_func__(self.OtomatikAv))

eklenir


def ToggleInventoryWindow(self):  aratýlýr  

üstüne eklenir

def OtomatikAv(self):
		import uiotomatikav
		self.otomatikav = uiotomatikav.otomatikav()
		self.otomatikav.Show()