#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x10F2FD0D67DE9C2A (_@habnab.it)
#
Name     : vcversioner
Version  : 2.16.0.0
Release  : 4
URL      : http://pypi.debian.net/vcversioner/vcversioner-2.16.0.0.tar.gz
Source0  : http://pypi.debian.net/vcversioner/vcversioner-2.16.0.0.tar.gz
Source99 : http://pypi.debian.net/vcversioner/vcversioner-2.16.0.0.tar.gz.asc
Summary  : Use version control tags to discover version numbers
Group    : Development/Tools
License  : ISC
Requires: vcversioner-legacypython
Requires: vcversioner-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
===========
        vcversioner
        ===========

%package legacypython
Summary: legacypython components for the vcversioner package.
Group: Default

%description legacypython
legacypython components for the vcversioner package.


%package python
Summary: python components for the vcversioner package.
Group: Default
Requires: vcversioner-legacypython

%description python
python components for the vcversioner package.


%prep
%setup -q -n vcversioner-2.16.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505073253
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505073253
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
