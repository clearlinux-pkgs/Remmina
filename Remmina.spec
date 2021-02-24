#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Remmina
Version  : 1.4.11
Release  : 24
URL      : https://github.com/FreeRDP/Remmina/archive/v1.4.11/Remmina-1.4.11.tar.gz
Source0  : https://github.com/FreeRDP/Remmina/archive/v1.4.11/Remmina-1.4.11.tar.gz
Summary  : The GTK+ Remote Desktop Client
Group    : Development/Tools
License  : GPL-2.0 OpenSSL
Requires: Remmina-bin = %{version}-%{release}
Requires: Remmina-data = %{version}-%{release}
Requires: Remmina-lib = %{version}-%{release}
Requires: Remmina-license = %{version}-%{release}
Requires: Remmina-locales = %{version}-%{release}
Requires: Remmina-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gettext
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : gtk+-dev
BuildRequires : json-glib-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libgcrypt-dev
BuildRequires : libsecret-dev
BuildRequires : libsoup-dev
BuildRequires : libssh-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(appindicator3-0.1)
BuildRequires : pkgconfig(atk)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(freerdp2)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libpcre2-8)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libsodium)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libssh)
BuildRequires : pkgconfig(libvncserver)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(spice-client-gtk-3.0)
BuildRequires : pkgconfig(spice-protocol)
BuildRequires : pkgconfig(telepathy-glib)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : spice-gtk-dev
BuildRequires : vte-dev

