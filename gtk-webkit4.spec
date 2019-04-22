# TODO: review configure options:
# - FTL_JIT on !x86_64?
# - WEB_RTC+MEDIA_STREAM (BR: openwebrtc)
#
# Conditional build:
%bcond_without	gtk2		# WebKitPluginProcess2 to load GTK+ 2.x based plugins
%bcond_without	introspection	# disable introspection
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
Version:	2.24.1
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	https://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
# Source0-md5:	ed70e2bf2476a58b17df3d051f42ce6a
Patch0:		x32.patch
Patch1:		%{name}-icu59.patch
Patch2:		%{name}-gir.patch
URL:		https://webkitgtk.org/
BuildRequires:	/usr/bin/ld.gold
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	at-spi2-core-devel >= 2.6.0
BuildRequires:	atk-devel
BuildRequires:	bison >= 2.3
BuildRequires:	cairo-devel >= 1.16.0
BuildRequires:	cmake >= 3.3
BuildRequires:	docbook-dtd412-xml
BuildRequires:	enchant2-devel >= 2
BuildRequires:	flex >= 2.5.34
BuildRequires:	fontconfig-devel >= 2.13.0
BuildRequires:	freetype-devel >= 1:2.9.0
BuildRequires:	gcc-c++ >= 6:6.0.0
BuildRequires:	geoclue2-devel >= 2.1.5
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.40
BuildRequires:	glibc-misc
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 1.32.0}
BuildRequires:	gperf >= 3.0.1
BuildRequires:	gstreamer-devel >= 1.14
BuildRequires:	gstreamer-gl-devel >= 1.8.3
# mpegts with -DUSE_GSTREAMER_MPEGTS=ON
#BuildRequires:	gstreamer-plugins-bad-devel >= 1.8.3
# app,audio,fft,pbutils,tag,video
BuildRequires:	gstreamer-plugins-base-devel >= 1.8.3
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.24.10}
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	harfbuzz-devel >= 1.4.2
BuildRequires:	harfbuzz-icu-devel >= 1.4.2
BuildRequires:	hyphen-devel
BuildRequires:	libgcrypt-devel >= 1.7.0
BuildRequires:	libicu-devel >= 59
BuildRequires:	libjpeg-devel
BuildRequires:	libnotify-devel
BuildRequires:	libpng-devel
BuildRequires:	libsecret-devel
BuildRequires:	libsoup-devel >= 2.48
BuildRequires:	libstdc++-devel >= 6:6.0.0
BuildRequires:	libtasn1-devel
BuildRequires:	libwebp-devel
BuildRequires:	libxml2-devel >= 1:2.8.0
BuildRequires:	libxslt-devel >= 1.1.7
BuildRequires:	openjpeg2-devel >= 2.2.0
BuildRequires:	pango-devel >= 1:1.32.0
BuildRequires:	perl-base >= 1:5.10.0
BuildRequires:	pkgconfig
%if %{with cairogl}
BuildRequires:	pkgconfig(cairo-egl)
BuildRequires:	pkgconfig(cairo-gl)
BuildRequires:	pkgconfig(cairo-glx)
%endif
BuildRequires:	python >= 1:2.7.0
BuildRequires:	rpmbuild(macros) >= 1.699
BuildRequires:	ruby >= 1:1.9
BuildRequires:	ruby-modules >= 1:1.9
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	woff2-devel >= 1.0.2
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	cairo >= 1.16.0
Requires:	fontconfig-libs >= 2.13.0
Requires:	freetype >= 1:2.9.0
Requires:	glib2 >= 1:2.40
Requires:	gstreamer >= 1.2.3
Requires:	gstreamer-plugins-base >= 1.2.3
%{?with_gtk2:Requires:	gtk+2 >= 2:2.24.10}
Requires:	gtk+3 >= 3.12.0
Requires:	harfbuzz >= 1.4.2
Requires:	libsoup >= 2.48
Requires:	libxml2 >= 1:2.8.0
Requires:	libxslt >= 1.1.7
Requires:	openjpeg2 >= 2.2.0
Requires:	pango >= 1:1.32.0
Requires:	woff2 >= 1.0.2
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
Requires:	glib2-devel >= 1:2.40
Requires:	gtk+3-devel >= 3.12.0
Requires:	libsoup-devel >= 2.48
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
%patch1 -p1
%patch2 -p1

%build
install -d build
cd build
%cmake .. \
	%{?with_cairogl:-DENABLE_ACCELERATED_2D_CANVAS=ON} \
	-DENABLE_GEOLOCATION=ON \
	-DENABLE_GTKDOC=ON \
	%{!?with_introspection:-DENABLE_INTROSPECTION=OFF} \
	%{!?with_gtk2:-DENABLE_PLUGIN_PROCESS_GTK2=OFF} \
	%{!?with_wayland:-DENABLE_WAYLAND_TARGET=OFF} \
%ifarch x32
	-DENABLE_C_LOOP=ON \
	-DENABLE_JIT=OFF \
	-DENABLE_SAMPLING_PROFILER=OFF \
%endif
	-DENABLE_VIDEO=ON \
	-DENABLE_WEB_AUDIO=ON \
	-DENABLE_WEBGL=ON \
%ifarch %{ix86} %{x8664} x32
	-DHAVE_SSE2_EXTENSIONS=ON \
%endif
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
%attr(755,root,root) %{_libexecdir}/webkit2gtk-4.0/WebKitPluginProcess
%attr(755,root,root) %{_libexecdir}/webkit2gtk-4.0/WebKitPluginProcess2
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
