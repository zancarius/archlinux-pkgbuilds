#!/usr/bin/env python2

# This script examines the PKGBUILD for java-commons-full and attaches a random
# mirror to each download. The intent is to limit the amount of load on any one
# mirror. If you need to test this package and randomly select mirrors from
# within the PKGBUILD (not recommended), use java-commons-full-scriptmirror.
#
# gen-mirrors.py should only be run when adding packages, adding mirrors, or
# making other alterations in which it would make sense to update the mirrors a
# particular set of packages is downloaded from.
#
# Whenever you add a new file to the PKGBUILD sources, use a path relative to
# the mirrors "commons" directory (e.g. io/binaries/commons-io-2.3-bin.tar.gz)
# or supply the fully-qualified domain name and path.
#
# Author: Benjamin A. Shelton <zancarius@gmail.com>
# Revision: 20120512
# License: Public domain. Do whatever you want with this file.

import os
import random
import re
import sys

if len(sys.argv) <= 1:
    print "Usage: %s PKGBUILD" % sys.argv[0]
    sys.exit(1)

pkgbuild = sys.argv[1]

if not os.path.exists(pkgbuild):
    print "File %s not found." % pkgbuild
    sys.exit(1)

# Mirror list. If you need more mirrors, add them here.
mirrors = [
    "http://www.eng.lsu.edu/mirrors/apache/commons/",
    "http://mirror.uoregon.edu/apache/commons/",
    "http://www.reverse.net/pub/apache/commons/",
    "http://apache.mirrors.lucidnetworks.net/commons/",
    "http://download.nextag.com/apache/commons/",
    "http://mirror.candidhosting.com/pub/apache/commons/",
    "http://apache.mirrors.tds.net/commons/",
    "http://mirror.olnevhost.net/pub/apache/commons/",
    "http://www.gtlib.gatech.edu/pub/apache/commons/",
    "http://apache.deathculture.net/commons/",
    "http://apache.mirrors.pair.com/commons/",
    "http://mirrors.gigenet.com/apache/commons/",
    "http://apache.mirrorcatalogs.com/commons/",
    "http://apache.petsads.us/commons/",
    "http://apache.mirrors.hoobly.com/commons/",
    "http://newverhost.com/pub/commons/",
    "http://mirror.candidhosting.com/pub/apache/commons/",
]

print "Opening %s" % pkgbuild

# PKGBUILDs aren't terribly large. We'll load the whole thing.
pkgdata = open(pkgbuild, "r").read()

# Match the entire source declaration.
sourceRegs = re.compile("^source=\(([^\)]+)\)", re.MULTILINE)
matches = sourceRegs.search(pkgdata)
if not matches:
    print "No source=() declaration found. Is this a PKGBUILD?"
    sys.exit(10)
source = matches.groups()[0]

# Match URIs and partial URIs, looking for the ending string.
uriRegs = re.compile("^\n?\s*(?:http://.*?/commons/)?(.*)$", re.MULTILINE)
matches = uriRegs.findall(source)
if not matches:
    print "No URIs found in the source=() declaration."
    sys.exit(20)

# Filter out the matches and prepend a random mirror to the front of the file.
# Then recombine the source=() declaration complete with new mirrors!
matches = [ mirrors[ random.randint(0, len(mirrors)-1) ] + match for match in matches if match != ""]
pkgdata = pkgdata.replace(source, "\n  "+"\n  ".join(matches)+"\n")

open(pkgbuild, "w").write(pkgdata)

print "Done!"