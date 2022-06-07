# TODO: review configure options:
# - FTL_JIT on !x86_64?
# - WEB_RTC+MEDIA_STREAM (BR: openwebrtc)
# - AVIF? (BR: libavif-devel >= 0.9.0)
# - JPEGXL? (BR: libjxl-devel)
# - THUNDER? (BR: Thunder + ThunderClientLibraries)
#
# Conditional build:
%bcond_without	introspection	# GObject introspection
%bcond_without	libsoup2	# webkit-4.0 (libsoup2 based) variant
%bcond_without	libsoup3	# webkit-4.1 (libsoup3 based) variant (HTTP/2 support)
%bcond_without	gtk3		# webkit-4.x (gtk3 based) variants
%bcond_without	gtk4		# webkit-5.0 (gtk4/libsoup3 based) variant
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
Version:	2.36.1
Release:	2
License:	BSD-like
Group:		X11/Libraries
Source0:	https://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
# Source0-md5:	e6100df7f82d95a4e65176b10f5ab011
Patch0:		x32.patch
Patch1:		%{name}-icu59.patch
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
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.22.0}
%{?with_gtk4:BuildRequires:	gtk4-devel >= 4.0}
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	harfbuzz-devel >= 1.4.2
BuildRequires:	harfbuzz-icu-devel >= 1.4.2
BuildRequires:	hyphen-devel
BuildRequires:	lcms2-devel
BuildRequires:	libgcrypt-devel >= 1.7.0
BuildRequires:	libicu-devel >= 61.2
BuildRequires:	libjpeg-devel
BuildRequires:	libmanette-devel >= 0.2.4
BuildRequires:	libnotify-devel
BuildRequires:	libpng-devel
BuildRequires:	libseccomp-devel
BuildRequires:	libsecret-devel
%{?with_libsoup2:BuildRequires:	libsoup-devel >= 2.54}
%{?with_libsoup3:BuildRequires:	libsoup3-devel >= 3.0}
# -std=c++2a
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	libtasn1-devel
BuildRequires:	libwebp-devel
BuildRequires:	libwpe-devel >= 1.3.0
BuildRequires:	libxml2-devel >= 1:2.8.0
BuildRequires:	libxslt-devel >= 1.1.7
BuildRequires:	openjpeg2-devel >= 2.2.0
BuildRequires:	pango-devel >= 1:1.32.0
BuildRequires:	perl-base >= 1:5.10.0
BuildRequires:	pkgconfig
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
Requires:	libstdc++-devel >= 6:8

%description devel
Development files for WebKit for GTK+ 3.

%description devel -l pl.UTF-8
Pliki programistyczne komponentu WebKit dla GTK+ 3.

%package apidocs
Summary:	API documentation for WebKit GTK+ 3 port
Summary(pl.UTF-8):	Dokumentacja API portu WebKitu do GTK+ 3
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
API documentation for WebKit GTK+ 3 port.

%description apidocs -l pl.UTF-8
Dokumentacja API portu WebKitu do GTK+ 3.

%package -n gtk-webkit4.1
Summary:	Port of WebKit embeddable web component to GTK+ 3 with HTTP/2 support
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK+ 3 z obsługą HTTP/2
Group:		X11/Libraries
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
Requires:	libsoup3 >= 3.0
Requires:	libxml2 >= 1:2.8.0
Requires:	libxslt >= 1.1.7
Requires:	openjpeg2 >= 2.2.0
Requires:	pango >= 1:1.32.0
Requires:	woff2 >= 1.0.2
Requires:	wpebackend-fdo >= 1.6.0

%description -n gtk-webkit4.1
gtk-webkit4.1 is a port of the WebKit embeddable web component to GTK+
3 with HTTP/2 (libsoup 3) support.

%description -n gtk-webkit4.1 -l pl.UTF-8
gtk-webkit4.1 to port osadzalnego komponentu WWW WebKit do GTK+ 3 z
obsługą HTTP/2 (libsoup 3).

%package -n gtk-webkit4.1-devel
Summary:	Development files for WebKit for GTK+ 3 with HTTP/2 support
Summary(pl.UTF-8):	Pliki programistyczne komponentu WebKit dla GTK+ 3 z obsługą HTTP/2
Group:		X11/Development/Libraries
Requires:	gtk-webkit4.1 = %{version}-%{release}
Requires:	glib2-devel >= 1:2.67.1
Requires:	gtk+3-devel >= 3.22.0
Requires:	libsoup3-devel >= 3.0
Requires:	libstdc++-devel >= 6:8

