import pyautogui

from tkinter import filedialog

file = input("File name: ")

filedirectory = filedialog.askdirectory()

va=pyautogui.screenshot()

va.save(r''+filedirectory+'/'+file+'.png')
