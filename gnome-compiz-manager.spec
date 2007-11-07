#
Summary:	Gnome compiz manager
Summary(pl.UTF-8):	Gnome compiz manager
Name:		gnome-compiz-manager
Version:	0.10.4
Release:	0.3
License:	GPL
Group:		Applications
Source0:	http://download.gna.org/gcm/gnome-compiz-manager/%{name}-%{version}.tar.gz
# Source0-md5:	654041b7bf9869e7d1724cb90739cdef
URL:		http://gandalfn.wordpress.com/
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	libwnck-devel >= 1.0
BuildRequires:	gnome-desktop-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome compiz manager is small utility, which manage GL Desktop
configuration on XGL/AiGLX.

%description -l pl.UTF-8
Gnome compiz manager jest małym narzędziem zarządzającym konfiguracją
pulpitu GL na XGL/AiGLX.

%package devel
Summary:	Header files for GNOME Compiz manager library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GNOME Compiz manager
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for GNOME Compiz manager library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GNOME Compiz manager.

%package libs
Summary:	Libraries for GNOME Compiz manager
Summary(pl.UTF-8):	Pliki bibliotek dla GNOME Compiz manager
Group:		Libraries

%description libs
Libraries for GNOME Compiz manager.

%description libs -l pl.UTF-8
Pliki bibliotel dla GNOME Compiz manager.

%package static
Summary:	Static library for GNOME Compiz manager
Summary(pl.UTF-8):	Plik biblioteki statycznej GNOME Compiz manager
Group:		Libraries

%description static
Static library for GNOME Compiz manager.

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-compiz-preferences.schemas

%preun
%gconf_schema_uninstall gnome-compiz-preferences.schemas

%post libs  -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/gnome-compiz-preferences.schemas
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}/*.plugin
%{_desktopdir}/*.desktop
%{_datadir}/%{name}
%{_mandir}/man1/*.1.*

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/libgnome-compiz-manager.la
%{_libdir}/libgnome-compiz-manager.so
%{_libdir}/%{name}/libgcp*.la
%{_pkgconfigdir}/%{name}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/%{name}/libgcp*.a
%{_libdir}/*.a
