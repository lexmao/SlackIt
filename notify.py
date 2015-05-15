#!/usr/bin/python

import os
import sys
import subprocess
from config import *
from registry import *


class Notify():

	
	#def set_notify_blacklist(self):


	# def set_notify_author(self,author):
		
	# 	registry.update({"author":author})


	# def set_notify_channel(self,channel):
		
	# 	registry.update({"channel":channel})


	# def set_notify_title(self,title):
	# 	title_with_author = "%s '%s' channel (from: %s)" % (title,registry['channel'],registry['author'])
	# 	registry.update({"title":title_with_author})


	# def set_notify_description(self,description):
	# 	registry.update({"description":description})


	def run_instance(self):

		def_title = current_notify["title"]
		def_desc = current_notify["description"]

		# get current path for icon
		current_dir = os.getcwd()
		icon_dir = "%s/slack-icon.png" % (current_dir)

		subprocess.Popen(['notify-send',"-i",icon_dir,def_title,def_desc]) 

		return
