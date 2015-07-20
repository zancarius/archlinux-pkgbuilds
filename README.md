# Arch Linux PKGBUILDs Collection, Zancarius-flavored

## WARNING: This is branch contains the *old* PKGBUILD archives

**Under this branch you will find PKGBUILDs that have been retired.** These
PKGBUILDs are interred in the `old` directory since I want to avoid
polluting the top level. Is this counter to "good" use of Git? Maybe.
But it doesn't really matter. I've removed this folder from the `master`
branch since it's apparent from recent experience that this serves as both
a source of confusion for individuals who are under the mistaken impression
that there exists only One True Way of Git repositories (which boggles my mind
considering the stupidly simplistic structure contained herein), *and* it
makes it unnecessarily difficult for the same to comprehend how someone
else might have a workflow that differs from their own. Shocking.

Almost scandalous, in fact.

Note: The general structure of this repo is probably a bit messy. But it
doesn't contain application sources either. It's just a place to hang my
PKGBUILDs. Don't like it? No problem. Fork it yourself. Make your own. If
you complain about it, I'll give you a full refund for $0.00.

## About

The PKGBUILDs contained in this repository are mostly just odds and ends that
I find useful for my own purposes. If you find them useful, too, feel free to
clone or fork this repository. Likewise, if you feel an update is lacking,
please don't hesitate to send a pull request.

Of particular note are the `java-commons-full` and
`java-commons-full-scriptmirror` PKGBUILDs. These both violate (and do so
with great ingenuity) the simplicity and generally accepted rules and
limitations for Arch PKGBUILDs. I would highly recommend against
suggesting these to other Arch users save for exceptional circumstances.
Nevertheless, they're provided as convenience packages for those who might
want to install the full Apache Commons distribution (minus those that don't
have binary builds), including the commons-daemon-native libraries, with a
single command. I intentionally chose not to build these as meta packages,
because not all Apache Commons libraries are available as official or AUR
packages, and there are several versions in the AUR that are out of date.
Also, if you'd rather specify your own mirror list, the
`java-commons-full-scriptmirror` PKGBUILD provides a fairly easy means of
specfying which (random) mirrors to use.

Be aware that the mirror selection logic in the
`java-commons-full-scriptmirror` may cause `makepkg` to fail unexpectedly.
I haven't yet resolved this issue and am open to ideas. :)

Below is a partial list and description of some of the packages. I'm currently
deciding whether or not to truncate this list because it's becoming somewhat
more noisome to maintain. Obviously, it was written at a time when my
repository contained many fewer packages, but the total number has since
grown as I've adopted and created a few more to support things I'm interested
in or find myself using periodically (Sentry, for instance). Chances are,
most of the packages you find here probably exist in the AUR, so any notes
specifically pointing out this particular fact are mostly useless.

## Updates

If you see a package that's out of date and simply cannot wait for me to
update the PKGBUILD, feel free to 1) flag it as out of date on the AUR in
case I haven't noticed (or forgot) and (optionally) 2) send a pull request
updating the outdated package(s). I try my best to check package versions
at least once a week (usually on a Saturday evening), comparing them to their
source repositories, and updating accordingly. Sometimes things fall through
the cracks, so if I've overlooked something, a gentle nudge should fix it.

As I sometimes (though rarely) add many packages in a single, large batch,
there may be times when the original PKGBUILD contains an inaccuracy either
in the project URL or the license. This is fairly rare as I try to catch
mistakes made from copying template PKGBUILDs, but it does happen on occasion.
Please don't feel offended if it does; it's probably an honest mistake that I
happened to overlook, but don't hesitate to alert me.

## babl-016

`babl-016` is one of two required builds for GIMP v2.6. Specifically, GIMP
requires this version of babl in order to function. If you're planning
on using GIMP 2.6, you'll need to build this.

## bsdmainutils

`bsdmainutils` is a PKGBUILD for Ubuntu's package of the same name. I happen
to use this package from the AUR and noticed one day that it had been
abandoned by its maintainer. I have since adopted it and will continue to
maintain the AUR package for the foreseeable future.

**This package is available in the AUR.**

## ccons

Some time ago, I was looking around for a C-style REPL and stumbled upon
`ccons` in the AUR and took note that it had been abandoned. I believe the
package was left as an orphan primarily because upstream's development
progress is somewhat slow and the repository is occasionally left in an
unbuildable state.

This PKGBUILD of ccons includes a series of patches to fix the build
process. It's not guaranteed to continue working, but I'll try to maintain
this as best as I can.

**This package is available in the AUR.**

## firefox-safebrowsing-opensuse

