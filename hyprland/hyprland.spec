Name:           hyprland
Version:        0.55.3
Release:        %autorelease
Summary:        Dynamic tiling Wayland compositor that doesn't sacrifice on its looks

# hyprland: BSD-3-Clause
# subprojects/hyprland-protocols: BSD-3-Clause
# subproject/udis86: BSD-2-Clause
# protocols/ext-workspace-unstable-v1.xml: HPND-sell-variant
# protocols/wlr-foreign-toplevel-management-unstable-v1.xml: HPND-sell-variant
# protocols/wlr-layer-shell-unstable-v1.xml: HPND-sell-variant
# protocols/idle.xml: LGPL-2.1-or-later
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/Hyprland
Source:        %{url}/releases/download/v%{version}/source-v%{version}.tar.gz

BuildRequires: bison
BuildRequires: byacc
BuildRequires: cmake
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: libX11-devel
BuildRequires:  libxml2-devel
BuildRequires: meson
BuildRequires: glaze-static
BuildRequires: libX11-devel
BuildRequires:  xkeyboard-config-devel

BuildRequires: pkgconfig(aquamarine)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(glslang)
BuildRequires: pkgconfig(hwdata)
BuildRequires: pkgconfig(hyprcursor)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(hyprwayland-scanner)
BuildRequires: pkgconfig(hyprwire)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libdisplay-info)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libinput) >= 1.28
BuildRequires: pkgconfig(libliftoff)
BuildRequires: pkgconfig(libseat)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(lua)
BuildRequires: pkgconfig(muparser)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(re2)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(tomlplusplus)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols) >= 1.45
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(xcb-composite)
BuildRequires: pkgconfig(xcb-dri3)
BuildRequires: pkgconfig(xcb-errors)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-present)
BuildRequires: pkgconfig(xcb-render)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-res)
BuildRequires: pkgconfig(xcb-shm)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xcb-xfixes)
BuildRequires: pkgconfig(xcb-xinput)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xwayland)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xkbcommon)

Requires:       xorg-x11-server-Xwayland
Requires:       aquamarine
Requires:       hyprcursor
Requires:       hyprgraphics
Requires:       hyprlang
Requires:       hyprutils

# Used in the default configuration
Recommends:     kitty
Recommends:     rofi
Recommends:     playerctl
Recommends:     brightnessctl
Recommends:     hyprland-qtutils
# Lack of graphical drivers may hurt the common use case
Recommends:     mesa-dri-drivers
# Logind needs polkit to create a graphical session
Recommends:     polkit
# https://wiki.hyprland.org/Useful-Utilities/Systemd-start
Recommends:     uwsm

Recommends:     (qt5-qtwayland if qt5-qtbase-gui)
Recommends:     (qt6-qtwayland if qt6-qtbase-gui)

%description
Hyprland is a dynamic tiling Wayland compositor that doesn't sacrifice
on its looks. It supports multiple layouts, fancy effects, has a
very flexible IPC model allowing for a lot of customization, a powerful
plugin system and more.

%package        devel
Summary:        Header and protocol files for %{name}
License:        BSD-3-Clause
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cpio
Obsoletes: hyprland-nvidia-devel < 1:0.32.3-2
Obsoletes: hyprland-legacyrenderer-devel < 0.49.0
Provides: hyprland-nvidia-devel
Requires:       git-core
Requires:       pkgconfig(xkbcommon)

%description    devel
%{summary}.

%prep
%autosetup -p1 -n %{name}-source

%build

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DNO_TESTS=TRUE \
    -DBUILD_TESTING=FALSE
%cmake_build

%install

%cmake_install

%files
%license LICENSE
%{_bindir}/[Hh]yprland
%{_bindir}/start-hyprland
%{_bindir}/hyprctl
%{_bindir}/hyprpm
%{_datadir}/hypr/
%{_datadir}/wayland-sessions/hyprland.desktop
%{_datadir}/wayland-sessions/hyprland-uwsm.desktop
%{_datadir}/xdg-desktop-portal/hyprland-portals.conf
%{_mandir}/man1/hyprctl.1*
%{_mandir}/man1/Hyprland.1*
%{bash_completions_dir}/hypr*
%{fish_completions_dir}/hypr*.fish
%{zsh_completions_dir}/_hypr*

%files devel
%{_datadir}/pkgconfig/hyprland.pc
%{_includedir}/hyprland/

%changelog
%autochangelog
