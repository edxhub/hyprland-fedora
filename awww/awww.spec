Name:           awww
Version:        0.12.1
Release:        %autorelease
Summary:        An Answer to your Wayland Wallpaper Woes
License:        GPL-3.0

URL:            https://codeberg.org/LGFae/%{name}
Source:         %{url}/archive/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  scdoc

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -p1 -n %{name}
cargo vendor
%cargo_prep -v vendor

%build
%cargo_build -f avif
./doc/gen.sh
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
install -Dpm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm755 target/release/%{name}-daemon %{buildroot}%{_bindir}/%{name}-daemon
install -Dpm644 completions/_%{name} %{buildroot}%{zsh_completions_dir}/_%{name}
install -Dpm644 completions/%{name}.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm644 completions/%{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm644 ./doc/generated/*.1 -t %{buildroot}%{_mandir}/man1

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc CHANGELOG.md
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-daemon
%{_mandir}/man1/%{name}*.1.*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
