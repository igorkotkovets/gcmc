#!/usr/bin/python

import sys, getopt
from googlecloudmessage import *
from propertiesreader import *
from userinput import *
from googlecloudmessagingclient import *
from messagevalidator import *


def main(argv):
    reader = PropertiesReader()
    message = reader.readProperties(argv)
    userInput = UserInput()
    validator = MessageValidator()
    while validator.isDataValid(message) == False:
        message = userInput.read(message)
    client = MessagingClient()
    client.send(message)


    print "title %s." % message.title
    print "body %s." % message.body
    print "key %s." % message.key


if __name__ == "__main__":
    main(sys.argv[1:])