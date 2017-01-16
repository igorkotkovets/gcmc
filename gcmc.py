#!/usr/bin/python

import sys, getopt
import urllib2
import json
from optparse import OptionParser
from sys import version_info


class GoogleCloudMessage(object):
    def __init__(self, title, body, key, to):
        self.title = title
        self.body = body
        self.key = key
        self.to = to


class PropertiesReader(object):
    def readProperties(self, argv):
        usage = "usage: %prog -t <title> -b <body> -k <key>"
        parser = OptionParser(usage=usage)
        parser.add_option("-t", "--title", dest="vartitle",
                          help="A notification title", metavar="STRING")
        parser.add_option("-b", "--body", dest="varbody",
                          help="A notification body", metavar="STRING")
        parser.add_option("-k", "--key", dest="varkey",
                          help="Google Cloud Server API key", metavar="STRING")
        parser.add_option("-d", "--destination", dest="vardestination",
                          help="A topic name", metavar="STRING")
        (options, args) = parser.parse_args()
        return  GoogleCloudMessage(options.vartitle, options.varbody, options.varkey, options.vardestination)


class UserInput(object):
    def _readInput(self, inputMessage):
        py3 = version_info[0] > 2  # creates boolean value for test that Python major version > 2
        if py3:
            userInput = input(inputMessage)
        else:
            userInput = raw_input(inputMessage)

        return userInput

    def readMessageParamsIfNeeded(self, message):
        title = message.title
        body = message.body
        key = message.key
        to = message.to
        if not title:
            title = self._readInput("Notification title: ")

        if not body:
            body = self._readInput("Notification body: ")

        while not key:
            key = self._readInput("API key(required): ")

        while not to:
            to = self._readInput("Topic(required): ")

        return GoogleCloudMessage(title, body, key, to)


class MessagingClient(object):
    def send(self, message):
        url = 'https://gcm-http.googleapis.com/gcm/send'
        bodyJsonDict = {}
        bodyJsonDict['to'] = message.to
        bodyJsonDict['content_available'] = True
        bodyJsonDict['priority'] = 'high'
        bodyJsonDict['notification'] = self._notificationDict(message)
        bodyJsonDict['data'] = self._dataDict(message)

        headersDict = {}
        headersDict['Content-Type'] = 'application/json'
        headersDict['Authorization'] = "key=%s" % message.key

        bodyJsonStr = json.dumps(bodyJsonDict)
        req = urllib2.Request(url, bodyJsonStr, headersDict)
        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError, response:
            pass
        the_page = response.read()
        print the_page

    def _notificationDict(self, message):
        notificationDict = {}
        notificationDict['body'] = message.body
        notificationDict['title'] = message.title
        notificationDict['sound'] = 'default'
        return notificationDict

    def _dataDict(self, message):
        dataDict = {}
        dataDict['score'] = '5x1'
        dataDict['time'] = '15:10'
        return dataDict



def main(argv):
    message = PropertiesReader().readProperties(argv)
    message = UserInput().readMessageParamsIfNeeded(message)
    MessagingClient().send(message)

if __name__ == "__main__":
    main(sys.argv[1:])