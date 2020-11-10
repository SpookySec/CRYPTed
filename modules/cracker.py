#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Author: 		rip meep
# Instagram: 	@rip.meep
# Github:		https://github.com/ripmeep

import requests
import sys
import re

class OnlineHashCrack(object):
	__HASHTYPES = ["md4", "md5", "sha1", "sha256", "sha384", "sha512"]

	def __init__(self, hash, hashtype) -> bool:
		self.__session = requests.session()
		self.hash = str(hash).lower()
		self.hashtype = str(hashtype).lower()
		self.plaintext = None
		self.__URL = f"https://md5decrypt.net/Api/api.php?hash={self.hash}&hash_type={self.hashtype}&email=deanna_abshire@proxymail.eu&code=1152464b80a61728"

	def Crack(self):
		if self.hashtype not in OnlineHashCrack.__HASHTYPES:
			raise Exception("Hashtype {} not valid ({})".format(self.hashtype, OnlineHashCrack.__HASHTYPES))

		response = self.__session.get(self.__URL)
		t = response.text

		if len(t) == 0 or "CODE ERREUR : " in t:
			return False

		self.plaintext = t.strip()

		return True

