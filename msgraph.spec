%define api	1
%define major 1
%define libname		%mklibname msgraph 
%define girname		%mklibname msgraph-gir
%define develname	%mklibname msgraph -d

Name:		msgraph
Version:	0.3.3
Release:	2
Summary:	Library to access MS Graph API for Microsoft 365
Group:		System/Libraries
License:	LGPL-3.0-or-later
URL:		https://gitlab.gnome.org/GNOME/msgraph
Source0:	https://download.gnome.org/sources/msgraph/0.2/msgraph-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(rest-1.0)
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(libuhttpmock-1.0) >= 0.10.0
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	gi-docgen
BuildRequires:	glib-networking

%description
libmsgraph is a GLib-based library for accessing online service APIs
using the MS Graph protocol.

%package -n	%{libname}
Summary:	Library to access MS Graph API for Microsoft 365
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n	%{libname}
libmsgraph is a GLib-based library for accessing online service APIs
using the MS Graph protocol.

%package -n	%{girname}
Summary:	GObject Introspection interface description for MS Graph
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}

%description -n	%{girname}
GObject Introspection interface description for MS Graph.

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	%{name}-%{api}-devel = %{EVRD}

%description -n	%{develname}
Header files for development with %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%license COPYING
%doc README* NEWS
%{_libdir}/lib%{name}-%{api}.so.%{version}
%{_libdir}/lib%{name}-%{api}.so.%{major}

%files -n %{girname}
%license COPYING
%{_libdir}/girepository-1.0/Msg-%{api}.typelib

%files -n %{develname}
%{_includedir}/msg/
%{_libdir}/lib%{name}-%{api}.so
%{_libdir}/pkgconfig/msgraph-1.pc
%{_datadir}/gir-1.0/Msg-%{api}.gir
%{_docdir}/msgraph-1/
