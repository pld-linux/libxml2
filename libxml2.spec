# TODO:
# - fix build without libxml2-devel (python library uses old headers)
#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_with	ftp		# FTP support
%bcond_without	legacy		# legacy API support
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
Version:	2.11.2
Release:	1
Epoch:		1
License:	MIT
Group:		Libraries
#Source0:	ftp://xmlsoft.org/libxml2/%{name}-%{version}.tar.gz
Source0:	https://download.gnome.org/sources/libxml2/2.11/%{name}-%{version}.tar.xz
# Source0-md5:	17cc55c83db69f5d236c784aef554529
Patch0:		%{name}-open.gz.patch
Patch1:		%{name}-largefile.patch
Patch2:		%{name}-libx32.patch
Patch3:		%{name}-python-setup.patch
# Fedora patches
# https://bugzilla.gnome.org/show_bug.cgi?id=789714
Patch11:	%{name}-python3-unicode-errors.patch
URL:		http://xmlsoft.org/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.16.3
BuildRequires:	libtool >= 2:2.0
BuildRequires:	pkgconfig
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
%endif
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
Obsoletes:	libxml2-python < 1:2.6

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
%if %{with zlib}
%patch0 -p1
%endif
%patch1 -p1
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
	%{?with_static_libs:--enable-static} \
	%{?with_ftp:--with-ftp} \
	%{?with_legacy:--with-legacy} \
	--with-lzma \
	--with-mem-debug%{!?with_mem_debug:=no} \
	--without-python \
	%{!?with_zlib:--without-zlib}

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
	devhelpdir=%{_gtkdocdir}/libxml2

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

install -d $RPM_BUILD_ROOT%{_examplesdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/libxml2/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
%doc Copyright NEWS README.md
%attr(755,root,root) %{_libdir}/libxml2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxml2.so.2
%dir %{_sysconfdir}/xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xml/catalog

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xml2-config
%attr(755,root,root) %{_libdir}/libxml2.so
%{_libdir}/libxml2.la
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
%{_docdir}/%{name}
%{_gtkdocdir}/libxml2
%{_examplesdir}/%{name}-%{version}
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
%{py_sitedir}/libxml2_python-%{version}-py*.egg-info
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
