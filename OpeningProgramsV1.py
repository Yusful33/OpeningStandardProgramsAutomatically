
import webbrowser
import os
import subprocess
import time 
import pyautogui
import cv2
#   
#   #Opens email
url = 'https://mail.google.com/mail/u/0/#inbox'
a_website = 'https://www.wsj.com'
##   # Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
##   
webbrowser.get(chrome_path).open(url)
webbrowser.open_new_tab(a_website)
time.sleep(3)
#
##Opens Outlook, Skype, Pulse, SAS, SecureFX
subprocess.Popen([r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"]) 
time.sleep(3)
subprocess.Popen([r"C:\Program Files\Microsoft Office\root\Office16\lync.EXE"]) 
time.sleep(3)
#Display current mouse position
import pyautogui
pyautogui.position()
#Can click at (x=685,y=1063 to open pulse)
#This Opens Pulse
pyautogui.moveTo(685,1063)

#Trying to click on a specific image but this didnt work
#image = pyautogui.locateOnScreen(r'C:\Users\ycattaneo\AppData\Local\Programs\Python\Python37-32\Scripts\pulse.png', grayscale=True)
#time.sleep(2)
#if image is None:
#    print('Image not found on the screen!')
#else:
#    pyautogui.click(image)

#Clicks on the Pulse App
pyautogui.click(685, 1063, clicks=2, interval=0.1, button='left')
time.sleep(1)
##Need to click at Point(x=938, y=587)
pyautogui.moveTo(938,587)
pyautogui.click(x=938, y=587, clicks=1, interval=0.1, button='left')
time.sleep(1)
code = '418724'
pyautogui.typewrite(code)  
pyautogui.press('enter')
time.sleep(4)
#Opening SE Guide
pyautogui.moveTo(778,1050)
pyautogui.click(x=778, y=1050, clicks=2, interval=0.1, button='left')
time.sleep(3)
pyautogui.press('enter') 
time.sleep(3)
#This is for once SE Guide is open 
pyautogui.moveTo(798,345)
pyautogui.click(x=938, y=587, clicks=1, interval=0.1, button='left')
time.sleep(1)
pyautogui.moveTo(1408,286)
pyautogui.click(x=1408, y=286, clicks=1, interval=0.1, button='left')
pyautogui.press('enter') 
time.sleep(1)
pyautogui.press('enter') 
time.sleep(1)
pyautogui.press('enter') 
time.sleep(1)
#Opening Documents
pyautogui.moveTo(21,533)
pyautogui.click(x=21, y=533, clicks=1, interval=0.1, button='left')

#This is used for opening Secure FX
subprocess.Popen([r"C:\Program Files\SASHome\SASEnterpriseGuide\7.1\SEGuide.EXE"]) 
time.sleep(3
