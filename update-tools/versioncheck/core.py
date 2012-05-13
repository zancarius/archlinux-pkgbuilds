# coding: utf-8

import httplib
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

def config (path):
    if os.path.exists(path):
        config = json.load(open(path, "r"))
    else:
        config = json.loads(path)
    return config

class Package(object):
    def __init__ (self, path):
        self.path = path
        self.config = config(path + os.path.sep + "version-info.json")
        self.package = open(path + os.path.sep + "PKGBUILD", "r").read()
        self.name = self.readName()

        self.fetchVersion()

    def fetchVersion (self):
        '''Fetches version information, usually from remote sites.'''
        aliases = self.config["packages"]["list-aliases"]
        packages = self.config["packages"]["list"]

        for package in packages:
            name = package
            if aliases.has_key(package):
                name = aliases[package]
            
            

            return

    def readName (self):
        '''Reads the package name from the PKGBUILD.'''
        regs = re.compile("^pkgname=(.*)$", re.MULTILINE)
        matches = regs.search(self.package)
        if matches:
            self.name = matches.groups()[0]

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

        for pkgdir in pkgdirs:
            package = Package(pkgdir)