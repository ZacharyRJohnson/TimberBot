import time
from ctypes import windll
import win32com.client as comclt
import win32api as winap
import win32con

wsh = comclt.Dispatch("WScript.Shell")
hdc = windll.user32.GetDC(0)

def click(x, y):
    winap.SetCursorPos((x,y))
    winap.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    winap.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def getPixel(x, y):
    return windll.gdi32.GetPixel(hdc, x, y)

def pressRight():
    wsh.SendKeys("{RIGHT}")
    time.sleep(.05)

def pressLeft():
    wsh.SendKeys("{LEFT}")
    time.sleep(.05)

def start():
    click(-(1920//2), 950) #location of play button
    time.sleep(1)

def run():
    side = 1 #character starts on right when game is refreshed
    for i in range(300):
        if(side):
            twoAbovePlayer = getPixel(-920, 620)
            if(twoAbovePlayer == 16775123 or twoAbovePlayer == 16380103):
                pressRight()
            else:
                pressRight()
                pressLeft()
                side = 0
            print(twoAbovePlayer)
        else:
            twoAbovePlayer = getPixel(-1020, 620)
            if(twoAbovePlayer == 16775123 or twoAbovePlayer == 16380103):
                pressLeft()
            else:
                pressLeft()
                pressRight()
                side = 1
            print(twoAbovePlayer)
        time.sleep(.12)
        
    
    

start()
#click(-920, 620)
run()
"""
rgb = getPixel(-920, 675)
r = rgb & 0xff
g = (rgb >> 8) & 0xff
b = (rgb >> 16) & 0xff
print("RGB(%d, %d, %d)" % (r, g, b))
print(rgb)
"""
