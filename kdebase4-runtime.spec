Name: kdebase4-runtime
Summary: K Desktop Environment - Base Runtime
Version: 4.7.95
Release: 2
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/kde-runtime-%version.tar.bz2
Patch0: kdebase-runtime-4.5.74-fix-htsearch-path.patch
Patch5: kdebase-runtime-4.3.2-knotify-fix-cpu-charge.patch
Patch8: kdebase-runtime-4.4.1-use-mdv-icon.patch

#(nl) DO NOT REMOVE, NEEDED FOR MDV/ROSA DEFAULT DESKTOP
Patch9: kdebase-runtime-4.6.4-do-not-show-homedesktop.patch
Patch10: kdebase-runtime-4.6.4-do-not-copy-trash.patch

BuildRequires: kdelibs4-devel >= 2:4.5.74
BuildRequires: phonon-devel >= 2:4.4.3
BuildRequires: strigi-devel >= 1:0.5.10-2
BuildRequires: soprano-devel >= 2.6.50
BuildRequires: OpenEXR-devel
BuildRequires: libalsa-devel
BuildRequires: attica-devel
BuildRequires: libxcursor-devel
BuildRequires: libcanberra-devel
BuildRequires: libexiv-devel
BuildRequires: jpeg-devel
BuildRequires: pulseaudio-devel
BuildRequires: libsmbclient-devel
BuildRequires: ssh-devel
BuildRequires: libxine-devel
BuildRequires: automoc4
Requires: kdelibs4-core
Requires: oxygen-icon-theme
Requires: libkactivities 
Suggests: kde4-l10n
Suggests: hicolor-icon-theme
Suggests: kde4-splash-mdv
Suggests: htdig
Suggests: kwallet-daemon
Suggests: kdialog
Suggests: gdb
Suggests: cagibi
Requires: soprano-plugin-redland
Requires: polkit-kde-1
Obsoletes: kdebase4-progs < 1:3.93.0-0.714129.2
Obsoletes: kdebase4-core < 1:3.93.0-0.714129.2
Obsoletes: kdebase4-common <= 1:3.80.3
Conflicts: kdebase4-workspace < 2:4.5.71
Conflicts: kdelibs4-core < 4.1.70
Conflicts: digikam < 0.10.0-1.beta5.2
Conflicts: kappfinder < 1:4.3.0
Conflicts: dolphin < 1:4.3.0
Conflicts: kdepim4-akonadi < 2:4.2.85-3
Conflicts: nepomuk-scribo < 1:0.6.0-3
Conflicts: kdelibs4-core < 2:4.4.86-1

BuildRoot: %_tmppath/%name-%version-%release-root

%description
KDE 4 application runtime components.

