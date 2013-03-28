%define major	3
%define libname		%mklibname xfixes %{major}
%define develname	%mklibname xfixes -d

Name:		libxfixes
Summary:	X Fixes  Library
Version:	5.0
Release:	4
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfixes-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	x11-proto-devel >= 7.6-3
BuildRequires:	x11-util-macros >= 1.0.1

%description
%{name} is a simple library designed to interface the X Fixes Extension.

%package -n %{libname}
Summary:	X Fixes  Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libname}
%{name} is a simple library designed to interface the X Fixes Extension.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libxfixes-devel = %{version}-%{release}
Obsoletes:	%{_lib}xfixes3-devel < 5.0
Obsoletes:	%{_lib}xfixes-static-devel < 5.0
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXfixes-%{version}

%build
autoreconf -fi
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

%changelog
* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 5.0-3
+ Revision: 783360
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 5.0-2
+ Revision: 745649
- rebuild
- disabled static build
- removed .la files
- cleaned up spec

* Mon Apr 11 2011 Matthew Dawkins <mattydaw@mandriva.org> 5.0-1
+ Revision: 652707
- defined major
- requires x11-proto-devel 7.6-3 or better
- new version 5.0

* Tue Mar 15 2011 Funda Wang <fwang@mandriva.org> 4.0.5-3
+ Revision: 644854
- correct obsoletes

* Fri Feb 18 2011 Matthew Dawkins <mattydaw@mandriva.org> 4.0.5-2
+ Revision: 638541
- dropped major from devel and static pkgs
- added proper provides and obsoletes

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 4.0.5-1mdv2011.0
+ Revision: 556456
- new release

* Mon Nov 09 2009 Thierry Vignaud <tv@mandriva.org> 4.0.4-1mdv2010.1
+ Revision: 463609
- new release

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.0.3-5mdv2010.0
+ Revision: 425898
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 4.0.3-4mdv2009.0
+ Revision: 223073
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 4.0.3-3mdv2008.1
+ Revision: 151684
- Update BuildRequires and rebuild.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 4.0.3-2mdv2008.1
+ Revision: 129248
- kill re-definition of %%buildroot on Pixel's request
- fix man pages extension


* Fri Feb 16 2007 Thierry Vignaud <tvignaud@mandriva.com> 4.0.3-2mdv2007.0
+ Revision: 121698
- bump release

* Tue Nov 21 2006 Thierry Vignaud <tvignaud@mandriva.com> 4.0.3-1mdv2007.1
+ Revision: 85952
- new release

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - X11R7.1
    - increment release
    - fixed more dependencies
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

