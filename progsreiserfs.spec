Summary:	Programs needed for manipulating reiserfs partitions
Summary(pl.UTF-8):	Programy niezbędne do manipulowania partycjami reiserfs
Name:		progsreiserfs
Version:	0.3.1
%define		subver	rc8
Release:	1.%{subver}.6
License:	GPL
Group:		Applications/System
Source0:	http://reiserfs.linux.kiev.ua/snapshots/%{name}-%{version}-%{subver}.tar.gz
# Source0-md5:	e545a171a207ec5b9045ceb1a982c1bd
Source1:	%{name}-pl.po
Patch0:		%{name}-Werror.patch
Patch1:		%{name}-sparc-linux.patch
Patch2:		%{name}-typo.patch
Patch3:		%{name}-am18.patch
Patch4:		%{name}-missing-nls.patch
URL:		http://reiserfs.linux.kiev.ua/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libuuid-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Progsreiserfs is a package that allows you to create, destroy, resize
and copy reiserfs filesystem.

%description -l pl.UTF-8
Progsreiserfs to pakiet pozwalający na tworzenie, niszczenie, zmianę
rozmiaru i kopiowanie systemu plików reiserfs.

%package devel
Summary:	Header files and libraries to develop reiserfs software
Summary(pl.UTF-8):	Pliki nagłówkowe i biblioteki do reiserfs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and libraries to develop software which operates on
reiserfs filesystems.

%description devel -l pl.UTF-8
Pliki nagłówkowe i biblioteki potrzebne do rozwoju oprogramowania
operującego na systemie plików reiserfs.

%package static
Summary:	Static reiserfs software libraries
Summary(pl.UTF-8):	Biblioteki statyczne do reiserfs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static reiserfs software libraries.

%description static -l pl.UTF-8
Biblioteki statyczne do reiserfs.

%prep
%setup -q -n %{name}-%{version}-%{subver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

cp -f %{SOURCE1} po/pl.po
%{__perl} -pi -e 's/(ALL_LINGUAS=")/$1pl /' configure.in

%build
# supplied libtool is broken (relink)
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-Werror
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install include/reiserfs/libprogs_tools.h $RPM_BUILD_ROOT%{_includedir}/reiserfs

# conflicts with reiserfsprogs
rm -f $RPM_BUILD_ROOT%{_sbindir}/{fsck,mkfs,resizefs,tunefs}.reiserfs
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/{fsck,mkfs,resizefs,tunefs}.reiserfs.8

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_sbindir}/cpfs.reiserfs
%attr(755,root,root) %{_libdir}/libdal-0.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdal-0.3.so.0
%attr(755,root,root) %{_libdir}/libreiserfs-0.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libreiserfs-0.3.so.0
%{_mandir}/man8/cpfs.reiserfs.8*
%{_mandir}/man8/reiserfs.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdal.so
%attr(755,root,root) %{_libdir}/libreiserfs.so
%{_libdir}/libdal.la
%{_libdir}/libreiserfs.la
%{_includedir}/dal
%{_includedir}/reiserfs
%{_aclocaldir}/progsreiserfs.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libdal.a
%{_libdir}/libreiserfs.a
