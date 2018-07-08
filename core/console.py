import os
import sys
import time

""" colors code ascii """
R = '\x1b[1;31m'
G = '\x1b[1;32m'
B = '\x1b[1;34m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'
HB = '\x1b[1;38;5;32m'
D = '\x1b[0m'

def set_windowTitle(title):
	set_title = "echo -ne '\e]0;%s\007'" % str(title)
	os.system('clear')
	os.system(set_title)
	
def slow_print(char):
	for c in char + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1.0/95)
		
def Banner():
	print('')
	slow_print('('+R+'R'+D+')'+'ivest')
	slow_print('('+G+'S'+D+')'+'hamir'+'          RSA-Encryption')
	slow_print('('+B+'A'+D+')'+'dleman'+'         (c) GDEV 2018')
	print('')
	print C+'='*32+D
	print('')
	
class pyConsole:
	
	R = '\x1b[1;31m'
	G = '\x1b[1;32m'
	B = '\x1b[1;34m'
	Y = '\x1b[1;33m'
	C = '\x1b[1;36m'
	HB = '\x1b[1;38;5;32m'
	D = '\x1b[0m'
	
	def Proc(self, mesg):
		return(self.B+'[+] '+self.D+mesg)
	def print_c(self, mesg):
		return(self.G+'[c] '+self.D+mesg)
	def print_m(self, mesg):
		return(self.G+'[m] '+self.D+mesg)
	def Err(self, mesg):
		return(self.R+'[!] '+self.D+mesg)