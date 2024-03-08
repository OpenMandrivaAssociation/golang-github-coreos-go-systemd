# Run tests in check section
%bcond_without check

# https://github.com/coreos/go-systemd
%global goipath		github.com/coreos/go-systemd
%global goaltipaths	github.com/coreos/go-systemd/v22
%global forgeurl	https://github.com/coreos/go-systemd
Version:		22.5.0

%gometa

Summary:	Go bindings to systemd socket activation, journal, D-Bus, and unit files
Name:		golang-github-coreos-go-systemd

Release:	1
Source0:	https://github.com/coreos/go-systemd/archive/v%{version}/go-systemd-%{version}.tar.gz
URL:		https://github.com/coreos/go-systemd
License:	ASL 2.0
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
Go bindings to systemd. The project has several packages:

 *  activation - for writing and using socket activation from Go
 *  daemon - for notifying systemd of service status changes
 *  dbus - for starting/stopping/inspecting running services and units
 *  journal - for writing to systemd's logging service, journald
 *  sdjournal - for reading from journald by wrapping its C API
 *  login1 - for integration with the systemd logind API
 *  machine1 - for registering machines/containers with systemd
 *  unit - for (de)serialization and comparison of unit files

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE NOTICE
%doc examples CONTRIBUTING.md README.md code-of-conduct.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n go-systemd-%{version}

%build
%gobuildroot

%install
%goinstall

# install alternative name
ln -fs . %{buildroot}%{_datadir}/gocode/src/%{goaltipaths}
echo \"%{_datadir}/gocode/src/%{goaltipaths}\" >> devel.file-list

%check
%if %{with check}
%gochecks -d dbus -d import1 -d internal/dlopen -d journal -d login1 -d machine1 -d sdjournal -d util
%endif

