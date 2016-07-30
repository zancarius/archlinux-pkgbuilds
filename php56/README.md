# PHP 5.6.x AUR fork from `php56-*`

This package is a fork of mickael9's PHP56 PKGBUILD with a couple of fairly
important differences:

 * This package does not use the `php56-*` prefix for *any* of its member
components. Instead, this package is intended to be a *complete* drop in
implementation replacement for PHP7.
 * This package does not include some other extras that are built, by default,
in both the official Arch packages and the `php56` AUR package. Notably, MSSQL
support is missing, among others.

There are reasons for this--perhaps reasons that aren't *great*--and primarily
rest on the necessity that I run software that is not presently compatible with
PHP7. PHP56 is not (yet) deprecated, although it will be within a couple of
years I'm sure, and I feel it's a bit premature to dump it in favor of PHP7.
Personally, I would have preferred packages that had a `php7` prefix, but it's
easy enough to fix.

In particular, it's worth mentioning that this package (due to the intentional
removal of any sort of prefix) is *completely incompatible with the official
PHP distribution* and as such has the appropriate `conflicts`. Do *not* use
this package if you intend to support PHP7 concurrently with PHP56--use the
`php56` package by mickael9 instead. If you're not sure why you would want to
use this package, then you don't need it (again use `php56` instead). Actually,
I ought to just say this: **If you need PHP 5.6.x support, you should use the
`php56` package from the AUR instead**.

If you have software that requires PHP56 and cannot be changed to use the
`php56-*` prefix, then that's probably the *only* reason to use this package.

**Do not upload this package to the AUR in any form.**

If you need php56-imagick support with this package, please see the package by
the same name in my repository here.
