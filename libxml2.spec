
%include	/usr/lib/rpm/macros.python

Summary:	libXML library
Summary(es):	Biblioteca libXML version 2
Summary(pl):	Biblioteka libxml2
Summary(pt_BR):	Biblioteca libXML versão 2
Name:		libxml2
Version:	2.4.22
Release:	1
License:	MIT
Group:		Libraries
Source0:	ftp://xmlsoft.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-man_fixes.patch
Patch2:		%{name}-open.gz.patch
URL:		http://xmlsoft.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-pythonprov
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you to manipulate XML files.

%description -l es
Esta biblioteca permite manipulación de archivos XML.

%description -l pl
Biblioteka libxml2 umo¿liwia manipulowaie zawarto¶ci± plików XML.

%description -l pt_BR
Esta biblioteca permite a manipulação de arquivos XML.

%package devel
Summary:	Header files etc to develop libxml2 applications
Summary(es):	Biblioteca y archivos de inclusión para desarrollo de aplicaciones libXML
Summary(pl):	Pliki nag³ówkowe i inne do libxml2
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações que usem a biblioteca libxml
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	zlib-devel

%description devel
Header files etc you can use to develop libxml2 applications.

%description devel -l es
Biblioteca y archivos de inclusión para desarrollo de aplicaciones
libXML.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe i inne do libxml2 niezbêdne przy
tworzeniu aplikacji opartych o tê bibliotekê.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
que usem a biblioteca libxml.

%package static
Summary:	Static libxml2 libraries
Summary(es):	Static libraries to develop libxml applications
Summary(pl):	Biblioteka statyczna libxml2
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento de aplicações que usem a biblioteca libxml
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libxml2 libraries.

%description static -l es
Static libraries, you can use to develop libxml applications.

%description static -l pl
Biblioteka statyczna libxml2.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento de aplicações que usem a
biblioteca libxml.

%package progs
Summary:	XML files parser
Summary(pl):	Parser plików XML
Group:		Applications/Text
Requires:	%{name} = %{version}

%description progs
XML files parser.

%description progs -l pl
Parser plików XML.

%package -n python-%{name}
Summary:	Python support for libxml2
Summary(pl):	Modu³y jêzyka Python dla biblioteki libxml2
Group:		Libraries/Python
Requires:	%{name} = %{version}
%pyrequires_eq	python
Obsoletes:	libxml2-python

%description -n python-%{name}
Python support for libxml2.

%description -n python-%{name} -l pl
Modu³y jêzyka Python dla biblioteki libxml2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

# install catalog file
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xml
LD_LIBRARY_PATH=.libs ./xmlcatalog --create \
	> $RPM_BUILD_ROOT%{_sysconfdir}/xml/catalog

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man3/*

%dir %{_sysconfdir}/xml
%config(noreplace) %verify(not mtime md5) %{_sysconfdir}/xml/catalog

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/{*.{gif,html},html/*}
%attr(755,root,root) %{_bindir}/xml2-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_pkgconfigdir}/*
%{_aclocaldir}/*.m4
%{_includedir}/libxml2
%{_mandir}/man1/xml2-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmlcatalog
%attr(755,root,root) %{_bindir}/xmllint
%{_mandir}/man1/xmlcatalog.1*
%{_mandir}/man1/xmllint.1*

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
