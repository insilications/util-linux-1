#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : util-linux
Version  : 2.28.2
Release  : 58
URL      : https://www.kernel.org/pub/linux/utils/util-linux/v2.28/util-linux-2.28.2.tar.xz
Source0  : https://www.kernel.org/pub/linux/utils/util-linux/v2.28/util-linux-2.28.2.tar.xz
Summary  : fdisk library
Group    : Development/Tools
License  : BSD-3-Clause BSD-4-Clause-UC GPL-2.0 LGPL-2.1
Requires: util-linux-bin
Requires: util-linux-python
Requires: util-linux-config
Requires: util-linux-lib
Requires: util-linux-data
Requires: util-linux-doc
Requires: util-linux-locales
BuildRequires : Linux-PAM-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : docbook-xml
BuildRequires : e2fsprogs
BuildRequires : gettext-bin
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libcap-ng-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : pkgconfig(tinfo)
BuildRequires : procps-ng
BuildRequires : python-dev
BuildRequires : readline-dev
BuildRequires : zlib-dev
Patch1: mount-nosetuid.patch
Patch2: agetty.patch
Patch3: default-issue.patch
Patch4: topology.patch

%description
util-linux
util-linux is a random collection of Linux utilities
Note that in years 2006-2010 this project used the name "util-linux-ng".

%package bin
Summary: bin components for the util-linux package.
Group: Binaries
Requires: util-linux-data
Requires: util-linux-config

%description bin
bin components for the util-linux package.


%package config
Summary: config components for the util-linux package.
Group: Default

%description config
config components for the util-linux package.


%package data
Summary: data components for the util-linux package.
Group: Data

%description data
data components for the util-linux package.


%package dev
Summary: dev components for the util-linux package.
Group: Development
Requires: util-linux-lib
Requires: util-linux-bin
Requires: util-linux-data
Provides: util-linux-devel

%description dev
dev components for the util-linux package.


%package doc
Summary: doc components for the util-linux package.
Group: Documentation

%description doc
doc components for the util-linux package.


%package extras
Summary: extras components for the util-linux package.
Group: Default

%description extras
extras components for the util-linux package.


%package lib
Summary: lib components for the util-linux package.
Group: Libraries
Requires: util-linux-data
Requires: util-linux-config

%description lib
lib components for the util-linux package.


%package locales
Summary: locales components for the util-linux package.
Group: Default

%description locales
locales components for the util-linux package.


%package python
Summary: python components for the util-linux package.
Group: Default

%description python
python components for the util-linux package.


