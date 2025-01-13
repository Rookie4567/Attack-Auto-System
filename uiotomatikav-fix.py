import dbg
import snd
import systemSetting
import chat
import app
import localeInfo
import chrmgr
import musicInfo
import background
import uiSelectMusic
import ahmetatalayInfo
import chr
try:
    import playerm2g2 as player
    chr.GetPixelPosition = player.GetMainCharacterPosition
except:
    import player
try:
    import chatm2g as chat
except:
    import chat
try:
    import m2netm2g as net
except:
    import net    
import net
import app
import time
import ui
dokoftowaniewida=0
tanrisure=0

class otomatikav(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__LoadDialog()
		self.OnUpdate()
		self.StartRefreshShow()
		self.PelerinRefreshShow()
		self.ToplamaRefreshShow()
		self.IksirRefreshShow()
		self.SkillRefreshShow()
		self.YenidenRefreshShow()
		self.TanrilarRefreshShow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def OnUpdate(self):
		if 1 == ahmetatalayInfo.Toplama:
			self.ClickAutoToplamaOnButton()

		if 1 == ahmetatalayInfo.Iksir:
			self.ClickAutoPositionlOnButton()

		if 1 == ahmetatalayInfo.Skill:
			self.ClickAutoSkilOnButton()

		if 1 == ahmetatalayInfo.YenidenDogus:
			self.ClickAutoYenidenOnButton()

		if 1 == ahmetatalayInfo.Tanrilar:
			self.ClickAutoTanrilarOnButton()

	def __Initialize(self):
		self.AutoPelerinButton = []
		self.AutoToplamaButton = []
		self.AutoStartButton = []
		self.AutoPositionlButton = []
		self.AutoSkilButton = []
		self.AutoYenidenButton = []
		self.AutoTanrilarButton = []

	def __LoadDialog(self):

		try:

			GetObject = self.GetChild
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/autowindow.py")
			#Pelerin
			self.board = GetObject("board")
			self.AutoPelerinButton.append(GetObject("AutoPelerinOnButton"))
			self.AutoPelerinButton.append(GetObject("AutoPelerinOffButton"))
			#Toplama
			self.AutoToplamaButton.append(GetObject("AutoToplamaOnButton"))
			self.AutoToplamaButton.append(GetObject("AutoToplamaOffButton"))
			#ÝKSÝR
			self.AutoPositionlButton.append(GetObject("AutoPositionlOnButton"))
			self.AutoPositionlButton.append(GetObject("AutoPositionlOffButton"))
			#Skiller
			self.AutoSkilButton.append(GetObject("AutoSkilOnButton"))
			self.AutoSkilButton.append(GetObject("AutoSkilOffButton"))
			#Skiller
			self.AutoYenidenButton.append(GetObject("AutoYenidenOnButton"))
			self.AutoYenidenButton.append(GetObject("AutoYenidenOffButton"))
			#Tanrilar
			self.AutoTanrilarButton.append(GetObject("AutoEjderhaOnButton"))
			self.AutoTanrilarButton.append(GetObject("AutoEjderhaOffButton"))
			#BAÞLAT
			self.AutoStartButton.append(GetObject("AutoStartOnButton"))
			self.AutoStartButton.append(GetObject("AutoStartOffButton"))

			#pelerin
			self.board.SetCloseEvent(self.Close)
			self.AutoPelerinButton[0].SAFE_SetEvent(self.ClickAutoPelerinOnButton)
			self.AutoPelerinButton[1].SAFE_SetEvent(self.ClickAutoPelerinOffButton)
			#toplama
			self.AutoToplamaButton[0].SAFE_SetEvent(self.ClickAutoToplamaOnButton)
			self.AutoToplamaButton[1].SAFE_SetEvent(self.ClickAutoToplamaOffButton)
			#Ýksir
			self.AutoPositionlButton[0].SAFE_SetEvent(self.ClickAutoPositionlOnButton)
			self.AutoPositionlButton[1].SAFE_SetEvent(self.ClickAutoPositionlOffButton)
			#Skiller
			self.AutoSkilButton[0].SAFE_SetEvent(self.ClickAutoSkilOnButton)
			self.AutoSkilButton[1].SAFE_SetEvent(self.ClickAutoSkilOffButton)
			#Yeniden Doðuþ
			self.AutoYenidenButton[0].SAFE_SetEvent(self.ClickAutoYenidenOnButton)
			self.AutoYenidenButton[1].SAFE_SetEvent(self.ClickAutoYenidenOffButton)
			#Tanrýlar
			self.AutoTanrilarButton[0].SAFE_SetEvent(self.ClickAutoTanrilarOnButton)
			self.AutoTanrilarButton[1].SAFE_SetEvent(self.ClickAutoTanrilarOffButton)
			#Start
			self.AutoStartButton[0].SAFE_SetEvent(self.ClickAutoStartOnButton)
			self.AutoStartButton[1].SAFE_SetEvent(self.ClickAutoStartOffButton)

		except:
			import exception
			exception.Abort("DuelloDialog.LoadDialog.BindObject")

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

########################### PELERÝN
	def pelerinystartfunkacja(self):
		self.pelerinystartfunkacjaczas=czas()
		self.pelerinystartfunkacjaczas.otwoz(0.5)
		self.pelerinystartfunkacjaczas.czas1(self.pelerinystartfunkacja)
		for i in xrange(90):
			a = player.GetItemIndex(i)
			if a==70038:
				net.SendItemUsePacket(i)
				break

	def pelerinystopfunkcja(self):
		self.pelerinystartfunkacjaczas=czas()
		self.pelerinystartfunkacjaczas.otwoz(100000000.0)
		self.pelerinystartfunkacjaczas.czas1(self.pelerinystartfunkacja)

	def ClickAutoPelerinOnButton(self):
		if 1 == ahmetatalayInfo.Start:
			ahmetatalayInfo.Pelerin = 1
			self.PelerinRefreshShow()
			self.pelerinystartfunkacja()
		else:
			self.ClickAutoPelerinOffButton()
			chat.AppendChat(1, "|cFF00FF00|H|h[Sistem] : Bu Özelliði Otomatik Av Baþlatmadan Kullanamassýn !")

	def ClickAutoPelerinOffButton(self):
		ahmetatalayInfo.Pelerin = 0
		self.PelerinRefreshShow()
		self.pelerinystopfunkcja()

	def PelerinRefreshShow(self):
		if ahmetatalayInfo.Pelerin == 1:
			self.AutoPelerinButton[0].Down()
			self.AutoPelerinButton[1].SetUp()
		else:
			self.AutoPelerinButton[0].SetUp()
			self.AutoPelerinButton[1].Down()
########################### PELERÝN

########################### TOPLAMA
	def ClickAutoToplamaOnButton(self):
		if 1 == ahmetatalayInfo.Start:
			ahmetatalayInfo.Toplama = 1
			self.ToplamaRefreshShow()
			player.PickCloseItem()
		else:
			self.ClickAutoToplamaOffButton()
			chat.AppendChat(1, "|cFF00FF00|H|h[Sistem] : Bu Özelliði Otomatik Av Baþlatmadan Kullanamassýn !")

	def ClickAutoToplamaOffButton(self):
		ahmetatalayInfo.Toplama = 0
		self.ToplamaRefreshShow()

	def ToplamaRefreshShow(self):
		if ahmetatalayInfo.Toplama == 1:
			self.AutoToplamaButton[0].Down()
			self.AutoToplamaButton[1].SetUp()
		else:
			self.AutoToplamaButton[0].SetUp()
			self.AutoToplamaButton[1].Down()
########################### TOPLAMA

########################### ÝKSÝR

	def autopotystartfunkacja(self):
			self.autopotystartfunkacjaczas=czas()
			self.autopotystartfunkacjaczas.otwoz(0.5)
			self.autopotystartfunkacjaczas.czas1(self.autopotystartfunkacja)
			maxhp = player.GetStatus(player.MAX_HP)
			aktualnehp = player.GetStatus(player.HP)
			if (float(aktualnehp) / float(maxhp)) * 100 < int(90):
				for i in xrange(90):
					a = player.GetItemIndex(i)
					if a==27001 or a==27002 or a==27003:
						net.SendItemUsePacket(i)
						break
			maxmp = player.GetStatus(player.MAX_SP)
			aktualnemp = player.GetStatus(player.SP)
			if (float(aktualnemp) / float(maxmp)) * 100 < int(90):
				for i in xrange(90):
					a = player.GetItemIndex(i)
					if a==27004 or a==27005 or a==27006:
						net.SendItemUsePacket(i)
						break

	def autopotystopfunkcja(self):
		self.autopotystartfunkacjaczas=czas()
		self.autopotystartfunkacjaczas.otwoz(100000000.0)
		self.autopotystartfunkacjaczas.czas1(self.autopotystartfunkacja)

	def ClickAutoPositionlOnButton(self):
		if 1 == ahmetatalayInfo.Start:
			ahmetatalayInfo.Iksir = 1
			self.autopotystartfunkacja()
			self.IksirRefreshShow()
		else:
			self.ClickAutoPositionlOffButton()
			chat.AppendChat(1, "|cFF00FF00|H|h[Sistem] : Bu Özelliði Otomatik Av Baþlatmadan Kullanamassýn !")

	def ClickAutoPositionlOffButton(self):
		ahmetatalayInfo.Iksir = 0
		self.IksirRefreshShow()
		self.autopotystopfunkcja()

	def IksirRefreshShow(self):
		if ahmetatalayInfo.Iksir == 1:
			self.AutoPositionlButton[0].Down()
			self.AutoPositionlButton[1].SetUp()
		else:
			self.AutoPositionlButton[0].SetUp()
			self.AutoPositionlButton[1].Down()

########################### ÝKSÝR

########################### Skill
	def ClickAutoSkilOnButton(self):
		if 1 == ahmetatalayInfo.Start:
			ahmetatalayInfo.Skill = 1
			self.SkillRefreshShow()
			player.ClickSkillSlot(1)
			player.ClickSkillSlot(2)
			player.ClickSkillSlot(3)
			player.ClickSkillSlot(4)
			player.ClickSkillSlot(5)
			player.ClickSkillSlot(6)
			player.ClickSkillSlot(7)
			player.ClickSkillSlot(8)
		else:
			self.ClickAutoSkilOffButton()
			chat.AppendChat(1, "|cFF00FF00|H|h[Sistem] : Bu Özelliði Otomatik Av Baþlatmadan Kullanamassýn !")

	def ClickAutoSkilOffButton(self):
		ahmetatalayInfo.Skill = 0
		self.SkillRefreshShow()

	def SkillRefreshShow(self):
		if ahmetatalayInfo.Skill == 1:
			self.AutoSkilButton[0].Down()
			self.AutoSkilButton[1].SetUp()
		else:
			self.AutoSkilButton[0].SetUp()
			self.AutoSkilButton[1].Down()
########################### Skill

########################### Yeniden Doðuþ

	def autorestartstartfunkcja(self):
		self.autorestartstartfunkcjaczas=czas()
		self.autorestartstartfunkcjaczas.otwoz(3.0)
		self.autorestartstartfunkcjaczas.czas1(self.autorestartstartfunkcja)
		maxhp=player.GetStatus(player.MAX_HP)
		aktualnehp=player.GetStatus(player.HP)
		if float(aktualnehp) / float(maxhp) * 100 < int(0):
			player.SetAttackKeyState(FALSE)
			net.SendChatPacket('/restart_here')

	def autorestartstopfunkcja(self):
		self.autorestartstartfunkcjaczas=czas()
		self.autorestartstartfunkcjaczas.otwoz(100000000.0)
		self.autorestartstartfunkcjaczas.czas1(self.autorestartstartfunkcja)

	def ClickAutoYenidenOnButton(self):
		if 1 == ahmetatalayInfo.Start:
			ahmetatalayInfo.YenidenDogus = 1
			self.YenidenRefreshShow()
			self.autorestartstartfunkcja()
		else:
			self.ClickAutoYenidenOffButton()
			chat.AppendChat(1, "|cFF00FF00|H|h[Sistem] : Bu Özelliði Otomatik Av Baþlatmadan Kullanamassýn !")

	def ClickAutoYenidenOffButton(self):
		ahmetatalayInfo.YenidenDogus = 0
		self.YenidenRefreshShow()
		self.autorestartstopfunkcja()

	def YenidenRefreshShow(self):
		if ahmetatalayInfo.YenidenDogus == 1:
			self.AutoYenidenButton[0].Down()
			self.AutoYenidenButton[1].SetUp()
		else:
			self.AutoYenidenButton[0].SetUp()
			self.AutoYenidenButton[1].Down()
########################### Yeniden Doðuþ

########################### Tanrýlar

	def dopalaczestartfunkcja(self):
		global tanrisure
		self.dopalaczestartfunkcjaczas=czas()
		self.dopalaczestartfunkcjaczas.otwoz(180.0)
		self.dopalaczestartfunkcjaczas.czas1(self.dopalaczestartfunkcja)
		tanrisure+=1
		if tanrisure == 500:
			for i in xrange(90):
				a = player.GetItemIndex(i)
				if a == 71027 or a == 71028 or a == 71029 or a == 71030 or a== 71031 or a== 71044 or a== 71045:
					net.SendItemUsePacket(i)
					tanrisure=0
					# break

	def dopalaczestopfunkcja(self):
		self.dopalaczestartfunkcjaczas=czas()
		self.dopalaczestartfunkcjaczas.otwoz(100000000.0)
		self.dopalaczestartfunkcjaczas.czas1(self.dopalaczestartfunkcja)

	def ClickAutoTanrilarOnButton(self):
		if 1 == ahmetatalayInfo.Start:
			ahmetatalayInfo.Tanrilar = 1
			self.TanrilarRefreshShow()
			self.dopalaczestartfunkcja()
		else:
			self.ClickAutoTanrilarOffButton()
			chat.AppendChat(1, "|cFF00FF00|H|h[Sistem] : Bu Özelliði Otomatik Av Baþlatmadan Kullanamassýn !")

	def ClickAutoTanrilarOffButton(self):
		ahmetatalayInfo.Tanrilar = 0
		self.TanrilarRefreshShow()
		self.dopalaczestopfunkcja()

	def TanrilarRefreshShow(self):
		if ahmetatalayInfo.Tanrilar == 1:
			self.AutoTanrilarButton[0].Down()
			self.AutoTanrilarButton[1].SetUp()
		else:
			self.AutoTanrilarButton[0].SetUp()
			self.AutoTanrilarButton[1].Down()
########################### Tanrýlar

########################### BAÞLAT
	def lvlbotstartfunkcja(self):
		global dokoftowaniewida
		self.lvlbotstartfunkcjaczas=czas()
		self.lvlbotstartfunkcjaczas.otwoz(2.0)
		self.lvlbotstartfunkcjaczas.czas1(self.lvlbotstartfunkcja)
		player.SetAttackKeyState(FALSE)
		o=player.GetMainCharacterIndex()
		dokoftowaniewida=dokoftowaniewida+5
		c=0
		for i in xrange(o-20000+dokoftowaniewida, o+200000+dokoftowaniewida):
			if chr.IsEnemy(i):
				dystans = player.GetCharacterDistance(i) 
				if dystans > 0 and dystans < 4000:
					if c==0:
						dystans2=dystans
						c=1
						a=i
						player.SetTarget(a)
						x, y, z = chr.GetPixelPosition(a)
						chr.MoveToDestPosition(o, int(x), int(y))
					if dystans2 > dystans:
						a=i
						dystans2=dystans
						player.SetTarget(a)
						x, y, z = chr.GetPixelPosition(a)
						chr.MoveToDestPosition(o, int(x), int(y))
					if dystans < 200:
						player.SetTarget(i)
						chr.SelectInstance(o)
						player.SetAttackKeyState(TRUE)
						x, y, z = chr.GetPixelPosition(a)
						chr.MoveToDestPosition(o, int(x), int(y))
						rnd = app.GetRandom(0, 3)
						chr.SetDirection(rnd)
						break

	def lvlbotstopfunkcja(self):
		global dokoftowaniewida
		dokoftowaniewida=0
		self.lvlbotstartfunkcjaczas=czas()
		self.lvlbotstartfunkcjaczas.otwoz(100000000.0)
		self.lvlbotstartfunkcjaczas.czas1(self.lvlbotstartfunkcja)
		player.SetAttackKeyState(FALSE)

	def ClickAutoStartOnButton(self):
		net.SendChatPacket("/otomatikav_komut2")
		if 1 == ahmetatalayInfo.Start:
			self.lvlbotstartfunkcja()
			ahmetatalayInfo.Start = 1
			self.StartRefreshShow()
		else:
			self.ClickAutoStartOffButton()
			ahmetatalayInfo.Start = 0
			self.StartRefreshShow()

	def ClickAutoStartOffButton(self):
		ahmetatalayInfo.Start = 0
		self.ClickAutoPelerinOffButton()
		self.ClickAutoPositionlOffButton()
		self.ClickAutoSkilOffButton()
		self.ClickAutoTanrilarOffButton()
		self.ClickAutoToplamaOffButton()
		self.ClickAutoYenidenOffButton()
		self.StartRefreshShow()
		self.lvlbotstopfunkcja()

	def StartRefreshShow(self):
		if ahmetatalayInfo.Start == 1:
			self.AutoStartButton[0].Down()
			self.AutoStartButton[1].SetUp()
		else:
			self.AutoStartButton[0].SetUp()
			self.AutoStartButton[1].Down()
########################### BAÞLAT

class czas(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def otwoz(self, waitTime):
		curTime = time.clock()
		self.endTime = curTime + waitTime
		self.Show()

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

	def czas1(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def OnUpdate(self):
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			return None
		return None

	def OnPressExitKey(self):
		self.Close()
		return TRUE