#!/usr/bin/python

import os
import sys
import string
import json
import urllib2
import time
from registry import *
from config import *


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


	def retrieve_channels_from_slack_team(self):

		GET_request = "https://slack.com/api/channels.list?token=%s&pretty=1" % (slack_team_token)

		channels = self.init_get_response(GET_request)

		return channels


	def get_channel_ID_from_channel_name(self,channel_name):

		channels = self.retrieve_channels_from_slack_team()

		for i in range(0,len(channels)):
			if channels["channels"][i]["name"] == channel_name:
				return channels["channels"][i]["id"]


	# def fetch_entire_channel_history_from_slack_team(self):

	# 	channel_ID = self.get_channel_ID_from_channel_name(channels) #edit...channels must be an array

	# 	GET_request = "https://slack.com/api/channels.history?token=%s&channel=%s&pretty=1" % (slack_team_token,channel_ID)

	# 	history = self.init_get_response(GET_request)

	# 	return history
		

	def fetch_channel_history_from_slack_team(self):

		time_string = str(time.time())
		split_timestring = time_string.split(".")
		latest_timestamp = split_timestring[0]

		channel_ID = self.get_channel_ID_from_channel_name(channels) #edit...channels must be an array

		if check_ts["ts"] == None or check_ts["ts"] == last_timestamp["ts"]:
			GET_request = "https://slack.com/api/channels.history?token=%s&channel=%s&latest=%s&oldest=%s&pretty=1" % (slack_team_token,channel_ID,latest_timestamp,last_timestamp["ts"])
		else:
			GET_request = "https://slack.com/api/channels.history?token=%s&channel=%s&oldest=%s&pretty=1" % (slack_team_token,channel_ID,last_timestamp["ts"])


		history = self.init_get_response(GET_request)

		return history


	def fetch_content_from_history(self):

		if ( check_ts["ts"] == None or check_ts["ts"] == last_timestamp["ts"] ):

			title = "No new messages on '%s' Slack channel" % (channels)
			current_notify["title"] = title
			current_notify["description"] = "Waiting for the next check..."

			check_ts["ts"] = last_timestamp["ts"]

			return


		check_ts["ts"] = last_timestamp["ts"]
		history = self.fetch_channel_history_from_slack_team()

		# counting_elements = json.loads(history)
		count = len(history['messages'])

		print count


		if count == 0:

			title = "No new messages on '%s' Slack channel" % (channels)
			current_notify["title"] = title
			current_notify["description"] = "Waiting for the next check..."

		elif count == 1:

			last_message = history["messages"][0]["text"]
			last_author = history["messages"][0]["user"]

			name = self.get_name_from_user_code(last_author)

			current_notify["author"] = name

			title = "You have a new message on '%s' Slack channel (from: %s)" % (channels,current_notify["author"])

			current_notify["title"] = title
			current_notify["description"] = last_message

		else:

			last_message = history["messages"][0]["text"]
			last_author = history["messages"][0]["user"]

			name = self.get_name_from_user_code(last_author)

			current_notify["author"] = name

			title = "You have %s new messages on %s Slack channel" % (count,channels)
			description = "Last message from %s : %s " % (current_notify["author"],last_message)

			current_notify["title"] = title
			current_notify["description"] = description

			
	def get_last_timestamp_from_history(self):

			history = self.fetch_channel_history_from_slack_team()
			last_ts = history["messages"][0]["ts"]
			split_ts = last_ts.split(".")

			last_timestamp["ts"] = split_ts[0]

			print last_timestamp



	# def get_last_author_from_history(self):

	# 	pair = self.fetch_last_message_and_author_ID_from_history()
	# 	users = self.get_list_of_users_from_team()


	# 	for i in range(0,len(users)):
	# 		if users["members"][i]["id"] == pair["author"]:
	# 			return users["members"][i]["name"]

	
	def run_instance(self):

		self.get_last_timestamp_from_history()
		self.fetch_content_from_history()

		print current_notify
		print current_notify["description"]
	
	