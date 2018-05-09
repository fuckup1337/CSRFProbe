#!/usr/bin/env python2
#coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    CSRF Probe     #
#-:-:-:-:-:-:-::-:-:#

#Author: the-Infected-Drake (@_tID)
#This module requires CSRFProbe
#https://github.com/the-Infected-Drake/CSRFProbe

import re
from build_Url import *
from impo import *

def build_Action(url, action):

	print O+' [*] Parsing URL parameters...'
	if action!='' and not re.match('#',action):
		return build_Url(url, action)
	else:
		return url
