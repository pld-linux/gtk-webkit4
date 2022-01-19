# TODO: review configure options:
# - FTL_JIT on !x86_64?
# - WEB_RTC+MEDIA_STREAM (BR: openwebrtc)
# - AVIF? (BR: libavif-devel >= 0.9.0)
# - THUNDER? (BR: Thunder + ThunderClientLibraries)
# - libsoup3 for HTTP/2 (drop USE_SOUP2=ON)? (BR: libsoup3-devel >= 2.99.9; changes abi tag from -4.0 to -4.1; doc tag remains -4.0)
# - gtk4 variant as gtk-webkit5 (-DUSE_GTK4=ON), (needs libsoup3, BR: gtk4-devel >= 3.98.5; changes abi and doc tags to -5.0)
#
# Conditional build:
%bcond_without	introspection	# GObject introspection
%bcond_with	cairogl		# accelerated 2D canvas using cairo-gl
%bcond_without	wayland		# Wayland target (requires GTK+ wayland target)
#
# it's not possible to build this with debuginfo on 32bit archs due to
# memory constraints during linking
%ifarch %{ix86} x32
%define		_enable_debug_packages		0
%endif
Summary:	Port of WebKit embeddable web component to GTK+ 3
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK+ 3
Name:		gtk-webkit4
# NOTE: 2.34.x is stable, 2.35.x devel
Version:	2.34.3
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	https://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
# Source0-md5:	de30c41fb57b2b024417669c22914752
Patch0:		x32.patch
Patch1:		%{name}-icu59.patch
Patch2:		%{name}-gir.patch
Patch3:		%{name}-npapi-remnants.patch
URL:		https://webkitgtk.org/
BuildRequires:	/usr/bin/ld.gold
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	OpenGLESv2-devel
BuildRequires:	at-spi2-core-devel >= 2.5.3
BuildRequires:	atk-devel >= 1:2.16.0
BuildRequires:	bubblewrap >= 0.3.1
BuildRequires:	cairo-devel >= 1.16.0
BuildRequires:	cmake >= 3.12
BuildRequires:	docbook-dtd412-xml
BuildRequires:	enchant2-devel >= 2
BuildRequires:	fontconfig-devel >= 2.13.0
BuildRequires:	freetype-devel >= 1:2.9.0
BuildRequires:	gcc-c++ >= 6:7.3.0
BuildRequires:	gettext-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.67.1
BuildRequires:	glibc-misc
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 1.32.0}
BuildRequires:	gperf >= 3.0.1
BuildRequires:	gstreamer-devel >= 1.14
BuildRequires:	gstreamer-gl-devel >= 1.10.0
# codecparsers,mpegts with -DUSE_GSTREAMER_MPEGTS=ON
#BuildRequires:	gstreamer-plugins-bad-devel >= 1.10.0
# app,audio,fft,pbutils,tag,video
BuildRequires:	gstreamer-plugins-base-devel >= 1.10.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	harfbuzz-devel >= 1.4.2
BuildRequires:	harfbuzz-icu-devel >= 1.4.2
BuildRequires:	hyphen-devel
BuildRequires:	libgcrypt-devel >= 1.7.0
BuildRequires:	libicu-devel >= 61.2
BuildRequires:	libjpeg-devel
BuildRequires:	libmanette-devel >= 0.2.4
BuildRequires:	libnotify-devel
BuildRequires:	libpng-devel
BuildRequires:	libseccomp-devel
BuildRequires:	libsecret-devel
BuildRequires:	libsoup-devel >= 2.54
BuildRequires:	libstdc++-devel >= 6:7.3.0
BuildRequires:	libtasn1-devel
BuildRequires:	libwebp-devel
BuildRequires:	libwpe-devel >= 1.3.0
BuildRequires:	libxml2-devel >= 1:2.8.0
BuildRequires:	libxslt-devel >= 1.1.7
BuildRequires:	openjpeg2-devel >= 2.2.0
BuildRequires:	pango-devel >= 1:1.32.0
BuildRequires:	perl-base >= 1:5.10.0
BuildRequires:	pkgconfig
%if %{with cairogl}
BuildRequires:	pkgconfig(cairo-egl) >= 1.10.2
BuildRequires:	pkgconfig(cairo-gl) >= 1.10.2
BuildRequires:	pkgconfig(cairo-glx) >= 1.10.2
%endif
BuildRequires:	python >= 1:2.7.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.699
BuildRequires:	ruby >= 1:1.9
BuildRequires:	ruby-modules >= 1:1.9
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
%if %{with wayland}
BuildRequires:	wayland-devel
BuildRequires:	wayland-egl-devel
BuildRequires:	wayland-protocols >= 1.12
%endif
BuildRequires:	wpebackend-fdo-devel >= 1.6.0
BuildRequires:	woff2-devel >= 1.0.2
BuildRequires:	xdg-dbus-proxy
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	at-spi2-core-libs >= 2.5.3
Requires:	atk >= 1:2.16.0
Requires:	cairo >= 1.16.0
Requires:	fontconfig-libs >= 2.13.0
Requires:	freetype >= 1:2.9.0
Requires:	glib2 >= 1:2.67.1
Requires:	gstreamer >= 1.2.3
Requires:	gstreamer-plugins-base >= 1.2.3
Requires:	gtk+3 >= 3.22.0
Requires:	harfbuzz >= 1.4.2
Requires:	libgcrypt >= 1.7.0
Requires:	libsoup >= 2.54
Requires:	libxml2 >= 1:2.8.0
Requires:	libxslt >= 1.1.7
Requires:	openjpeg2 >= 2.2.0
Requires:	pango >= 1:1.32.0
Requires:	woff2 >= 1.0.2
Requires:	wpebackend-fdo >= 1.6.0
%{?with_introspection:Conflicts:	gir-repository < 0.6.5-7}
# Source/JavaScriptCore/CMakeLists.txt /WTF_CPU_
ExclusiveArch:	%{ix86} %{x8664} x32 %{arm} aarch64 hppa mips ppc ppc64 ppc64le s390 s390x sh4
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
Requires:	glib2-devel >= 1:2.67.1
Requires:	gtk+3-devel >= 3.22.0
Requires:	libsoup-devel >= 2.54
Requires:	libstdc++-devel >= 6:7.3.0

