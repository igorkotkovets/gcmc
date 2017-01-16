#!/usr/bin/python

class MessageValidator(object):
    def isDataValid(self, message):
        if not message.title:
            return False

        if not message.body:
            return False

        if not message.key:
            return False

        return True