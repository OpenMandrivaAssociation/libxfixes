%define major 3
%define libname %mklibname xfixes %{major}
%define devname %mklibname xfixes -d

Summary:	X Fixes  Library
Name:		libxfixes
Version:	5.0.1
Release:	10
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfixes-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
%{name} is a simple library designed to interface the X Fixes Extension.

%package -n %{libname}
Summary:	X Fixes  Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
%{name} is a simple library designed to interface the X Fixes Extension.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libxfixes-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -qn libXfixes-%{version}
#autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXfixes.so.%{major}*

%files -n %{devname}
%{_libdir}/libXfixes.so
%{_libdir}/pkgconfig/xfixes.pc
%{_includedir}/X11/extensions/Xfixes.h
%{_mandir}/man3/Xfixes.*

