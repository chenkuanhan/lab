import os
import time
os.system("adb shell 'getevent -lt | grep -i BTN_TOUCH'")
for i in range(500):
	os.system("adb shell input tap 851 2340")
	time.sleep(1)
