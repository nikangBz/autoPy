#import
import push
import time
#def 
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
	time.sleep(10)
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
#time设置
	#切换场景time
def _stepBlackTime():
	time.sleep(5)
#来回设置
def _stepBackHome10001():
		#脱离战斗
		_stepSleepInit()
		#往回走
		_runN(pushS,4)
		_stepBlackTime()
		_runN(pushA,20)
		_runN(pushW,4)
		_stepBlackTime()
		_runN(pushW,20)
		_stepPC()
def _stepBackBattle10001():
		_runN(pushS,18)
		_stepBlackTime()
		_runN(pushD,20)
		_runN(pushW,4)
##############		


def stepBackHome(N):
	if N == 10001:
		_stepBackHome10001()
		
def stepBackBattle(N):
	if N == 10001:
		_stepBackBattle10001()

