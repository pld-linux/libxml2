
%include	/usr/lib/rpm/macros.python

Summary:	libXML library
Summary(es):	Biblioteca libXML version 2
Summary(pl):	Biblioteka libxml2
Summary(pt_BR):	Biblioteca libXML vers�o 2
Name:		libxml2
Version:	2.4.15
Release:	1
License:	MIT
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(it):	Librerie
Group(ja):	�饤�֥��
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(sv):	Bibliotek
Group(uk):	��̦�����
Source0:	ftp://xmlsoft.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-man_fixes.patch
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
Esta biblioteca permite manipulaci�n de archivos XML.

%description -l pl
Biblioteka libxml2 umo�liwia manipulowaie zawarto�ci� plik�w XML.

%description -l pt_BR
Esta biblioteca permite a manipula��o de arquivos XML.

%package devel
Summary:	Header files etc to develop libxml2 applications
Summary(es):	Biblioteca y archivos de inclusi�n para desarrollo de aplicaciones libXML
Summary(pl):	Pliki nag��wkowe i inne do libxml2
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para desenvolvimento de aplica��es que usem a biblioteca libxml
Group:		Development/Libraries
Group(cs):	V�vojov� prost�edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(it):	Sviluppo/Librerie
Group(ja):	��ȯ/�饤�֥��
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(sv):	Utveckling/Bibliotek
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}
Requires:	zlib-devel

%description devel
Header files etc you can use to develop libxml2 applications.

%description -l es devel
Biblioteca y archivos de inclusi�n para desarrollo de aplicaciones
libXML.

%description -l pl devel
Pakiet ten zawiera pliki nag��wkowe i inne do libxml2 niezb�dne przy
tworzeniu aplikacji opartych o t� bibliotek�.

%description -l pt_BR devel
Bibliotecas e arquivos de inclus�o para desenvolvimento de aplica��es
que usem a biblioteca libxml.

%package static
Summary:	Static libxml2 libraries
Summary(es):	Static libraries to develop libxml applications
Summary(pl):	Biblioteka statyczna libxml2
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento de aplica��es que usem a biblioteca libxml
Group:		Development/Libraries
Group(cs):	V�vojov� prost�edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(it):	Sviluppo/Librerie
Group(ja):	��ȯ/�饤�֥��
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(sv):	Utveckling/Bibliotek
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
Static libxml2 libraries.

%description -l es static
Static libraries, you can use to develop libxml applications.

%description -l pl static
Biblioteka statyczna libxml2.

%description -l pt_BR static
Bibliotecas est�ticas para desenvolvimento de aplica��es que usem a
biblioteca libxml.

%package progs
Summary:	XML files parser
Summary(pl):	Parser plik�w XML
Group:		Applications/Text
Group(cs):	Aplikace/Text
Group(da):	Programmer/Tekst
Group(de):	Applikationen/Text
Group(es):	Aplicaciones/Texto
Group(fr):	Applications/Texte
Group(it):	Applicazioni/Testo
Group(ja):	���ץꥱ�������/�ƥ�����
Group(no):	Applikasjoner/Tekst
Group(pl):	Aplikacje/Tekst
Group(pt):	Aplica��es/Texto
Group(ru):	����������/������ � ��������
Group(sv):	Till�mpningar/Text
Requires:	%{name} = %{version}

%description progs
XML files parser.

%description -l pl progs
Parser plik�w XML.

%package -n python-%{name}
Summary:	Python support for libxml2
Summary(pl):	Modu�y j�zyka Python dla biblioteki libxml2
Group:		Development/Languages/Python
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Python
Group(da):	Udvikling/Sprog/Python
Group(de):	Entwicklung/Sprachen/Python
Group(es):	Desarrollo/Lenguajes/Python
Group(fr):	Development/Langues/Python
Group(it):	Sviluppo/Linguaggi/Python
Group(ja):	��ȯ/����/Python
Group(no):	Utvikling/Programmeringsspr�k/Python
Group(pl):	Programowanie/J�zyki/Python
Group(pt):	Desenvolvimento/Linguagens/Python
Group(ru):	����������/�����/Python
Group(sv):	Utveckling/Spr�k/Python
%requires_eq	python
Obsoletes:	libxml2-python

%description -n python-%{name}
Python support for libxml2.

%description -n python-%{name} -l pl
Modu�y j�zyka Python dla biblioteki libxml2.

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

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

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

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
