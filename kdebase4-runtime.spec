Name:		kdebase4-runtime
Summary:	K Desktop Environment - Base Runtime
Version:	4.10.3
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPL
URL:		http://www.kde.org
%define is_beta %(if test `echo %version |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/kde-runtime-%{version}.tar.xz
Source1:	kdebase4-runtime.rpmlintrc
Patch0:		kdebase-runtime-4.5.74-fix-htsearch-path.patch
Patch1:		kde-runtime-4.9.98-link-tirpc.patch
# See http://bugs.rosalinux.ru/show_bug.cgi?id=1902
Patch2:		kde-runtime-4.10.2-kdesu-encoding.patch
Patch5:		kdebase-runtime-4.3.2-knotify-fix-cpu-charge.patch
Patch8:		kdebase-runtime-4.4.1-use-mdv-icon.patch

#(nl) DO NOT REMOVE, NEEDED FOR MDV/ROSA DEFAULT DESKTOP
Patch9:		kdebase-runtime-4.6.4-do-not-show-homedesktop.patch
Patch10:	kdebase-runtime-4.6.4-do-not-copy-trash.patch

Patch100:	kdebase-runtime-4.8.0-knetattachxdg.patch
Patch101:	kde-runtime-4.10.0-l10n-ru.patch
Patch102:	kde-runtime-4.8.2-save-i18n-settings.patch
Patch103:	kde-runtime-4.9.3-kcmlocale-fix-translations.patch

BuildRequires:	kdelibs4-devel >= 5:4.9.98-2
BuildRequires:	kdepimlibs4-devel
BuildRequires:	nepomuk-core-devel
BuildRequires:	jpeg-devel
BuildRequires:	ssh-devel
BuildRequires:	automoc4
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(libattica)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libstreams)
BuildRequires:	pkgconfig(NetworkManager)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(soprano)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(libtirpc)
BuildRequires:	pkgconfig(libntrack-qt4)
BuildRequires:	ntrack-devel
BuildRequires:	openslp-devel

Requires:	kdelibs4-core
Requires:	oxygen-icon-theme
Requires:	libkactivities
Suggests:	kde4-l10n
Suggests:	hicolor-icon-theme
Suggests:	kde4-splash-mdv
Suggests:	htdig
Suggests:	kwallet-daemon
Suggests:	kdialog
Suggests:	gdb
Suggests:	cagibi
Requires:	soprano-plugin-redland
Requires:	polkit-kde-1
Conflicts:	kdebase4-workspace < 2:4.10.0
Conflicts:	nepomuk-scribo < 1:0.6.0-3

%description
KDE 4 application runtime components.

%files
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmremotewidgets.conf
%{_sysconfdir}/xdg/menus/kde-information.menu
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/*services/*.service
%{_datadir}/polkit-1/actions/*.policy
#
%{_kde_bindir}/kcmshell4
%{_kde_bindir}/kde-cp
%{_kde_bindir}/kde-mv
%{_kde_bindir}/kde-open
%{_kde_bindir}/kde4
%{_kde_bindir}/kde4-menu
%{_kde_bindir}/kdebugdialog
%{_kde_bindir}/kdesu
%{_kde_bindir}/keditfiletype
%{_kde_bindir}/kfile4
%{_kde_bindir}/kglobalaccel
%{_kde_bindir}/khelpcenter
%{_kde_bindir}/khotnewstuff-upload
%{_kde_bindir}/khotnewstuff4
%{_kde_bindir}/kiconfinder
%{_kde_bindir}/kioclient
%{_kde_bindir}/kmimetypefinder
%{_kde_bindir}/knotify4
%{_kde_bindir}/kquitapp
%{_kde_bindir}/kreadconfig
%{_kde_bindir}/kstart
%{_kde_bindir}/ksvgtopng
%{_kde_bindir}/ktraderclient
%{_kde_bindir}/ktrash
%{_kde_bindir}/kuiserver
%{_kde_bindir}/kwriteconfig
%{_kde_bindir}/nepomukcontroller
%{_kde_bindir}/plasmapkg
%{_kde_bindir}/plasma-remote-helper
%{_kde_bindir}/solid-hardware
%{_kde_autostart}/nepomukcontroller.desktop
%{_kde_libdir}/kconf_update_bin/phonon_devicepreference_update
%{_kde_libdir}/kconf_update_bin/phonon_deviceuids_update
%{_kde_libdir}/kde4/comicbookthumbnail.so
%{_kde_libdir}/kde4/cursorthumbnail.so
%{_kde_libdir}/kde4/djvuthumbnail.so
%{_kde_libdir}/kde4/exrthumbnail.so
%{_kde_libdir}/kde4/fixhosturifilter.so
%{_kde_libdir}/kde4/htmlthumbnail.so
%{_kde_libdir}/kde4/imagethumbnail.so
%{_kde_libdir}/kde4/jpegthumbnail.so
%{_kde_libdir}/kde4/kcm_attica.so
%{_kde_libdir}/kde4/kcm_cgi.so
%{_kde_libdir}/kde4/kcm_componentchooser.so
%{_kde_libdir}/kde4/kcm_device_automounter.so
%{_kde_libdir}/kde4/kcm_emoticons.so
%{_kde_libdir}/kde4/kcm_filetypes.so
%{_kde_libdir}/kde4/kcm_icons.so
%{_kde_libdir}/kde4/kcm_kded.so
%{_kde_libdir}/kde4/kcm_kdnssd.so
%{_kde_libdir}/kde4/kcm_knotify.so
%{_kde_libdir}/kde4/kcm_locale.so
%{_kde_libdir}/kde4/kcm_nepomuk.so
%{_kde_libdir}/kde4/kcm_phonon.so
%{_kde_libdir}/kde4/kcm_trash.so
%{_kde_libdir}/kde4/kcmspellchecking.so
%{_kde_libdir}/kde4/kded_desktopnotifier.so
%{_kde_libdir}/kde4/kded_device_automounter.so
%{_kde_libdir}/kde4/kded_kpasswdserver.so
%{_kde_libdir}/kde4/kded_ktimezoned.so
%{_kde_libdir}/kde4/kded_nepomuksearchmodule.so
%{_kde_libdir}/kde4/kded_networkstatus.so
%{_kde_libdir}/kde4/kded_networkwatcher.so
%{_kde_libdir}/kde4/kded_phononserver.so
%{_kde_libdir}/kde4/kded_recentdocumentsnotifier.so
%{_kde_libdir}/kde4/kded_remotedirnotify.so
%{_kde_libdir}/kde4/kded_solidautoeject.so
%{_kde_libdir}/kde4/kded_soliduiserver.so
%{_kde_libdir}/kde4/kio_about.so
%{_kde_libdir}/kde4/kio_applications.so
%{_kde_libdir}/kde4/kio_archive.so
%{_kde_libdir}/kde4/kio_bookmarks.so
%{_kde_libdir}/kde4/kio_cgi.so
%{_kde_libdir}/kde4/kio_desktop.so
%{_kde_libdir}/kde4/kio_filter.so
%{_kde_libdir}/kde4/kio_finger.so
%{_kde_libdir}/kde4/kio_fish.so
%{_kde_libdir}/kde4/kio_floppy.so
%{_kde_libdir}/kde4/kio_info.so
%{_kde_libdir}/kde4/kio_man.so
%{_kde_libdir}/kde4/kio_nepomuk.so
%{_kde_libdir}/kde4/kio_nepomuksearch.so
%{_kde_libdir}/kde4/kio_network.so
%{_kde_libdir}/kde4/kio_nfs.so
%{_kde_libdir}/kde4/kio_recentdocuments.so
%{_kde_libdir}/kde4/kio_remote.so
%{_kde_libdir}/kde4/kio_settings.so
%{_kde_libdir}/kde4/kio_sftp.so
%{_kde_libdir}/kde4/kio_tags.so
%{_kde_libdir}/kde4/kio_thumbnail.so
%{_kde_libdir}/kde4/kio_timeline.so
%{_kde_libdir}/kde4/kio_trash.so
%{_kde_libdir}/kde4/kshorturifilter.so
%{_kde_libdir}/kde4/kuriikwsfilter.so
%{_kde_libdir}/kde4/kurisearchfilter.so
%{_kde_libdir}/kde4/libkmanpart.so
%{_kde_libdir}/kde4/librenaudioplugin.so
%{_kde_libdir}/kde4/librenimageplugin.so
%{_kde_libdir}/kde4/localdomainurifilter.so
%{_kde_libdir}/kde4/plasma-kpart.so
%{_kde_libdir}/kde4/plasma_appletscript_declarative.so
%{_kde_libdir}/kde4/plasma_appletscript_simple_javascript.so
%{_kde_libdir}/kde4/plasma_containment_newspaper.so
%{_kde_libdir}/kde4/plasma_dataenginescript_javascript.so
%{_kde_libdir}/kde4/plasma_packagestructure_javascriptaddon.so
%{_kde_libdir}/kde4/plasma_runnerscript_javascript.so
%{_kde_libdir}/kde4/svgthumbnail.so
%{_kde_libdir}/kde4/textthumbnail.so
%{_kde_libdir}/kde4/imports/org/kde/qtextracomponents/libqtextracomponentsplugin.so
%{_kde_libdir}/kde4/imports/org/kde/qtextracomponents/qmldir
%{_kde_libdir}/kde4/windowsexethumbnail.so
%{_kde_libdir}/kde4/windowsimagethumbnail.so
%{_kde_libdir}/kde4/imports/org/kde/plasma
%{_kde_libdir}/kde4/libexec
%{_kde_libdir}/kde4/plugins
%{_kde_libdir}/kde4/imports/org/kde/draganddrop/qmldir
%{_kde_libdir}/kde4/imports/org/kde/draganddrop/libdraganddropplugin.so
%{_kde_libdir}/kde4/imports/org/kde/runnermodel/qmldir
%{_kde_libdir}/kde4/imports/org/kde/runnermodel/librunnermodelplugin.so
%{_kde_libdir}/kde4/imports/org/kde/locale/qmldir
%{_kde_libdir}/kde4/imports/org/kde/locale/liblocalebindingsplugin.so
%{_kde_libdir}/kde4/platformimports
%{_kde_libdir}/kde4/kio_smb.so
%{_kde_libdir}/attica_kde.so
%{_kde_libdir}/libkdeinit4_kcmshell4.so
%{_kde_libdir}/libkdeinit4_kglobalaccel.so
%{_kde_libdir}/libkdeinit4_khelpcenter.so
%{_kde_libdir}/libkdeinit4_kuiserver.so
%{_kde_libdir}/libknotifyplugin.so
%{_kde_applicationsdir}/*.desktop
%{_kde_appsdir}/desktoptheme
%{_kde_appsdir}/drkonqi
%{_kde_appsdir}/hardwarenotifications
%{_kde_appsdir}/kcm_componentchooser
%{_kde_appsdir}/kcm_phonon
%{_kde_appsdir}/kcmlocale
%{_kde_appsdir}/kconf_update/*.upd
%{_kde_appsdir}/kde
%{_kde_appsdir}/kglobalaccel
%{_kde_appsdir}/khelpcenter
%{_kde_appsdir}/kio_bookmarks
%{_kde_appsdir}/kio_desktop
%{_kde_appsdir}/kio_docfilter
%{_kde_appsdir}/kio_finger
%{_kde_appsdir}/kio_info
%{_kde_appsdir}/konqsidebartng
%{_kde_appsdir}/ksmserver
%{_kde_appsdir}/libphonon
%{_kde_appsdir}/phonon
%{_kde_appsdir}/remoteview
%{_kde_appsdir}/konqueror/dirtree/remote/smb-network.desktop
%{_kde_datadir}/config.kcfg/*.kcfg
%{_kde_configdir}/*.knsrc
%{_kde_configdir}/kshorturifilterrc
%{_kde_datadir}/desktop-directories/*.directory
%{_kde_datadir}/emoticons/kde4
%{_kde_iconsdir}/default.kde4
%{_kde_iconsdir}/hicolor/*/apps/*
%{_kde_services}/*.protocol
%{_kde_services}/comicbookthumbnail.desktop
%{_kde_services}/componentchooser.desktop
%{_kde_services}/cursorthumbnail.desktop
%{_kde_services}/desktopthumbnail.desktop
%{_kde_services}/device_automounter_kcm.desktop
%{_kde_services}/directorythumbnail.desktop
%{_kde_services}/djvuthumbnail.desktop
%{_kde_services}/emoticons.desktop
%{_kde_services}/exrthumbnail.desktop
%{_kde_services}/filetypes.desktop
%{_kde_services}/fixhosturifilter.desktop
%{_kde_services}/htmlthumbnail.desktop
%{_kde_services}/icons.desktop
%{_kde_services}/imagethumbnail.desktop
%{_kde_services}/jpegthumbnail.desktop
%{_kde_services}/kcm_attica.desktop
%{_kde_services}/kcm_kdnssd.desktop
%{_kde_services}/kcm_nepomuk.desktop
%{_kde_services}/kcm_phonon.desktop
%{_kde_services}/kcmcgi.desktop
%{_kde_services}/kcmkded.desktop
%{_kde_services}/kcmnotify.desktop
%{_kde_services}/kcmtrash.desktop
%{_kde_services}/kglobalaccel.desktop
%{_kde_services}/khelpcenter.desktop
%{_kde_services}/kmanpart.desktop
%{_kde_services}/knotify4.desktop
%{_kde_services}/kshorturifilter.desktop
%{_kde_services}/kuiserver.desktop
%{_kde_services}/kuriikwsfilter.desktop
%{_kde_services}/kurisearchfilter.desktop
%{_kde_services}/language.desktop
%{_kde_services}/localdomainurifilter.desktop
%{_kde_services}/plasma-containment-newspaper.desktop
%{_kde_services}/plasma-kpart.desktop
%{_kde_services}/plasma-packagestructure-javascript-addon.desktop
%{_kde_services}/plasma-scriptengine-applet-declarative.desktop
%{_kde_services}/plasma-scriptengine-applet-simple-javascript.desktop
%{_kde_services}/plasma-scriptengine-dataengine-javascript.desktop
%{_kde_services}/plasma-scriptengine-runner-javascript.desktop
%{_kde_services}/renaudiodlg.desktop
%{_kde_services}/renimagedlg.desktop
%{_kde_services}/searchproviders
%{_kde_services}/spellchecking.desktop
%{_kde_services}/svgthumbnail.desktop
%{_kde_services}/textthumbnail.desktop
%{_kde_services}/windowsexethumbnail.desktop
%{_kde_services}/windowsimagethumbnail.desktop
%{_kde_services}/kded/*.desktop
%{_kde_servicetypes}/*.desktop
%{_kde_datadir}/locale/currency
%{_kde_datadir}/locale/l10n/*/*
%{_kde_datadir}/locale/l10n/*.desktop
%{_kde_mandir}/man?/*
%{_kde_datadir}/mime/packages/*.xml
%{_kde_datadir}/sounds/*
%doc %{_kde_docdir}/HTML/en/*

#--------------------------------------------------------------

%package -n kwallet-daemon
Summary:	Kwallet daemon
Group:		Development/KDE and Qt
Conflicts:	%{name} < 1:4.5.71

%description -n kwallet-daemon
Kwallet daemon.

%files -n kwallet-daemon
%{_kde_bindir}/kwalletd
%{_kde_libdir}/libkdeinit4_kwalletd.so
%{_kde_appsdir}/kwalletd
%{_kde_services}/kwalletd.desktop

#--------------------------------------------------------------

%define kwalletbackend_major 4
%define libkwalletbackend %mklibname kwalletbackend %{kwalletbackend_major}

%package -n %{libkwalletbackend}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkwalletbackend}
KDE 4 core library.

%files -n %{libkwalletbackend}
%{_kde_libdir}/libkwalletbackend.so.%{kwalletbackend_major}*

#--------------------------------------------------------------

%define molletnetwork_major 4
%define libmolletnetwork %mklibname molletnetwork %{molletnetwork_major}

%package -n %{libmolletnetwork}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libmolletnetwork}
KDE 4 core library.

%files -n %{libmolletnetwork}
%{_kde_libdir}/libmolletnetwork.so.%{molletnetwork_major}*

#--------------------------------------------------------------

%package devel
Group:		Development/KDE and Qt
Summary:	Header files and documentation for compiling KDE applications
Requires:	kdelibs4-devel
Requires:	%{name} = %{EVRD}
Requires:	%{libkwalletbackend} = %{EVRD}
Requires:	%{libmolletnetwork} = %{EVRD}

%description devel
This package includes the header files you will need to compile applications
for KDE. Also included is the KDE API documentation in HTML format for easy
browsing.

%files devel
%{_kde_includedir}/*.h
%{_kde_libdir}/libkwalletbackend.so
%{_kde_libdir}/libmolletnetwork.so
%{_kde_appsdir}/cmake/modules/*.cmake

#-----------------------------------------------------------------------------

%prep
%setup -q -n kde-runtime-%{version}

%patch0 -p1 -b .htsearch
%patch1 -p1 -b .tirpclinkage~
%patch2 -p1 -b .kdesu~
%patch5 -p1 -b .bug_49814
%patch8 -p0
%patch9 -p0
%patch10 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_kde_iconsdir}/hicolor/index.theme

mkdir -p %{buildroot}%{_kde_bindir}
ln -s %{_kde_libdir}/kde4/libexec/kdesu %{buildroot}%{_kde_bindir}/kdesu

%changelog
* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Sat Apr 20 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-3
- Adjust Conflicts with kdebase4-workspace to avoid file conflict (plasmapkg.1.xz)

* Mon Apr 08 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-2
- Add kdesu-encoding patch to fix Rosa bug 1902

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0
- Add kde-runtime-4.9.98-link-tirpc patch (bero)
- Add BuildRequires pkgconfig(libtirpc), pkgconfig(libntrack-qt4),
  ntrack-devel, openslp-devel (bero)
- Update files - new file kio_tags.so (bero)
- Re-diff l10n-ru patch

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Sat Aug 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0
- Re-diff l10n patch
- Add rpmlint filter file

* Thu Jul 12 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-2
- Update to 4.8.97
- Convert some BuildRequires to pkgconfig style
- Add pkgconfig(NetworkManager) to BuildRequires
- Use better kde path macros in files

* Thu Jun 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- Update to 4.8.95
- Update file list

* Tue Jun 19 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.90-1
- Update to 4.8.90
- Add nepomuk-core-devel to BuildRequires
- Add pkgconfig(libkactivities) to BuildRequires
- Add kdepimlibs4-devel to BuildRequires
- Drop nepomuk-related stuff that was moved to nepomuk-core

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.4-1
- update to 4.8.4

* Thu May 17 2012 Sergey Borovkov <sergey.borovkov@osinit.ru> 1:4.8.3-2
- Kde language setting create ~/.i18n file to affect non kde application

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.3-1
- update to 4.8.3

* Thu Apr 19 2012 Mikhail Kompaniets <mkompan@mezon.ru> 1:4.8.2-3
- Russian localization for .desktop files

* Mon Apr 09 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.2-2
- fix libnepomukdatamanagement (devel)

* Mon Mar 12 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.2-1
- update to 4.8.2

* Mon Mar 12 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.1-1
- update to 4.8.1

* Tue Feb 14 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-2
+ Revision: 773947
- Rebuild against new attica rpm

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762413
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758114
- New upstream tarball

* Sun Jan 01 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-2
+ Revision: 748618
- New version

* Thu Dec 29 2011 Zé <ze@mandriva.org> 1:4.7.90-2
+ Revision: 748206
- clean remaining defattr
- list dbus related files without a prefix since dbus only looks in /usr/share/dbus-1 (like is done in kdelibs,seams that was forgoten here)
- do the same for polkit related files
- seams dbus interface .xml files are not development files as discussed with main kde developers
- bump release to build against new attica

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 739331
- New upstream tarball

* Mon Nov 21 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.80-1
+ Revision: 732252
- Remove Patch 1000: merged upstream
- New upstream tarball

* Fri Nov 18 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-2
+ Revision: 731613
- Fix file list
- Remove activitymanager from CMakeLists.txt
- Do not use bundled libkactivities

* Fri Aug 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-1
+ Revision: 697176
- New version 4.7.41

* Mon Aug 01 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.40-1
+ Revision: 692628
- New version 4.7.40

* Fri Jul 08 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.90-1
+ Revision: 689324
- Fix file list
- Fix file list
- New version kde 4.7 rc1

* Mon Jun 27 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.4-5
+ Revision: 687432
- Do not copy trash on the desktop by default

* Tue Jun 21 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.4-4
+ Revision: 686471
- Fix P9
- Do not add the Home.desktop file on the desktop for new accounts
- add nepomukcontroller.desktop
- Autostart nepomukcontroller is nepomuk is enabled

* Tue Jun 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.4-2
+ Revision: 685167
- Fix file list
- Apply P200
- Fix patch list
- Update nepomuk patch
- New version 4.6.4

* Tue Jun 07 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.3-2
+ Revision: 683021
- Add new nepomuk files
- Fix file list
- Sync nepomuk with trunk
- remove buildroot

* Sat May 14 2011 Funda Wang <fwang@mandriva.org> 1:4.6.3-1
+ Revision: 674398
- new version 4.6.3

* Tue Apr 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.2-1
+ Revision: 650768
- Remove mkrel
- New version 4.6.2

* Tue Mar 08 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.1-2
+ Revision: 642768
- Do not use %%mkrel anymore
- Fix file list
- New version 4.6.1

* Sat Jan 29 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.0-2
+ Revision: 633873
- Fix file list
- Fix file list
- Fix file list
- Remove merged patch
- New version KDE 4.6 Final

  + John Balcaen <mikala@mandriva.org>
    - Add patch100 from upstream to fix kde #250977 (Fix crash when a NFS mount contains a .Trash-$UID subdir)

* Thu Jan 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.95-1mdv2011.0
+ Revision: 629131
- New version KDE 4.6 RC2

* Thu Dec 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.90-1mdv2011.0
+ Revision: 624074
- New upstream tarball

* Thu Dec 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.85-1mdv2011.0
+ Revision: 617898
- Fix file list
- New upstream tarball

  + Funda Wang <fwang@mandriva.org>
    - rebuild for new exiv2

* Fri Nov 26 2010 Funda Wang <fwang@mandriva.org> 1:4.5.80-1mdv2011.0
+ Revision: 601488
- new verison 4.5.80 (aka 4.6 beta1)
- should be plain filename for icon

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 1:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599110
- new snapshot 4.5.77

* Sat Nov 13 2010 Funda Wang <fwang@mandriva.org> 1:4.5.76-0.svn1196361.1mdv2011.0
+ Revision: 597067
- new snapshot 4.5.76
- rediff htsearch patch
- add symbolic link to kdesu (mdv#61592), like fedora, suse and pclinuxos
- chgrp is not supported when packaging

* Thu Oct 28 2010 Funda Wang <fwang@mandriva.org> 1:4.5.74-0.svn1190490.1mdv2011.0
+ Revision: 589706
- update file list
- bump req
- New snapshot 4.5.74

* Thu Oct 07 2010 Funda Wang <fwang@mandriva.org> 1:4.5.71-0.svn1183366.1mdv2011.0
+ Revision: 584032
- fix requires
- fix epoch
- New snapshot 4.5.71
- BR canberra for speaker setup

* Tue Sep 14 2010 Funda Wang <fwang@mandriva.org> 1:4.5.68-1mdv2011.0
+ Revision: 578309
- update file list
- New snapshot 4.5.68

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove old conflicts

* Fri Sep 03 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.67-2mdv2011.0
+ Revision: 575579
- Rebuild
- Fix file list
- New version 4.5.67

* Tue Aug 31 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.65-4mdv2011.0
+ Revision: 574893
- Fix conflicts
  CCBUG: 60862

* Tue Aug 31 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.65-3mdv2011.0
+ Revision: 574721
- fix groups
- Fix file list
- Update to version 4.5.65

* Tue Aug 24 2010 Colin Guthrie <cguthrie@mandriva.org> 1:4.5.0-3mdv2011.0
+ Revision: 572591
- Remove previous patch that removed calls to snd_config_update_free_global(). Underlying issue fixed in libalsa2 now

* Thu Aug 19 2010 Colin Guthrie <cguthrie@mandriva.org> 1:4.5.0-2mdv2011.0
+ Revision: 571299
- Rediff speaker-setup patch
- Apply patch that removes potentially evil calls to snd_config_update_free_global() in phonon bits

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.0-1mdv2011.0
+ Revision: 566579
- New upstream tarball
- Update to version 4.5.0

  + Funda Wang <fwang@mandriva.org>
    - suggests cagibi for kio_network's UpnpNetworkBuilder

* Wed Jul 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.95-1mdv2011.0
+ Revision: 562406
- kde 4.4.95

* Tue Jul 27 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.92-1mdv2011.0
+ Revision: 561574
- Update to kde 4.5 Rc2

  + Colin Guthrie <cguthrie@mandriva.org>
    - Add the Speaker Setup GUI (PulseAudio)

* Wed Jun 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-10mdv2010.1
+ Revision: 548746
- Add nepomuk module on systemsettings

* Sat Jun 19 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-9mdv2010.1
+ Revision: 548339
- Update nepomuk patch

* Wed May 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-8mdv2010.1
+ Revision: 546296
- Fix crash at nepomuk start
  CCBUG: 59287

* Wed May 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-7mdv2010.1
+ Revision: 546138
- Rebuild in release mode

* Mon May 17 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-6mdv2010.1
+ Revision: 544916
- Add branch patches:
        - Fix next and previous page functions in khelpcenter ( P102 )
        - Use the BrowserExtension to navigate between page ( P103 )
        - Schedule TOC builds as part of a setOpen ( P104 )
        - Use _helper.viewFocusBrush() in place of kcolorscheme(...) ( P105 )
        - Added protection to disable animation when target is destroyed. ( P106 )
        - Check QX11Info::depth() to decide whether alphachannel can be use to paint widgets ( Patch107 )
        - do not draw menu frame+background for embedded menus ( P108 )

* Fri May 14 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-5mdv2010.1
+ Revision: 544792
- Add nepomuk module on systemsettings

* Fri May 14 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-4mdv2010.1
+ Revision: 544745
- Update nepomuk patch

* Sun May 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-3mdv2010.1
+ Revision: 544273
- Versionnate buildrequires
- Update nepomuk patch
- Update nepomuk part ( sync from trunk )
  Move patch4 and patch 9

* Thu May 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-2mdv2010.1
+ Revision: 542801
- Rebuild because of missing src.rpm
- Update to version 4.4.3

* Fri Apr 30 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.2-3mdv2010.1
+ Revision: 541379
- Add back buildrequires removed by error in commit 530765
- Add kdelibs4-devel as buildrequires
- Fix patch101
- Fix encoding in k{read,write}conf
- Fix minimum version rhbz#582968
- Add patch to fix a crash in device automounter

* Tue Mar 30 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.2-1mdv2010.1
+ Revision: 530047
- Disable patch7
- Sync nepomuk with trunk
  Remove merge patch
  Remove old patches
- Update to version 4.4.2
- Change kde-l10n Requires into suggestscd

* Wed Mar 17 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-3mdv2010.1
+ Revision: 524455
- Use mdv icon for the Home folder

* Fri Mar 12 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-2mdv2010.1
+ Revision: 518416
- Fix inotify patch again
- Fix inofity patch
- Add branch patch fixing indexing
- Update inotify patch
  Enable patch7

* Thu Mar 11 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-1mdv2010.1
+ Revision: 517925
- Remove merged patches
- Fix release
- Update to version 4.4.1

* Thu Feb 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-8mdv2010.1
+ Revision: 510925
- Create phonon-xine-kcm, this will allow to remove xine deps in main installs

* Fri Feb 19 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-7mdv2010.1
+ Revision: 508381
- Add branch patches fixing nepomuk

* Wed Feb 17 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-6mdv2010.1
+ Revision: 507314
- Backport nepomuk fixes from branch

* Tue Feb 16 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-5mdv2010.1
+ Revision: 506627
- Fix previous patch
- Update inotify patch

* Mon Feb 15 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-4mdv2010.1
+ Revision: 506220
- Add backported patch

* Thu Feb 11 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-3mdv2010.1
+ Revision: 504251
- Add nepomuk patch from strueg
- We need to require polkit-kde-1 because
  of the use Auth backend, add this require fixes
  the saving of hours on the clock kcm

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-2mdv2010.1
+ Revision: 503190
- Remove merged patch
- Update to version 4.4.0
- Fix file list
- Backport Coherence support from trunk

* Tue Feb 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.98-2mdv2010.1
+ Revision: 499740
- Disable kglobalaccel notification by default

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.98-1mdv2010.1
+ Revision: 498953
- Update to version 4.3.98 aka "kde 4.4 RC3"
- soprano redland is now a runtime dep

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.95-1mdv2010.1
+ Revision: 495939
- Removed unused buildrequire
- Update to kde 4.4 Rc2

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1:4.3.90-2mdv2010.1
+ Revision: 488771
- rebuilt against libjpeg v8

* Sat Jan 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.90-1mdv2010.1
+ Revision: 488181
- Update to 4.4 Rc1

* Thu Dec 31 2009 Funda Wang <fwang@mandriva.org> 1:4.3.85-2mdv2010.1
+ Revision: 484303
- rebuild for new exiv2

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove X11-devel buildrequire

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.85-1mdv2010.1
+ Revision: 480620
- Fix file list
- Update to kde 4.4 beta 2
  Remove merged patches

* Fri Dec 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.80-2mdv2010.1
+ Revision: 473458
- Add nepomuk fixes from trunk

* Thu Dec 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.80-1mdv2010.1
+ Revision: 472965
- package all currency folder
- Fix file list
- Add buildrequires
- Update to kde 4.4 Beta 1
  Activate kio_sftp again with new libssh-devel

* Tue Dec 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.77-2mdv2010.1
+ Revision: 472223
- Add conflict to ease upgrade

* Thu Nov 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.77-1mdv2010.1
+ Revision: 470376
- Fix file list
- Remove merged patch
- Update to kde 4.3.77
  Add branch switch for beta and final releases

* Sun Nov 22 2009 Colin Guthrie <cguthrie@mandriva.org> 1:4.3.75-2mdv2010.1
+ Revision: 469039
- Update for slightly changed API in phonon trunk (PulseAudio related)

* Mon Nov 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.75-1mdv2010.1
+ Revision: 466559
- Update to kde 4.3.75

* Thu Nov 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-5mdv2010.1
+ Revision: 465292
- Fix Buildrequires: Really build sftp kioslave so we need ssh-devel

* Wed Nov 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-4mdv2010.1
+ Revision: 464594
- Rebuild against new qt
- Fix xine buildrequire
- Add buildrequire

* Mon Nov 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-2mdv2010.1
+ Revision: 463378
- Fix buildrequires to enable kio_sftp again

* Fri Nov 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-1mdv2010.1
+ Revision: 461717
- Update to kde 4.3.73
  Fix file list
  Remove merged patches
  Fix BuildRequires

* Wed Oct 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.2-10mdv2010.0
+ Revision: 459716
- Add patch to fix a security issue ( http://www.ocert.org/advisories/ocert-2009-015.html )

* Mon Oct 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.2-9mdv2010.0
+ Revision: 459340
- Fix nepomuk patches

* Sat Oct 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.2-8mdv2010.0
+ Revision: 459143
- Fixed mdv version

* Wed Oct 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.2-7mdv2010.0
+ Revision: 458646
- Add nepomuk patches  ( asked by S. lauriere )

* Fri Oct 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.2-6mdv2010.0
+ Revision: 457961
- backport a patch from trunk fixing kwallet default size

* Thu Oct 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.2-5mdv2010.0
+ Revision: 457484
- Apply patch5
- Fix CPU load ( Bug #49814)

* Wed Oct 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.2-4mdv2010.0
+ Revision: 455349
- [Backport]properly fail to initialize if the soprano model could not be created

* Tue Oct 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.2-3mdv2010.0
+ Revision: 455283
- Activate nepomuk patches

* Tue Oct 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.2-2mdv2010.0
+ Revision: 455270
- backport a fix in nepomuk kcm

* Mon Oct 05 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.2-1mdv2010.0
+ Revision: 454256
- New upstream release 4.3.2.

* Fri Oct 02 2009 Colin Guthrie <cguthrie@mandriva.org> 1:4.3.1-15mdv2010.0
+ Revision: 452494
- Update pulseaudio-related patches to be compatible with latest phonon (note: no specific pulseaudio support here - it's all handed off to the phonon backend)

* Wed Sep 23 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.1-14mdv2010.0
+ Revision: 448009
- Integrate smartfile from nepomuk

  + Colin Guthrie <cguthrie@mandriva.org>
    - Update pulseaudio patches to work more generically based on what the backend supports

* Sun Sep 20 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-12mdv2010.0
+ Revision: 444827
- Add missing epoch for krootwarning obsolete

* Sun Sep 20 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-11mdv2010.0
+ Revision: 444787
- Add forgoten Epoch for Krozat

* Sat Sep 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-10mdv2010.0
+ Revision: 444782
- Add missing epoch in obsoletes

* Fri Sep 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-9mdv2010.0
+ Revision: 444253
- Rebuild
- More obsoletes for kde3 upgrade
- Add obsolete for kde3 upgrade

* Wed Sep 16 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.1-6mdv2010.0
+ Revision: 443606
- Try number 2134^e545 of nepomuk integration

* Tue Sep 15 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.1-5mdv2010.0
+ Revision: 441654
- Fix cyclic build requires caused by bad nepomuk patch
- Added requested nepomuk patches by mandriva nepomuk kde team. Some of then forced to add patch fuzz.

* Mon Sep 14 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-4mdv2010.0
+ Revision: 439069
- Add back lost patch

* Sun Sep 13 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-2mdv2010.0
+ Revision: 438579
- Obsolete kde3 packages

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.1-1mdv2010.0
+ Revision: 423168
- New upstream release 4.3.1.

* Tue Aug 18 2009 Funda Wang <fwang@mandriva.org> 1:4.3.0-4mdv2010.0
+ Revision: 417522
- rebuild for new libjpeg v7

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.0-3mdv2010.0
+ Revision: 409036
- New upstream release 4.3.0.

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix version

* Wed Jul 22 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.98-1mdv2010.0
+ Revision: 398679
- Update to KDE 4.3 RC3

* Fri Jul 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.96-1mdv2010.0
+ Revision: 394329
- Update to Rc2

* Sat Jun 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.95-2mdv2010.0
+ Revision: 390088
- Show knetattach only in KDE (Bug #49538)

* Thu Jun 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.95-1mdv2010.0
+ Revision: 389079
- Update to ke 4.3Rc1

* Fri Jun 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.90-2mdv2010.0
+ Revision: 382922
- Biump release
- Remove merged patches
- Update to beta2
- add Suggests for kdialog, kdeui uses it for editing
  toolbars (bnc#490559)

* Fri May 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.88-2mdv2010.0
+ Revision: 380721
- Bump release
- Update to kde 4.2.88

* Fri May 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.87-2mdv2010.0
+ Revision: 378631
- Fix conflict against kdebase4-workspace

* Fri May 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.87-1mdv2010.0
+ Revision: 378572
- Fix file list
- update to kde 4.2.87

* Sun May 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.85-4mdv2010.0
+ Revision: 376582
- Fix file list
- Fix versionnate conflicts
- Fix conflicts with kdepim-akonadi

  + Helio Chissini de Castro <helio@mandriva.com>
    - Added back lzma/xz patch

* Fri May 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.85-1mdv2010.0
+ Revision: 373477
- Remove non existing BuildRequires
- Fix Requires on next kdelibs4
- Fix file list
- Add buildrequires
- Update  to kde 4.2.85

* Mon May 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.71-0.svn961800.1mdv2010.0
+ Revision: 371559
- Fix file list
- Fix file list
- Update to kde 4.2.71

* Thu Apr 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.70-0.svn954171.1mdv2010.0
+ Revision: 369153
- Update to kde 4.2.70
  Remove branch patches

* Fri Apr 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-7mdv2009.1
+ Revision: 365929
- Add some upstream patches from branch
    Fixes a layouting issue ( KDE bug #178953)

* Sun Apr 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-6mdv2009.1
+ Revision: 364256
- Add some upstream patches from branch
        - Patch101: start kttsd when necessary

* Sun Apr 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-5mdv2009.1
+ Revision: 364084
- Add some upstream patches from branch
        - Patch100: extract .cc files, not .cpp from kioslave infos

* Sun Mar 29 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.2-4mdv2009.1
+ Revision: 362167
- Restore icons from original package, since there's was unintentional split too soon

* Fri Mar 27 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.2-1mdv2009.1
+ Revision: 361619
- Upgrade to KDE 4.2.2 try#1 packages.

* Wed Mar 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.1-2mdv2009.1
+ Revision: 353570
- [Trunk] start nepomuk after plasma ( start faster )

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - fix duplicate definition of xz protocol in lzma.protocol (VERIFYME?)
    - revert accidental removal of tar.bz2 from screateResourceUri in opranoindexwriter.cpp

* Fri Feb 27 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.1-1mdv2009.1
+ Revision: 345623
- KDE 4.2.1 try#1 upstream release

* Tue Feb 24 2009 Colin Guthrie <cguthrie@mandriva.org> 1:4.2.0-4mdv2009.1
+ Revision: 344337
- Update pulseaudio device hiding patch.

* Tue Feb 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-3mdv2009.1
+ Revision: 341374
+ rebuild (emptylog)

* Mon Feb 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-2mdv2009.1
+ Revision: 340857
- Rebuild against qt4.5

* Tue Jan 27 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.0-1mdv2009.1
+ Revision: 334190
- Update with official 4.2.0 upstream tarball ( now with less verbosity i hope )
- Update with ixed tarball from upstream

* Sat Jan 10 2009 Anssi Hannula <anssi@mandriva.org> 1:4.1.96-4mdv2009.1
+ Revision: 328111
- fix versioned conflicts on kappfinder

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - fix conflicts with kappfinder

* Fri Jan 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.96-2mdv2009.1
+ Revision: 327477
- Fix Conflicts with kdebase4-runtime

* Thu Jan 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.96-1mdv2009.1
+ Revision: 327253
- Fix file list
- Fix lzma patch

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - update and fix lzma patch to work with new kde and also add support for new xz

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.96

* Mon Jan 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.85-5mdv2009.1
+ Revision: 324947
- Fix desktop kioslave translations again

* Sun Jan 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.85-4mdv2009.1
+ Revision: 324518
- Rebuild because of missing source rpm
- Fix translation of desktop files on the desktop:/ kioslave

* Tue Dec 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.85-2mdv2009.1
+ Revision: 317737
- Rebuild in debug mode

* Fri Dec 12 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.85-1mdv2009.1
+ Revision: 313703
- Update with Beta 1 - 4.1.85

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.82-2mdv2009.1
+ Revision: 312976
- Rebuild package because the -1mdv2009.1 was to shy to come on the mirors
- Update to kde 4.1.82

* Sun Nov 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.81-1mdv2009.1
+ Revision: 308454
- Update to kde 4.1.81
  Fix BuildRequires
  Fix File list

* Sun Nov 30 2008 Anssi Hannula <anssi@mandriva.org> 1:4.1.80-2mdv2009.1
+ Revision: 308332
- oxygen-icon-theme conflicts with old digikam for smooth upgrade

  + Thierry Vignaud <tv@mandriva.org>
    - Suggests gdb for drkonqi (#45272)

* Wed Nov 19 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.80-1mdv2009.1
+ Revision: 304542
- Update with Beta 1 - 4.1.80

* Thu Nov 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.73-1mdv2009.1
+ Revision: 302768
- Update to kde 4.1.73

* Sun Nov 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.71-3mdv2009.1
+ Revision: 299238
- Fix Requires of devel package

* Sun Nov 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.71-2mdv2009.1
+ Revision: 299225
- Fix Conflicts against nepomuk-kde

* Fri Oct 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.71-1mdv2009.1
+ Revision: 296895
- New version 4.1.71

* Wed Oct 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.70-3mdv2009.1
+ Revision: 296583
- Add requires on kwallet-daemon

* Tue Oct 21 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:4.1.70-2mdv2009.1
+ Revision: 296103
- Add proper conflicts so that cooker upgrade is not broken

* Mon Oct 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.70-1mdv2009.1
+ Revision: 295749
- Fix file list
- Fix Requires
- Fix File list
- Fix File list
- Update to kde 4.1.70
  Remove Nepomuk patches
  Remove backported patches
  Remove patches that belong to phonon now
  Add patch to fix build

* Tue Sep 30 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.2-3mdv2009.0
+ Revision: 290126
- Added splash requires in the proper package

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix htsearch path
    - Add htdig as Requires needed for khelpcenter

* Thu Sep 25 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.2-1mdv2009.0
+ Revision: 288215
- KDE 4.1.2 arriving.

* Sat Sep 20 2008 Colin Guthrie <cguthrie@mandriva.org> 1:4.1.1-5mdv2009.0
+ Revision: 286056
- Do not mark pulseaudio output as advanced
- Require xine-pulse in the phonon-xine backend

* Fri Sep 19 2008 Colin Guthrie <cguthrie@mandriva.org> 1:4.1.1-4mdv2009.0
+ Revision: 285840
- Update pulseaudio cosmetics patch to enumerate capture devices which are not (currently) handled in Phonon

* Fri Sep 19 2008 Colin Guthrie <cguthrie@mandriva.org> 1:4.1.1-3mdv2009.0
+ Revision: 285789
- Add an experimental patch to ignore audio devices when pulseaudio is activated

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove wrong source

* Mon Sep 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.1-2mdv2009.0
+ Revision: 278339
- Welcome back experimental Nepomuk

* Fri Aug 29 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.1-1mdv2009.0
+ Revision: 277148
- Upgrade to forthcoming 4.1.1 packages

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - [BUGFIX] Nepomukservices process makes my CPU reach 65%% (Bug #42474)

* Sat Aug 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.0-8mdv2009.0
+ Revision: 275327
- Backport the complete nepomuk folder from trunk fixes crashes of nepomuk
- [BUGFIX] Fix "kioclient does not return after execution of command." (Bug #43068)

* Thu Aug 21 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.0-7mdv2009.0
+ Revision: 274630
- Add patch300 to fix icon on the network panel of Dolphin (reported and tested by Anne )

* Wed Aug 13 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-6mdv2009.0
+ Revision: 271349
- Daily branch patch update

* Tue Aug 05 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.0-5mdv2009.0
+ Revision: 263911
- Fix file list
- Activate Nepomuk backports from kde 4.2
- more nepomuk backport patches
- Start to backport nepomuk from trunk ( not activated for the moment)

* Mon Aug 04 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-4mdv2009.0
+ Revision: 263054
- Update with current branch 4.1 patches
- Update with current branch 4.1 patches

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Do not apply for the moment (need a little more work)
    - Add forgoten patch
    -Fix patch 102 ( still need to fix patch104 (not applied yet ))
    - Add versionnate against strigi
    - Add patches from trunk to optimise nepomuk
    - Add patches from trunk to optimise nepomuk

* Wed Jul 30 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-3mdv2009.0
+ Revision: 255170
- kdebase4-runtime no more requires any phonon package, since is suppose to be required by kdecore now. phonon-xine have a new provides called phonon-backend providing 4.2.0 as their virtual version

* Tue Jul 29 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-2mdv2009.0
+ Revision: 253955
- Start updates from post 4.1.0 branch on cooker only. All patches comes with full description inside.

* Thu Jul 24 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-1mdv2009.0
+ Revision: 246986
- Update with Release Candidate 1 - 4.1.0

* Thu Jul 24 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:4.0.98-2mdv2009.0
+ Revision: 245135
- fix docbook document
- add missing docbook file to liblzma patch
- bump release
- add lzma support (P0)

* Thu Jul 10 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.98-1mdv2009.0
+ Revision: 233181
- Update with Release Candidate 1 - 4.0.98

* Sun Jul 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.85-1mdv2009.0
+ Revision: 232308
- Update to kde 4.0.85

* Fri Jun 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.84-1mdv2009.0
+ Revision: 229393
- Update with new snapshot tarballs 4.0.84

* Fri Jun 20 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.83-2mdv2009.0
+ Revision: 227584
- devel package was blocked due missing epoch

* Fri Jun 20 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.83-1mdv2009.0
+ Revision: 227523
- Phonon devel is in their own package now
- We can use since 4.0.81, so this avoids wait for bs everytime..
- Update with new snapshot tarballs 4.0.83

* Thu Jun 12 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.82-3mdv2009.0
+ Revision: 218297
- Update with new snapshot tarballs 4.0.82
- Update with new snapshot tarballs 4.0.82

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Change summary

  + Pixel <pixel@mandriva.com>
    - add rpm filetrigger running gtk-update-icon-cache when rpm install/remove oxygen icons

  + Frederik Himpe <fhimpe@mandriva.org>
    - Add Requires xine-plugins on phonon-xine, otherwise phonon constantly
      crashes (Mandriva bug #41210)

* Tue Jun 03 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.81-2mdv2009.0
+ Revision: 214702
- Update with new snapshot tarballs 4.0.81

* Fri May 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.81-1mdv2009.0
+ Revision: 213263
- New snapshot kde 4.0.81

* Sat May 24 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.80-1mdv2009.0
+ Revision: 210775
- New upstream kde4 4.1 beta1

* Fri May 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.74-2mdv2009.0
+ Revision: 208151
- Versionnate BuildRequires
- Rebuild against new kdepimlibs4

* Fri May 16 2008 Funda Wang <fwang@mandriva.org> 1:4.0.74-1mdv2009.0
+ Revision: 208040
- New version 4.0.74

* Tue May 13 2008 Anssi Hannula <anssi@mandriva.org> 1:4.0.73-3mdv2009.0
+ Revision: 206729
- drop bogus buildrequires on networkmanager-devel
- add Conflicts for old KDE3 packages for smooth upgrade

* Thu May 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.73-2mdv2009.0
+ Revision: 204554
- Update to kde 4.0.73

* Thu May 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.72-2mdv2009.0
+ Revision: 199902
- Fix File list
- Fix file list
- Update to kde 4.0.72
- Fix File list
- Fix file list
- New week-end New snapshot 4.0.70
- New snapshot 4.0.69

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 alpha 1
    - Starting to push new infrastructure for devel KDE 4.1. KDE 4 will be on / now. KDE is dead. Long live KDE vi kdenetwork4/SPECS/kdenetwork4.spec ;-)

* Fri Mar 28 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.3-1mdv2008.1
+ Revision: 190971
- Update for last stable release 4.0.3

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Requires the translation package by default now

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-2mdv2008.1
+ Revision: 182140
- Rebuild against new qt4 changes

* Sat Mar 01 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.2-1mdv2008.1
+ Revision: 177359
- New upstream bugfix release 4.0.2

* Wed Feb 20 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.1-3mdv2008.1
+ Revision: 173224
- Update nepomuk with trunk modifications. Requested by nepomuk maintainer, Sebastian Trueg

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add ifdef statement to allow backports again

* Wed Feb 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.1-2mdv2008.1
+ Revision: 167174
- rebuild

* Sun Feb 10 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.1-1mdv2008.1
+ Revision: 164757
- Updating for stable KDE 4.0.1
- No more branches. From now, we will be using the monthly official KDE tarballs, as discussed by Mandriva KDE Team

* Sun Jan 27 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.0-1.765565.2mdv2008.1
+ Revision: 158544
- Rebuild because of missing signature

* Thu Jan 24 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.0-1.765565.1mdv2008.1
+ Revision: 157493
- Update to 4.0 branch
- Included nepomuk trunk patch, as requested by Sebastian Trueg

* Tue Jan 08 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.0-1mdv2008.1
+ Revision: 146521
- Update for final stable 4.0.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-1.752237.1mdv2008.1
+ Revision: 137359
- New snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-1mdv2008.1
+ Revision: 117062
- New snapshot

  + Helio Chissini de Castro <helio@mandriva.com>
    - import kdebase4-runtime


