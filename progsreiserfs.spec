%define		_rc	rc8
Summary:	Programs needed for manipulating reiserfs partitions
Summary(pl):	Programy niezb�dne do manipulowania partycjami reiserfs
Name:		progsreiserfs
Version:	0.3.1
Release:	1.%{_rc}.4
License:	GPL
Group:		Applications/System
Source0:	http://reiserfs.linux.kiev.ua/snapshots/%{name}-%{version}-%{_rc}.tar.gz
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

%description -l pl
Progsreiserfs to pakiet pozwalaj�cy na tworzenie, niszczenie, zmian�
rozmiaru i kopiowanie systemu plik�w reiserfs.

%package devel
Summary:	Header files and libraries to develop reiserfs software
Summary(pl):	Pliki nag��wkowe i biblioteki do reiserfs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and libraries to develop software which operates on
reiserfs filesystems.

%description devel -l pl
Pliki nag��wkowe i biblioteki potrzebne do rozwoju oprogramowania
operuj�cego na systemie plik�w reiserfs.

%package static
Summary:	Static reiserfs software libraries
Summary(pl):	Biblioteki statyczne do reiserfs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static reiserfs software libraries.

%description static -l pl
Biblioteki statyczne do reiserfs.

%prep
%setup -q -n %{name}-%{version}-%{_rc}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/dal
%{_includedir}/reiserfs
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
