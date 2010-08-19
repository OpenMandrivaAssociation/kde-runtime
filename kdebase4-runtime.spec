%define branch 0
%{?_branch: %{expand: %%global branch 1}}


%if %branch
%define kde_snapshot svn1138650
%endif

Name: kdebase4-runtime
Summary: K Desktop Environment - Base Runtime
Version: 4.5.0
Release: %mkrel 2
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-runtime-%version%kde_snapshot.tar.bz2
%else
Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-runtime-%version.tar.bz2
%endif
Patch0: kdebase-runtime-4.1.1-fix-htsearch-path.patch
Patch1: kdebase-runtime-4.2.95-fix-desktop-files.patch
Patch3: kdebase-runtime-nepomuk-strigi2.patch
Patch5: kdebase-runtime-4.3.2-knotify-fix-cpu-charge.patch
Patch6: kdebase-runtime-nepomuk-strigi-eventmonitor.patch
Patch8: kdebase-runtime-4.4.1-use-mdv-icon.patch
Patch9: kdebase-runtime-nepomuk-strigi-smartfile.patch
# Branch patches 100 -> 199

# Trunk patches 200 -> 299

# Testing Patches 300 -> ...
Patch300: kdebase-runtime-4.5-speakersetup.patch
Patch301: kdebase-runtime-4.5-alsa-global-config.patch

