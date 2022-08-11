### Imports ###
import sys
import hashlib
import os

### Global Colors ###
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


### Functions ###
def menu():
	os.system('clear')
	print(bcolors.HEADER + bcolors.BOLD)
	print("__________        ___________                       .___            ")
	print("\______   \___.__.\_   _____/ ____   ____  ____   __| _/___________ ")
	print(" |     ___<   |  | |    __)_ /    \_/ ___\/  _ \ / __ |/ __ \_  __ \ ")
	print(" |    |    \___  | |        \   |  \  \__(  <_> ) /_/ \  ___/|  | \/")
	print(" |____|    / ____|/_______  /___|  /\___  >____/\____ |\___  >__|   ")
	print("           \/             \/     \/     \/           \/    \/       ")
	print(bcolors.ENDC + bcolors.BOLD)
	print("                         -----== v1.0 ==-----      ")
	print("                               by: Kain            ")
	print("\n")
	print("                             [{}01{}{}] MD5      ".format(bcolors.HEADER,bcolors.ENDC,bcolors.BOLD))
	print("                             [{}02{}{}] SHA1     ".format(bcolors.HEADER,bcolors.ENDC,bcolors.BOLD))
	print("                             [{}03{}{}] SHA256   ".format(bcolors.HEADER,bcolors.ENDC,bcolors.BOLD))
	print("                             [{}04{}{}] SHA512   ".format(bcolors.HEADER,bcolors.ENDC,bcolors.BOLD))
	print("")
	option = int(input(bcolors.WARNING + "{}{}[{}{}*{}{}] {}{}Select Option: {}".format(bcolors.ENDC,bcolors.BOLD,bcolors.HEADER,bcolors.BOLD,bcolors.ENDC,bcolors.BOLD,bcolors.HEADER,bcolors.BOLD,bcolors.ENDC)))
	print("")

	# Option Checker
	if option == 1:
		md5()
	elif option == 2:
		sha1()
	elif option == 3:
		sha256()
	elif option == 4:
		sha512()
	else:
		print('error')

def md5():
	message = input("{}{}[{}{}MD5{}{}] Text to be encoded: {}".format(bcolors.ENDC,bcolors.BOLD,bcolors.HEADER,bcolors.BOLD,bcolors.ENDC,bcolors.BOLD,bcolors.ENDC))
	md5 = hashlib.md5(message.encode())
	print("{}{}[{}{}+{}{}]{} ".format(bcolors.ENDC,bcolors.BOLD,bcolors.HEADER,bcolors.BOLD,bcolors.ENDC,bcolors.BOLD,bcolors.OKGREEN) + md5.hexdigest(),"\n")
	loop()

def sha1():
	message = input("{}{}[{}{}SHA1{}{}] Text to be encoded: {}".format(bcolors.ENDC,bcolors.BOLD,bcolors.HEADER,bcolors.BOLD,bcolors.ENDC,bcolors.BOLD,bcolors.ENDC))
	sha = hashlib.sha1(message.encode())
	print("{}{}[{}{}+{}{}]{} ".format(bcolors.ENDC,bcolors.BOLD,bcolors.HEADER,bcolors.BOLD,bcolors.ENDC,bcolors.BOLD,bcolors.OKGREEN) + sha.hexdigest(),"\n")
	loop()

def sha256():
	message = input("{}{}[{}{}SHA256{}{}] Text to be encoded: {}".format(bcolors.ENDC,bcolors.BOLD,bcolors.HEADER,bcolors.BOLD,bcolors.ENDC,bcolors.BOLD,bcolors.ENDC))
	sha = hashlib.sha256(message.encode())
	print("{}{}[{}{}+{}{}]{} ".format(bcolors.ENDC,bcolors.BOLD,bcolors.HEADER,bcolors.BOLD,bcolors.ENDC,bcolors.BOLD,bcolors.OKGREEN) + sha.hexdigest(),"\n")
	loop()

def sha512():
	message = input("{}{}[{}{}SHA512{}{}] Text to be encoded: {}".format(bcolors.ENDC,bcolors.BOLD,bcolors.HEADER,bcolors.BOLD,bcolors.ENDC,bcolors.BOLD,bcolors.ENDC))
	sha = hashlib.sha512(message.encode())
	print("{}{}[{}{}+{}{}]{} ".format(bcolors.ENDC,bcolors.BOLD,bcolors.HEADER,bcolors.BOLD,bcolors.ENDC,bcolors.BOLD,bcolors.OKGREEN) + sha.hexdigest(),"\n")
	loop()

def loop():
	again = input("\n{}{}[{}{}!{}{}] Encode again? [y/n]: {}".format(bcolors.ENDC,bcolors.BOLD,bcolors.HEADER,bcolors.BOLD,bcolors.ENDC,bcolors.BOLD,bcolors.ENDC))
	if again == "y":
		menu()
	elif again == "n":
		pass
menu()
