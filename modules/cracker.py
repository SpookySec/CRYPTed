#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Author: 		rip meep
# Instagram: 	@rip.meep
# Github:		https://github.com/ripmeep


import requests
import sys
import re

class OnlineHashCrack(object):
	def __init__(self, hash: str) -> bool:
		self.hash = hash
		self.plaintext = None
		self.__URL = "https://hashes.com/en/decrypt/hash"

	def Crack(self):
		self.__session = requests.Session()
		self.__response = self.__session.get(self.__URL)
		self.__cookies = self.__session.cookies.get_dict()
		self.__params = {'csrf_token': None, 'hashes': None, 'submitted': 'true'}
		self.__csrf_token = self.__cookies['csrf_cookie']

		if (self.__response.status_code != 200):
			return False

		self.__headers = {
			"Host": "hashes.com",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Language": "en-US,en;q=0.5",
			"Accept-Encoding": "gzip, deflate, br",
			"Content-Type": "application/x-www-form-urlencoded",
			"Content-Length": "98",
			"Origin": "https://hashes.com",
			"DNT": "1",
			"Connection": "keep-alive",
			"Referer": "https://hashes.com/en/decrypt/hash",
			"Cookie": "csrf_cookie={}".format(self.__csrf_token),
			"Upgrade-Insecure-Requests": "1"
		}

		self.__params['csrf_token'] = self.__csrf_token
		self.__params['hashes'] = self.hash

		data = "csrf_token={}&hashes={}&submitted={}".format(self.__params["csrf_token"], self.__params["hashes"], self.__params["submitted"])
		self.__response = self.__session.post(self.__URL, headers=self.__headers, data=data)

		if (self.__response.status_code != 200):
			return False

		r = self.__response.text

		try:
			self.plaintext = re.findall("<div class=\"py-1\">(.*?)</div>", r)[0]
			self.plaintext = self.plaintext.split(":")

			self.plaintext = self.plaintext[1]

			return True
		except:
			return False