%description devel
Development files for WebKit for GTK+ 3.

%description devel -l pl.UTF-8
Pliki programistyczne komponentu WebKit dla GTK+ 3.

%package apidocs
Summary:	WebKit API documentation
Summary(pl.UTF-8):	Dokumentacja API WebKita
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
WebKit API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API WebKita.

%prep
%setup -q -n webkitgtk-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
install -d build
cd build
%cmake .. \
	%{?with_cairogl:-DENABLE_ACCELERATED_2D_CANVAS=ON} \
	-DENABLE_GEOLOCATION=ON \
	-DENABLE_GTKDOC=ON \
	%{!?with_introspection:-DENABLE_INTROSPECTION=OFF} \
	-DENABLE_VIDEO=ON \
	%{!?with_wayland:-DENABLE_WAYLAND_TARGET=OFF} \
	-DENABLE_WEB_AUDIO=ON \
	-DENABLE_WEBGL=ON \
%ifarch x32
	-DENABLE_C_LOOP=ON \
	-DENABLE_JIT=OFF \
	-DENABLE_SAMPLING_PROFILER=OFF \
%endif
%ifarch %{ix86} %{x8664} x32
	-DHAVE_SSE2_EXTENSIONS=ON \
%endif
	-DPORT=GTK \
	-DSHOULD_INSTALL_JS_SHELL=ON \
	-DUSE_SOUP2=ON

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
%attr(755,root,root) %{_bindir}/WebKitWebDriver
%attr(755,root,root) %{_libdir}/libwebkit2gtk-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebkit2gtk-4.0.so.37
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjavascriptcoregtk-4.0.so.18
%if %{with introspection}
%{_libdir}/girepository-1.0/JavaScriptCore-4.0.typelib
%{_libdir}/girepository-1.0/WebKit2-4.0.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-4.0.typelib
%endif
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/webkit2gtk-4.0
%endif
%attr(755,root,root) %{_libexecdir}/webkit2gtk-4.0/WebKitNetworkProcess
%attr(755,root,root) %{_libexecdir}/webkit2gtk-4.0/WebKitWebProcess
%attr(755,root,root) %{_libexecdir}/webkit2gtk-4.0/jsc
%dir %{_libdir}/webkit2gtk-4.0
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
%{_gtkdocdir}/jsc-glib-4.0
%{_gtkdocdir}/webkit2gtk-4.0
%{_gtkdocdir}/webkitdomgtk-4.0
