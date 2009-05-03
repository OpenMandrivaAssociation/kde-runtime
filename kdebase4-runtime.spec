%define kderevision svn961800

Name: kdebase4-runtime
Summary: K Desktop Environment - Base Runtime
Version: 4.2.71
Release: %mkrel 0.%kderevision.1
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-runtime-%version.%kderevision.tar.bz2
Patch2: kdebase-runtime-4.1.1-fix-htsearch-path.patch
# Patches from trunk
#Testing
Patch301: kdebase-runtime-4.2.0-mandriva-pulseaudio-ignore-audiodevices.patch
BuildRequires: kde4-macros
BuildRequires: kdelibs4-devel >= 2:4.1.81
BuildRequires: kdepimlibs4-devel >= 2:4.1.81
BuildRequires: strigi-devel >= 1:0.5.10-2
BuildRequires: soprano-devel >= 2.0.98
BuildRequires: fontconfig-devel >= 2.1-9mdk
BuildRequires: pam-devel
BuildRequires: freetype2-devel
BuildRequires: libsasl-devel
BuildRequires: openldap-devel
BuildRequires: avahi-compat-libdns_sd-devel 
BuildRequires: avahi-client-devel
BuildRequires: libsmbclient-devel > 3.0
BuildRequires: libieee1284-devel
BuildRequires: OpenEXR-devel
BuildRequires: hal-devel 
BuildRequires: libusb-devel
BuildRequires: libxml2-utils
BuildRequires: X11-devel
BuildRequires: GL-devel
BuildRequires: bdftopcf
BuildRequires: imake
BuildRequires: libraw1394-devel
BuildRequires: libxklavier-devel
BuildRequires: lua-devel
BuildRequires: resmgr-devel
BuildRequires: bluez-devel
BuildRequires: boost-devel
BuildRequires: xrdb
BuildRequires: qimageblitz-devel
Requires: kdelibs4-core
Requires: oxygen-icon-theme
Requires: hicolor-icon-theme
Requires: kde4-l10n
Requires: kde4-splash-mdv
Requires: htdig
Requires: kwallet-daemon
Suggests: gdb
Obsoletes: kdebase4-progs < 1:3.93.0-0.714129.2
Obsoletes: kdebase4-core  < 1:3.93.0-0.714129.2
Obsoletes: kdebase4-common <= 1:3.80.3
Conflicts: kdebase4-workspace < 2:4.1.70
Conflicts: kdelibs4-core < 4.1.70
Conflicts: nepomuk-kde < 4.1.71-0.878903.1
Conflicts: kdebase-common < 1:3.5.9-38
Conflicts: kdebase-progs < 1:3.5.9-38
Conflicts: kdebase-konsole < 1:3.5.9-38
Conflicts: digikam < 0.10.0-1.beta5.2
Conflicts: kappfinder < 1:4.1.96-2
Conflicts: dolphin < 1:4.2.2-8
BuildRoot: %_tmppath/%name-%version-%release-root

%description
KDE 4 application runtime components.

