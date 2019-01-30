
CHROOT=".chroot"

build:
	makechrootpkg -c -r "$(CHROOT)"

create-chroot:
	mkarchroot -C pacman.conf -M /etc/makepkg.conf "$(CHROOT)/root" base-devel boost bzip2 cmake inetutils jemalloc libaio libsystemd libxml2 lz4 lzo openssl xz zlib
