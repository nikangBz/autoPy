#文件关系如下
#主文件-挂机场景文件-地点设置 - 按键设置
#					-战斗设置
#main-scenes-stepBack	- push
#			-stepBattle -
#可调参数	使用技能,场景地点编号,在场景战斗时间
#深度参数	secenes：脱离战斗时间_stepInitTime，场景切换时间_stepBlackTime
#		 	push: 按键push时间
#import
import scenes
import time
#main
time.sleep(2)
while True:
	#scenesFromBattle(使用技能,场景地点编号,在场景战斗时间)
	#scenesFromHome(stepBattleN,stepBackN,battleTimeN):
	scenes.scenesFromBattle(10004,10001,60)
	#scenes.scenesFromHome(10004,10001,60)



	