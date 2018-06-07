# -*- coding: utf-8 -*
#import
import push
import time
#def 
#可调参数：脱离战斗时间_stepInitTime，场景切换时间_stepBlackTime
#time设置
	#切换场景time
def _stepBlackTime():
	time.sleep(8)
def _stepInitTime():
	time.sleep(15)
#保证脱离战斗
def _stepSleepInitModule():
	
	time.sleep(1)
	push.touchD()
	time.sleep(0.1)
	push.touchS()
	time.sleep(0.1)
	push.pushSpace()
	push.pushSpace()
def _stepSleepInit():
	_stepSleepInitModule()
	_stepInitTime()
	_stepSleepInitModule()
	
#走N步路
def _runN(func,N):
	i = 0
	while i<N:
		func()
		i+=1
#小精灵PC治疗
def _stepPC():
		
		time.sleep(2)
		push.pushSpace()
		time.sleep(4)
		push.pushSpace()
		time.sleep(4)
		push.pushSpace()
		time.sleep(4)
		push.pushSpace()
		time.sleep(4)
		push.pushSpace()
		

#来回设置
def _stepBackHome10001():
		#脱离战斗
		print("正在脱离战斗...")
		_stepSleepInit()
		print("正在矫正位置...")
		#矫正位置
		_runN(push.pushD,20)
		_stepSleepInit()
		_runN(push.pushD,20)
		_runN(push.pushA,4)
		_stepSleepInit()
		print("脱离战斗！")
		#往回走
		print("正在返回PC宠物中心...")
		_runN(push.pushS,4)
		_stepBlackTime()
		_runN(push.pushA,20)
		_runN(push.pushW,4)
		_stepBlackTime()
		print("返回PC宠物中心！")
		_runN(push.pushW,20)
		print("正在对宠物进行治疗...")
		_stepPC()
		print("宠物治疗结束！")
def _stepBackBattle10001():
		print("正在返回战场...")
		_runN(push.pushS,20)
		_stepBlackTime()
		_runN(push.pushD,20)
		_runN(push.pushW,4)
		_stepBlackTime()
		print("返回战场!")
##############		


def stepBackHome(N):
	if N == 0:
		pass
	if N == 10001:
		_stepBackHome10001()
		
def stepBackBattle(N):
	if N == 0:
		pass
	if N == 10001:
		_stepBackBattle10001()

