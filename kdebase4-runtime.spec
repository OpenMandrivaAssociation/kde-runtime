Name:          kdebase4-runtime
Summary:       K Desktop Environment
Version: 4.0.82
Epoch:         1
Group:         Graphical desktop/KDE
License:       GPL
URL:           http://www.kde.org
Release: %mkrel 2
Source:        ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-runtime-%version.tar.bz2
BuildRequires: kde4-macros
BuildRequires: cmake
BuildRequires: kdelibs4-devel >= %version
BuildRequires: kdepimlibs4-devel >= %version
BuildRequires: strigi-devel
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
Requires:      kdelibs4-core
Requires:      oxygen-icon-theme
Requires:      phonon-xine
Requires:      kde4-l10n
Obsoletes:     kdebase4-progs < 1:3.93.0-0.714129.2
Obsoletes:     kdebase4-core  < 1:3.93.0-0.714129.2
Obsoletes:     kdebase4-common <= 1:3.80.3
Conflicts:     kdebase4-workspace <= 1:4.0.68-1
# (Anssi 05/2008) KDE3 before move to /opt/kde3:
Conflicts:     kdebase-common < 1:3.5.9-38
Conflicts:     kdebase-progs < 1:3.5.9-38
Conflicts:     kdebase-konsole < 1:3.5.9-38
BuildRoot:     %_tmppath/%name-%version-%release-root

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
%_kde_appsdir/kio_man/kio_man.css
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
%_kde_sysconfdir/xdg/menus/kde-information.menu
%_kde_datadir/applications/kde4/Help.desktop
%_kde_datadir/config/khotnewstuff.knsrc
%_kde_datadir/config/kshorturifilterrc
%_kde_datadir/desktop-directories
%_kde_datadir/kde4/services/*
%_kde_datadir/kde4/servicetypes/*
%_kde_appsdir/remoteview/smb-network.desktop
%_kde_datadir/locale/l10n/*/*
%_kde_datadir/locale/l10n/*.desktop
%_kde_datadir/locale/en_US
%_kde_datadir/sounds
%_kde_libdir/kde4/*
%_kde_libdir/libkdeinit4_*
%_kde_libdir/kconf_update_bin/phonon_devicepreference_update
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
%_datadir/dbus-1/interfaces/*
#(nl) Excluding because they are on Phonon-xine
%exclude %_kde_libdir/kde4/kcm_phononxine.so
%exclude %_kde_libdir/kde4/phonon_xine.so
%exclude %_kde_datadir/kde4/services/kcm_phononxine.desktop
%exclude %_kde_datadir/kde4/services/phononbackends/xine.desktop

#--------------------------------------------------------------

%package -n oxygen-icon-theme
Group: Graphical desktop/KDE
Summary: Oxygen icon theme
Provides: kde4-icon-theme
Obsoletes: kdelibs4-common >= 30000000:3.80.3
# Fallback hicolor icons
Requires: hicolor-icon-theme
# (Anssi 05/2008) KDE3 before move to /opt/kde3:
Conflicts: kdebase-common < 1:3.5.9-38

%description -n oxygen-icon-theme
Oxygen KDE 4 icon theme. Complains with FreeDesktop.org naming schema

%files -n oxygen-icon-theme
%defattr(-,root,root,-)
%_kde_configdir/emoticons.knsrc
%_kde_iconsdir/oxygen
%_kde_iconsdir/hicolor/*/*/*
%_kde_datadir/emoticons/*
%_kde_datadir/config/icons.knsrc
%_kde_iconsdir/default.kde4
%exclude %_kde_iconsdir/hicolor/index.theme
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.*

#-----------------------------------------------------------------------------

%package -n phonon-xine
Summary: Xine backend to Phonon
Group: Sound
BuildRequires: libxine-devel
Obsoletes: kde4-phonon-xine < 1:3.93.0-0.714129.2
#fhimpe: fix bug #41210: without xine-plugins phonon-xine always crashes
Requires: xine-plugins

%description -n phonon-xine
Xine backend to Phonon.

%files -n phonon-xine
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_phononxine.so
%_kde_libdir/kde4/phonon_xine.so
%_kde_datadir/kde4/services/kcm_phononxine.desktop
%_kde_datadir/kde4/services/phononbackends/xine.desktop

#-----------------------------------------------------------------------------
 
%define kaudiodevicelist_major 4
%define libkaudiodevicelist %mklibname kaudiodevicelist %kaudiodevicelist_major

%package -n %libkaudiodevicelist
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: %{_lib}kdecore5 >= 30000000:3.80.3
Obsoletes: %{_lib}kaudiodevicelist5 < 3.93.0-0.714006.1
Obsoletes: %{_lib}cupsdconf4 < 3.93.0-0.728415.2
Obsoletes: %{_lib}kdefx5 < 3.93.0-0.728415.2
Obsoletes: %{_lib}kdeprint_management4 < 3.94.1-0.728203.3
Obsoletes: %{_lib}kdeprint5 < 3.94.1-0.728203.3

%description -n %libkaudiodevicelist
KDE 4 core library.

%post -n %libkaudiodevicelist -p /sbin/ldconfig
%postun -n %libkaudiodevicelist -p /sbin/ldconfig

%files -n %libkaudiodevicelist
%defattr(-,root,root)
%_kde_libdir/libkaudiodevicelist.so.%{kaudiodevicelist_major}*

#-----------------------------------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Header files and documentation for compiling KDE applications
Requires: kdelibs4-devel
Requires: %libkaudiodevicelist = %version

%description devel
This package includes the header files you will need to compile applications
for KDE. Also included is the KDE API documentation in HTML format for easy
browsing.

%files devel
%defattr(-,root,root,-)
%{_kde_includedir}/phonon
%{_kde_libdir}/libkaudiodevicelist.so

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdebase-runtime-%version

%build
%cmake_kde4 

%make


%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %buildroot%{_var}/lib/rpm/filetriggers
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.filter << EOF
^./usr/share/icons/oxygen/
EOF
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/oxygen
fi
EOF
chmod 755 %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-oxygen.script

%clean
rm -fr %buildroot

