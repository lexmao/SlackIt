#!/usr/bin/python

'''
 This file is part of SlackIt

 Copyright(c) 2014 Gabriele Salvatori
 http://www.salvatorigabriele.com
 salvatorigabriele@gmail.com

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

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
