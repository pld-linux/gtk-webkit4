# TODO: review configure options:
# - GAMEPAD
# - BATTERY_STATUS (BR: upower-devel)
# - FTL_JIT (BR: llvm, libcxxabi?)
# - MEDIA_STREAM (BR: openwebrtc)
#
# Conditional build:
%bcond_without	gtk2		# WebKitPluginProcess2 to load GTK+ 2.x based plugins
%bcond_without	introspection	# disable introspection
%bcond_with	seccomp		# seccomp filters (broken as of 2.6.5)
%bcond_with	wayland		# Wayland target (broken as of 2.6.[0-5])
#
# it's not possible to build this with debuginfo on 32bit archs due to
# memory constraints during linking
%ifarch %{ix86} x32
%define		_enable_debug_packages		0
%endif
Summary:	Port of WebKit embeddable web component to GTK+ 3
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK+ 3
Name:		gtk-webkit4
Version:	2.10.2
Release:	3
License:	BSD-like
Group:		X11/Libraries
Source0:	http://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
# Source0-md5:	892e3077ad6c10c8233e7e8b5497cd7a
Patch0:		x32.patch
URL:		http://webkitgtk.org/
BuildRequires:	/usr/bin/ld.gold
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	at-spi2-core-devel >= 2.6.0
BuildRequires:	atk-devel
BuildRequires:	bison >= 2.3
BuildRequires:	cairo-devel >= 1.10.2
BuildRequires:	cmake >= 2.8.12
BuildRequires:	enchant-devel >= 0.22
BuildRequires:	flex >= 2.5.34
BuildRequires:	fontconfig-devel >= 2.8.0
BuildRequires:	freetype-devel >= 1:2.4.2
BuildRequires:	gcc-c++ >= 6:4.9
BuildRequires:	geoclue2-devel >= 2.1.5
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	glibc-misc
BuildRequires:	gnutls-devel >= 3.0.0
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 1.32.0}
BuildRequires:	gperf >= 3.0.1
BuildRequires:	gstreamer-devel >= 1.0.3
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.3
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.24.10}
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	harfbuzz-devel >= 0.9.7
BuildRequires:	harfbuzz-icu-devel >= 0.9.7
BuildRequires:	hyphen-devel
BuildRequires:	libicu-devel >= 4.2.1
BuildRequires:	libjpeg-devel
BuildRequires:	libnotify-devel
BuildRequires:	libpng-devel
BuildRequires:	libsecret-devel
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libstdc++-devel >= 6:4.9
BuildRequires:	libwebp-devel
BuildRequires:	libxml2-devel >= 1:2.8.0
BuildRequires:	libxslt-devel >= 1.1.7
BuildRequires:	pango-devel >= 1:1.32.0
BuildRequires:	perl-base >= 1:5.10.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.7.0
BuildRequires:	rpmbuild(macros) >= 1.699
BuildRequires:	ruby >= 1.8.7
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
#BuildRequires:	udev-glib-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	cairo >= 1.10.2
Requires:	enchant >= 0.22
Requires:	fontconfig-libs >= 2.8.0
Requires:	freetype >= 1:2.4.2
Requires:	glib2 >= 1:2.36.0
Requires:	gstreamer >= 1.0.3
Requires:	gstreamer-plugins-base >= 1.0.3
%{?with_gtk2:Requires:	gtk+2 >= 2:2.24.10}
Requires:	gtk+3 >= 3.12.0
Requires:	harfbuzz >= 0.9.7
Requires:	libsoup >= 2.42.0
Requires:	libxml2 >= 1:2.8.0
Requires:	libxslt >= 1.1.7
Requires:	pango >= 1:1.32.0
%{?with_introspection:Conflicts:	gir-repository < 0.6.5-7}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# __once_call, __once_called non-function symbols from libstdc++
%define		skip_post_check_so	lib.*gtk-4.0.*

%description
gtk-webkit4 is a port of the WebKit embeddable web component to GTK+
3.

