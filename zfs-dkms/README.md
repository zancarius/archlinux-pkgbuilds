# Arch Linux ZoL + Patches

**THIS IS NOT THE OFFICIAL zfs-dkms PACKAGE.**

I'm retaining the name exclusively for my own use so I can more easily migrate
to the official `zfs-dkms` once these fixes make it into the stable branch. Do
not attempt to submit this to the AUR in any way, shape, or form (there's
already a `zfs-dkms-git` that should be following most of the patches here--use
that instead).

This package contains patches supplied by [rwanyoike](https://github.com/rwanyoike)
whose work comprises a number of extensive rewrites, available on the
[archzfs](https://github.com/archzfs/archzfs/) AUR git repo. A few other minor
fixes are included as well, limiting error reporting on boot, but may not be
available upstream. This package may introduce other patches from upstream as
time permits but is included as a temporary stop gap for users (like myself)
who  want to follow zfs-dkms stable, want some of the newer fixes from
upstream, and don't want to install the related `*-git` packages.

Use this at your own risk. If you want rwanyoike's patches, applied officially,
use `zfs-dkms-git` instead. (This will require that you install other -git
packages as well.)