%description -n gtk-webkit4.1-devel
Development files for WebKit for GTK+ 3 with HTTP/2 support.

%description -n gtk-webkit4.1-devel -l pl.UTF-8
Pliki programistyczne komponentu WebKit dla GTK+ 3 z obsługą HTTP/2.

%package -n gtk-webkit5
Summary:	Port of WebKit embeddable web component to GTK 4
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK 4
Group:		X11/Libraries
Requires:	at-spi2-core-libs >= 2.5.3
Requires:	atk >= 1:2.16.0
Requires:	cairo >= 1.16.0
Requires:	fontconfig-libs >= 2.13.0
Requires:	freetype >= 1:2.9.0
Requires:	glib2 >= 1:2.67.1
Requires:	gstreamer >= 1.2.3
Requires:	gstreamer-plugins-base >= 1.2.3
Requires:	gtk4 >= 4.0
Requires:	harfbuzz >= 1.4.2
Requires:	libgcrypt >= 1.7.0
Requires:	libsoup3 >= 3.0
Requires:	libxml2 >= 1:2.8.0
Requires:	libxslt >= 1.1.7
Requires:	openjpeg2 >= 2.2.0
Requires:	pango >= 1:1.32.0
Requires:	woff2 >= 1.0.2
Requires:	wpebackend-fdo >= 1.6.0

%description -n gtk-webkit5
gtk-webkit5 is a port of the WebKit embeddable web component to GTK 4.

%description -n gtk-webkit5 -l pl.UTF-8
gtk-webkit5 to port osadzalnego komponentu WWW WebKit do GTK+ 4.

%package -n gtk-webkit5-devel
Summary:	Development files for WebKit for GTK 4
Summary(pl.UTF-8):	Pliki programistyczne komponentu WebKit dla GTK 4
Group:		X11/Development/Libraries
Requires:	gtk-webkit5 = %{version}-%{release}
Requires:	glib2-devel >= 1:2.67.1
Requires:	gtk4-devel >= 4.0
Requires:	libsoup3-devel >= 3.0
Requires:	libstdc++-devel >= 6:8

%description -n gtk-webkit5-devel
Development files for WebKit for GTK 4.

%description -n gtk-webkit5-devel -l pl.UTF-8
Pliki programistyczne komponentu WebKit dla GTK 4.

%package -n gtk-webkit5-apidocs
Summary:	API documentation for WebKit GTK 4 port
Summary(pl.UTF-8):	Dokumentacja API portu WebKitu do GTK 4
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description -n gtk-webkit5-apidocs
API documentation for WebKit GTK 4 port.

%description -n gtk-webkit5-apidocs -l pl.UTF-8
Dokumentacja API portu WebKitu do GTK 4.

%prep
%setup -q -n webkitgtk-%{version}
%patch0 -p1
%patch1 -p1

%build
for kind in %{?with_gtk3:%{?with_libsoup2:soup2} %{?with_libsoup3:soup3}} %{?with_gtk4:gtk4} ; do
install -d build-${kind}
cd build-${kind}
# gtk4 variant is missing some files in dist:
# Source/WebKit/UIProcess/API/gtk/docs/webkit2gtk-5.0-sections.txt
# Source/WebKit/UIProcess/API/gtk/docs/webkit2gtk-5.0.types
# don't know how to generate them, disable GTKDOC for now
%cmake .. \
	-DENABLE_GEOLOCATION=ON \
	$([ "$kind" != "gtk4" ] && echo -DENABLE_GTKDOC=ON) \
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
	$([ "$kind" = "gtk4" ] && echo -DUSE_GTK4=ON) \
	$([ "$kind" = "soup2" ] && echo -DUSE_SOUP2=ON)

%{__make}
cd ..
done

%install
rm -rf $RPM_BUILD_ROOT

for kind in %{?with_gtk3:%{?with_libsoup2:soup2} %{?with_libsoup3:soup3}} %{?with_gtk4:gtk4} ; do
%{__make} -C build-${kind} install \
	DESTDIR=$RPM_BUILD_ROOT
done

