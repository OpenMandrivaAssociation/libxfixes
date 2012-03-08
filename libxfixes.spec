%define major	3
%define libname		%mklibname xfixes %{major}
%define develname	%mklibname xfixes -d

Name: libxfixes
Summary:  X Fixes  Library
Version: 5.0
Release: 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXfixes-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 7.6-3
BuildRequires: x11-util-macros >= 1.0.1

%description
%{name} is a simple library designed to interface the X Fixes Extension.

%package -n %{libname}
Summary:  X Fixes  Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
%{name} is a simple library designed to interface the X Fixes Extension.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Provides: libxfixes-devel = %{version}-%{release}
Obsoletes: %{_lib}xfixes3-devel
Obsoletes: %{_lib}xfixes-static-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXfixes-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXfixes.so.%{major}*

%files -n %{develname}
%{_libdir}/libXfixes.so
%{_libdir}/pkgconfig/xfixes.pc
%{_includedir}/X11/extensions/Xfixes.h
%{_mandir}/man3/Xfixes.*

