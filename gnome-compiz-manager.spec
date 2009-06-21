Summary:	GNOME compiz manager
Summary(pl.UTF-8):	Zarządca compiza dla GNOME
Name:		gnome-compiz-manager
Version:	0.10.4
Release:	4
License:	LGPL v2.1+ (library), GPL v2+ (the rest)
Group:		X11/Applications
Source0:	http://download.gna.org/gcm/gnome-compiz-manager/%{name}-%{version}.tar.gz
# Source0-md5:	654041b7bf9869e7d1724cb90739cdef
URL:		http://gandalfn.wordpress.com/
BuildRequires:	gnome-desktop-devel >= 2.0
BuildRequires:	gob2 >= 2.0.14
BuildRequires:	gtk+2-devel >= 2:2.10
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	libwnck-devel >= 1.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME compiz manager is small utility, which manage GL Desktop
configuration on XGL/AIGLX.

%description -l pl.UTF-8
GNOME compiz manager jest małym narzędziem zarządzającym konfiguracją
pulpitu GL na XGL/AIGLX.

%package libs
Summary:	Libraries for GNOME Compiz manager
Summary(pl.UTF-8):	Pliki bibliotek dla GNOME Compiz managera
License:	LGPL v2.1+ (library), GPL v2+ (plugins)
Group:		Libraries
Requires:	gtk+2 >= 2:2.10

%description libs
Libraries for GNOME Compiz manager.

%description libs -l pl.UTF-8
Pliki bibliotek dla GNOME Compiz managera.

%package devel
Summary:	Header files for GNOME Compiz manager library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GNOME Compiz managera
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gnome-desktop-devel >= 2.0
Requires:	gtk+2-devel >= 2:2.10
Requires:	libgnomeui-devel >= 2.0
Requires:	librsvg-devel >= 2.0
Requires:	libwnck-devel >= 1.0

%description devel
Header files for GNOME Compiz manager library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GNOME Compiz managera.

%package static
Summary:	Static library for GNOME Compiz manager
Summary(pl.UTF-8):	Plik biblioteki statycznej GNOME Compiz managera
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library for GNOME Compiz managera.

%description static -l pl.UTF-8
Plik biblioteki statycznej dla GNOME Compiz manager.

%prep
%setup -q

%build
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-compiz-preferences.schemas

%preun
%gconf_schema_uninstall gnome-compiz-preferences.schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/gnome-compiz-preferences.schemas
%attr(755,root,root) %{_bindir}/compiz-tray-icon
%attr(755,root,root) %{_bindir}/gnome-compiz-preferences
%{_libdir}/%{name}/gcp-page-*.plugin
%{_datadir}/%{name}
%{_desktopdir}/gnome-compiz-preferences.desktop
%{_mandir}/man1/compiz-tray-icon.1*
%{_mandir}/man1/gnome-compiz-preferences.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-compiz-manager.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-compiz-manager.so.0
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libgcp_page_*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-compiz-manager.so
%{_libdir}/libgnome-compiz-manager.la
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnome-compiz-manager.a
