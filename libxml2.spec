Summary:	libXML library
Summary(pl):	Biblioteka libxml2
Name:		libxml2
Version:	2.4.3
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://xmlsoft.org/%{name}-%{version}.tar.gz
URL:		http://xmlsoft.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel >= 4.2
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	zlib-devel

%description devel
Header files etc you can use to develop libxml2 applications.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe i inne do libxml2 niezbêdne przy
tworzeniu aplikacji opartych o tê bibliotekê.

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

%package progs
Summary:	XML files parser
Summary(pl):	Parser plików XML
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Development/Librairies
Group(pl):	Aplikacje/Tekst
Requires:	%{name} = %{version}

%description progs
XML files parser.

%description -l pl progs
Parser plików XML.

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

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
%{_pkgconfigdir}/*
%{_aclocaldir}/*.m4
%{_includedir}/libxml
%{_mandir}/man1/xml2-config.1*
%{_mandir}/man4/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmllint
%{_mandir}/man1/xmllint.1*
