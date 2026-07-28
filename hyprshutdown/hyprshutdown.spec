Name:           hyprshutdown
Version:        0.1.1
Release:        %autorelease -b4
Summary:        A graceful shutdown utility for Hyprland
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires: glaze-static

BuildRequires:  pkgconfig(hyprtoolkit)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pixman-1)

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/hyprshutdown

%changelog
%autochangelog
