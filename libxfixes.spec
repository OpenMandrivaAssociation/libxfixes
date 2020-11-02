%define major 3
%define libname %mklibname xfixes %{major}
%define devname %mklibname xfixes -d

# libXfixes is used by wine and steam
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%if %{with compat32}
%define lib32name libxfixes%{major}
%define dev32name libxfixes-devel
%endif

%global optflags %{optflags} -O3

Summary:	X Fixes  Library
Name:		libxfixes
Version:	5.0.3
Release:	6
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfixes-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
%if %{with compat32}
BuildRequires:	devel(libX11)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmpc)
%endif

%description
%{name} is a simple library designed to interface the X Fixes Extension.

%package -n %{libname}
Summary:	X Fixes  Library
Group:		Development/X11

%description -n %{libname}
%{name} is a simple library designed to interface the X Fixes Extension.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	X Fixes Library (32-bit)
Group:		Development/X11

%description -n %{lib32name}
%{name} is a simple library designed to interface the X Fixes Extension.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXfixes-%{version} -p1
export CONFIGURE_TOP="`pwd`"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXfixes.so.%{major}*

%files -n %{devname}
%{_libdir}/libXfixes.so
%{_libdir}/pkgconfig/xfixes.pc
%{_includedir}/X11/extensions/Xfixes.h
%{_mandir}/man3/Xfixes.*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXfixes.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXfixes.so
%{_prefix}/lib/pkgconfig/xfixes.pc
%endif
