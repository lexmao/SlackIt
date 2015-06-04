#!/usr/bin/python

'''
 This file is part of SlackIt

 Copyright(c) 2015 Gabriele Salvatori
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
import string
import json
import urllib2
import time
from registry import *
from config import *
from websocket import create_connection


class Connect():


	def init_get_response(self,request):

		response = urllib2.urlopen(request)
		output = json.load(response)

		return output


	def get_list_of_users_from_team(self):

		GET_request = "https://slack.com/api/users.list?token=%s&pretty=1" % (slack_team_token)

		users = self.init_get_response(GET_request)

		return users


	def get_name_from_user_code(self,code):

		users = self.get_list_of_users_from_team()

		for i in range(0,len(users)):
			if users["members"][i]["id"] == code:
				return users["members"][i]["name"]


	def get_websocket_url_from_RTM(self):

		url = "https://slack.com/api/rtm.start?token=%s" % (slack_team_token)
		response = urllib2.urlopen(url)
		output = json.load(response)

		websocket_url = output["url"]

		return websocket_url


	def init_connection_with_websocket(self):

			w_socket = self.get_websocket_url_from_RTM()
			socket = create_connection(w_socket)

			while True:

				result = socket.recv()

				print result

				# author = result["user"]
				# text = result["text"]
				# channel = result["channel"]

				# title = "You have a new message from %s (channel: %s )" % (author,channel)

				# current_notify["title"] = title
				# current_notify["description"] = text

				# notification = Notify()
				# notification.run_instance()



	def run_instance(self):

		self.init_connection_with_websocket()