%if "%{_gtkdocdir}" != "%{_datadir}/gtk-doc/html"
install -d $RPM_BUILD_ROOT%{_gtkdocdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/* $RPM_BUILD_ROOT%{_gtkdocdir}
%endif

%{?with_gtk3:%{?with_libsoup2:%find_lang WebKit2GTK-4.0}}
%{?with_gtk3:%{?with_libsoup3:%find_lang WebKit2GTK-4.1}}
%{?with_gtk4:%find_lang WebKit2GTK-5.0}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n gtk-webkit4.1 -p /sbin/ldconfig
%postun	-n gtk-webkit4.1 -p /sbin/ldconfig

%post	-n gtk-webkit5 -p /sbin/ldconfig
%postun	-n gtk-webkit5 -p /sbin/ldconfig

%if %{with gtk3} && %{with libsoup2}
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
%endif

%if %{with gtk3}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/jsc-glib-4.0
%{_gtkdocdir}/webkit2gtk-4.0
%{_gtkdocdir}/webkitdomgtk-4.0
%endif

%if %{with gtk3} && %{with libsoup3}
%files -n gtk-webkit4.1 -f WebKit2GTK-4.1.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_libdir}/libwebkit2gtk-4.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebkit2gtk-4.1.so.0
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-4.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjavascriptcoregtk-4.1.so.0
%if %{with introspection}
%{_libdir}/girepository-1.0/JavaScriptCore-4.1.typelib
%{_libdir}/girepository-1.0/WebKit2-4.1.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-4.1.typelib
%endif
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/webkit2gtk-4.1
%endif
%attr(755,root,root) %{_libexecdir}/webkit2gtk-4.1/WebKitNetworkProcess
%attr(755,root,root) %{_libexecdir}/webkit2gtk-4.1/WebKitWebProcess
%attr(755,root,root) %{_libexecdir}/webkit2gtk-4.1/jsc
%dir %{_libdir}/webkit2gtk-4.1
%dir %{_libdir}/webkit2gtk-4.1/injected-bundle
%attr(755,root,root) %{_libdir}/webkit2gtk-4.1/injected-bundle/libwebkit2gtkinjectedbundle.so

%files -n gtk-webkit4.1-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebkit2gtk-4.1.so
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-4.1.so
%if %{with introspection}
%{_datadir}/gir-1.0/JavaScriptCore-4.1.gir
%{_datadir}/gir-1.0/WebKit2-4.1.gir
%{_datadir}/gir-1.0/WebKit2WebExtension-4.1.gir
%endif
%{_includedir}/webkitgtk-4.1
%{_pkgconfigdir}/javascriptcoregtk-4.1.pc
%{_pkgconfigdir}/webkit2gtk-4.1.pc
%{_pkgconfigdir}/webkit2gtk-web-extension-4.1.pc
%endif

%if %{with gtk4}
%files -n gtk-webkit5 -f WebKit2GTK-5.0.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_libdir}/libwebkit2gtk-5.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebkit2gtk-5.0.so.0
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-5.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjavascriptcoregtk-5.0.so.0
%if %{with introspection}
%{_libdir}/girepository-1.0/JavaScriptCore-5.0.typelib
%{_libdir}/girepository-1.0/WebKit2-5.0.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-5.0.typelib
%endif
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/webkit2gtk-5.0
%endif
%attr(755,root,root) %{_libexecdir}/webkit2gtk-5.0/WebKitNetworkProcess
%attr(755,root,root) %{_libexecdir}/webkit2gtk-5.0/WebKitWebProcess
%attr(755,root,root) %{_libexecdir}/webkit2gtk-5.0/jsc
%dir %{_libdir}/webkit2gtk-5.0
%dir %{_libdir}/webkit2gtk-5.0/injected-bundle
%attr(755,root,root) %{_libdir}/webkit2gtk-5.0/injected-bundle/libwebkit2gtkinjectedbundle.so

%files -n gtk-webkit5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebkit2gtk-5.0.so
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-5.0.so
%if %{with introspection}
%{_datadir}/gir-1.0/JavaScriptCore-5.0.gir
%{_datadir}/gir-1.0/WebKit2-5.0.gir
%{_datadir}/gir-1.0/WebKit2WebExtension-5.0.gir
%endif
%{_includedir}/webkitgtk-5.0
%{_pkgconfigdir}/javascriptcoregtk-5.0.pc
%{_pkgconfigdir}/webkit2gtk-5.0.pc
%{_pkgconfigdir}/webkit2gtk-web-extension-5.0.pc

# disabled for now, see note on cmake
%if 0
%files -n gtk-webkit5-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/jsc-glib-5.0
%{_gtkdocdir}/webkit2gtk-5.0
%{_gtkdocdir}/webkitdomgtk-5.0
%endif
%endif
