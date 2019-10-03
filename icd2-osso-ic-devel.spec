Summary:	Compatibility header files for osso-ic
Summary(pl.UTF-8):	Pliki nagłówkowe dla zgodności z osso-ic
Name:		icd2-osso-ic-devel
Version:	2.0.1
Release:	1
License:	LGPL v2.1
Group:		Development/Libraries
#Source0Download: https://github.com/maemo-leste/icd2-osso-ic-dev/releases
Source0:	https://github.com/maemo-leste/icd2-osso-ic-dev/archive/%{version}/icd2-osso-ic-dev-%{version}.tar.gz
# Source0-md5:	08ead4ac22c922d7ff8d3394ee3c3d50
Patch0:		%{name}-version.patch
URL:		https://maemo.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	sed >= 4.0
Obsoletes:	osso-ic-oss-devel < 2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The following internal header files are provided for backwards
compatibility with osso-ic: osso-ic-dbus.h, osso-ic-gconf.h,
osso-ic.h.

osso-ic.h contains only two remaining defines that are used elsewhere.
The package osso-ic-oss that provided the included header files has
been deprecated and removed from Maemo.

This package should be used only by Connectivity subsystem components
as it contains only internal interface definitions.

%description -l pl.UTF-8
Ten pakiet zawiera następujące wewnętrzne pliki nagłówkowe dla
wstecznej zgodności z osso-ic: osso-ic-dbus.h, osso-ic-gconf.h,
osso-ic.h.

Plik osso-ic.h zawiera tylko dwie pozostałe definicje, które są
jeszcze gdzieś używane. Pakiet osso-ic-oss dostarczający wcześniej
ten plik jest już przestarzały i został usunięty z projektu Maemo.

Ten pakiet powinien być używany tylko dla komponentów podsystemu
łączności (Connectivity), jako że zawiera tylko definicje interfejsów
wewnętrznych.

%prep
%setup -q -n icd2-osso-ic-dev-%{version}
%patch0 -p1

%{__sed} -i -e 's/@VERSION@/%{version}/' configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_npkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_includedir}/icd
%{_includedir}/icd/osso-ic*.h
%{_npkgconfigdir}/osso-ic.pc