BuildRequires: kde4-macros
BuildRequires: kdelibs4-devel >= 2:%version
BuildRequires: kdepimlibs4-devel >= 2:%version
BuildRequires: strigi-devel >= 1:0.5.10-2
BuildRequires: soprano-devel >= 2.3.67
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
BuildRequires: GL-devel
BuildRequires: bdftopcf
BuildRequires: imake
BuildRequires: libraw1394-devel
BuildRequires: libxklavier-devel
BuildRequires: lua-devel
BuildRequires: bluez-devel
BuildRequires: boost-devel
BuildRequires: xrdb
BuildRequires: qimageblitz-devel
BuildRequires: pulseaudio-devel
BuildRequires: openslp-devel 
BuildRequires: ssh-devel >= 0.4.2
BuildRequires: libxine-devel
BuildRequires: libssh-devel >= 0.3.92
BuildRequires: attica-devel
BuildRequires: shared-desktop-ontologies-devel >= 0.4
BuildRequires: libexiv-devel
Requires: kdelibs4-core
Requires: oxygen-icon-theme
Suggests: kde4-l10n
Suggests: hicolor-icon-theme
Suggests: kde4-splash-mdv
Suggests: htdig
Suggests: kwallet-daemon
Suggests: kdialog
Suggests: gdb
Suggests: cagibi
Requires:  soprano-plugin-redland
Requires:  polkit-kde-1
Obsoletes: kdebase4-progs < 1:3.93.0-0.714129.2
Obsoletes: kdebase4-core  < 1:3.93.0-0.714129.2
Obsoletes: kdebase4-common <= 1:3.80.3
Conflicts: kdebase4-workspace < 2:4.2.87-1
Conflicts: kdelibs4-core < 4.1.70
%if %mdkversion >= 201000
Obsoletes: kdebase3 < 1:3.5.10-24
Obsoletes: kdebase3-common < 1:3.5.10-24
Obsoletes: kdebase3-progs < 1:3.5.10-24
Obsoletes: kdebase3-konsole < 1:3.5.10-24
Obsoletes: kdebase < 1:3.5.10-24
Obsoletes: kdebase-common < 1:3.5.10-24
Obsoletes: kdebase-progs < 1:3.5.10-24
Obsoletes: kdebase-konsole < 1:3.5.10-24
Obsoletes: krootwarning < 2:2008.1.1-10
Obsoletes: krozat < 2:2008.1.6-5
Obsoletes: ksplash-engine-moodin < 0.4.2-15
Obsoletes: mdklaunchhelp < 2:2007-3
%endif
Conflicts: digikam < 0.10.0-1.beta5.2
Conflicts: kappfinder < 1:4.3.0
Conflicts: dolphin < 1:4.3.0
Conflicts: kdepim4-akonadi < 2:4.2.85-3
Conflicts: nepomuk-scribo < 1:0.6.0-3
Conflicts: kdelibs4-core <  2:4.4.86-1

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
%_kde_autostart/nepomukserver.desktop
%_kde_bindir/kuiserver
%_kde_bindir/ksvgtopng
%_kde_bindir/kcmshell4
%_kde_bindir/kde4-menu
%_kde_bindir/kdebugdialog
%_kde_bindir/kde-cp
%_kde_bindir/kde-mv
%_kde_bindir/kde-open
%_kde_bindir/kfile4
%_kde_bindir/khotnewstuff4
%_kde_bindir/khotnewstuff-upload
%_kde_bindir/kioclient
%_kde_bindir/kmimetypefinder
%_kde_bindir/plasmapkg
%_kde_libdir/strigi/strigiindex_nepomukbackend.so
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
%_kde_appsdir/remoteview/network.desktop
%_kde_appsdir/kio_bookmarks
%_kde_appsdir/kio_desktop
%_kde_appsdir/kglobalaccel
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
%_kde_mandir/man1/kdesu.1*
%_kde_mandir/man8/nepomukserver.8*
%_kde_mandir/man8/nepomukservicestub.8*
%_kde_docdir/*/*/kioslave
%_kde_docdir/*/*/kdebugdialog
%_kde_docdir/*/*/network
%_kde_datadir/apps/kconf_update/kuriikwsfilter.upd
%_kde_appsdir/konqueror/dirtree/remote/smb-network.desktop
%_kde_appsdir/konqsidebartng/virtual_folders/remote/virtualfolder_network.desktop
%_kde_datadir/apps/cmake/modules/*
%_kde_datadir/config.kcfg/*
%_kde_appsdir/ksmserver/windowmanagers
%_kde_appsdir/nepomukstorage
%_kde_appsdir/kio_docfilter
%_kde_configdir/emoticons.knsrc
%_kde_iconsdir/hicolor/*/*/*
%_kde_datadir/emoticons/*
%_kde_datadir/config/icons.knsrc
%_kde_iconsdir/default.kde4
%_kde_appsdir/desktoptheme/default
%_kde_appsdir/desktoptheme/oxygen
%_kde_datadir/mime/packages/network.xml
%_kde_appsdir/nepomukstrigiservice
%_kde_libdir/attica_kde.so
%_kde_datadir/config/khotnewstuff_upload.knsrc
%_kde_datadir/locale/currency
%_kde_appsdir/hardwarenotifications
%_sysconfdir/dbus-1/system.d/org.kde.kcontrol.kcmremotewidgets.conf
%_kde_datadir/dbus-1/system-services/org.kde.kcontrol.kcmremotewidgets.service
%_kde_datadir/polkit-1/actions/org.kde.kcontrol.kcmremotewidgets.policy
%exclude %_kde_iconsdir/hicolor/index.theme
%exclude %_kde_libdir/kde4/kcm_phononxine.so
%exclude %_kde_datadir/kde4/services/kcm_phononxine.desktop

#--------------------------------------------------------------

%package -n phonon-xine-kcm 
Summary:    Phonon Xine KCM
Group: Development/KDE and Qt

%description -n phonon-xine-kcm
This package provide the KCM for Phonon Xine.

%files -n phonon-xine-kcm
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_phononxine.so
%_kde_datadir/kde4/services/kcm_phononxine.desktop

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

%files -n %libkwalletbackend
%defattr(-,root,root)
%_kde_libdir/libkwalletbackend.so.%{kwalletbackend_major}*

#--------------------------------------------------------------

%define molletnetwork_major 4
%define libmolletnetwork %mklibname molletnetwork %molletnetwork_major

%package -n %libmolletnetwork
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libmolletnetwork
KDE 4 core library.

%files -n %libmolletnetwork
%defattr(-,root,root)
%_kde_libdir/libmolletnetwork.so.%{molletnetwork_major}*

#-----------------------------------------------------------------------------

%package   devel
Group:     Development/KDE and Qt
Summary:   Header files and documentation for compiling KDE applications
Requires:  kdelibs4-devel >= 2:4.2.96
Requires:  kdelibs4-experimental-devel >= 4.2.96
Requires:  %name = %epoch:%version
Requires:  %libkwalletbackend = %epoch:%version
Requires:  %libmolletnetwork = %epoch:%version

%description devel
This package includes the header files you will need to compile applications
for KDE. Also included is the KDE API documentation in HTML format for easy
browsing.

%files devel
%defattr(-,root,root,-)
%{_kde_libdir}/libkwalletbackend.so
%{_kde_libdir}/libmolletnetwork.so
%{_kde_datadir}/dbus-1/interfaces/*

#-----------------------------------------------------------------------------

%prep
%if %branch
%setup -q -n kdebase-runtime-%version%kde_snapshot
%else
%setup -q -n kdebase-runtime-%version
%endif

#%patch0 -p1
%patch1 -p0
%patch5 -p1 -b .bug_49814
%patch8 -p0
%patch9 -p0 -b .nepomuk
%patch300 -p1
%patch301 -p1
%build
%cmake_kde4
%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

