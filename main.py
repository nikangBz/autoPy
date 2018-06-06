#文件关系如下
#主文件-挂机场景文件-地点设置 - 按键设置
#					-战斗设置
#main-scenes-stepBack	- push
#			-stepBattle -

#import
import scenes
import time
#main
time.sleep(2)
while True:
	#scenesFromBattle(stepBattleN,stepBackN,battleTimeN)
	#scenesFromHome(stepBattleN,stepBackN,battleTimeN):
	#scenes.scenesFromBattle(10001,10001,2)
	scenes.scenesFromHome(10001,10001,2)



	