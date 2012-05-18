# Arch Linux PKGBUILD Collection, Zancarius-flavored

The PKGBUILDs contained in this repository are mostly just odds and ends that
I find useful for my own purposes. If you find them useful, too, feel free to
clone or fork this repository. Likewise, if you feel an update is lacking,
please don't hesitate to send a pull request.

Of particulr note are the `java-commons-full` and
`java-commons-full-scriptmirror` PKGBUILDs. These both violate (and do so
with great severity) the simplicity and generally accepted rules and
limitations for more Arch builds. I would highly recommend against
suggesting these to other Arch users if you can help it. Nevertheless,
they're provided as convenience packages for those who might want to install
the full Apache Commons distribution (minus those that don't have binary
builds), including the commons-daemon-native libraries, with a single
command. I intentionally chose not to build these as meta packages, because
not all Apache Commons libraries are available as official or AUR packages,
and there are several in the AUR that are out of date. Also, if you'd
rather specify your own mirror list, the `java-commons-full-scriptmirror`
PKGBUILD provides a fairly easy means of specfying which (random) mirrors
to use.

## GNU Miscfiles

The GNU Miscfiles (`miscfiles`) PKGBUILD provides all the databaes and other
assorted bits and pieces that are part of the Miscfiles distribution,
including the Webster's Second Internation English wordlist and its
appendix. If you find that the official `community/words` package isn't
quite up to par and are more accustomed to the words list that ships with
Gentoo, you should consider installing this one. A symlink will be created
to the `/usr/share/dict/web2` file as `/usr/share/dict/words` if and only
if the `words` symlink does not already exist; care is taken not to
conflict in any way with the `community/words` package. Everything else
in the Miscfiles distribution is installed in `/usr/share/miscfiles`.

## Gimp 2.6.x

The `gimp-26` PKGBUILDs are provided as a temporary stopgap for the issues
related to sub-pixel hinting and how Gimp's text tool currently handles
rendering fonts using sub-pixel hinting. For certain configurations like
my own, sub-pixel hinting at the window manager level causes Gimp to
render plain white text with green and yellow artifacts. Until this is
corrected upstream, I have provided a package build to revert Gimp to
the 2.6.x (currently 2.6.12) branch.

`gimp-26` currently requires that you replace the `babl` and `gegl`
packages with the PKGBUILDs provided in my repository; it won't build with
any other versions! Only Babl version 0.1.6 and Gegl 0.1.8 will work. If
you'd rather do the work yourself, you'll need to checkout and update
the Gimp, Babl, and Gegl repositories from the [Arch Linux SVN
Repositories](http://www.archlinux.org/svn/) (**important**: read the
warnings there first!), specifically revision r148734.
