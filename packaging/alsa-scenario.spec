Name:       alsa-scenario
Summary:    ALSA Scenario pkg
Version: 0.2.1
Release:    13
Group:      Multimedia/Audio
License:    LGPLv2+
Source0:    %{name}-%{version}.tar.gz
Source1001: 	alsa-scenario.manifest
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
cp %{SOURCE1001} .


%build
cp -f /usr/share/libtool/config/config.guess %{_builddir}/%{name}-%{version}/
cp -f /usr/share/libtool/config/config.sub %{_builddir}/%{name}-%{version}/
%configure --disable-static
make %{?jobs:-j%jobs}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%{_libdir}/libascenario-0.2.so.*


%files devel
%manifest %{name}.manifest
%{_includedir}/alsa/*.h
%{_libdir}/libascenario.so
%{_libdir}/pkgconfig/libascenario.pc

