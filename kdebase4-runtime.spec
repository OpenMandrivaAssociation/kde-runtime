%define branch 1
%{?_branch: %{expand: %%global branch 1}}
%define revision 746973

Name: kdebase4-runtime
Summary: K Desktop Environment
Version: 3.97.1
Release: %mkrel 1
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-runtime-%version.%revision.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-runtime-%version.tar.bz2
%endif
BuildRequires: kde4-macros
BuildRequires: cmake
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: strigi-devel
BuildRequires: soprano-devel
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
BuildRequires: libnetworkmanager-util-devel
BuildRequires: networkmanager-devel
BuildRequires: bluez-devel
BuildRequires: boost-devel
BuildRequires: xrdb
BuildRequires: qimageblitz-devel
Requires: kdelibs4-core
Requires: oxygen-icon-theme
Requires: phonon-xine
Obsoletes: kdebase4-progs < 1:3.93.0-0.714129.2
Obsoletes: kdebase4-core  < 1:3.93.0-0.714129.2
Obsoletes: kdebase4-common <= 1:3.80.3
Conflicts: kdebase4-workspace < 1:3.94.1-0.728613.1

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
%_kde_appsdir/kio_thumbnail/pics/thumbnailfont_7x4.png
%_kde_bindir/kuiserver
%_kde_libdir/libkdeinit4_kuiserver.so
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
%_kde_configdir/xdg/menus/kde-information.menu
%_kde_datadir/applications/kde4/Help.desktop
%_kde_datadir/config/khotnewstuffrc
%_kde_datadir/config/kshorturifilterrc
%_kde_datadir/desktop-directories
%dir %_kde_datadir/kde4/services
%_kde_datadir/kde4/services/*
%dir %_kde_datadir/kde4/servicetypes
%_kde_datadir/kde4/servicetypes/*
%_kde_appsdir/remoteview/smb-network.desktop
%_kde_datadir/locale/l10n/*/*
%_kde_datadir/locale/l10n/*.desktop
%_kde_datadir/locale/en_US
%_kde_datadir/sounds
%dir %_kde_libdir/kde4
%_kde_libdir/kde4/*
%_kde_libdir/libkdeinit4_kcmshell4.so
%_kde_libdir/libkdeinit4_khelpcenter.so
%_kde_bindir/khelpcenter
%_kde_appsdir/khelpcenter
%_kde_docdir/*/*/khelpcenter
%_kde_docdir/*/*/kcontrol
%_kde_docdir/*/*/kdesu
%_kde_datadir/man/man1/kdesu.1
%_kde_docdir/*/*/kioslave
%_kde_docdir/*/*/kdebugdialog
%_kde_datadir/apps/kconf_update/kuriikwsfilter.upd
%_kde_datadir/apps/konqueror/dirtree/remote/smb-network.desktop
%_kde_datadir/apps/cmake/modules/*
%_kde_datadir/config.kcfg/*
%_datadir/dbus-1/interfaces/*
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

%description -n oxygen-icon-theme
Oxygen KDE 4 icon theme. Complains with FreeDesktop.org naming schema

%files -n oxygen-icon-theme
%defattr(-,root,root,-)
%dir %_kde_iconsdir/oxygen
%_kde_iconsdir/*/index.theme
%_kde_iconsdir/*/*/*/*
%_kde_datadir/emoticons/*
%_kde_iconsdir/oxygen/scalable/export_pngs.sh

#-----------------------------------------------------------------------------

%package -n phonon-xine
Summary: Xine backend to Phonon
Group: Sound
BuildRequires: libxine-devel
Obsoletes: kde4-phonon-xine < 1:3.93.0-0.714129.2

%description -n phonon-xine
Xine backend to Phonon.

%files -n phonon-xine
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_phononxine.so
%_kde_libdir/kde4/phonon_xine.so
%_kde_datadir/kde4/services/kcm_phononxine.desktop
%_kde_datadir/kde4/services/phononbackends/xine.desktop

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

# kcalc.svgz crashes kicker
rm -rf %buildroot/%_kde_iconsdir/oxygen/scalable/apps/small/16x16/kcalc.svgz

%clean
rm -fr %buildroot

