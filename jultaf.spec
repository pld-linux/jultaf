Summary:	Jumble Library for Tcl and Friends
Summary(pl):	Zestaw skrypt�w dla Tcl i powi�zanych.
Name:		jultaf
Version:	0.0.9
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Group(de):	Entwicklung/Sprachen/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Source0:	http://www.linuxia.de/jultaf/%{name}-%{version}.tar.gz
Patch0:		%{name}-build.patch
URL:		http://www.linuxia.de/jultaf/
BuildRequires:	tcl-devel
BuildRequires:	postgresql-devel
BuildRequires:	gdbm-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jultaf is a collection of Tcl/[incr Tcl] scripts and loadable
extensions:
- generic functions for list, array, string manipulation
- functions for error handling and code interpreting
- an extension for profiling Tcl scripts
- extensions for GDBM, RPM, Postgres and mSQL access
- a script that generates package index files

Jultaf is labeled as alpha software. Nevertheless many parts are quite
stable and functional. The profiling extension is experimental and the
mSQL extension untested.

%description -l pl
Jultaf to kolekcja skrypt�w Tcl/[incr Tcl] oraz �adowalnych modu��w:
- typowe funkcje do obs�ugi list, tablic i modyfikacji string�w
- funkcje do obs�ugi i interpretacji b��d�w w kodzie
- rozszerzenie do profilowania skrypt�w Tcl
- rozszerzenia umo�liwiaj�ce dost�p do baz GDBM, RPM, Postgres oraz
  mSQL
- skrypt do generowania indeks�w plik�w w pakietach

%prep
%setup  -q
%patch0 -p1

%build
CPPFLAGS="-I%{_includedir}/pgsql"; export CPPFLAGS
ITCLSH=%{_bindir}/tclsh; export ITCLSH
%configure \
	--with-gdbm \
	--with-prof \
	--with-pq
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{makeinstall}

gzip -9nf CREDITS Change* NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc html/*.{html,gif,css}
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/jultaf*
%{_infodir}/*
