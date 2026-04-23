%define debug_package %{nil}

Name:           gebaar-libinput-fork
Version:        0.1.5
Release:        1
Summary:        A Super Simple WM Independent Touchpad Gesture Daemon for libinput
Group:          System/Configuration/Hardware
License:        GPLv3
URL:            https://github.com/9ary/gebaar-libinput-fork
Source0:        https://github.com/9ary/gebaar-libinput-fork/archive/refs/tags/v%{version}.tar.gz

# Use pkgconfig/cmake names for 2026 stability
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libudev)

Requires:       libinput
Conflicts:      gebaar
Provides:       gebaar

%description
A Super Simple WM Independent Touchpad Gesture Daemon for libinput. 
Forked version with additional features.

%prep
%autosetup -p1

%build
# OpenMandriva 2026 macros automatically handle optimization flags
%cmake -G Ninja
%ninja_build

%install
%ninja_install

# Explicitly handle documentation and license paths
install -Dm644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE
install -Dm644 README.md %{buildroot}%{_docdir}/%{name}/README.md

%files
%{_bindir}/gebaard
%{_datadir}/licenses/%{name}/LICENSE
%{_docdir}/%{name}/README.md
