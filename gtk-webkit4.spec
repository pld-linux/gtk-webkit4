# TODO: review configure options:
# - FTL_JIT on !x86_64?
# - WEB_RTC (experimental) + MEDIA_STREAM (BR: openwebrtc)
# - ENCRYPTED_MEDIA (experimental)
# - THUNDER? (BR: Thunder + ThunderClientLibraries)
# - WEBDRIVER_BIDI (experimental)
# - WK_WEB_EXTENSIONS (experimental)
#
# Conditional build:
%bcond_without	introspection	# GObject introspection
%bcond_without	sysprof		# sysprof profiling
%bcond_without	wayland		# Wayland target (requires GTK+ wayland target)
%ifarch x32
%bcond_without	lowmem		# try to reduce build memory usage by adjusting gcc gc
%else
%bcond_with	lowmem		# try to reduce build memory usage by adjusting gcc gc
%endif
%bcond_with	lowmem2		# try to reduce build memory usage by disabling unified build (long)
#define max_bundle_size		# max size of unified build bundle, default is 8
#
# it's not possible to build this with debuginfo on 32bit archs due to
# memory constraints during linking and x86_64 debuginfo packages kill poldek
%define		_enable_debug_packages		0

Summary:	Port of WebKit embeddable web component to GTK+ 3
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK+ 3
Name:		gtk-webkit4
# 2.50.x is the last with webkit2gtk-4.0 library (gtk+3/libsoup-2 variant); other variants continuation in gtk-webkit4.1.spec
Version:	2.50.6
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	https://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
# Source0-md5:	30e318a7bd316fcd1937902f987f7d65
Patch0:		x32.patch
Patch1:		%{name}-icu59.patch
Patch2:		parallel-gir.patch
Patch3:		%{name}-driver-version-suffix.patch
Patch4:		max-bundle-size.patch
Patch5:		webkitgtk-serializers.patch
URL:		https://webkitgtk.org/
BuildRequires:	/usr/bin/ld.gold
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	OpenGLESv2-devel
BuildRequires:	at-spi2-core-devel >= 2.5.3
BuildRequires:	atk-devel >= 1:2.16.0
BuildRequires:	bubblewrap >= 0.3.1
BuildRequires:	cairo-devel >= 1.16.0
BuildRequires:	cmake >= 3.20
BuildRequires:	docbook-dtd412-xml
BuildRequires:	enchant2-devel >= 2
# or libspiel-devel with -DUSE_SPIEL=ON
BuildRequires:	flite-devel >= 2.2
BuildRequires:	fontconfig-devel >= 2.13.0
BuildRequires:	freetype-devel >= 1:2.9.0
BuildRequires:	gettext-devel
BuildRequires:	gettext-tools
BuildRequires:	gi-docgen
BuildRequires:	glib2-devel >= 1:2.70.0
BuildRequires:	glibc-misc
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 1.32.0}
BuildRequires:	gperf >= 3.0.1
# gstreamer,gstreamer-base
BuildRequires:	gstreamer-devel >= 1.18.4
BuildRequires:	gstreamer-gl-devel >= 1.18.4
# codecparsers,mpegts,webrtc
BuildRequires:	gstreamer-plugins-bad-devel >= 1.18.4
# allocators,app,audio,fft,pbutils,rtp,sdp,tag,video
BuildRequires:	gstreamer-plugins-base-devel >= 1.18.4
BuildRequires:	gstreamer-transcoder-devel >= 1.18.4
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	harfbuzz-devel >= 2.7.4
BuildRequires:	harfbuzz-icu-devel >= 2.7.4
BuildRequires:	hyphen-devel
BuildRequires:	lcms2-devel >= 2
%ifarch %arch64
%ifnarch %arch_with_atomics128
BuildRequires:	libatomic-devel
%endif
%endif
BuildRequires:	libavif-devel >= 0.9.0
BuildRequires:	libdrm-devel
BuildRequires:	libepoxy-devel >= 1.5.4
BuildRequires:	libgcrypt-devel >= 1.7.0
BuildRequires:	libicu-devel >= 70.1
BuildRequires:	libjpeg-devel
BuildRequires:	libjxl-devel >= 0.7.0
BuildRequires:	libmanette-devel >= 0.2.4
BuildRequires:	libnotify-devel
BuildRequires:	libpng-devel
BuildRequires:	libseccomp-devel
BuildRequires:	libsecret-devel
BuildRequires:	libsoup-devel >= 2.54
# -std=c++23; WebKitCommon.cmake says gcc 11.2.0 is minimum
BuildRequires:	libstdc++-devel >= 6:12.2
BuildRequires:	libtasn1-devel
BuildRequires:	libwebp-devel
BuildRequires:	libxml2-devel >= 1:2.9.13
BuildRequires:	libxslt-devel >= 1.1.13
BuildRequires:	openjpeg2-devel >= 2.2.0
BuildRequires:	openssl-devel >= 3.0.0
BuildRequires:	pango-devel >= 1:1.32.0
BuildRequires:	perl-base >= 1:5.10.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.7.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.029
BuildRequires:	ruby >= 1:2.5
BuildRequires:	ruby-modules >= 1:2.5
%if "%{ruby_version}" >= "3.0"
BuildRequires:	ruby-getoptlong
%endif
BuildRequires:	sqlite3-devel >= 3
%{?with_sysprof:BuildRequires:	sysprof-devel >= 3.38}
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	unifdef
%if %{with wayland}
BuildRequires:	wayland-devel >= 1.20
BuildRequires:	wayland-egl-devel
BuildRequires:	wayland-protocols >= 1.24
%endif
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
Requires:	glib2 >= 1:2.70.0
Requires:	gstreamer >= 1.2.3
Requires:	gstreamer-plugins-base >= 1.2.3
Requires:	gtk+3 >= 3.22.0
Requires:	harfbuzz >= 2.7.4
Requires:	libepoxy >= 1.5.4
Requires:	libgcrypt >= 1.7.0
Requires:	libjxl >= 0.7.0
Requires:	libsoup >= 2.54
Requires:	libxml2 >= 1:2.9.13
Requires:	libxslt >= 1.1.13
Requires:	openjpeg2 >= 2.2.0
Requires:	pango >= 1:1.32.0
Requires:	wayland >= 1.20
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
Requires:	glib2-devel >= 1:2.70.0
Requires:	gtk+3-devel >= 3.22.0
Requires:	libsoup-devel >= 2.54
Requires:	libstdc++-devel >= 6:11.2

