# coding: utf-8

import json
import os
import re
import sys
import time

class DirectoryList(list):

    def __add__ (self, item):
        if os.path.isdir(item):
            super(DirectoryList, self).append(item)
        return self

    def __iadd__ (self, item):
        if os.path.isdir(item):
            super(DirectoryList, self).append(item)
        return self

    def __isub__ (self, item):
        if os.path.isdir(item) and item in self:
            super(DirectoryList, self).remove(item)
        return self

    def __setitem__ (self, key, item):
        if os.path.isdir(item):
            print 'is dir'
            super(DirectoryList, self).__setitem__(key, item)

    def append (self, item):
        if os.path.isdir(item):
            super(DirectoryList, self).append(item)

class Config(object):

    def __init__ (self, config=""):

        self.config = {}

        if os.path.exists(config):
            print "file"
            self.config = json.load(open(config, "r"))
        else:
            print "string"
            self.config = json.loads(config)

        print self.config

class Check(object):

    def __init__ (self, pkgroot=""):

        self._pkgroot = None

        self.pkgroot = pkgroot

    def getpkgroot (self):
        return self._pkgroot
    def setpkgroot (self, pkgroot):
        if pkgroot != "" and os.path.exists(pkgroot):
            self._pkgroot = pkgroot
    pkgroot = property(
        getpkgroot,
        setpkgroot,
        None,
        "Gets or sets the package root."
    )

    def checkVersions (self):
        '''Checks file versions in all configured packages.'''

        pkgdirs = DirectoryList()

        for pkgdir in os.listdir(self.pkgroot):
            if os.path.exists(self.pkgroot + os.path.sep + pkgdir +
                os.path.sep + "version-info.json"):
                pkgdirs += self.pkgroot + os.path.sep + pkgdir

        print pkgdirs