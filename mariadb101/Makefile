
CHROOT := ".chroot"

build:
	mkarchroot -C pacman.conf -M /etc/makepkg.conf "$(CHROOT)/root" base-devel boost bzip2 cmake inetutils jemalloc libaio libsystemd libxml2 lz4 lzo openssl xz zlib
	makechrootpkg -c -r "$(CHROOT)"
.PHONY: build