%description devel
Development files for WebKit for GTK+ 3.

%description devel -l pl.UTF-8
Pliki programistyczne komponentu WebKit dla GTK+ 3.

%package apidocs
Summary:	API documentation for WebKit GTK+ 3 port
Summary(pl.UTF-8):	Dokumentacja API portu WebKitu do GTK+ 3
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for WebKit GTK+ 3 port.

%description apidocs -l pl.UTF-8
Dokumentacja API portu WebKitu do GTK+ 3.

%prep
%setup -q -n webkitgtk-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
CXXFLAGS="%{rpmcxxflags} -DNDEBUG %{?with_lowmem:--param ggc-min-expand=20 --param ggc-min-heapsize=65536}"
%cmake -B build-soup2 \
	-DENABLE_GEOLOCATION=ON \
	-DENABLE_GTKDOC=ON \
	%{!?with_introspection:-DENABLE_INTROSPECTION=OFF} \
	%{?with_lowmem2:-DENABLE_UNIFIED_BUILDS=OFF} \
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
	-DUSE_GTK4=OFF \
	-DUSE_LIBBACKTRACE=OFF \
	-DUSE_SOUP2=ON \
	%{!?with_sysprof:-DUSE_SYSPROF_CAPTURE=OFF} \
	%{?max_bundle_size:-DUNIFIED_BUILD_MAX_BUNDLE_SIZE=%{max_bundle_size}}

%{__make} -C build-soup2

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build-soup2 install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/{javascriptcoregtk,webkit*gtk}-* $RPM_BUILD_ROOT%{_gidocdir}

%find_lang WebKitGTK-4.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f WebKitGTK-4.0.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/WebKitWebDriver-4.0
%{_libdir}/libwebkit2gtk-4.0.so.*.*.*
%ghost %{_libdir}/libwebkit2gtk-4.0.so.37
%{_libdir}/libjavascriptcoregtk-4.0.so.*.*.*
%ghost %{_libdir}/libjavascriptcoregtk-4.0.so.18
%if %{with introspection}
%{_libdir}/girepository-1.0/JavaScriptCore-4.0.typelib
%{_libdir}/girepository-1.0/WebKit2-4.0.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-4.0.typelib
%endif
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/webkit2gtk-4.0
%endif
%attr(755,root,root) %{_libexecdir}/webkit2gtk-4.0/MiniBrowser
%attr(755,root,root) %{_libexecdir}/webkit2gtk-4.0/WebKitGPUProcess
%attr(755,root,root) %{_libexecdir}/webkit2gtk-4.0/WebKitNetworkProcess
%attr(755,root,root) %{_libexecdir}/webkit2gtk-4.0/WebKitWebProcess
%attr(755,root,root) %{_libexecdir}/webkit2gtk-4.0/jsc
%dir %{_libdir}/webkit2gtk-4.0
%dir %{_libdir}/webkit2gtk-4.0/injected-bundle
%{_libdir}/webkit2gtk-4.0/injected-bundle/libwebkit2gtkinjectedbundle.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/libwebkit2gtk-4.0.so
%{_libdir}/libjavascriptcoregtk-4.0.so
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
%{_gidocdir}/javascriptcoregtk-4.0
%{_gidocdir}/webkit2gtk-4.0
%{_gidocdir}/webkit2gtk-web-extension-4.0
