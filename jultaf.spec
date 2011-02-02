Summary:	Jumble Library for Tcl and Friends
Summary(pl.UTF-8):	Zestaw skryptów dla Tcl i powiązanych
Name:		jultaf
Version:	0.0.9
Release:	2
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://www.linuxia.de/jultaf/%{name}-%{version}.tar.gz
# Source0-md5:	00ab6b112fa775e0dc4420d615a554e9
Patch0:		%{name}-build.patch
Patch1:		%{name}-info.patch
URL:		http://www.linuxia.de/jultaf/
BuildRequires:	gdbm-devel
BuildRequires:	postgresql-devel
BuildRequires:	tcl-devel
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

%description -l pl.UTF-8
Jultaf to kolekcja skryptów Tcl/[incr Tcl] oraz ładowalnych modułów:
- typowe funkcje do obsługi list, tablic i modyfikacji stringów
- funkcje do obsługi i interpretacji błędów w kodzie
- rozszerzenie do profilowania skryptów Tcl
- rozszerzenia umożliwiające dostęp do baz GDBM, RPM, Postgres oraz
  mSQL
- skrypt do generowania indeksów plików w pakietach

%prep
%setup	-q
%patch0 -p1
%patch1 -p1

%build
CPPFLAGS="-I%{_includedir}/pgsql"; export CPPFLAGS
ITCLSH=%{_bindir}/tclsh; export ITCLSH
%configure2_13 \
	--with-gdbm \
	--with-prof \
	--with-pq
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{makeinstall}

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc html/*.{html,gif,css}
%doc CREDITS Change* NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/jultaf*
%{_infodir}/*.info*
