%define         _rc         rc7
Summary:	Programs needed for manipulating reiserfs partitions
Summary(pl):	Programy niezbêdne do manipulowania partycjami reiserfs
Name:		progsreiserfs
Version:	0.3.1
Release:	1.%{_rc}.1
License:	GPL
Group:		Applications/System
Source0:	http://reiserfs.linux.kiev.ua/snapshots/%{name}-%{version}-%{_rc}.tar.gz
Patch0:		%{name}-Werror.patch
URL:		http://reiserfs.linux.kiev.ua/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 1:1.4.2-9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Progsreiserfs is a package that allows you to create, destroy, resize
and copy reiserfs filesystem.

%description -l pl
Progsreiserfs to pakiet pozwalaj±cy na tworzenie, niszczenie, zmianê
rozmiaru i kopiowanie systemu plików reiserfs.

%package devel
Summary:	Header files and libraries to develop reiserfs software
Summary(pl):	Pliki nag³ówkowe i biblioteki do reiserfs
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and libraries to develop software which operates on
reiserfs filesystems.

%description devel -l pl
Pliki nag³ówkowe i biblioteki potrzebne do rozwoju oprogramowania
operuj±cego na systemie plików reiserfs.

%package static
Summary:	Static reiserfs software libraries
Summary(pl):	Biblioteki statyczne do reiserfs
Group:		Development/Libraries

%description static
Static reiserfs software libraries.

%description static -l pl
Biblioteki statyczne do reiserfs.

%prep
%setup -q -n %{name}-%{version}-%{_rc}
%patch -p1

%build
# supplied libtool is broken (relink)
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
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