%prep
%setup -q -n util-linux-2.28.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export LANG=C
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export FCFLAGS="$CFLAGS -Os -ffunction-sections "
export FFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%reconfigure --disable-static --disable-use-tty-group \
--enable-makeinstall-chown \
--enable-makeinstall-setuid \
--enable-socket-activation \
--disable-kill \
--disable-chfn-chsh \
--disable-nologin \
--enable-libmount-force-mountinfo
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang util-linux
## make_install_append content
mkdir %{buildroot}/usr/lib/systemd/system/sockets.target.wants
ln -s ../uuidd.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/uuidd.socket
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/fdformat
%exclude /usr/bin/i386
%exclude /usr/bin/linux32
%exclude /usr/bin/login
%exclude /usr/bin/mkfs.bfs
%exclude /usr/bin/mkfs.cramfs
%exclude /usr/bin/zramctl
/usr/bin/addpart
/usr/bin/agetty
/usr/bin/blkdiscard
/usr/bin/blkid
/usr/bin/blockdev
/usr/bin/cal
/usr/bin/cfdisk
/usr/bin/chcpu
/usr/bin/chrt
/usr/bin/col
/usr/bin/colcrt
/usr/bin/colrm
/usr/bin/column
/usr/bin/ctrlaltdel
/usr/bin/delpart
/usr/bin/dmesg
/usr/bin/eject
/usr/bin/fallocate
/usr/bin/fdisk
/usr/bin/findfs
/usr/bin/findmnt
/usr/bin/flock
/usr/bin/fsck
/usr/bin/fsck.cramfs
/usr/bin/fsck.minix
/usr/bin/fsfreeze
/usr/bin/fstrim
/usr/bin/getopt
/usr/bin/hexdump
/usr/bin/hwclock
/usr/bin/ionice
/usr/bin/ipcmk
/usr/bin/ipcrm
/usr/bin/ipcs
/usr/bin/isosize
/usr/bin/last
/usr/bin/lastb
/usr/bin/ldattach
/usr/bin/linux64
/usr/bin/logger
/usr/bin/look
/usr/bin/losetup
/usr/bin/lsblk
/usr/bin/lscpu
/usr/bin/lsipc
/usr/bin/lslocks
/usr/bin/lslogins
/usr/bin/lsns
/usr/bin/mcookie
/usr/bin/mesg
/usr/bin/mkfs
/usr/bin/mkfs.minix
/usr/bin/mkswap
/usr/bin/more
/usr/bin/mount
/usr/bin/mountpoint
/usr/bin/namei
/usr/bin/nsenter
/usr/bin/partx
/usr/bin/pg
/usr/bin/pivot_root
/usr/bin/prlimit
/usr/bin/raw
/usr/bin/readprofile
/usr/bin/rename
/usr/bin/renice
/usr/bin/resizepart
/usr/bin/rev
/usr/bin/rtcwake
/usr/bin/runuser
/usr/bin/script
/usr/bin/scriptreplay
/usr/bin/setarch
/usr/bin/setpriv
/usr/bin/setsid
/usr/bin/setterm
/usr/bin/sfdisk
/usr/bin/su
/usr/bin/sulogin
/usr/bin/swaplabel
/usr/bin/swapoff
/usr/bin/swapon
/usr/bin/switch_root
/usr/bin/tailf
/usr/bin/taskset
/usr/bin/ul
/usr/bin/umount
/usr/bin/uname26
/usr/bin/unshare
/usr/bin/utmpdump
/usr/bin/uuidd
/usr/bin/uuidgen
/usr/bin/wall
/usr/bin/wdctl
/usr/bin/whereis
/usr/bin/wipefs
/usr/bin/x86_64

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/fstrim.service
/usr/lib/systemd/system/fstrim.timer
/usr/lib/systemd/system/sockets.target.wants/uuidd.socket
/usr/lib/systemd/system/uuidd.service
/usr/lib/systemd/system/uuidd.socket

