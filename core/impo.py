#!/usr/bin/env python2
#coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    CSRF Probe     #
#-:-:-:-:-:-:-::-:-:#

#Author: the-Infected-Drake (@_tID)
#This module requires CSRFProbe
#https://github.com/the-Infected-Drake/CSRFProbe

import difflib
import cookielib
import urlparse
import requests
from bs4 import BeautifulSoup
import urllib
import urllib2
import sys
import mechanize
import os
import re
import time
import logging
import scapy
sys.path.append('modules/')
from scapy.all import *
from form10 import *
from form20 import *
from inputin import *
from banner import *
from banner1 import *
from request import *
from colors import *
from csrf_main import *

