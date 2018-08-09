
import requests
import time
from random import *
import random
import json
import bs4
import datetime
from bs4 import BeautifulSoup as soup
from fake_useragent import UserAgent
from colorama import Fore, init

ua = UserAgent()
sess = requests.Session()

with open("sailsconfig.json") as file:
	config = json.load(file)
	file.close()

useproxies = config['useproxies']
domain = config['domain']

def random_line(fname):
    lines = open(fname).read().splitlines()
    return choice(lines)




def enter_raffle():
	headers = {
	"Access-Control-Allow-Headers": "*",	
	"Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
	"DNT": "1",
	"Origin": "https://www.xhibition.co",
	"Referer": "https://www.xhibition.co/pages/raffles",
	"User-Agent": str(ua.Chrome)
	}


	data = [
	  ('g', 'NwK4ig'),
	  ('$fields', '$source,$email,$consent_method,$consent_form_id,$consent_form_version'),
	  ('$list_fields', ''),
	  ('$timezone_offset', '-4'),
	  ('$source', 'Air Max 1 \'Parra\' Sale'),
	  ('$email', email),
	  ('$consent_method', 'Klaviyo Form'),
	  ('$consent_form_id', 'JPz5hN'),
	  ('$consent_form_version', '29778'),
		]

	proxy = ""
	if useproxies == "true":
		while proxy == "":  
			proxy = random_line("proxies.txt")
		try:
			proxytest = proxy.split(":")[2]
			userpass = True
		except IndexError:
			userpass = False
		if userpass == True:
			ip = proxy.split(":")[0]
			port = proxy.split(":")[1]
			userpassproxy = ip + ":" + port
			proxyuser = proxy.split(":")[2].rstrip()
			proxypass = proxy.split(":")[3].rstrip()

		if userpass == True:
			proxies = {'http': 'http://' + proxyuser + ':' + proxypass + '@' + userpassproxy, 'https': 'http://' + proxyuser + ':' + proxypass + '@' + userpassproxy}
		if userpass == False:
			proxies = {'http': 'http://' + proxy, 'https': 'http://' + proxy}


		r = sess.post("https://a.klaviyo.com/ajax/subscriptions/subscribe", headers=headers, data=data, proxies=proxies)
	
	else:
		r = sess.post("https://a.klaviyo.com/ajax/subscriptions/subscribe", headers=headers, data=data)


	
	print(r.text)


entries = 10
if(__name__ == "__main__"):
	print(Fore.BLUE + "---------------------------")
	print(Fore.BLUE + "|" + Fore.WHITE + " Korn's Xhibition Raffle Script " + Fore.BLUE + "|")
	print(Fore.BLUE + "---------------------------\n")
	print(Fore.WHITE)
	for x in range(0, entries):
		first_name = random.choice(["Jackson", "Aiden", "Sophia", "Emma", "Olivia", "Lucas", "Ava", "Liam", "Mia", "Noah", "Ethan", "Isabella", "Riley", "Caden", "Aria", "Mason", "Elijah", "Zoe", "Lily", "Michael", "Benjamin", "Emily", "James", "Chloe", "Abigail", "Avery", "Evelyn", "Daniel", "Jack", "Madison", "Caleb", "Alexander", "Daniel", "Jack", "Evelyn", "Isaac", "Cameron", "Julian", "Eli", "Peyton", "Mackenzie", "Maria", "Camilla", "John", "Lincoln", "Brayden", "Victoria"])
		email = first_name + str(randint(00000,10000)) + domain
		time.sleep(3)
		enter_raffle()

