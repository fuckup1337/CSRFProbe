#!/usr/bin/env python2
#coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    CSRF Probe     #
#-:-:-:-:-:-:-::-:-:#

#Author: the-Infected-Drake (@_tID)
#This module requires CSRFProbe
#https://github.com/the-Infected-Drake/CSRFProbe

import random
import string
from random import Random
from colors import *

def rand_String():

	print GR+' [*] Parsing input strings...'
	return ''.join( Random().sample(string.letters, 6))
