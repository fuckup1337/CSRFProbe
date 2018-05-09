#!/usr/bin/env python2
#coding: utf-8

#-:-:-:-:-:-:-::-:-:#
#    CSRF Probe     #
#-:-:-:-:-:-:-::-:-:#

#Author: the-Infected-Drake (@_tID)
#This module requires CSRFProbe
#https://github.com/the-Infected-Drake/CSRFProbe

from globalvars import *
from impo import *
import sys
sys.path.append('modules/')
from in_vars import *
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def csrf_main():

	os.system('clear')
	banner()
	banner1()
	web = inputin()
	form1 = form10()
	form2 = form20()

	Cookie0 = cookielib.CookieJar()
	Cookie1 = cookielib.CookieJar()
	resp1 = urllib2.build_opener(urllib2.HTTPCookieProcessor(Cookie0))
	resp2 = urllib2.build_opener(urllib2.HTTPCookieProcessor(Cookie1)) 

	actionDone = []

	csrf=''
	init1 = web
	form = Form_Debugger()

	bs1=BeautifulSoup(form1, "lxml").findAll('form',action=True)[0]
	bs2=BeautifulSoup(form2, "lxml").findAll('form',action=True)[0]

	action = init1

	resp1.open(action)
	resp2.open(action)

	crawler = Crawler_Handler(init1,resp1)
	print GR+" [*] Initializing crawling and scanning..."

	try:

		while crawler.noinit():
		    url = crawler.next()

		    print C+' [+] Crawling :> ' +B+ url
			
		    try:
			soup=crawler.process(web)
			if not soup:
				continue;

			i=0
			print O+' [*] Retrieving all forms on ' +C+ url +O+'...'
			for m in getAllForms(soup):
				action = Uri_Checker.buildAction(url,m['action'])
				if not action in actionDone and action!='':
					try:
						print 
						result = form.prepareFormInputs(m)
						r1 = request(url, action, result, resp1)
						result = form.prepareFormInputs(m)	
						r2 = request(url, action, result, resp2)

						if(len(csrf)>0):

							if not re.search(csrf, r2):
								print G+ '[+] Looks like we got a CSRF vulnerability on '+O+url+G+'!\n'

								try:
								    if m['name']:
									print R+'\n +---------+'
									print R+' |   PoC   |'
									print R+' +---------+\n'
									print B+' [+] URL : ' +P+url
									print C+' [+] Name : ' +O+m['name']
									print G+' [+] Action : ' +O+m['action']

								except KeyError:

									print R+'\n +---------+'
									print R+' |   PoC   |'
									print R+' +---------+\n'
									print B+' [+] URL : ' +P+url
									print G+' [+] Action : ' +O+m['action']

								print O+' [+] Code : '+W+urllib.urlencode(result)
								print ''

							continue;

						o2 = resp2.open(url).read()

						try:
							form2 = getAllForms(BeautifulSoup(o2, 'lxml'))[i]

						except IndexError:
							print R+' [-] Form returned a Error!'
							time.sleep(0.5)
							print G+' [+] Moving on...'
							continue;

						print GR+' [*] Preparing form inputs...'
						contents2 = form.prepareFormInputs(form2)
						r3 = request(url,action,contents2,resp2)

						try:
							checkdiff = difflib.ndiff(r1.splitlines(1),r2.splitlines(1))
							checkdiff0 = difflib.ndiff(r1.splitlines(1),r3.splitlines(1))

							result12 = []
							for n in checkdiff:
								if re.match('\+|-',n):
									result12.append(n)
							result13 = []
							for n in checkdiff0:
								if re.match('\+|-',n):
									result13.append(n)

							if len(result12)<=len(result13):

								try:
								    if m['name']:
									print R+'\n +---------+'
									print R+' |   PoC   |'
									print R+' +---------+\n'
									print B+' [+] URL : ' +P+url
									print C+' [+] Name : ' +O+m['name']
									print G+' [+] Action : ' +W+m['action']

								except KeyError:

									print R+'\n +---------+'
									print R+' |   PoC   |'
									print R+' +---------+\n'
									print B+' [+] URL : ' +P+url
									print G+' [+] Action : ' +W+m['action']

								print O+' [+] Code : '+W+urllib.urlencode(result)
								print ''

						except:
							pass

					except urllib2.HTTPError, msg:
						print msg.__str__()					

				actionDone.append(action)
				i+=1

		    except urllib2.URLError:
		    	print R+' [!] Exception at : '+url
		    	time.sleep(0.4)
		    	print G+' [+] Moving on...'
		    	continue;

		print G+" [+] Scan completed!"

	except urllib2.HTTPError as e:
	    if str(e.code) == '403':
		print R+' [-] HTTP Authentication Error!'
		print R+' [!] Error Code : ' +O+ str(e.code)
		pass

	except KeyboardInterrupt:
		print R+' [-] User Interrupt!'
		print R+' [!] Aborted!'