%files
%defattr(-,root,root)
%_datadir/dbus-1/services/*
%_kde_appsdir/drkonqi
%_kde_appsdir/kcm_componentchooser
%_kde_appsdir/kcmlocale
%_kde_appsdir/kde
%_kde_appsdir/kio_finger/kio_finger.css
%_kde_appsdir/kio_finger/kio_finger.pl
%_kde_appsdir/kio_info/kde-info2html
%_kde_appsdir/kio_info/kde-info2html.conf
#%_kde_appsdir/kio_man/kio_man.css
%_kde_appsdir/kio_thumbnail/*
%_kde_autostart/nepomukserver.desktop
%_kde_bindir/kuiserver
%_kde_appsdir/kstyle
%_kde_bindir/ksvgtopng
%_kde_bindir/kcmshell4
%_kde_bindir/kde4-menu
%_kde_bindir/kdebugdialog
%_kde_bindir/kde-cp
%_kde_bindir/kde-mv
%_kde_bindir/kde-open
%_kde_bindir/kfile4
%_kde_bindir/khotnewstuff4
%_kde_bindir/kioclient
%_kde_bindir/kmimetypefinder
%_kde_libdir/strigi/strigiindex_sopranobackend.so
%_kde_datadir/applications/kde4/knetattach.desktop
%_kde_docdir/*/*/knetattach
%_kde_bindir/knotify4
%_kde_bindir/kquitapp
%_kde_bindir/kreadconfig
%_kde_bindir/kstart
%_kde_bindir/ktraderclient
%_kde_bindir/ktrash
%_kde_bindir/kwriteconfig
%_kde_bindir/kde4
%_kde_bindir/kiconfinder
%_kde_bindir/nepomukserver
%_kde_bindir/nepomukservicestub
%_kde_bindir/solid-hardware
%_kde_bindir/keditfiletype
%_kde_bindir/kglobalaccel
%_kde_sysconfdir/xdg/menus/kde-information.menu
%_kde_datadir/applications/kde4/Help.desktop
%_kde_datadir/config/khotnewstuff.knsrc
%_kde_datadir/config/kshorturifilterrc
%_kde_datadir/desktop-directories
%_kde_datadir/kde4/services/*
%_kde_datadir/kde4/servicetypes/*
%_kde_appsdir/remoteview/smb-network.desktop
%_kde_appsdir/kio_bookmarks
%_kde_appsdir/kio_desktop
%_kde_datadir/locale/l10n/*/*
%_kde_datadir/locale/l10n/*.desktop
%_kde_datadir/locale/en_US
%_kde_datadir/sounds
%_kde_libdir/kde4/*
%_kde_libdir/libkdeinit4_*
%_kde_libdir/kconf_update_bin/phonon_devicepreference_update
%_kde_libdir/kconf_update_bin/phonon_deviceuids_update
%_kde_appsdir/kcm_phonon
%_kde_appsdir/kconf_update/devicepreference.upd
%_kde_appsdir/libphonon
%_kde_appsdir/phonon
%_kde_bindir/khelpcenter
%_kde_appsdir/khelpcenter
%_kde_docdir/*/*/khelpcenter
%_kde_docdir/*/*/kcontrol
%_kde_docdir/*/*/kdesu
%_kde_mandir/man1/kdesu.1.*
%_kde_docdir/*/*/kioslave
%_kde_docdir/*/*/kdebugdialog
%_kde_datadir/apps/kconf_update/kuriikwsfilter.upd
%_kde_datadir/apps/konqueror/dirtree/remote/smb-network.desktop
%_kde_datadir/apps/cmake/modules/*
%_kde_datadir/config.kcfg/*
%_kde_appsdir/ksmserver/windowmanagers
%_kde_appsdir/nepomukstrigiservice/nepomukstrigiservice.notifyrc
%_kde_appsdir/nepomukstorage/nepomukstorage.notifyrc
%_kde_appsdir/nepomuk/ontologies
%_kde_appsdir/kio_docfilter
#%_kde_appsdir/kconf_update/kdedglobalaccel_kde42.upd
%_kde_configdir/emoticons.knsrc
%_kde_iconsdir/hicolor/*/*/*
%_kde_datadir/emoticons/*
%_kde_datadir/config/icons.knsrc
%_kde_iconsdir/default.kde4
%_kde_appsdir/desktoptheme/default
%exclude %_kde_iconsdir/hicolor/index.theme
 
#--------------------------------------------------------------

%package -n kwallet-daemon
Summary: Kwallet daemon
Group: Development/KDE and Qt

%description -n kwallet-daemon
Kwallet daemon.

%files -n kwallet-daemon
%defattr(-,root,root)
%_kde_bindir/kwalletd
%_kde_appsdir/kwalletd

#--------------------------------------------------------------

%define kwalletbackend_major 4
%define libkwalletbackend %mklibname kwalletbackend %kwalletbackend_major

%package -n %libkwalletbackend
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kwalletbackend5 < 3.93.0-0.714006.1

%description -n %libkwalletbackend
KDE 4 core library.

%if %mdkversion < 200900
%post -n %libkwalletbackend -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkwalletbackend -p /sbin/ldconfig
%endif

%files -n %libkwalletbackend
%defattr(-,root,root)
%_kde_libdir/libkwalletbackend.so.%{kwalletbackend_major}*

#-----------------------------------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Header files and documentation for compiling KDE applications
Requires: kdelibs4-devel
Requires: %name = %epoch:%version
Requires:  %libkwalletbackend = %epoch:%version

%description devel
This package includes the header files you will need to compile applications
for KDE. Also included is the KDE API documentation in HTML format for easy
browsing.

%files devel
%defattr(-,root,root,-)
%{_kde_libdir}/libkwalletbackend.so
%{_kde_datadir}/dbus-1/interfaces/*

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdebase-runtime-%version.%kderevision
%patch2 -p1
#Test patches
%patch301 -p1
%build
%cmake_kde4 

%make


%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

