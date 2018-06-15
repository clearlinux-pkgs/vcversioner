#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x10F2FD0D67DE9C2A (_@habnab.it)
#
Name     : vcversioner
Version  : 2.16.0.0
Release  : 13
URL      : http://pypi.debian.net/vcversioner/vcversioner-2.16.0.0.tar.gz
Source0  : http://pypi.debian.net/vcversioner/vcversioner-2.16.0.0.tar.gz
Source99 : http://pypi.debian.net/vcversioner/vcversioner-2.16.0.0.tar.gz.asc
Summary  : Use version control tags to discover version numbers
Group    : Development/Tools
License  : ISC
Requires: vcversioner-python3
Requires: vcversioner-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
===========
        vcversioner
        ===========

%package python
Summary: python components for the vcversioner package.
Group: Default
Requires: vcversioner-python3

%description python
python components for the vcversioner package.


%package python3
Summary: python3 components for the vcversioner package.
Group: Default
Requires: python3-core

%description python3
python3 components for the vcversioner package.


%prep
%setup -q -n vcversioner-2.16.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523049518
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