%files
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmremotewidgets.conf
%{_sysconfdir}/xdg/menus/kde-information.menu
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/*services/*.service
%{_datadir}/polkit-1/actions/*.policy
#
%_kde_bindir/kcmshell4
%_kde_bindir/kde-cp
%_kde_bindir/kde-mv
%_kde_bindir/kde-open
%_kde_bindir/kde4
%_kde_bindir/kde4-menu
%_kde_bindir/kdebugdialog
%_kde_bindir/kdesu
%_kde_bindir/keditfiletype
%_kde_bindir/kfile4
%_kde_bindir/kglobalaccel
%_kde_bindir/khelpcenter
%_kde_bindir/khotnewstuff-upload
%_kde_bindir/khotnewstuff4
%_kde_bindir/kiconfinder
%_kde_bindir/kioclient
%_kde_bindir/kmimetypefinder
%_kde_bindir/knotify4
%_kde_bindir/kquitapp
%_kde_bindir/kreadconfig
%_kde_bindir/kstart
%_kde_bindir/ksvgtopng
%_kde_bindir/ktraderclient
%_kde_bindir/ktrash
%_kde_bindir/kuiserver
%_kde_bindir/kwriteconfig
%_kde_bindir/nepomukbackup
%_kde_bindir/nepomukserver
%_kde_bindir/nepomukservicestub
%_kde_bindir/nepomukcontroller
%_kde_bindir/nepomukindexer
%_kde_bindir/plasmapkg
%_kde_bindir/plasma-remote-helper
%_kde_bindir/solid-hardware
%_kde_bindir/nepomuk-simpleresource-rcgen
%_kde_datadir/autostart/nepomukcontroller.desktop
%_kde_libdir/kconf_update_bin/phonon_devicepreference_update
%_kde_libdir/kconf_update_bin/phonon_deviceuids_update
%_kde_libdir/kde4/comicbookthumbnail.so
%_kde_libdir/kde4/cursorthumbnail.so
%_kde_libdir/kde4/djvuthumbnail.so
%_kde_libdir/kde4/exrthumbnail.so
%_kde_libdir/kde4/fixhosturifilter.so
%_kde_libdir/kde4/htmlthumbnail.so
%_kde_libdir/kde4/imagethumbnail.so
%_kde_libdir/kde4/jpegthumbnail.so
%_kde_libdir/kde4/kcm_attica.so
%_kde_libdir/kde4/kcm_cgi.so
%_kde_libdir/kde4/kcm_componentchooser.so
%_kde_libdir/kde4/kcm_device_automounter.so
%_kde_libdir/kde4/kcm_emoticons.so
%_kde_libdir/kde4/kcm_filetypes.so
%_kde_libdir/kde4/kcm_icons.so
%_kde_libdir/kde4/kcm_kded.so
%_kde_libdir/kde4/kcm_kdnssd.so
%_kde_libdir/kde4/kcm_knotify.so
%_kde_libdir/kde4/kcm_locale.so
%_kde_libdir/kde4/kcm_nepomuk.so
%_kde_libdir/kde4/kcm_phonon.so
%_kde_libdir/kde4/kcm_trash.so
%_kde_libdir/kde4/kcmspellchecking.so
%_kde_libdir/kde4/kded_desktopnotifier.so
%_kde_libdir/kde4/kded_device_automounter.so
%_kde_libdir/kde4/kded_kpasswdserver.so
%_kde_libdir/kde4/kded_ktimezoned.so
%_kde_libdir/kde4/kded_nepomuksearchmodule.so
%_kde_libdir/kde4/kded_networkstatus.so
%_kde_libdir/kde4/kded_networkwatcher.so
%_kde_libdir/kde4/kded_phononserver.so
%_kde_libdir/kde4/kded_remotedirnotify.so
%_kde_libdir/kde4/kded_solidautoeject.so
%_kde_libdir/kde4/kded_soliduiserver.so
%_kde_libdir/kde4/kio_about.so
%_kde_libdir/kde4/kio_applications.so
%_kde_libdir/kde4/kio_archive.so
%_kde_libdir/kde4/kio_bookmarks.so
%_kde_libdir/kde4/kio_cgi.so
%_kde_libdir/kde4/kio_desktop.so
%_kde_libdir/kde4/kio_filter.so
%_kde_libdir/kde4/kio_finger.so
%_kde_libdir/kde4/kio_fish.so
%_kde_libdir/kde4/kio_floppy.so
%_kde_libdir/kde4/kio_info.so
%_kde_libdir/kde4/kio_man.so
%_kde_libdir/kde4/kio_nepomuk.so
%_kde_libdir/kde4/kio_nepomuksearch.so
%_kde_libdir/kde4/nepomukfileindexer.so
%_kde_libdir/kde4/kio_network.so
%_kde_libdir/kde4/kio_nfs.so
%_kde_libdir/kde4/kio_remote.so
%_kde_libdir/kde4/kio_settings.so
%_kde_libdir/kde4/kio_sftp.so
%_kde_libdir/kde4/kio_thumbnail.so
%_kde_libdir/kde4/kio_timeline.so
%_kde_libdir/kde4/kio_trash.so
%_kde_libdir/kde4/kshorturifilter.so
%_kde_libdir/kde4/kuriikwsfilter.so
%_kde_libdir/kde4/kurisearchfilter.so
%_kde_libdir/kde4/libkmanpart.so
%_kde_libdir/kde4/librenaudioplugin.so
%_kde_libdir/kde4/librenimageplugin.so
%_kde_libdir/kde4/localdomainurifilter.so
%_kde_libdir/kde4/nepomukbackupsync.so
%_kde_libdir/kde4/nepomukfilewatch.so
%_kde_libdir/kde4/nepomukqueryservice.so
%_kde_libdir/kde4/nepomukstorage.so
%_kde_libdir/kde4/plasma-kpart.so
%_kde_libdir/kde4/plasma_appletscript_declarative.so
%_kde_libdir/kde4/plasma_appletscript_simple_javascript.so
%_kde_libdir/kde4/plasma_containment_newspaper.so
%_kde_libdir/kde4/plasma_dataenginescript_javascript.so
%_kde_libdir/kde4/plasma_packagestructure_javascriptaddon.so
%_kde_libdir/kde4/plasma_runnerscript_javascript.so
%_kde_libdir/kde4/svgthumbnail.so
%_kde_libdir/kde4/textthumbnail.so
%_kde_libdir/kde4/imports/org/kde/qtextracomponents/libqtextracomponentsplugin.so
%_kde_libdir/kde4/imports/org/kde/qtextracomponents/qmldir
%_kde_libdir/kde4/windowsexethumbnail.so
%_kde_libdir/kde4/windowsimagethumbnail.so
%_kde_libdir/kde4/imports/org/kde/plasma
%_kde_libdir/kde4/libexec
%_kde_libdir/kde4/plugins
%_kde_libdir/kde4/imports/org/kde/draganddrop/libdragdropplugin.so
%_kde_libdir/kde4/imports/org/kde/draganddrop/qmldir
%_kde_libdir/kde4/platformimports
%_kde_libdir/kde4/kio_smb.so
%_kde_libdir/attica_kde.so
%_kde_libdir/libkdeinit4_kcmshell4.so
%_kde_libdir/libkdeinit4_kglobalaccel.so
%_kde_libdir/libkdeinit4_khelpcenter.so
%_kde_libdir/libkdeinit4_kuiserver.so
%_kde_libdir/libkdeinit4_nepomukserver.so
%_kde_libdir/libknotifyplugin.so
%_kde_libdir/libnepomukcommon.so
%_kde_libdir/libnepomukdatamanagement.so
%_kde_applicationsdir/*.desktop
%_kde_appsdir/desktoptheme
%_kde_appsdir/drkonqi
%_kde_appsdir/hardwarenotifications
%_kde_appsdir/kcm_componentchooser
%_kde_appsdir/kcm_phonon
%_kde_appsdir/kcmlocale
%_kde_appsdir/kconf_update/*.upd
%_kde_appsdir/kde
%_kde_appsdir/kglobalaccel
%_kde_appsdir/khelpcenter
%_kde_appsdir/kio_bookmarks
%_kde_appsdir/kio_desktop
%_kde_appsdir/kio_docfilter
%_kde_appsdir/kio_finger
%_kde_appsdir/kio_info
%_kde_appsdir/konqsidebartng
%_kde_appsdir/ksmserver
%_kde_appsdir/libphonon
%_kde_appsdir/nepomukstorage
%_kde_appsdir/nepomukfilewatch
%_kde_appsdir/fileindexerservice
%_kde_appsdir/phonon
%_kde_appsdir/remoteview
%_kde_appsdir/konqueror/dirtree/remote/smb-network.desktop
%_kde_autostart/nepomukserver.desktop
%_kde_datadir/config.kcfg/*.kcfg
%_kde_configdir/*.knsrc
%_kde_configdir/kshorturifilterrc
%_kde_datadir/desktop-directories/*.directory
%_kde_datadir/emoticons/kde4
%_kde_iconsdir/default.kde4
%_kde_iconsdir/hicolor/*/apps/*
%_kde_services/*.protocol
%_kde_services/comicbookthumbnail.desktop
%_kde_services/componentchooser.desktop
%_kde_services/cursorthumbnail.desktop
%_kde_services/desktopthumbnail.desktop
%_kde_services/device_automounter_kcm.desktop
%_kde_services/directorythumbnail.desktop
%_kde_services/djvuthumbnail.desktop
%_kde_services/emoticons.desktop
%_kde_services/exrthumbnail.desktop
%_kde_services/filetypes.desktop
%_kde_services/fixhosturifilter.desktop
%_kde_services/htmlthumbnail.desktop
%_kde_services/icons.desktop
%_kde_services/imagethumbnail.desktop
%_kde_services/jpegthumbnail.desktop
%_kde_services/kcm_attica.desktop
%_kde_services/kcm_kdnssd.desktop
%_kde_services/kcm_nepomuk.desktop
%_kde_services/kcm_phonon.desktop
%_kde_services/kcmcgi.desktop
%_kde_services/kcmkded.desktop
%_kde_services/kcmnotify.desktop
%_kde_services/kcmtrash.desktop
%_kde_services/kglobalaccel.desktop
%_kde_services/khelpcenter.desktop
%_kde_services/kmanpart.desktop
%_kde_services/knotify4.desktop
%_kde_services/kshorturifilter.desktop
%_kde_services/kuiserver.desktop
%_kde_services/kuriikwsfilter.desktop
%_kde_services/kurisearchfilter.desktop
%_kde_services/language.desktop
%_kde_services/localdomainurifilter.desktop
%_kde_services/nepomukbackupsync.desktop
%_kde_services/nepomukfilewatch.desktop
%_kde_services/nepomukqueryservice.desktop
%_kde_services/nepomukremovablestorageservice.desktop
%_kde_services/nepomukstorage.desktop
%_kde_services/nepomukstrigiservice.desktop
%_kde_services/nepomukontologyloader.desktop
%_kde_services/nepomukactivitiesservice.desktop
%_kde_services/nepomukfileindexer.desktop
%_kde_services/plasma-containment-newspaper.desktop
%_kde_services/plasma-kpart.desktop
%_kde_services/plasma-packagestructure-javascript-addon.desktop
%_kde_services/plasma-scriptengine-applet-declarative.desktop
%_kde_services/plasma-scriptengine-applet-simple-javascript.desktop
%_kde_services/plasma-scriptengine-dataengine-javascript.desktop
%_kde_services/plasma-scriptengine-runner-javascript.desktop
%_kde_services/renaudiodlg.desktop
%_kde_services/renimagedlg.desktop
%_kde_services/searchproviders
%_kde_services/spellchecking.desktop
%_kde_services/svgthumbnail.desktop
%_kde_services/textthumbnail.desktop
%_kde_services/windowsexethumbnail.desktop
%_kde_services/windowsimagethumbnail.desktop
%_kde_services/kded/*.desktop
%_kde_servicetypes/*.desktop
%_kde_datadir/locale/currency
%_kde_datadir/locale/l10n/*/*
%_kde_datadir/locale/l10n/*.desktop
%_kde_mandir/man?/*
%_kde_datadir/mime/packages/*.xml
%_kde_datadir/ontology/kde/*
%_kde_datadir/sounds/*
%doc %_kde_docdir/HTML/en/*

#--------------------------------------------------------------

%package -n phonon-xine-kcm 
Summary: Phonon Xine KCM
Group: Development/KDE and Qt

%description -n phonon-xine-kcm
This package provide the KCM for Phonon Xine.

%files -n phonon-xine-kcm
%_kde_libdir/kde4/kcm_phononxine.so
%_kde_datadir/kde4/services/kcm_phononxine.desktop

#--------------------------------------------------------------

%package -n kwallet-daemon
Summary: Kwallet daemon
Group: Development/KDE and Qt
Conflicts: %{name} < 1:4.5.71

%description -n kwallet-daemon
Kwallet daemon.

%files -n kwallet-daemon
%_kde_bindir/kwalletd
%_kde_libdir/libkdeinit4_kwalletd.so
%_kde_appsdir/kwalletd
%_kde_services/kwalletd.desktop

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
%_kde_libdir/libmolletnetwork.so.%{molletnetwork_major}*

#--------------------------------------------------------------

%define nepomuksync_major 4
%define libnepomuksync %mklibname nepomuksync %nepomuksync_major

%package -n %libnepomuksync
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libnepomuksync
KDE 4 core library.

%files -n %libnepomuksync
%_kde_libdir/libnepomuksync.so.%{nepomuksync_major}*

#-----------------------------------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Header files and documentation for compiling KDE applications
Requires: kdelibs4-devel >= 2:4.5.71
Requires: %name = %epoch:%version
Requires: %libkwalletbackend = %epoch:%version
Requires: %libmolletnetwork = %epoch:%version
Requires: %libnepomuksync = %epoch:%version

%description devel
This package includes the header files you will need to compile applications
for KDE. Also included is the KDE API documentation in HTML format for easy
browsing.

%files devel
%{_kde_includedir}/*.h
%{_kde_includedir}/nepomuk
%{_kde_libdir}/libkwalletbackend.so
%{_kde_libdir}/libmolletnetwork.so
%{_kde_libdir}/libnepomuksync.so
%{_kde_appsdir}/cmake/modules/*.cmake

#-----------------------------------------------------------------------------

%prep
%setup -q -n kde-runtime-%version

%patch0 -p1 -b .htsearch
%patch5 -p1 -b .bug_49814
%patch8 -p0
%patch9 -p0
%patch10 -p1

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

rm -f %buildroot%_kde_iconsdir/hicolor/index.theme

mkdir -p %{buildroot}%{_kde_bindir}
ln -s %_kde_libdir/kde4/libexec/kdesu %{buildroot}%{_kde_bindir}/kdesu
