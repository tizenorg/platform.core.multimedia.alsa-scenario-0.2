Name:       alsa-scenario
Summary:    ALSA Scenario pkg
Version: 0.2.1
Release:    13
Group:      TO_BE/FILLED_IN
License:    LGPLv2+
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(alsa)


%description
ALSA Scenario package



%package devel
Summary:    ALSA Scenario pkg (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
ALSA Scenario package (devel)


%prep
%setup -q


%build
cp -f /usr/share/libtool/config/config.guess %{_builddir}/%{name}-%{version}/
cp -f /usr/share/libtool/config/config.sub %{_builddir}/%{name}-%{version}/
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%manifest alsa-scenario.manifest
/usr/lib/libascenario-0.2.so.*


%files devel
/usr/include/alsa/*.h
/usr/lib/libascenario.so
/usr/lib/pkgconfig/libascenario.pc

