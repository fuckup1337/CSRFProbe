#!/usr/bin/env python2
#coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    CSRF Probe     #
#-:-:-:-:-:-:-::-:-:#

#Author: the-Infected-Drake (@_tID)
#This module requires CSRFProbe
#https://github.com/the-Infected-Drake/CSRFProbe

from colors import *

def inputin():

	web = raw_input(C+' [$] Enter target address :> '+G)

	if 'http' not in web:
		web = 'http://' + web
	if web.endswith('/'):
		return web
	else:
		web = web + '/'
		return web
