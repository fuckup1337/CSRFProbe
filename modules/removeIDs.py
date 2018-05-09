#!/usr/bin/env python2
#coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    CSRF Probe     #
#-:-:-:-:-:-:-::-:-:#

#Author: the-Infected-Drake (@_tID)
#This module requires CSRFProbe
#https://github.com/the-Infected-Drake/CSRFProbe

import Uri_Checker
import re

def removeIDs(Uri_Checker):

	p = re.compile('=[0-9]+')
	Uri_Checker = p.sub('=',Uri_Checker)
	p = re.compile('(title=)[^&]*')
	Uri_Checker = p.sub('\\1',Uri_Checker)
	return Uri_Checker
