#
# Conditional build:
%bcond_without	python	# don't build python module
%bcond_without	static_libs # don't build static libraries
#
%{?with_python:%include	/usr/lib/rpm/macros.python}
Summary:	libXML library
Summary(es):	Biblioteca libXML version 2
Summary(pl):	Biblioteka libXML wersja 2
Summary(pt_BR):	Biblioteca libXML versão 2
Name:		libxml2
Version:	2.6.26
Release:	3
Epoch:		1
License:	MIT
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libxml2/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	ce342b4d7b6d83e10cfa4d3f82bf75fd
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-man_fixes.patch
Patch2:		%{name}-open.gz.patch
Patch3:		%{name}-DESTDIR.patch
URL:		http://xmlsoft.org/
BuildRequires:	autoconf >= 2.2
BuildRequires:	automake
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	ncurses-devel
%{?with_python:BuildRequires:	python-devel}
%{?with_python:BuildRequires:	python-modules}
BuildRequires:	readline-devel >= 4.2
%{?with_python:BuildRequires:	rpm-pythonprov}
BuildRequires:	zlib-devel
Obsoletes:	xml-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you to manipulate XML files.

%description -l es
Esta biblioteca permite manipulación de archivos XML.

%description -l pl
Biblioteka libxml2 umo¿liwia manipulowanie zawarto¶ci± plików XML.

%description -l pt_BR
Esta biblioteca permite a manipulação de arquivos XML.

%package devel
Summary:	Header files etc to develop libxml2 applications
Summary(es):	Biblioteca y archivos de inclusión para desarrollo de aplicaciones libXML
Summary(pl):	Pliki nag³ówkowe i inne do libxml2
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações que usem a biblioteca libxml
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

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
Summary(pl):	Analizator sk³adniowy plików XML
Group:		Applications/Text
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description progs
XML files parser.

%description progs -l pl
Analizator sk³adniowy plików XML.

%package -n python-%{name}
Summary:	Python support for libxml2
Summary(pl):	Modu³y jêzyka Python dla biblioteki libxml2
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
%pyrequires_eq	python-libs
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
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--enable-static=no}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

# move examples to proper dir
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-devel-%{version} \
	$RPM_BUILD_ROOT%{_examplesdir}/python-%{name}-%{version}
mv $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples/* \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-devel-%{version}
%if %{with python}
mv -f $RPM_BUILD_ROOT%{_docdir}/%{name}-python-%{version}/examples/* \
	$RPM_BUILD_ROOT%{_examplesdir}/python-%{name}-%{version}
%endif

# move html doc to -devel package
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-devel-%{version}
mv -f $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-devel-%{version}
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# deal with gtk-doc files
install -d $RPM_BUILD_ROOT%{_gtkdocdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/* $RPM_BUILD_ROOT%{_gtkdocdir}

# install catalog file
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xml
LD_LIBRARY_PATH=.libs ./xmlcatalog --create \
	> $RPM_BUILD_ROOT%{_sysconfdir}/xml/catalog

%if %{with python}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{py,la,a}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog Copyright NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man3/*

%dir %{_sysconfdir}/xml
%config(noreplace) %verify(not md5 mtime) %{_sysconfdir}/xml/catalog

%files devel
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-devel-%{version}
%attr(755,root,root) %{_bindir}/xml2-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*
%{_aclocaldir}/*.m4
%{_includedir}/libxml2
%{_mandir}/man1/xml2-config.1*
%{_examplesdir}/%{name}-devel-%{version}
%{_gtkdocdir}/libxml2

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmlcatalog
%attr(755,root,root) %{_bindir}/xmllint
%{_mandir}/man1/xmlcatalog.1*
%{_mandir}/man1/xmllint.1*

%if %{with python}
%files -n python-%{name}
%defattr(644,root,root,755)
%doc %{_examplesdir}/python-%{name}-%{version}
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
%endif
