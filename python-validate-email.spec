# Created by pyp2rpm-3.3.2
%global pypi_name validate-email

Name:           python-%{pypi_name}
Version:        1.3
Release:        5
Summary:        Validate_email verify if an email address is valid and really exists
Group:          Development/Python
License:        LGPL
URL:            https://github.com/syrusakbary/validate_email
Source0:        https://files.pythonhosted.org/packages/source/v/%{pypi_name}/validate_email-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)

BuildRequires:  python-devel
BuildRequires:  python3dist(setuptools)

%description
 Validate_email Validate_email is a package for Python that check if an email
is valid, properly formatted and really exists.INSTALLATION First, you must
do:: pip install validate_emailExtra For check the domain mx and verify email
exits you must have the pyDNS package installed:: pip install pyDNSBasic
usage:: from validate_email import validate_email is_valid...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
 Validate_email Validate_email is a package for Python that check if an email
is valid, properly formatted and really exists.INSTALLATION First, you must
do:: pip install validate_emailExtra For check the domain mx and verify email
exits you must have the pyDNS package installed:: pip install pyDNSBasic
usage:: from validate_email import validate_email is_valid...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 Validate_email Validate_email is a package for Python that check if an email
is valid, properly formatted and really exists.INSTALLATION First, you must
do:: pip install validate_emailExtra For check the domain mx and verify email
exits you must have the pyDNS package installed:: pip install pyDNSBasic
usage:: from validate_email import validate_email is_valid...


%prep
%autosetup -n validate_email-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/validate_email.py*
%{python2_sitelib}/validate_email-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/validate_email.py
%{python3_sitelib}/validate_email-%{version}-py*.*.egg-info
