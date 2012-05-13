#!/usr/bin/env python2
# coding: utf-8

'''
This script updates PKGBUILD version information automatically in my Arch Linux
PKGBULD repo (https://github.com/zancarius/archlinux-pkgbuilds). It accepts a
single directory as its sole argument, containing the package builds, and will
examine each one for a "version-info.json" file. This file contains detailed
instructions on which varible(s) to update, URL(s) to examine for updated
version information, and other useful information
'''

import sys

from versioncheck.core import Check

if __name__ == "__main__":
    #config = Config("../java-commons-full-scriptmirror/version-info.json")

    if len(sys.argv) <= 1:
        print "Usage: %s <pkgroot>" % sys.argv[0]
        sys.exit(1)

    check = Check(sys.argv[1])
    check.checkVersions()
