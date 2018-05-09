#!/usr/bin/env python2
#coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    CSRF Probe     #
#-:-:-:-:-:-:-::-:-:#

#Author: the-Infected-Drake (@_tID)
#This module requires CSRFProbe
#https://github.com/the-Infected-Drake/CSRFProbe

import re
from bs4 import BeautifulSoup

def get_AllForms(soup):

	return soup.findAll('form',action=True,method=re.compile("post", re.IGNORECASE))

