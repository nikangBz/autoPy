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
	#右 左 空格 空格
	push.pushD()
	time.sleep(0.1)
	push.pushA()
	time.sleep(0.1)
	push.touchSpace()
	push.touchSpace()
def stepBattle(N):
	if N == 10001:
		_stepBattle10001()


