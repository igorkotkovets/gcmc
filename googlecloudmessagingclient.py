#!/usr/bin/python

import urllib
import urllib2
import json

class MessagingClient(object):
    def send(self, message):
        url = 'https://gcm-http.googleapis.com/gcm/send'
        bodyJsonDict = {}
        bodyJsonDict['to'] = '/topics/global-ios'
        bodyJsonDict['content_available'] = 'true'
        bodyJsonDict['priority'] = 'high'
        bodyJsonDict['notification'] = self._notificationDict(message)
        bodyJsonDict['data'] = self._dataDict(message)

        headersDict = {}
        headersDict['Content-Type'] = 'application/json'
        headersDict['Authorization'] = "key=%s" % message.key

        data = urllib.quote(json.dumps(bodyJsonDict))
        req = urllib2.Request(url, data, headersDict)
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
