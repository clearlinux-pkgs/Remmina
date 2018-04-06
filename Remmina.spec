#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Remmina
Version  : 1.2.0.rcgit.27
Release  : 1
URL      : https://github.com/FreeRDP/Remmina/archive/v1.2.0-rcgit.27.tar.gz
Source0  : https://github.com/FreeRDP/Remmina/archive/v1.2.0-rcgit.27.tar.gz
Summary  : The GTK+ Remote Desktop Client
Group    : Development/Tools
License  : GPL-2.0 OpenSSL
Requires: Remmina-bin
Requires: Remmina-lib
Requires: Remmina-data
Requires: Remmina-locales
Requires: Remmina-doc
BuildRequires : cmake
BuildRequires : gtk+-dev
BuildRequires : json-glib-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libsoup-dev
BuildRequires : libssh-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(freerdp2)
BuildRequires : pkgconfig(libvncserver)
BuildRequires : pkgconfig(spice-protocol)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : vte-dev

%description
[![Build Status](https://travis-ci.org/FreeRDP/Remmina.png)](https://travis-ci.org/FreeRDP/Remmina) [![Bountysource](https://img.shields.io/bountysource/team/remmina/activity.svg)](https://www.bountysource.com/teams/remmina) [![CodeTriage](https://www.codetriage.com/freerdp/remmina/badges/users.svg)](https://www.codetriage.com/freerdp/remmina)

%package bin
Summary: bin components for the Remmina package.
Group: Binaries
Requires: Remmina-data

%description bin
bin components for the Remmina package.


%package data
Summary: data components for the Remmina package.
Group: Data

%description data
data components for the Remmina package.


%package dev
Summary: dev components for the Remmina package.
Group: Development
Requires: Remmina-lib
Requires: Remmina-bin
Requires: Remmina-data
Provides: Remmina-devel

%description dev
dev components for the Remmina package.


%package doc
Summary: doc components for the Remmina package.
Group: Documentation

%description doc
doc components for the Remmina package.


%package lib
Summary: lib components for the Remmina package.
Group: Libraries
Requires: Remmina-data

%description lib
lib components for the Remmina package.


%package locales
Summary: locales components for the Remmina package.
Group: Default

%description locales
locales components for the Remmina package.


%prep
%setup -q -n Remmina-1.2.0-rcgit.27

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523048243
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DWITH_AVAHI=off -DWITH_APPINDICATOR=off -DWITH_FREERDP=on -DWITH_TELEPATHY=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1523048243
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
%find_lang remmina

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/remmina

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.remmina.Remmina.desktop
/usr/share/applications/remmina-file.desktop
/usr/share/icons/hicolor/128x128/apps/remmina.png
/usr/share/icons/hicolor/16x16/actions/remmina-dynres.png
/usr/share/icons/hicolor/16x16/actions/remmina-fit-window.png
/usr/share/icons/hicolor/16x16/actions/remmina-fullscreen.png
/usr/share/icons/hicolor/16x16/actions/remmina-pin-down.png
/usr/share/icons/hicolor/16x16/actions/remmina-pin-up.png
/usr/share/icons/hicolor/16x16/actions/remmina-scale.png
/usr/share/icons/hicolor/16x16/actions/remmina-switch-page.png
/usr/share/icons/hicolor/16x16/apps/remmina-panel-inverted.png
/usr/share/icons/hicolor/16x16/apps/remmina-panel.png
/usr/share/icons/hicolor/16x16/apps/remmina.png
/usr/share/icons/hicolor/16x16/emblems/remmina-nx.png
/usr/share/icons/hicolor/16x16/emblems/remmina-rdp-ssh.png
/usr/share/icons/hicolor/16x16/emblems/remmina-rdp.png
/usr/share/icons/hicolor/16x16/emblems/remmina-sftp.png
/usr/share/icons/hicolor/16x16/emblems/remmina-tool.png
/usr/share/icons/hicolor/16x16/emblems/remmina-vnc-ssh.png
/usr/share/icons/hicolor/16x16/emblems/remmina-vnc.png
/usr/share/icons/hicolor/16x16/emblems/remmina-xdmcp-ssh.png
/usr/share/icons/hicolor/16x16/emblems/remmina-xdmcp.png
/usr/share/icons/hicolor/22x22/actions/remmina-dynres.png
/usr/share/icons/hicolor/22x22/actions/remmina-fit-window.png
/usr/share/icons/hicolor/22x22/actions/remmina-fullscreen.png
/usr/share/icons/hicolor/22x22/actions/remmina-scale.png
/usr/share/icons/hicolor/22x22/actions/remmina-switch-page.png
/usr/share/icons/hicolor/22x22/apps/remmina-panel-inverted.png
/usr/share/icons/hicolor/22x22/apps/remmina-panel.png
/usr/share/icons/hicolor/22x22/apps/remmina.png
/usr/share/icons/hicolor/22x22/emblems/remmina-nx.png
/usr/share/icons/hicolor/22x22/emblems/remmina-rdp-ssh.png
/usr/share/icons/hicolor/22x22/emblems/remmina-rdp.png
/usr/share/icons/hicolor/22x22/emblems/remmina-sftp.png
/usr/share/icons/hicolor/22x22/emblems/remmina-tool.png
/usr/share/icons/hicolor/22x22/emblems/remmina-vnc-ssh.png
/usr/share/icons/hicolor/22x22/emblems/remmina-vnc.png
/usr/share/icons/hicolor/22x22/emblems/remmina-xdmcp-ssh.png
/usr/share/icons/hicolor/22x22/emblems/remmina-xdmcp.png
/usr/share/icons/hicolor/24x24/apps/remmina-panel-inverted.png
/usr/share/icons/hicolor/24x24/apps/remmina-panel.png
/usr/share/icons/hicolor/24x24/apps/remmina.png
/usr/share/icons/hicolor/32x32/apps/remmina.png
/usr/share/icons/hicolor/48x48/apps/remmina.png
/usr/share/icons/hicolor/64x64/apps/remmina.png
/usr/share/icons/hicolor/72x72/apps/remmina.png
/usr/share/icons/hicolor/96x96/apps/remmina.png
/usr/share/icons/hicolor/scalable/apps/remmina.svg
/usr/share/metainfo/org.remmina.Remmina.appdata.xml
/usr/share/mime/packages/remmina-mime.xml
/usr/share/remmina/external_tools/functions.sh
/usr/share/remmina/external_tools/launcher.sh
/usr/share/remmina/external_tools/remmina_filezilla_sftp.sh
/usr/share/remmina/external_tools/remmina_filezilla_sftp_pki.sh
/usr/share/remmina/external_tools/remmina_nslookup.sh
/usr/share/remmina/external_tools/remmina_ping.sh
/usr/share/remmina/external_tools/remmina_traceroute.sh
/usr/share/remmina/ui/remmina_about.glade
/usr/share/remmina/ui/remmina_key_chooser.glade
/usr/share/remmina/ui/remmina_main.glade
/usr/share/remmina/ui/remmina_mpc.glade
/usr/share/remmina/ui/remmina_preferences.glade
/usr/share/remmina/ui/remmina_spinner.glade
/usr/share/remmina/ui/remmina_string_list.glade

%files dev
%defattr(-,root,root,-)
/usr/include/remmina/plugin.h
/usr/include/remmina/remmina_trace_calls.h
/usr/include/remmina/types.h
/usr/lib64/pkgconfig/remmina.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/remmina/plugins/remmina-plugin-exec.so
/usr/lib64/remmina/plugins/remmina-plugin-nx.so
/usr/lib64/remmina/plugins/remmina-plugin-rdp.so
/usr/lib64/remmina/plugins/remmina-plugin-vnc.so
/usr/lib64/remmina/plugins/remmina-plugin-xdmcp.so

%files locales -f remmina.lang
%defattr(-,root,root,-)