%description -l pl.UTF-8
gtk-webkit4 to port osadzalnego komponentu WWW WebKit do GTK+ 3.

%package devel
Summary:	Development files for WebKit for GTK+ 3
Summary(pl.UTF-8):	Pliki programistyczne komponentu WebKit dla GTK+ 3
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.36.0
Requires:	gtk+3-devel >= 3.12.0
Requires:	libsoup-devel >= 2.42.0
Requires:	libstdc++-devel >= 6:4.9

%description devel
Development files for WebKit for GTK+ 3.

%description devel -l pl.UTF-8
Pliki programistyczne komponentu WebKit dla GTK+ 3.

%package apidocs
Summary:	WebKit API documentation
Summary(pl.UTF-8):	Dokumentacja API WebKita
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
WebKit API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API WebKita.

%prep
%setup -q -n webkitgtk-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	-DENABLE_CREDENTIAL_STORAGE=ON \
	-DENABLE_GEOLOCATION=ON \
	-DENABLE_GTKDOC=ON \
	%{!?with_introspection:-DENABLE_INTROSPECTION=OFF} \
	%{!?with_gtk2:-DENABLE_PLUGIN_PROCESS_GTK2=OFF} \
	%{?with_seccomp:-DENABLE_SECCOMP_FILTERS=ON} \
	%{?with_wayland:-DENABLE_WAYLAND_TARGET=ON} \
%ifarch x32
	-DENABLE_JIT=OFF \
%endif
	-DENABLE_VIDEO=ON \
	-DENABLE_WEB_AUDIO=ON \
	-DENABLE_WEBGL=ON \
	-DPORT=GTK \
	-DSHOULD_INSTALL_JS_SHELL=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%if "%{_gtkdocdir}" != "%{_datadir}/gtk-doc/html"
install -d $RPM_BUILD_ROOT%{_gtkdocdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/* $RPM_BUILD_ROOT%{_gtkdocdir}
%endif

%find_lang WebKit2GTK-4.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f WebKit2GTK-4.0.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/jsc
%attr(755,root,root) %{_libdir}/libwebkit2gtk-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebkit2gtk-4.0.so.37
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjavascriptcoregtk-4.0.so.18
%if %{with introspection}
%{_libdir}/girepository-1.0/JavaScriptCore-4.0.typelib
%{_libdir}/girepository-1.0/WebKit2-4.0.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-4.0.typelib
%endif
%dir %{_libdir}/webkit2gtk-4.0
%attr(755,root,root) %{_libdir}/webkit2gtk-4.0/WebKitDatabaseProcess
%attr(755,root,root) %{_libdir}/webkit2gtk-4.0/WebKitNetworkProcess
%attr(755,root,root) %{_libdir}/webkit2gtk-4.0/WebKitPluginProcess
%attr(755,root,root) %{_libdir}/webkit2gtk-4.0/WebKitPluginProcess2
%attr(755,root,root) %{_libdir}/webkit2gtk-4.0/WebKitWebProcess
%dir %{_libdir}/webkit2gtk-4.0/injected-bundle
%attr(755,root,root) %{_libdir}/webkit2gtk-4.0/injected-bundle/libwebkit2gtkinjectedbundle.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebkit2gtk-4.0.so
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-4.0.so
%if %{with introspection}
%{_datadir}/gir-1.0/JavaScriptCore-4.0.gir
%{_datadir}/gir-1.0/WebKit2-4.0.gir
%{_datadir}/gir-1.0/WebKit2WebExtension-4.0.gir
%endif
%{_includedir}/webkitgtk-4.0
%{_pkgconfigdir}/javascriptcoregtk-4.0.pc
%{_pkgconfigdir}/webkit2gtk-4.0.pc
%{_pkgconfigdir}/webkit2gtk-web-extension-4.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/webkit2gtk-4.0
%{_gtkdocdir}/webkitdomgtk-4.0
