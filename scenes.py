# -*- coding: utf-8 -*
import stepBack
import stepBattle

#1-战斗位置
# 	stepBack.stepBackHome(N)
# 	stepBack.stepBackBattle(N)

#2-战斗方式
# 	stepBattle.stepBattle(N)

def scenesFromBattle(stepBattleN,stepBackN,battleTimeN):
	#战斗
	#回家
	#回战场
	i = 0 
	while i <1000:
		print(i)
		stepBattle.stepBattle(stepBattleN)
		i+=1
		if i == battleTimeN :
			stepBack.stepBackHome(stepBackN)
			stepBack.stepBackBattle(stepBackN)
			i = 0

def scenesFromHome(stepBattleN,stepBackN,battleTimeN):
	stepBack.stepBackBattle(stepBackN)
	i = 0 
	while i <1000:
		print(i)
		stepBattle.stepBattle(stepBattleN)
		i+=1
		if i == battleTimeN :
			stepBack.stepBackHome(stepBackN)
			stepBack.stepBackBattle(stepBackN)
			i = 0

	
