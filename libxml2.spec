Summary:	libXML library
Summary(pl):	Biblioteka libxml2
Name:		libxml2
Version:	2.3.0
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/libxml/%{name}-%{version}.tar.gz
URL:		http://xmlsoft.org/
Requires:	iconv
BuildRequires:	iconv
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This library allows you to manipulate XML files.

%description -l pl
Biblioteka libxml2 umo¿liwia manipulowaie zawarto¶ci± plików XML.

%package devel
Summary:	Header files etc to develop libxml2 applications
Summary(pl):	Pliki nag³ówkowe i inne do libxml2
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files etc you can use to develop libxml2 applications.

%description -l pl devel
Pakiet ten zaziewra pliki nag³ówkowe i inne do libxml2 niezbêdne przy
tworzeniu aplikacji opartych o t± bibliotekê.

%package static
Summary:	Static libxml2 libraries
Summary(pl):	Biblioteka statyczna libxml2
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libxml2 libraries.

%description -l pl static
Biblioteka statyczna libxml2.

%prep
%setup -q

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_aclocaldir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/aclocal/* $RPM_BUILD_ROOT%{_aclocaldir}

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
#rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/{*.{gif,html},html/*}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_libdir}/pkgconfig/*
%{_aclocaldir}/*.m4
%{_includedir}/libxml
%{_mandir}/man*/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
