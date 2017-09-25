# usr/bin/env python3
import win32clipboard as w
import win32con
import os

def getText():
	w.OpenClipboard()
	# d = w.GetClipboardData(win32con.CF_TEXT)
	d = w.GetClipboardData()
	w.CloseClipboard()
	return d

def setText(aString):
	w.OpenClipboard()
	w.EmptyClipboard()
	w.SetClipboardData(win32con.CF_TEXT, aString)
	w.CloseClipboard()

with open('clipboard.txt','a') as f:
	content = getText()
	f.write("\r\n")
	f.write(content)
	f.write("\r\n")

os_command = "notepad.exe clipboard.txt"
os.system(os_command)
