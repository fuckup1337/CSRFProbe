#!/usr/bin/env python2
#coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    CSRF Probe     #
#-:-:-:-:-:-:-::-:-:#

#Author: the-Infected-Drake (@_tID)
#This module requires CSRFProbe
#https://github.com/the-Infected-Drake/CSRFProbe

import urllib
from colors import *

def getvarsput(url, mname, maction, result):

	try:
	    if mname:
		print R+'\n +---------+'
		print R+' |   PoC   |'
		print R+' +---------+\n'
		print B+' [+] URL : ' +P+url
		print C+' [+] Name : ' +O+mname
		print G+' [+] Action : ' +O+maction

	except KeyError:

		print R+'\n +---------+'
		print R+' |   PoC   |'
		print R+' +---------+\n'
		print B+' [+] URL : ' +P+url
		print G+' [+] Action : ' +O+maction

	print O+' [+] Code : '+W+urllib.urlencode(result)
	print ''

