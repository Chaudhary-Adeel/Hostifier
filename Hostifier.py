#!/usr/bin/env python

# The MIT License (MIT)

# Copyright (c) 2014 Muhammad Adeel

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

class Coloring:
	def __init__(self):
		self.green = "\033[92m"
		self.bold = "\033[1m"
		self.red = "\033[91m"
		self.die = "\033[0m"

COLOR = Coloring()

try:
	import os, sys, string, socket, time
except IOError:
	print COLOR.bold + "[!] Error:" + COLOR.die + " Can't Import Modules Properly."
	exit()

def banner():
	print COLOR.bold + COLOR.red + '''
    __  __           __  _ _____          
   / / / /___  _____/ /_(_) __(_)__  _____
  / /_/ / __ \/ ___/ __/ / /_/ / _ \/ ___/
 / __  / /_/ (__  ) /_/ / __/ /  __/ /    
/_/ /_/\____/____/\__/_/_/ /_/\___/_/     
==========================================
# Author: Muhammad Adeel                 #
# Blog: http://urdusecurity.blogspot.com #
# Mail: Chaudhary1337@gmail.com          #
==========================================''' + COLOR.die
banner()
# variables 

Dname = raw_input('\n(Domain Name)> ')
subdomains = raw_input('(SubDomains Filename)> ')
varFile = open(subdomains, 'r')
var = open(subdomains, 'r')
varLength = var.readlines()

def Hostifier(Dname, varFile, varLength):
	global a
	global b
	a = 0
	b = 0
	print COLOR.bold + COLOR.green + "[+] Subdomains Loaded: " + COLOR.die + str(len(varLength))
	print COLOR.bold + "\n -- Thanks For Using Hostifier -- " + COLOR.die
	print COLOR.bold + "[+] Starting at: {0}".format(time.ctime()) + COLOR.die + "\n"
	for sd in varFile.read().split('\n'):
		a = a + 1
		varX = chr(27)
		# credits to neuro
		sys.stdout.write(varX + '[2K' + varX + '[G')
		sys.stdout.write('[+] Trying | ' + sd + ' |' + ' --')
		sys.stdout.flush()
		try:
			sock = socket.gethostbyname_ex(sd+"."+Dname)
			print sock
			b = b + 1
		except:
			pass
	sys.stdout.write(varX + '[2K' + varX + '[G')
	print COLOR.bold + "[+] Ending at: {0}".format(time.ctime()) + COLOR.die
	print COLOR.green + COLOR.bold + "[+] Total Results: {0}".format(b) + COLOR.die
	varFile.close()


Hostifier(Dname, varFile, varLength)
		
def main():
	if __name__ == '__main__':
		main()
