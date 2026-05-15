Name:           waybar
Version:        0.15.0
Release:        %autorelease
Summary:        Highly customizable Wayland bar for Sway and Wlroots based compositors, with workspaces support for Hyprland
License:        MIT
URL:            https://github.com/Alexays/Waybar
Source:        %{url}/archive/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.49.0
BuildRequires:  scdoc
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(catch2)
BuildRequires:  pkgconfig(date)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(fmt) >= 8.1.1
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(playerctl)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(spdlog) >= 1.10.0
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wireplumber-0.5)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(xkbregistry)
BuildRequires:  python3dist(packaging)
BuildRequires:  pkgconfig(libgps)

Conflicts:      waybar
Provides:       waybar

Enhances:       hyprland
Recommends:     (font(fontawesome6free) or font(fontawesome5free))

%description
%{summary}.

%prep
%autosetup -p1 -n Waybar-%{version}

%build
%meson \
    -Dsndio=disabled \
    -Dcava=disabled \
    -Dwireplumber=enabled
%meson_build

%install
%meson_install
# remove man pages for disabled modules
for module in cava sndio %{!?with_wireplumber:wireplumber} wlr-workspaces; do
    rm -f %{buildroot}%{_mandir}/man5/%{name}-${module}.5
done

%check
%meson_test

%post
%systemd_user_post waybar.service

%preun
%systemd_user_preun waybar.service


%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/xdg/waybar
%config(noreplace) %{_sysconfdir}/xdg/waybar/config.jsonc
%config(noreplace) %{_sysconfdir}/xdg/waybar/style.css
%{_bindir}/waybar
%{_mandir}/man5/waybar*
%{_userunitdir}/waybar.service

%changelog
%autochangelog
