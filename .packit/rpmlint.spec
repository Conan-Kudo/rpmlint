%{!?python3: %global python3 %{__python3}}

Name:           rpmlint
Version:        2.0.0
Release:        0%{?dist}
Summary:        Tool for checking common errors in RPM packages

License:        GPLv2+
URL:            https://github.com/rpm-software-management/rpmlint
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%if 0%{?suse_version}
# Unfortunately, these don't get pulled in automatically...
BuildRequires:  python-rpm-macros
BuildRequires:  python-rpm-generators
%endif

# For tests
BuildRequires:  dash
BuildRequires:  python3dist(file-magic)
BuildRequires:  python3dist(pybeam)
BuildRequires:  python3dist(pyenchant)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-flake8)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(pyxdg)
BuildRequires:  python3dist(rpm)
BuildRequires:  python3dist(toml)
BuildRequires:  python3dist(zstd)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/checkbashisms
BuildRequires:  /usr/bin/desktop-file-validate

%if 0%{?suse_version}
BuildRequires:  myspell-en_US
BuildRequires:  myspell-cs_CZ
%else
BuildRequires:  hunspell-en
BuildRequires:  hunspell-cs
%endif

Requires:       /bin/bash
Requires:       /usr/bin/appstream-util
Requires:       /usr/bin/bzip2
Requires:       /usr/bin/checkbashisms
Requires:       /usr/bin/cpio
Requires:       /usr/bin/desktop-file-validate
Requires:       /usr/bin/groff
Requires:       /usr/bin/gtbl
Requires:       /usr/bin/ldd
Requires:       /usr/bin/man
Requires:       /usr/bin/perl
Requires:       /usr/bin/readelf
Requires:       /usr/bin/xz
Requires:       /usr/bin/zstd

# Enable Python dependency generation
%{?python_enable_dependency_generator}

%description
rpmlint is a tool for checking common errors in RPM packages. Binary
and source packages as well as spec files can be checked.


%prep
%autosetup


%build
%py3_build


%install
%py3_install


%check
%python3 -m pytest


%files
%license COPYING
%doc README*
%{_bindir}/rpmlint
%{_bindir}/rpmdiff
%{python3_sitelib}/rpmlint*


%changelog
