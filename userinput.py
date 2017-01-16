#!/usr/bin/python

from googlecloudmessage import *
from sys import version_info

class UserInput(object):


    def _readInput(self, inputMessage):
        py3 = version_info[0] > 2  # creates boolean value for test that Python major version > 2
        if py3:
            userInput = input(inputMessage)
        else:
            userInput = raw_input(inputMessage)

        return userInput

    def read(self, message):
        title = message.title
        body = message.body
        key = message.key
        if not title:
            title = self._readInput("Notification title: ")

        if not body:
            body = self._readInput("Notification body: ")

        while not key:
            key = self._readInput("API key(required): ")

        return GoogleCloudMessage(title, body, key)

