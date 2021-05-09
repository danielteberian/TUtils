import os

cmd = input("TUtils: ")

if str(cmd) == ("help"):
   print('\n\n\n### Available Commands\nHELP: Displays this menu.\nLIST: Lists all files and subdirectories in current directory.')

if str(cmd) == ('list'):
   print(lsdir)

if str(cmd) == ('version'):
   print("TUtils - v0.0.2\nCopyright 2021, Daniel P. Teberian. All rights reserved.")
