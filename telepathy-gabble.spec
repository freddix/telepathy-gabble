Summary:	Gabble is a Jabber connection manager
Name:		telepathy-gabble
Version:	0.16.3
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-gabble/%{name}-%{version}.tar.gz
# Source0-md5:	8fde66e4bf6bd01b0c785784a6928381
BuildRequires:	dbus-glib-devel
BuildRequires:	libnice-devel
BuildRequires:	libxslt-progs
BuildRequires:	openssl-devel
BuildRequires:	pkg-config
BuildRequires:	python
BuildRequires:	sqlite3-devel
BuildRequires:	telepathy-glib-devel
Provides:	telepathy-service
Requires:	ca-certificates
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/telepathy

%description
Gabble is a Jabber connection manager.

%prep
%setup -q

%build
%configure \
	--disable-static	\
	--with-ca-certificates=%{_sysconfdir}/certs/ca-certificates.crt	\
	--with-tls=openssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libexecdir}/*/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%dir %{_libexecdir}/gabble-0
%dir %{_libexecdir}/gabble-0/lib
%dir %{_libexecdir}/gabble-0/plugins
%attr(755,root,root) %{_bindir}/telepathy-gabble-xmpp-console
%attr(755,root,root) %{_libexecdir}/telepathy-gabble
%attr(755,root,root) %{_libexecdir}/gabble-0/lib/*.so
%attr(755,root,root) %{_libexecdir}/gabble-0/plugins/*.so
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.gabble.service
%{_datadir}/telepathy/managers/gabble.manager
%{_mandir}/man8/telepathy-gabble.8*

