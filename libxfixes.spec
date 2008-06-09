%define libxfixes %mklibname xfixes 3
Name: libxfixes
Summary:  X Fixes  Library
Version: 4.0.3
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXfixes-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
%{name} is a simple library designed to interface the X Fixes Extension.

#-----------------------------------------------------------

%package -n %{libxfixes}
Summary:  X Fixes  Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxfixes}
%{name} is a simple library designed to interface the X Fixes Extension.

#-----------------------------------------------------------

%package -n %{libxfixes}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxfixes} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxfixes-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxfixes}-devel
Development files for %{name}

%pre -n %{libxfixes}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxfixes}-devel
%defattr(-,root,root)
%{_libdir}/libXfixes.so
%{_libdir}/libXfixes.la
%{_libdir}/pkgconfig/xfixes.pc
%{_includedir}/X11/extensions/Xfixes.h
%{_mandir}/man3/Xfixes.*

#-----------------------------------------------------------

%package -n %{libxfixes}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxfixes}-devel = %{version}
Provides: libxfixes-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxfixes}-static-devel
Static development files for %{name}

%files -n %{libxfixes}-static-devel
%defattr(-,root,root)
%{_libdir}/libXfixes.a

#-----------------------------------------------------------

%prep
%setup -q -n libXfixes-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libxfixes}
%defattr(-,root,root)
%{_libdir}/libXfixes.so.3
%{_libdir}/libXfixes.so.3.1.0


