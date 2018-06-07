# -*- coding: utf-8 -*
#import
import win32api
import win32con
import time
#可调参数_pushSleepTime
#def
def _pushSleepTime():
	time.sleep(0.09)

def pushW():
		#W=87 S=83 A=65 D=68 V=86 Space=32
	win32api.keybd_event(87,0,0,0)
	_pushSleepTime()
	win32api.keybd_event(87,0,win32con.KEYEVENTF_KEYUP,0)
def pushS():
	win32api.keybd_event(83,0,0,0)
	_pushSleepTime()
	win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0)
def pushA():
	win32api.keybd_event(65,0,0,0)
	_pushSleepTime()
	win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)
def pushD():
	win32api.keybd_event(68,0,0,0)
	_pushSleepTime()
	win32api.keybd_event(68,0,win32con.KEYEVENTF_KEYUP,0)
def pushSpace():
	win32api.keybd_event(32,0,0,0)
	_pushSleepTime()
	win32api.keybd_event(32,0,win32con.KEYEVENTF_KEYUP,0)
def pushV():
	win32api.keybd_event(86,0,0,0)
	_pushSleepTime()
	win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)
###touch###
def touchW():
		#W=87 S=83 A=65 D=68 V=86 Space=32
	win32api.keybd_event(87,0,0,0)
	win32api.keybd_event(87,0,win32con.KEYEVENTF_KEYUP,0)
def touchS():
	win32api.keybd_event(83,0,0,0)
	win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0)
def touchA():
	win32api.keybd_event(65,0,0,0)
	win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)
def touchD():
	win32api.keybd_event(68,0,0,0)
	win32api.keybd_event(68,0,win32con.KEYEVENTF_KEYUP,0)
def touchSpace():
	win32api.keybd_event(32,0,0,0)
	win32api.keybd_event(32,0,win32con.KEYEVENTF_KEYUP,0)
def touchV():
	win32api.keybd_event(86,0,0,0)
	win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)
