# -*- coding: utf-8 -*
#import
import push
import time

#走N步路
def _runN(func,N):
	i = 0
	while i<N:
		func()
		i+=1
############
def _stepBattle10001():
	print("使用技能 “1” 进行战斗")
	_runN(push.pushD,4)
	time.sleep(0.1)
	_runN(push.pushA,4)
	time.sleep(0.1)
	push.touchSpace()
	push.touchSpace()
def _stepBattle10002():
	print("使用技能 “2” 进行战斗")
	_runN(push.pushD,4)
	time.sleep(0.1)
	_runN(push.pushA,4)
	time.sleep(0.1)
	push.touchSpace()
	push.touchD()
	push.touchSpace()
def _stepBattle10003():
	print("使用技能 “3” 进行战斗")
	_runN(push.pushD,4)
	time.sleep(0.1)
	_runN(push.pushA,4)
	time.sleep(0.1)
	push.touchSpace()
	push.touchS()
	push.touchSpace()
def _stepBattle10004():
	print("使用技能 “4” 进行战斗")
	_runN(push.pushD,4)
	time.sleep(0.1)
	_runN(push.pushA,4)
	time.sleep(0.1)
	push.touchSpace()
	push.touchD()
	push.touchS()
	push.touchSpace()
def stepBattle(N):
	if   N == 10001:
		_stepBattle10001()
	elif N == 10002:
		_stepBattle10002()
	elif N == 10003:
		_stepBattle10003()
	elif N == 10004:
		_stepBattle10004()



