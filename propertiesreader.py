#!/usr/bin/python


import sys, getopt
from googlecloudmessage import *


class PropertiesReader(object):
    def readProperties(self, argv):
        title = ''
        body = ''
        key = ''
        try:
            opts, args = getopt.getopt(argv, "ht:b:k", ["title=", "body=", "key="])
        except getopt.GetoptError:
            print 'main.py -t <title> -b <body> -k <key>'
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print 'main.py -t <title> -b <body> -k <key>'
                sys.exit()
            elif opt in ("-t", "--title"):
                title = arg
            elif opt in ("-b", "--body"):
                body = arg
            elif opt in ("-k", "--key"):
                key = arg

        return  GoogleCloudMessage(title, body, key)
