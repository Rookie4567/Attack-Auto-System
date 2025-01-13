#CODED BY AHMET ATALAY
import uiScriptLocale
import item
import app
import localeInfo

BOARD_WIDTH = 200
BOARD_HIGHT = 600
BAR_WIDTH = 400
GOLD_COLOR	= 0xFFFEE3AE
#CODED BY AHMET ATALAY
window = {
	"name" : "AutoWindow",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HIGHT,
			
			"title" : "Otomatik Av",
		
			"children" :
			(
				## ¾×Æ¼ºê ½ºÅ³¼ÂÆÃ.Bar
				{
					"name" : "HorizontalBar1",
					"type" : "horizontalbar",
					"x" : 20,
					"y" : 40,
					"width" : BAR_WIDTH / 2 -40,

					"children":
					(
						## ¾×Æ¼ºê ½ºÅ³¼ÂÆÃ Text
						{
							"name" : "BaseInfo", "type" : "text", "x" : 8, "y" : 2, "text" : "Beceriler",
						},
						## AutoSkillClearButton
						{
							"name" : "AutoSkillClearButton",
							"type" : "button",

							"x" : BOARD_WIDTH/2+30,
							"y" : 0,

							"text" : "Boþalt",

							"default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
						},
					),
				},
				## ¾×Æ¼ºê ½ºÅ³ ¼ÂÆÃ Slot
				{
					"name" : "Auto_Active_Skill_Slot_Table",
					"type" : "slot",

					"x" : 25,
					"y" : 65,

					"width" : 200,
					"height" : 400,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub",

					"slot" :	(
									## Active SKill
									{"index": 0, "x": 1,"y":  4, "width":32, "height":32},
									{"index": 1, "x":38+3,"y":  4, "width":32, "height":32},
									{"index": 2, "x":75+6,"y":  4, "width":32, "height":32},
									{"index": 3, "x":113+8,"y":  4, "width":32, "height":32},
									{"index": 4, "x": 1,"y": 70, "width":32, "height":32},
									{"index": 5, "x":38+3,"y": 70, "width":32, "height":32},
									{"index": 6, "x":75+6,"y": 70, "width":32, "height":32},
									{"index": 7, "x":113+8,"y": 70, "width":32, "height":32},
									## Position
									{"index": 9, "x": 1,"y":  170, "width":32, "height":32},
									{"index": 10, "x":38+3,"y":  170, "width":32, "height":32},
									{"index": 11, "x":75+6,"y":  170, "width":32, "height":32},
									{"index": 12, "x":113+8,"y":  170, "width":32, "height":32},
									{"index": 13, "x": 1,"y": 240, "width":32, "height":32},
									{"index": 14, "x":38+3,"y": 240, "width":32, "height":32},
									{"index": 15, "x":75+6,"y": 240, "width":32, "height":32},
									{"index": 16, "x":113+8,"y": 240, "width":32, "height":32},
								),

				},
				# editline Ãß°¡.
				# Line1
				{
					"name" : "cool_time_Image0", "type" : "image", "x" : 22, "y" : 108,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline0", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				{
					"name" : "cool_time_Image1", "type" : "image", "x" : 22+40, "y" : 108,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline1", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				{
					"name" : "cool_time_Image2", "type" : "image", "x" : 22+80, "y" : 108,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline2", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				{
					"name" : "cool_time_Image3", "type" : "image", "x" : 22+120, "y" : 108,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline3", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				# Line2
				{
					"name" : "cool_time_Image4", "type" : "image", "x" : 22, "y" : 108+66,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline4", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				{
					"name" : "cool_time_Image5", "type" : "image", "x" : 22+40, "y" : 108+66,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline5", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				{
					"name" : "cool_time_Image6", "type" : "image", "x" : 22+80, "y" : 108+66,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline6", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				{
					"name" : "cool_time_Image7", "type" : "image", "x" : 22+120, "y" : 108+66,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline7", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				# Line3
				{
					"name" : "cool_time_Image8", "type" : "image", "x" : 22, "y" : 108+(66*2)+35,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline8", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				{
					"name" : "cool_time_Image9", "type" : "image", "x" : 22+40, "y" : 108+(66*2)+35,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline9", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				{
					"name" : "cool_time_Image10", "type" : "image", "x" : 22+80, "y" : 108+(66*2)+35,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline10", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				{
					"name" : "cool_time_Image11", "type" : "image", "x" : 22+120, "y" : 108+(66*2)+35,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline11", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				
				# Line4
				{
					"name" : "cool_time_Image12", "type" : "image", "x" : 22, "y" : 108+(66*3)+38,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline12", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				{
					"name" : "cool_time_Image13", "type" : "image", "x" : 22+40, "y" : 108+(66*3)+38,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline13", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				{
					"name" : "cool_time_Image14", "type" : "image", "x" : 22+80, "y" : 108+(66*3)+38,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline14", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				{
					"name" : "cool_time_Image15", "type" : "image", "x" : 22+120, "y" : 108+(66*3)+38,
					"image" : "d:/ymir work/ui/public/parameter_slot_00.sub",
					"children":
					(
						{
						"name" : "editline15", "type" : "editline","x" : 3, "y" : 3,
						"input_limit" : 4, "only_number" : 1, "width" : 90, "height" : 20,
						},
					),
				},
				## ¹°¾à ¼ÂÆÃ.Bar
				{#CODED BY AHMET ATALAY
					"name" : "HorizontalBar1",
					"type" : "horizontalbar",
					"x" : 20,
					"y" : 210,
					"width" : BAR_WIDTH / 2 -40,

					"children":#CODED BY AHMET ATALAY
					(
						## ¾×Æ¼ºê ½ºÅ³¼ÂÆÃ Text
						{
							"name" : "BaseInfo", "type" : "text", "x" : 8, "y" : 2, "text" : "Ýksirler",
						},				
						## AutoPositionClearButton
						{
							"name" : "AutoPositionClearButton",
							"type" : "button",

							"x" : BOARD_WIDTH/2+30,
							"y" : 0,

							"text" : "Boþalt",

							"default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
						},
					),
				},
				## ¼³Á¤ Bar #CODED BY AHMET ATALAY
				{
					"name" : "HorizontalBar1",
					"type" : "horizontalbar",
					"x" : 20,
					"y" : 370,
					"width" : BAR_WIDTH / 2-40,
				
					"children":
					(#CODED BY AHMET ATALAY
						## ¼ÂÆÃ Text
						{ "name" : "BaseInfo", "type" : "text", "x" : 8, "y" : 2, "text" : "Ayarlar", },
						{ "name" : "BaseInfo", "type" : "text", "x" : 1, "y" : 25, "text" : "Pelerin", },
						{ "name" : "BaseInfo", "type" : "text", "x" : 1, "y" : 45, "text" : "Toplama", },
						{ "name" : "BaseInfo", "type" : "text", "x" : 1, "y" : 65, "text" : "Ýksirler", },
						{ "name" : "BaseInfo", "type" : "text", "x" : 1, "y" : 85, "text" : "Skiller", },
						{ "name" : "BaseInfo", "type" : "text", "x" : 1, "y" : 105, "text" : "Y.Doðuþ ", },
						{ "name" : "BaseInfo", "type" : "text", "x" : 1, "y" : 125, "text" : "Tanrýlar ", },
						## AutoAllClearButton
						{
							"name" : "AutoAllClearButton",
							"type" : "button",

							"x" : BOARD_WIDTH/2+30,
							"y" : 0,

							"text" : "Boþalt",

							"default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
						},#CODED BY AHMET ATALAY
					),#CODED BY AHMET ATALAY
				},
				## Pelerin Sistemi ON
				{#CODED BY AHMET ATALAY
					"name" : "AutoPelerinOnButton",
					"type" : "radio_button",

					"x" : 90,
					"y" : 320+23+50,

					"text" : "Açýk",

					"default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
				},#CODED BY AHMET ATALAY
				##  Pelerin Sistemi OFF #CODED BY AHMET ATALAY
				{
					"name" : "AutoPelerinOffButton",
					"type" : "radio_button",

					"x" : 90+45,
					"y" : 320+23+50,

					"text" : "Kapalý",

					"default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
				},
				## Toplama Sistemi ON #CODED BY AHMET ATALAY
				{
					"name" : "AutoToplamaOnButton",
					"type" : "radio_button",

					"x" : 90,
					"y" : 320+43+50,

					"text" : "Açýk",

					"default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
				},
				## Toplama Sistemi OFF #CODED BY AHMET ATALAY 
				{
					"name" : "AutoToplamaOffButton",
					"type" : "radio_button",

					"x" : 90+45,
					"y" : 320+43+50,

					"text" : "Kapalý",

					"default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
				},
				## Ýksirler on Button #CODED BY AHMET ATALAY
				{
					"name" : "AutoPositionlOnButton",
					"type" : "radio_button",

					"x" : 90,
					"y" : 320+63+50,

					"text" : "Açýk",

					"default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
				},
				## iksirler off Button #CODED BY AHMET ATALAY
				{
					"name" : "AutoPositionlOffButton",
					"type" : "radio_button",

					"x" : 90+45,
					"y" : 320+63+50,

					"text" : "Kapalý",

					"default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
				},				
				## Skiller Açýk Buton #CODED BY AHMET ATALAY
				{
					 "name" : "AutoSkilOnButton",
					 "type" : "radio_button",

					 "x" : 90,
					 "y" : 320+83+50,

					 "text" : "Açýk",

					 "default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
					 "over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
					 "down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
				},
				# Skiller Kapalý Buton #CODED BY AHMET ATALAY
				{
					 "name" : "AutoSkilOffButton",
					 "type" : "radio_button",

					 "x" : 90+45,
					 "y" : 320+83+50,

					 "text" : "Kapalý",

					 "default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
					 "over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
					 "down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
				},
				## Yeniden doðuþ Açýk Buton #CODED BY AHMET ATALAY
				{
					 "name" : "AutoYenidenOnButton",
					 "type" : "radio_button",

					 "x" : 90,
					 "y" : 320+103+50,

					 "text" : "Açýk",

					 "default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
					 "over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
					 "down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
				},
				# yeniden doðuþ Kapalý Buton #CODED BY AHMET ATALAY
				{
					 "name" : "AutoYenidenOffButton",
					 "type" : "radio_button",

					 "x" : 90+45,
					 "y" : 320+103+50,

					 "text" : "Kapalý",

					 "default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
					 "over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
					 "down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
				},
				## Ejderha Tanrýlarý Açýk Buton #CODED BY AHMET ATALAY
				{
					 "name" : "AutoEjderhaOnButton",
					 "type" : "radio_button",

					 "x" : 90,
					 "y" : 320+123+50,

					 "text" : "Açýk",

					 "default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
					 "over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
					 "down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
				},
				#  Ejderha Tanrýlarý Kapalý Buton #CODED BY AHMET ATALAY
				{
					 "name" : "AutoEjderhaOffButton",
					 "type" : "radio_button",

					 "x" : 90+45,
					 "y" : 320+123+50,

					 "text" : "Kapalý",

					 "default_image" : "d:/ymir work/ui/public/Small_Button_01.sub",
					 "over_image" : "d:/ymir work/ui/public/Small_Button_02.sub",
					 "down_image" : "d:/ymir work/ui/public/Small_Button_03.sub",
				},
				## Baþlatma Butonu #CODED BY AHMET ATALAY
				{
					"name" : "AutoStartOnButton",
					"type" : "radio_button",

					"x" : 60,
					"y" : 500+50+10,

					"text" : "Baþla",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				# Durdurma Butonu #CODED BY AHMET ATALAY
				{
					"name" : "AutoStartOffButton",
					"type" : "radio_button",

					"x" : 125,
					"y" : 500+50+10,

					"text" : "Dur",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				## AutoToolTip Button
				{
					"name" : "AutoToolTIpButton",
					"type" : "button",

					"x" : 155,
					"y" : 8,

					"default_image" : "d:/ymir work/ui/pattern/q_mark_01.tga",
					"over_image" : "d:/ymir work/ui/pattern/q_mark_02.tga",
					"down_image" : "d:/ymir work/ui/pattern/q_mark_01.tga",
				},					
			),
		},
	),
}
#CODED BY AHMET ATALAY
#CODED BY AHMET ATALAY
#CODED BY AHMET ATALAY
#CODED BY AHMET ATALAY