Some time ago, the official Firefox package dropped safebrowsing support.
I've since readded it to the mozconfig and have included all of the OpenSUSE
patches from `firefox-kde-opensuse`, maintained by Weng Xuetian, along with
a few other improvements (for instance, jemalloc is enabled by default).

If you don't have xulrunner installed or have Eclipse installed, you may
find that you can't build this package. Unfortunately, there's not much
I can suggest beyond [building it in a chroot](https://wiki.archlinux.org/index.php/DeveloperWiki:Building_in_a_Clean_Chroot).
Don't worry, building from a chroot is easy--it's just somewhat
inconvenient. You also shouldn't have to downgrade your glibc or apply
glibc-related patches to get it to build.

## gegl-018

`gegl-018` exists for the same reason babl-016 does--to support gimp-26.
This specific version of gegl is *also* required to build gimp-26, so you'll
need to remove any existing versions from your system (there should be
a conflicts in the PKGBUILD). This package, along with babl-016, will
be maintained for as long as I can maintain gimp-26 or until GIMP 2.8
has improved sufficiently that I've decided to switch to it, whichever
causes me to terminate support first.

## gimp-26

The `gimp-26` PKGBUILDs are provided as a temporary stopgap for issues
related to sub-pixel hinting and the behavior of Gimp's text tool. For
certain configurations like my own, sub-pixel hinting at the window
manager level causes Gimp to render plain white text with green and yellow
artifacts around the edges. Until this is corrected upstream, I have
provided a package build to revert Gimp to the 2.6.x (currently 2.6.12)
branch.

`gimp-26` currently requires that you replace the `babl` and `gegl`
packages with the PKGBUILDs provided in my repository; it won't build with
the official versions! Gimp 2.6.12 will build only with Babl version 0.1.6
and Gegl 0.1.8. If you'd rather do the work yourself, you'll need to
checkout and update the Gimp, Babl, and Gegl repositories from the [Arch
Linux SVN Repositories](http://www.archlinux.org/svn/) (**important**:
read the warnings there first!), specifically revision r148734.

## java-commons-full-scriptmirror

This PKGBUILD was originally developed as a test to randomly pick from
a selection of known mirrors for the Apache Commons collection. Because
of the amount of selection logic in the PKGBUILD, this will never be
a candidate for submission to the AUR. Instead, this is a convenience
script for those of you who might want to be polite stewards of the
Internet and refuse to leech bandwidth from a single mirror.

## java-commons-full

`java-commons-full` is identical to `java-commons-full-scriptmirror`
with the notable exception that its selection of source servers are
pre-generated from a known list using an external Pythoon script.
Otherwise, `java-commons-full` is the full collection of Apache Commons
(where applicable and available) and is provided as a convenience over
manually installing every Commons package by hand.

## miscfiles

This is the GNU Miscfiles (`miscfiles`) PKGBUILD. It provides all of the
databaes and other assorted bits and pieces that are part of the standard
Miscfiles distribution, including the Webster's Second Internation English
word list and its appendix. If you find that the official `community/words`
package isn't quite up to par and are more accustomed to the words list
that ships with Gentoo, you should consider installing this one. A symlink
to `/usr/share/dict/web2` will be created as `/usr/share/dict/words` if and
only if the `words` symlink does not already exist; care is taken to avoid
conflicts with the `community/words` package. Everything else in the
Miscfiles distribution is installed in `/usr/share/miscfiles`.

**This package is available in the AUR.**

## python2-httpbin-git

This is a PKGBUILD supplying [Kenneth Reitz](https://github.com/kennethreitz)'
httpbin HTTP server. httpbin is useful for running HTTP client unit tests
against and supports much of the basic grammar in HTTP 1.1.

Be warned that this package will pull in quite a large number of
dependencies.

**This package is available in the AUR.**

## python2-omnijson

`python2-omnijson` serves as a simple wrapper for a large number of
Python JSON implementations and is a convenience project for installations
that may vary in what they support. This PKGBUILD pulls `python2-omnijson`
from the Python Package Index (PyPI).

**This package is available in the AUR.**

## python2-raven-git

Raven is a frontend to Sentry, which is a real time logging service.
httpbin requires Raven; this is the Git version of the package and
is written by [David Cramer](https://github.com/dcramer).

## python2-raven

Raven is a frontend to Sentry, which is a real time logging service.
httpbin requires Raven; this is the latest official build of Raven
available from the Python Package Index (PyPI) and is written by
the same author as `python2-raven-git`.

**This package is availble in the AUR.**

## python2-sentry

Sentry is a real time logging service and is required by httpbin
in order to function. This is the latest official build of Sentry
available from the Python Package Index (PyPI) and is written by
the same author as `python2-raven`.

**This package is available in the AUR.**