%description
[![](https://img.shields.io/liberapay/receives/Remmina.svg?logo=liberapay)](https://liberapay.com/Remmina/donate)
[![](https://img.shields.io/liberapay/patrons/remmina.svg?logo=liberapay)](https://liberapay.com/Remmina/donate)
[![Build Status](https://gitlab.com/Remmina/Remmina/badges/master/pipeline.svg)](https://gitlab.com/Remmina/Remmina/pipelines)
[![Translation status](https://hosted.weblate.org/widgets/remmina/-/remmina/svg-badge.svg)](https://hosted.weblate.org/engage/remmina/?utm_source=widget)
[![remmina](https://snapcraft.io//remmina/badge.svg)](https://snapcraft.io/remmina)

%package bin
Summary: bin components for the Remmina package.
Group: Binaries
Requires: Remmina-data = %{version}-%{release}
Requires: Remmina-license = %{version}-%{release}

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
Requires: Remmina-lib = %{version}-%{release}
Requires: Remmina-bin = %{version}-%{release}
Requires: Remmina-data = %{version}-%{release}
Provides: Remmina-devel = %{version}-%{release}
Requires: Remmina = %{version}-%{release}

%description dev
dev components for the Remmina package.


%package lib
Summary: lib components for the Remmina package.
Group: Libraries
Requires: Remmina-data = %{version}-%{release}
Requires: Remmina-license = %{version}-%{release}

%description lib
lib components for the Remmina package.


%package license
Summary: license components for the Remmina package.
Group: Default

%description license
license components for the Remmina package.


%package locales
Summary: locales components for the Remmina package.
Group: Default

%description locales
locales components for the Remmina package.


%package man
Summary: man components for the Remmina package.
Group: Default

%description man
man components for the Remmina package.


%prep
%setup -q -n Remmina-1.4.11
cd %{_builddir}/Remmina-1.4.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613604559
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DWITH_APPINDICATOR=OFF \
-DWITH_AVAHI=OFF \
-DWITH_CUPS=OFF \
-DWITH_FREERDP=ON \
-DWITH_FREERDP3=OFF \
-DWITH_GCRYPT=ON \
-DWITH_GETTEXT=ON \
-DWITH_KIOSK_SESSION=ON \
-DWITH_SPICE=ON \
-DWITH_TELEPATHY=OFF \
-DWITH_VTE=ON
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1613604559
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Remmina
cp %{_builddir}/Remmina-1.4.11/COPYING %{buildroot}/usr/share/package-licenses/Remmina/ffe386a510e8e12e7b831dc0c3630f89c5cd4aff
cp %{_builddir}/Remmina-1.4.11/LICENSE %{buildroot}/usr/share/package-licenses/Remmina/62df4d47ea6d73566d5e8de65d8e126fd096fc4f
cp %{_builddir}/Remmina-1.4.11/LICENSE.OpenSSL %{buildroot}/usr/share/package-licenses/Remmina/e3ca00760c7f1c1d8e8b306eb7e41f3bf4d7f10a
pushd clr-build
%make_install
popd
%find_lang remmina

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-session-remmina
/usr/bin/remmina
/usr/bin/remmina-file-wrapper
/usr/bin/remmina-gnome

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.remmina.Remmina.desktop
/usr/share/applications/remmina-file.desktop
/usr/share/applications/remmina-gnome.desktop
/usr/share/gnome-session/sessions/remmina-gnome.session
/usr/share/icons/hicolor/128x128/apps/org.remmina.Remmina.png
/usr/share/icons/hicolor/128x128/apps/remmina-panel-inverted.png
/usr/share/icons/hicolor/128x128/apps/remmina-panel.png
/usr/share/icons/hicolor/16x16/apps/org.remmina.Remmina.png
/usr/share/icons/hicolor/16x16/apps/remmina-panel-inverted.png
/usr/share/icons/hicolor/16x16/apps/remmina-panel.png
/usr/share/icons/hicolor/22x22/apps/org.remmina.Remmina.png
/usr/share/icons/hicolor/22x22/apps/remmina-panel-inverted.png
/usr/share/icons/hicolor/22x22/apps/remmina-panel.png
/usr/share/icons/hicolor/24x24/apps/org.remmina.Remmina.png
/usr/share/icons/hicolor/24x24/apps/remmina-panel-inverted.png
/usr/share/icons/hicolor/24x24/apps/remmina-panel.png
/usr/share/icons/hicolor/256x256/apps/org.remmina.Remmina.png
/usr/share/icons/hicolor/256x256/apps/remmina-panel-inverted.png
/usr/share/icons/hicolor/256x256/apps/remmina-panel.png
/usr/share/icons/hicolor/32x32/apps/org.remmina.Remmina.png
/usr/share/icons/hicolor/32x32/apps/remmina-panel-inverted.png
/usr/share/icons/hicolor/32x32/apps/remmina-panel.png
/usr/share/icons/hicolor/48x48/apps/org.remmina.Remmina.png
/usr/share/icons/hicolor/48x48/apps/remmina-panel-inverted.png
/usr/share/icons/hicolor/48x48/apps/remmina-panel.png
/usr/share/icons/hicolor/64x64/apps/org.remmina.Remmina.png
/usr/share/icons/hicolor/64x64/apps/remmina-panel-inverted.png
/usr/share/icons/hicolor/64x64/apps/remmina-panel.png
/usr/share/icons/hicolor/72x72/apps/org.remmina.Remmina.png
/usr/share/icons/hicolor/72x72/apps/remmina-panel-inverted.png
/usr/share/icons/hicolor/72x72/apps/remmina-panel.png
/usr/share/icons/hicolor/96x96/apps/org.remmina.Remmina.png
/usr/share/icons/hicolor/96x96/apps/remmina-panel-inverted.png
/usr/share/icons/hicolor/96x96/apps/remmina-panel.png
/usr/share/icons/hicolor/apps/org.remmina.Remmina-symbolic.svg
/usr/share/icons/hicolor/apps/remmina-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-camera-photo-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-connect-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-disconnect-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-document-save-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-document-send-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-duplicate-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-dynres-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-fit-window-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-fullscreen-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-go-bottom-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-keyboard-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-pan-down-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-pan-up-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-pin-down-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-pin-up-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-preferences-system-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-scale-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-switch-page-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/remmina-system-run-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/view-list.svg
/usr/share/icons/hicolor/scalable/apps/org.remmina.Remmina.svg
/usr/share/icons/hicolor/scalable/apps/remmina-panel-inverted.svg
/usr/share/icons/hicolor/scalable/apps/remmina-panel.svg
/usr/share/icons/hicolor/scalable/emblems/remmina-nx-symbolic.svg
/usr/share/icons/hicolor/scalable/emblems/remmina-rdp-ssh-symbolic.svg
/usr/share/icons/hicolor/scalable/emblems/remmina-rdp-symbolic.svg
/usr/share/icons/hicolor/scalable/emblems/remmina-sftp-symbolic.svg
/usr/share/icons/hicolor/scalable/emblems/remmina-spice-ssh-symbolic.svg
/usr/share/icons/hicolor/scalable/emblems/remmina-spice-symbolic.svg
/usr/share/icons/hicolor/scalable/emblems/remmina-ssh-symbolic.svg
/usr/share/icons/hicolor/scalable/emblems/remmina-tool-symbolic.svg
/usr/share/icons/hicolor/scalable/emblems/remmina-vnc-ssh-symbolic.svg
/usr/share/icons/hicolor/scalable/emblems/remmina-vnc-symbolic.svg
/usr/share/icons/hicolor/scalable/emblems/remmina-xdmcp-ssh-symbolic.svg
/usr/share/icons/hicolor/scalable/emblems/remmina-xdmcp-symbolic.svg
/usr/share/icons/hicolor/scalable/panel/remmina-panel-inverted.svg
/usr/share/icons/hicolor/scalable/panel/remmina-panel.svg
/usr/share/metainfo/org.remmina.Remmina.appdata.xml
/usr/share/mime-packages/remmina-mime.xml
/usr/share/remmina/external_tools/functions.sh
/usr/share/remmina/external_tools/launcher.sh
/usr/share/remmina/external_tools/remmina_filezilla_sftp.sh
/usr/share/remmina/external_tools/remmina_filezilla_sftp_pki.sh
/usr/share/remmina/external_tools/remmina_nslookup.sh
/usr/share/remmina/external_tools/remmina_ping.sh
/usr/share/remmina/external_tools/remmina_traceroute.sh
"/usr/share/remmina/theme/3024 Day.colors"
"/usr/share/remmina/theme/3024 Night.colors"
/usr/share/remmina/theme/Adventure.colors
/usr/share/remmina/theme/AdventureTime.colors
/usr/share/remmina/theme/Afterglow.colors
/usr/share/remmina/theme/AlienBlood.colors
/usr/share/remmina/theme/Andromeda.colors
/usr/share/remmina/theme/Argonaut.colors
/usr/share/remmina/theme/Arthur.colors
/usr/share/remmina/theme/AtelierSulphurpool.colors
/usr/share/remmina/theme/Atom.colors
/usr/share/remmina/theme/AtomOneLight.colors
/usr/share/remmina/theme/Aurora.colors
"/usr/share/remmina/theme/Banana Blueberry.colors"
/usr/share/remmina/theme/Batman.colors
"/usr/share/remmina/theme/Belafonte Day.colors"
"/usr/share/remmina/theme/Belafonte Night.colors"
/usr/share/remmina/theme/BirdsOfParadise.colors
/usr/share/remmina/theme/Blazer.colors
"/usr/share/remmina/theme/Blue Matrix.colors"
/usr/share/remmina/theme/BlueBerryPie.colors
/usr/share/remmina/theme/BlulocoDark.colors
/usr/share/remmina/theme/BlulocoLight.colors
/usr/share/remmina/theme/Borland.colors
/usr/share/remmina/theme/Breeze.colors
"/usr/share/remmina/theme/Bright Lights.colors"
/usr/share/remmina/theme/Broadcast.colors
/usr/share/remmina/theme/Brogrammer.colors
"/usr/share/remmina/theme/Builtin Dark.colors"
"/usr/share/remmina/theme/Builtin Light.colors"
"/usr/share/remmina/theme/Builtin Pastel Dark.colors"
"/usr/share/remmina/theme/Builtin Solarized Dark.colors"
"/usr/share/remmina/theme/Builtin Solarized Light.colors"
"/usr/share/remmina/theme/Builtin Tango Dark.colors"
"/usr/share/remmina/theme/Builtin Tango Light.colors"
/usr/share/remmina/theme/C64.colors
/usr/share/remmina/theme/CLRS.colors
/usr/share/remmina/theme/Calamity.colors
/usr/share/remmina/theme/Chalk.colors
/usr/share/remmina/theme/Chalkboard.colors
/usr/share/remmina/theme/ChallengerDeep.colors
/usr/share/remmina/theme/Chester.colors
/usr/share/remmina/theme/Ciapre.colors
"/usr/share/remmina/theme/Cobalt Neon.colors"
/usr/share/remmina/theme/Cobalt2.colors
/usr/share/remmina/theme/CrayonPonyFish.colors
/usr/share/remmina/theme/Cyberdyne.colors
"/usr/share/remmina/theme/Dark Pastel.colors"
/usr/share/remmina/theme/Dark+.colors
/usr/share/remmina/theme/Darkside.colors
/usr/share/remmina/theme/Desert.colors
/usr/share/remmina/theme/DimmedMonokai.colors
/usr/share/remmina/theme/Django.colors
/usr/share/remmina/theme/DjangoRebornAgain.colors
/usr/share/remmina/theme/DjangoSmooth.colors
/usr/share/remmina/theme/DoomOne.colors
/usr/share/remmina/theme/DotGov.colors
/usr/share/remmina/theme/Dracula+.colors
/usr/share/remmina/theme/Dracula.colors
"/usr/share/remmina/theme/Duotone Dark.colors"
/usr/share/remmina/theme/ENCOM.colors
/usr/share/remmina/theme/Earthsong.colors
/usr/share/remmina/theme/Elemental.colors
/usr/share/remmina/theme/Elementary.colors
"/usr/share/remmina/theme/Espresso Libre.colors"
/usr/share/remmina/theme/Espresso.colors
/usr/share/remmina/theme/Fahrenheit.colors
/usr/share/remmina/theme/Fideloper.colors
/usr/share/remmina/theme/FirefoxDev.colors
/usr/share/remmina/theme/Firewatch.colors
/usr/share/remmina/theme/FishTank.colors
/usr/share/remmina/theme/Flat.colors
/usr/share/remmina/theme/Flatland.colors
/usr/share/remmina/theme/Floraverse.colors
/usr/share/remmina/theme/ForestBlue.colors
/usr/share/remmina/theme/Framer.colors
/usr/share/remmina/theme/FrontEndDelight.colors
/usr/share/remmina/theme/FunForrest.colors
/usr/share/remmina/theme/Galaxy.colors
/usr/share/remmina/theme/Github.colors
/usr/share/remmina/theme/Glacier.colors
/usr/share/remmina/theme/Grape.colors
/usr/share/remmina/theme/Grass.colors
"/usr/share/remmina/theme/Gruvbox Dark.colors"
"/usr/share/remmina/theme/Gruvbox Light.colors"
/usr/share/remmina/theme/Guezwhoz.colors
/usr/share/remmina/theme/Hacktober.colors
/usr/share/remmina/theme/Hardcore.colors
/usr/share/remmina/theme/Harper.colors
/usr/share/remmina/theme/Highway.colors
"/usr/share/remmina/theme/Hipster Green.colors"
/usr/share/remmina/theme/Hivacruz.colors
/usr/share/remmina/theme/Homebrew.colors
/usr/share/remmina/theme/Hopscotch.256.colors
/usr/share/remmina/theme/Hopscotch.colors
/usr/share/remmina/theme/Hurtado.colors
/usr/share/remmina/theme/Hybrid.colors
/usr/share/remmina/theme/IC_Green_PPL.colors
/usr/share/remmina/theme/IC_Orange_PPL.colors
/usr/share/remmina/theme/IR_Black.colors
"/usr/share/remmina/theme/Jackie Brown.colors"
/usr/share/remmina/theme/Japanesque.colors
/usr/share/remmina/theme/Jellybeans.colors
"/usr/share/remmina/theme/JetBrains Darcula.colors"
/usr/share/remmina/theme/Kibble.colors
/usr/share/remmina/theme/Kolorit.colors
/usr/share/remmina/theme/Konsolas.colors
"/usr/share/remmina/theme/Lab Fox.colors"
/usr/share/remmina/theme/Laser.colors
"/usr/share/remmina/theme/Later This Evening.colors"
/usr/share/remmina/theme/Lavandula.colors
/usr/share/remmina/theme/LiquidCarbon.colors
/usr/share/remmina/theme/LiquidCarbonTransparent.colors
/usr/share/remmina/theme/LiquidCarbonTransparentInverse.colors
"/usr/share/remmina/theme/Man Page.colors"
/usr/share/remmina/theme/Material.colors
/usr/share/remmina/theme/MaterialDark.colors
/usr/share/remmina/theme/MaterialDarker.colors
/usr/share/remmina/theme/MaterialOcean.colors
/usr/share/remmina/theme/Mathias.colors
/usr/share/remmina/theme/Medallion.colors
/usr/share/remmina/theme/Mirage.colors
/usr/share/remmina/theme/Misterioso.colors
/usr/share/remmina/theme/Molokai.colors
/usr/share/remmina/theme/MonaLisa.colors
"/usr/share/remmina/theme/Monokai Remastered.colors"
"/usr/share/remmina/theme/Monokai Soda.colors"
"/usr/share/remmina/theme/Monokai Vivid.colors"
/usr/share/remmina/theme/N0tch2k.colors
/usr/share/remmina/theme/Neopolitan.colors
/usr/share/remmina/theme/Neutron.colors
"/usr/share/remmina/theme/Night Owlish Light.colors"
"/usr/share/remmina/theme/NightLion v1.colors"
"/usr/share/remmina/theme/NightLion v2.colors"
"/usr/share/remmina/theme/Nocturnal Winter.colors"
/usr/share/remmina/theme/Novel.colors
/usr/share/remmina/theme/Obsidian.colors
/usr/share/remmina/theme/Ocean.colors
/usr/share/remmina/theme/OceanicMaterial.colors
/usr/share/remmina/theme/Ollie.colors
/usr/share/remmina/theme/OneHalfDark.colors
/usr/share/remmina/theme/OneHalfLight.colors
"/usr/share/remmina/theme/Operator Mono Dark.colors"
"/usr/share/remmina/theme/Overnight Slumber.colors"
/usr/share/remmina/theme/Pandora.colors
"/usr/share/remmina/theme/Paraiso Dark.colors"
"/usr/share/remmina/theme/Parasio Dark.colors"
/usr/share/remmina/theme/PaulMillr.colors
/usr/share/remmina/theme/PencilDark.colors
/usr/share/remmina/theme/PencilLight.colors
"/usr/share/remmina/theme/Piatto Light.colors"
/usr/share/remmina/theme/Pnevma.colors
"/usr/share/remmina/theme/Popping and Locking.colors"
"/usr/share/remmina/theme/Pro Light.colors"
/usr/share/remmina/theme/Pro.colors
"/usr/share/remmina/theme/Purple Rain.colors"
/usr/share/remmina/theme/Rapture.colors
"/usr/share/remmina/theme/Red Alert.colors"
"/usr/share/remmina/theme/Red Planet.colors"
"/usr/share/remmina/theme/Red Sands.colors"
/usr/share/remmina/theme/Relaxed.colors
/usr/share/remmina/theme/Rippedcasts.colors
"/usr/share/remmina/theme/Rouge 2.colors"
/usr/share/remmina/theme/Royal.colors
/usr/share/remmina/theme/Ryuuko.colors
/usr/share/remmina/theme/Sakura.colors
"/usr/share/remmina/theme/Scarlet Protocol.colors"
/usr/share/remmina/theme/SeaShells.colors
"/usr/share/remmina/theme/Seafoam Pastel.colors"
/usr/share/remmina/theme/Seti.colors
/usr/share/remmina/theme/Shaman.colors
/usr/share/remmina/theme/Slate.colors
/usr/share/remmina/theme/SleepyHollow.colors
/usr/share/remmina/theme/Smyck.colors
/usr/share/remmina/theme/Snazzy.colors
/usr/share/remmina/theme/SoftServer.colors
"/usr/share/remmina/theme/Solarized Darcula.colors"
"/usr/share/remmina/theme/Solarized Dark - Patched.colors"
"/usr/share/remmina/theme/Solarized Dark Higher Contrast.colors"
"/usr/share/remmina/theme/Solarized Dark.colors"
"/usr/share/remmina/theme/Solarized Light.colors"
"/usr/share/remmina/theme/SpaceGray Eighties Dull.colors"
"/usr/share/remmina/theme/SpaceGray Eighties.colors"
/usr/share/remmina/theme/SpaceGray.colors
/usr/share/remmina/theme/Spacedust.colors
/usr/share/remmina/theme/Spiderman.colors
/usr/share/remmina/theme/Spring.colors
/usr/share/remmina/theme/Square.colors
/usr/share/remmina/theme/Subliminal.colors
/usr/share/remmina/theme/Sundried.colors
/usr/share/remmina/theme/Symfonic.colors
"/usr/share/remmina/theme/Tango Adapted.colors"
"/usr/share/remmina/theme/Tango Half Adapted.colors"
/usr/share/remmina/theme/Teerb.colors
"/usr/share/remmina/theme/Terminal Basic.colors"
"/usr/share/remmina/theme/Thayer Bright.colors"
"/usr/share/remmina/theme/The Hulk.colors"
"/usr/share/remmina/theme/Tinacious Design (Dark).colors"
"/usr/share/remmina/theme/Tinacious Design (Light).colors"
"/usr/share/remmina/theme/Tomorrow Night Blue.colors"
"/usr/share/remmina/theme/Tomorrow Night Bright.colors"
"/usr/share/remmina/theme/Tomorrow Night Burns.colors"
"/usr/share/remmina/theme/Tomorrow Night Eighties.colors"
"/usr/share/remmina/theme/Tomorrow Night.colors"
/usr/share/remmina/theme/Tomorrow.colors
/usr/share/remmina/theme/ToyChest.colors
/usr/share/remmina/theme/Treehouse.colors
/usr/share/remmina/theme/Twilight.colors
/usr/share/remmina/theme/Ubuntu.colors
/usr/share/remmina/theme/UltraViolent.colors
/usr/share/remmina/theme/UnderTheSea.colors
/usr/share/remmina/theme/Unikitty.colors
/usr/share/remmina/theme/Urple.colors
/usr/share/remmina/theme/Vaughn.colors
/usr/share/remmina/theme/VibrantInk.colors
"/usr/share/remmina/theme/Violet Dark.colors"
"/usr/share/remmina/theme/Violet Light.colors"
/usr/share/remmina/theme/WarmNeon.colors
/usr/share/remmina/theme/Wez.colors
/usr/share/remmina/theme/Whimsy.colors
/usr/share/remmina/theme/WildCherry.colors
/usr/share/remmina/theme/Wombat.colors
/usr/share/remmina/theme/Wryan.colors
/usr/share/remmina/theme/Zenburn.colors
/usr/share/remmina/theme/ayu.colors
/usr/share/remmina/theme/ayu_light.colors
/usr/share/remmina/theme/coffee_theme.colors
/usr/share/remmina/theme/cyberpunk.colors
/usr/share/remmina/theme/deep.colors
/usr/share/remmina/theme/idea.colors
/usr/share/remmina/theme/idleToes.colors
/usr/share/remmina/theme/jubi.colors
/usr/share/remmina/theme/lovelace.colors
/usr/share/remmina/theme/midnight-in-mojave.colors
/usr/share/remmina/theme/nord.colors
/usr/share/remmina/theme/primary.colors
/usr/share/remmina/theme/purplepeter.colors
/usr/share/remmina/theme/rebecca.colors
/usr/share/remmina/theme/shades-of-purple.colors
/usr/share/remmina/theme/synthwave-everything.colors
/usr/share/remmina/theme/synthwave.colors
/usr/share/remmina/ui/remmina_about.glade
/usr/share/remmina/ui/remmina_key_chooser.glade
/usr/share/remmina/ui/remmina_main.glade
/usr/share/remmina/ui/remmina_mpc.glade
/usr/share/remmina/ui/remmina_news.glade
/usr/share/remmina/ui/remmina_preferences.glade
/usr/share/remmina/ui/remmina_search.glade
/usr/share/remmina/ui/remmina_snap_info_dialog.glade
/usr/share/remmina/ui/remmina_spinner.glade
/usr/share/remmina/ui/remmina_string_list.glade
/usr/share/remmina/ui/remmina_unlock.glade
/usr/share/xsessions/remmina-gnome.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/remmina/plugin.h
/usr/include/remmina/remmina_trace_calls.h
/usr/include/remmina/types.h
/usr/lib64/pkgconfig/remmina.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/remmina/plugins/remmina-plugin-exec.so
/usr/lib64/remmina/plugins/remmina-plugin-nx.so
/usr/lib64/remmina/plugins/remmina-plugin-rdp.so
/usr/lib64/remmina/plugins/remmina-plugin-secret.so
/usr/lib64/remmina/plugins/remmina-plugin-spice.so
/usr/lib64/remmina/plugins/remmina-plugin-st.so
/usr/lib64/remmina/plugins/remmina-plugin-vnc.so
/usr/lib64/remmina/plugins/remmina-plugin-xdmcp.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Remmina/62df4d47ea6d73566d5e8de65d8e126fd096fc4f
/usr/share/package-licenses/Remmina/e3ca00760c7f1c1d8e8b306eb7e41f3bf4d7f10a
/usr/share/package-licenses/Remmina/ffe386a510e8e12e7b831dc0c3630f89c5cd4aff

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnome-session-remmina.1
/usr/share/man/man1/remmina-file-wrapper.1
/usr/share/man/man1/remmina-gnome.1
/usr/share/man/man1/remmina.1

%files locales -f remmina.lang
%defattr(-,root,root,-)

