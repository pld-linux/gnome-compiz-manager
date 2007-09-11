#
Summary:	Gnome compiz manager
Summary(pl.UTF-8):	Gnome compiz manager
Name:		gnome-compiz-manager
Version:	0.10.4
Release:	0.1
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
Summary(pl.UTF-8):	Pliki bibliotel dla GNOME Compiz manager
Group:		Libraries

%description libs
Libraries for GNOME Compiz manager.

%description libs -l pl.UTF-8
Pliki bibliotel dla GNOME Compiz manager.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 \
	autostartdir=%{_datadir}/gnome/autostart
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{name}.schemas

%preun
%gconf_schema_uninstall %{name}.schemas

%post libs  -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/gnome-compiz-preferences.schemas
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_desktopdir}/*.desktop
%doc %{_docdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*.1.*

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so*
%{_libdir}/*.so*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