%files data
%defattr(-,root,root,-)
%exclude /usr/share/bash-completion/completions/fsck.minix
/usr/share/bash-completion/completions/addpart
/usr/share/bash-completion/completions/blkdiscard
/usr/share/bash-completion/completions/blkid
/usr/share/bash-completion/completions/blockdev
/usr/share/bash-completion/completions/cal
/usr/share/bash-completion/completions/cfdisk
/usr/share/bash-completion/completions/chcpu
/usr/share/bash-completion/completions/chrt
/usr/share/bash-completion/completions/col
/usr/share/bash-completion/completions/colcrt
/usr/share/bash-completion/completions/colrm
/usr/share/bash-completion/completions/column
/usr/share/bash-completion/completions/ctrlaltdel
/usr/share/bash-completion/completions/delpart
/usr/share/bash-completion/completions/dmesg
/usr/share/bash-completion/completions/eject
/usr/share/bash-completion/completions/fallocate
/usr/share/bash-completion/completions/fdformat
/usr/share/bash-completion/completions/fdisk
/usr/share/bash-completion/completions/findmnt
/usr/share/bash-completion/completions/flock
/usr/share/bash-completion/completions/fsck
/usr/share/bash-completion/completions/fsck.cramfs
/usr/share/bash-completion/completions/fsfreeze
/usr/share/bash-completion/completions/fstrim
/usr/share/bash-completion/completions/getopt
/usr/share/bash-completion/completions/hexdump
/usr/share/bash-completion/completions/hwclock
/usr/share/bash-completion/completions/ionice
/usr/share/bash-completion/completions/ipcmk
/usr/share/bash-completion/completions/ipcrm
/usr/share/bash-completion/completions/ipcs
/usr/share/bash-completion/completions/isosize
/usr/share/bash-completion/completions/last
/usr/share/bash-completion/completions/ldattach
/usr/share/bash-completion/completions/logger
/usr/share/bash-completion/completions/look
/usr/share/bash-completion/completions/losetup
/usr/share/bash-completion/completions/lsblk
/usr/share/bash-completion/completions/lscpu
/usr/share/bash-completion/completions/lsipc
/usr/share/bash-completion/completions/lslocks
/usr/share/bash-completion/completions/lslogins
/usr/share/bash-completion/completions/lsns
/usr/share/bash-completion/completions/mcookie
/usr/share/bash-completion/completions/mesg
/usr/share/bash-completion/completions/mkfs
/usr/share/bash-completion/completions/mkfs.bfs
/usr/share/bash-completion/completions/mkfs.cramfs
/usr/share/bash-completion/completions/mkfs.minix
/usr/share/bash-completion/completions/mkswap
/usr/share/bash-completion/completions/more
/usr/share/bash-completion/completions/mount
/usr/share/bash-completion/completions/mountpoint
/usr/share/bash-completion/completions/namei
/usr/share/bash-completion/completions/nsenter
/usr/share/bash-completion/completions/partx
/usr/share/bash-completion/completions/pg
/usr/share/bash-completion/completions/pivot_root
/usr/share/bash-completion/completions/prlimit
/usr/share/bash-completion/completions/raw
/usr/share/bash-completion/completions/readprofile
/usr/share/bash-completion/completions/rename
/usr/share/bash-completion/completions/renice
/usr/share/bash-completion/completions/resizepart
/usr/share/bash-completion/completions/rev
/usr/share/bash-completion/completions/rtcwake
/usr/share/bash-completion/completions/runuser
/usr/share/bash-completion/completions/script
/usr/share/bash-completion/completions/scriptreplay
/usr/share/bash-completion/completions/setarch
/usr/share/bash-completion/completions/setpriv
/usr/share/bash-completion/completions/setsid
/usr/share/bash-completion/completions/setterm
/usr/share/bash-completion/completions/sfdisk
/usr/share/bash-completion/completions/su
/usr/share/bash-completion/completions/swaplabel
/usr/share/bash-completion/completions/swapoff
/usr/share/bash-completion/completions/swapon
/usr/share/bash-completion/completions/tailf
/usr/share/bash-completion/completions/taskset
/usr/share/bash-completion/completions/ul
/usr/share/bash-completion/completions/umount
/usr/share/bash-completion/completions/unshare
/usr/share/bash-completion/completions/utmpdump
/usr/share/bash-completion/completions/uuidd
/usr/share/bash-completion/completions/uuidgen
/usr/share/bash-completion/completions/wall
/usr/share/bash-completion/completions/wdctl
/usr/share/bash-completion/completions/whereis
/usr/share/bash-completion/completions/wipefs
/usr/share/bash-completion/completions/zramctl

%files dev
%defattr(-,root,root,-)
/usr/include/blkid/blkid.h
/usr/include/libfdisk/libfdisk.h
/usr/include/libmount/libmount.h
/usr/include/libsmartcols/libsmartcols.h
/usr/include/uuid/uuid.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/util-linux/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*
%exclude /usr/share/doc/util-linux/getopt/getopt-parse.tcsh
%exclude /usr/share/man/man1/login.1

%files extras
%defattr(-,root,root,-)
/usr/bin/fdformat
/usr/bin/i386
/usr/bin/linux32
/usr/bin/mkfs.bfs
/usr/bin/mkfs.cramfs
/usr/bin/zramctl
/usr/share/bash-completion/completions/fsck.minix

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

%files locales -f util-linux.lang 
%defattr(-,root,root,-)

