#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-websocket_client
Version  : 1.5.0
Release  : 101
URL      : https://files.pythonhosted.org/packages/02/cd/1adc1276f1e8f6a929783f4c2992ec7a4934a81f8ced3d4a87191cc168c2/websocket-client-1.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/02/cd/1adc1276f1e8f6a929783f4c2992ec7a4934a81f8ced3d4a87191cc168c2/websocket-client-1.5.0.tar.gz
Summary  : WebSocket client for Python with low level API options
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-websocket_client-bin = %{version}-%{release}
Requires: pypi-websocket_client-license = %{version}-%{release}
Requires: pypi-websocket_client-python = %{version}-%{release}
Requires: pypi-websocket_client-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![docs](https://readthedocs.org/projects/websocket-client/badge/?style=flat)](https://websocket-client.readthedocs.io/)
[![Build Status](https://github.com/websocket-client/websocket-client/actions/workflows/build.yml/badge.svg)](https://github.com/websocket-client/websocket-client/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/websocket-client/websocket-client/branch/master/graph/badge.svg?token=pcXhUQwiL3)](https://codecov.io/gh/websocket-client/websocket-client)
[![PyPI Downloads](https://pepy.tech/badge/websocket-client)](https://pepy.tech/project/websocket-client)
[![PyPI version](https://img.shields.io/pypi/v/websocket_client)](https://pypi.org/project/websocket_client/)

%package bin
Summary: bin components for the pypi-websocket_client package.
Group: Binaries
Requires: pypi-websocket_client-license = %{version}-%{release}

%description bin
bin components for the pypi-websocket_client package.


%package license
Summary: license components for the pypi-websocket_client package.
Group: Default

%description license
license components for the pypi-websocket_client package.


%package python
Summary: python components for the pypi-websocket_client package.
Group: Default
Requires: pypi-websocket_client-python3 = %{version}-%{release}

%description python
python components for the pypi-websocket_client package.


%package python3
Summary: python3 components for the pypi-websocket_client package.
Group: Default
Requires: python3-core
Provides: pypi(websocket_client)

%description python3
python3 components for the pypi-websocket_client package.


%prep
%setup -q -n websocket-client-1.5.0
cd %{_builddir}/websocket-client-1.5.0
pushd ..
cp -a websocket-client-1.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1674750456
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-websocket_client
cp %{_builddir}/websocket-client-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-websocket_client/2829260f879a224e12c095d688551d2965d0b882 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wsdump

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-websocket_client/2829260f879a224e12c095d688551d2965d0b882

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
