# TODO: fix tests and doc
#
# Conditional build:
%bcond_with	doc	# Sphinx documentation [broken, requires git repo?]
%bcond_with	tests	# subunit tests (FIXME: incomplete dependencies, some fail)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	reno: a New Way to manage Release Notes
Summary(pl.UTF-8):	reno: nowy sposób zarządzania informacjami o wydaniu (Release Notes)
Name:		python-reno
Version:	2.2.0
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/reno
Source0:	https://files.pythonhosted.org/packages/source/r/reno/reno-%{version}.tar.gz
# Source0-md5:	cacb861fa82ef46caca91e0d50306642
URL:		http://docs.openstack.org/developer/reno/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 1.4
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-PyYAML >= 3.1.0
BuildRequires:	python-babel >= 1.3
BuildRequires:	python-coverage >= 3.6
BuildRequires:	python-dulwich >= 0.15.0
#BuildRequires:	python-hacking >= 0.12.0
#BuildRequires:	python-hacking < 0.14
BuildRequires:	python-mock >= 1.2
BuildRequires:	python-oslosphinx >= 2.5.0
#BuildRequires:	python-oslotest >= 1.10.0
BuildRequires:	python-six >= 1.9.0
BuildRequires:	python-subunit >= 0.0.18
BuildRequires:	python-testrepository >= 0.0.18
BuildRequires:	python-testscenarios >= 0.4
BuildRequires:	python-testtools # >= 1.4.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-pbr >= 1.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyYAML >= 3.1.0
BuildRequires:	python3-babel >= 1.3
BuildRequires:	python3-coverage >= 3.6
BuildRequires:	python3-dulwich >= 0.15.0
#BuildRequires:	python3-hacking >= 0.12.0
#BuildRequires:	python3-hacking < 0.14
BuildRequires:	python3-oslosphinx >= 2.5.0
#BuildRequires:	python3-oslotest >= 1.10.0
BuildRequires:	python3-six >= 1.9.0
BuildRequires:	python3-subunit >= 0.0.18
BuildRequires:	python3-testrepository >= 0.0.18
BuildRequires:	python3-testscenarios >= 0.4
BuildRequires:	python3-testtools # >= 1.4.0
%endif
%endif
%if %{with doc}
BuildRequires:	python3-docutils >= 0.11
BuildRequires:	python3-oslosphinx >= 2.5.0
BuildRequires:	sphinx-pdg
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reno is a release notes manager designed with high throughput in mind,
supporting fast distributed development teams without introducing
additional development processes. The goal is to encourage detailed
and accurate release notes for every release.

%description -l pl.UTF-8
Reno to zarządca informacji o wydaniu, zaprojektowany z myślą o dużym
przepływie, obsługujący szybkie, rozproszone zespoły programistów bez
wprowadzania dodatkowych procesów. Celem jest wspieranie szczegółowych
i dokładnych informacji dla każdego wydania.

%package -n python3-reno
Summary:	reno: a New Way to manage Release Notes
Summary(pl.UTF-8):	reno: nowy sposób zarządzania informacjami o wydaniu (Release Notes)
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-reno
Reno is a release notes manager designed with high throughput in mind,
supporting fast distributed development teams without introducing
additional development processes. The goal is to encourage detailed
and accurate release notes for every release.

%description -n python3-reno -l pl.UTF-8
Reno to zarządca informacji o wydaniu, zaprojektowany z myślą o dużym
przepływie, obsługujący szybkie, rozproszone zespoły programistów bez
wprowadzania dodatkowych procesów. Celem jest wspieranie szczegółowych
i dokładnych informacji dla każdego wydania.

%package apidocs
Summary:	API documentation for reno
Summary(pl.UTF-8):	Dokumentacja API modułu reno
Group:		Documentation

%description apidocs
API documentation for reno.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu reno.

%prep
%setup -q -n reno-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test} %{?with_doc:build_sphinx}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/reno
%{py_sitescriptdir}/reno-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-reno
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/reno
%{py3_sitescriptdir}/reno-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
