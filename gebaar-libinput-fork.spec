Name:           gebaar-libinput-fork
Version:        0.1.5
Release:        2
Summary:        WM Independent Touchpad Gesture Daemon for libinput
Group:          System/Configuration/Hardware
License:        GPLv3
URL:            https://github.com/9ary/gebaar-libinput-fork
Source0:        https://github.com/9ary/gebaar-libinput-fork/archive/refs/tags/v%{version}.tar.gz
#Patch0:         fix-stdcxxfs.patch

BuildRequires:  clang
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
%autosetup -n %{name}-%{version} -p1

%define _build_compiler clang

%build
%cmake -G Ninja
%ninja_build

%install
%ninja_install

%files
%{_bindir}/gebaard
%license LICENSE
%doc README.md
