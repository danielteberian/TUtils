import os

#command = input("Welcome to TUtils. Enter a command: ")

#if command() == "help"(
 #  print("help")
#)


welcomemsg = str("WELCOME TO TUTILS v0.0.1")
print(str(welcomemsg))

cmd = input("TYPE 'help' TO LIST AVAILABLE COMMANDS.\nEnter a command: ")

if str(cmd) == ("help"):
   print('### Available Commands\n HELP: Displays this menu.')
else:
   print('Command not recognized.')


#echo = input("Enter a word/string to be echoed: ")
#print(str(echo))
