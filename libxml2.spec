Summary:	libXML library
Summary(es):	Biblioteca libXML version 2
Summary(pl):	Biblioteka libxml2
Summary(pt_BR):	Biblioteca libXML vers„o 2
Name:		libxml2
Version:	2.4.13
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://xmlsoft.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-man_fixes.patch
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

%description -l es
Esta biblioteca permite manipulaciÛn de archivos XML.

%description -l pl
Biblioteka libxml2 umoøliwia manipulowaie zawarto∂ci± plikÛw XML.

%description -l pt_BR
Esta biblioteca permite a manipulaÁ„o de arquivos XML.

%package devel
Summary:	Header files etc to develop libxml2 applications
Summary(es):	Biblioteca y archivos de inclusiÛn para desarrollo de aplicaciones libXML
Summary(pl):	Pliki nag≥Ûwkowe i inne do libxml2
Summary(pt_BR):	Bibliotecas e arquivos de inclus„o para desenvolvimento de aplicaÁıes que usem a biblioteca libxml
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Requires:	zlib-devel

%description devel
Header files etc you can use to develop libxml2 applications.

%description -l es devel
Biblioteca y archivos de inclusiÛn para desarrollo de aplicaciones
libXML.

%description -l pl devel
Pakiet ten zawiera pliki nag≥Ûwkowe i inne do libxml2 niezbÍdne przy
tworzeniu aplikacji opartych o tÍ bibliotekÍ.

%description -l pt_BR devel
Bibliotecas e arquivos de inclus„o para desenvolvimento de aplicaÁıes
que usem a biblioteca libxml.

%package static
Summary:	Static libxml2 libraries
Summary(es):	Static libraries to develop libxml applications
Summary(pl):	Biblioteka statyczna libxml2
Summary(pt_BR):	Bibliotecas est·ticas para desenvolvimento de aplicaÁıes que usem a biblioteca libxml
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static libxml2 libraries.

%description -l es static
Static libraries, you can use to develop libxml applications.

%description -l pl static
Biblioteka statyczna libxml2.

%description -l pt_BR static
Bibliotecas est·ticas para desenvolvimento de aplicaÁıes que usem a
biblioteca libxml.

%package progs
Summary:	XML files parser
Summary(pl):	Parser plikÛw XML
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Development/Librairies
Group(pl):	Aplikacje/Tekst
Requires:	%{name} = %{version}

%description progs
XML files parser.

%description -l pl progs
Parser plikÛw XML.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%{_mandir}/man4/*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/{*.{gif,html},html/*}
%attr(755,root,root) %{_bindir}/*
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
