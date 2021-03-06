# TODO:
# - fix build without libxml2-devel (python library uses old headers)
#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	python2		# CPython 2.x module
%bcond_without	python3		# CPython 3.x module
%bcond_without	static_libs	# static library
%bcond_without	zlib		# zlib support
%bcond_with	mem_debug	# libxml2 memory debuging
%bcond_without	tests		# "make check" call

Summary:	libXML library version 2
Summary(es.UTF-8):	Biblioteca libXML version 2
Summary(pl.UTF-8):	Biblioteka libXML wersja 2
Summary(pt_BR.UTF-8):	Biblioteca libXML versão 2
Name:		libxml2
Version:	2.9.12
Release:	1
Epoch:		1
License:	MIT
Group:		Libraries
Source0:	ftp://xmlsoft.org/libxml2/%{name}-%{version}.tar.gz
# Source0-md5:	f433a39be087a9f0b197eb2307ad9f75
Patch0:		%{name}-man_fixes.patch
Patch1:		%{name}-open.gz.patch
Patch2:		%{name}-largefile.patch
Patch3:		%{name}-libx32.patch
# Fedora patches
# https://bugzilla.gnome.org/show_bug.cgi?id=789714
Patch11:	%{name}-python3-unicode-errors.patch
URL:		http://xmlsoft.org/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1.4
BuildRequires:	libtool >= 2:2.0
%if %{with python2}
BuildRequires:	python-devel >= 2.0
BuildRequires:	python-modules >= 2.0
BuildRequires:	rpm-pythonprov
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	xz-devel
%{?with_zlib:BuildRequires:	zlib-devel >= 1.2.3.3}
# history support in xmllint is disabled by default
#BuildRequires:	ncurses-devel
#BuildRequires:	readline-devel >= 4.2
Requires:	zlib >= 1.2.3.3
Obsoletes:	xml-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you to manipulate XML files.

%description -l es.UTF-8
Esta biblioteca permite manipulación de archivos XML.

%description -l pl.UTF-8
Biblioteka libxml2 umożliwia manipulowanie zawartością plików XML.

%description -l pt_BR.UTF-8
Esta biblioteca permite a manipulação de arquivos XML.

%package devel
Summary:	Header files etc to develop libxml2 applications
Summary(es.UTF-8):	Biblioteca y archivos de inclusión para desarrollo de aplicaciones libXML
Summary(pl.UTF-8):	Pliki nagłówkowe i inne do libxml2
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações que usem a biblioteca libxml
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	xz-devel
Requires:	zlib-devel

%description devel
Header files etc you can use to develop libxml2 applications.

%description devel -l es.UTF-8
Biblioteca y archivos de inclusión para desarrollo de aplicaciones
libXML.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i inne do libxml2 niezbędne przy
tworzeniu aplikacji opartych o tę bibliotekę.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
que usem a biblioteca libxml.

%package static
Summary:	Static libxml2 libraries
Summary(es.UTF-8):	Static libraries to develop libxml applications
Summary(pl.UTF-8):	Biblioteka statyczna libxml2
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento de aplicações que usem a biblioteca libxml
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libxml2 libraries.

%description static -l es.UTF-8
Static libraries, you can use to develop libxml applications.

%description static -l pl.UTF-8
Biblioteka statyczna libxml2.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento de aplicações que usem a
biblioteca libxml.

%package apidocs
Summary:	libxml2 API documentation
Summary(pl.UTF-8):	Dokumentacja API libxml2
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
libxml2 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libxml2.

%package progs
Summary:	XML files parser
Summary(pl.UTF-8):	Analizator składniowy plików XML
Group:		Applications/Text
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description progs
XML files parser.

%description progs -l pl.UTF-8
Analizator składniowy plików XML.

%package -n python-%{name}
Summary:	libxml2 module for Python 2.x
Summary(pl.UTF-8):	Moduł libxml2 dla Pythona 2.x
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-libs
Obsoletes:	libxml2-python

%description -n python-%{name}
This is the libxml2 module for Python 2.x, providing access to the
libxml2 library.

%description -n python-%{name} -l pl.UTF-8
Ten pakiet zawiera moduł libxml2 dla Pythona 2.x, zapewniający dostęp
do biblioteki libxml2.

%package -n python3-%{name}
Summary:	libxml2 module for Python 3.x
Summary(pl.UTF-8):	Moduł libxml2 dla Pythona 3.x
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python3-libs

%description -n python3-%{name}
This is the libxml2 module for Python 3.x, providing access to the
libxml2 library.

%description -n python3-%{name} -l pl.UTF-8
Ten pakiet zawiera moduł libxml2 dla Pythona 3.x, zapewniający dostęp
do biblioteki libxml2.

%prep
%setup -q
%patch0 -p1
%if %{with zlib}
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch11 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--without-python \
	%{!?with_zlib:--without-zlib} \
	--with-lzma \
	--with%{!?with_mem_debug:out}-mem-debug

%{__make}

%if %{with python2}
cd python
%py_build
cd ..
%endif


%if %{with python3}
cd python
%py3_build
cd ..
%endif

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	devhelpdir=%{_gtkdocdir}/libxml2 \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

%if %{with python2}
cd python
%py_install

%py_postclean
cd ..
%endif

%if %{with python3}
cd python
%py3_install
cd ..
%endif

# move html doc to -devel package
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-devel-%{version}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-devel-%{version}
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# install catalog file
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xml
LD_LIBRARY_PATH=.libs ./xmlcatalog --create \
	> $RPM_BUILD_ROOT%{_sysconfdir}/xml/catalog

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog Copyright NEWS README TODO
%attr(755,root,root) %{_libdir}/libxml2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxml2.so.2
%{_mandir}/man3/libxml.3*

%dir %{_sysconfdir}/xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xml/catalog

%files devel
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-devel-%{version}
%attr(755,root,root) %{_bindir}/xml2-config
%attr(755,root,root) %{_libdir}/libxml2.so
%{_libdir}/libxml2.la
%attr(755,root,root) %{_libdir}/xml2Conf.sh
%{_libdir}/cmake/libxml2
%{_pkgconfigdir}/libxml-2.0.pc
%{_aclocaldir}/libxml.m4
%{_includedir}/libxml2
%{_mandir}/man1/xml2-config.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxml2.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libxml2
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmlcatalog
%attr(755,root,root) %{_bindir}/xmllint
%{_mandir}/man1/xmlcatalog.1*
%{_mandir}/man1/xmllint.1*

%if %{with python2}
%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/libxml2mod.so
%{py_sitedir}/drv_libxml2.py[co]
%{py_sitedir}/libxml2.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/libxml2_python-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{name}
%defattr(644,root,root,755)
%{py3_sitedir}/__pycache__/*.py[co]
%{py3_sitedir}/drv_libxml2.py
%{py3_sitedir}/libxml2.py
%{py3_sitedir}/libxml2_python-%{version}-py*.egg-info
%attr(755,root,root) %{py3_sitedir}/libxml2mod.cpython-*.so
%endif
