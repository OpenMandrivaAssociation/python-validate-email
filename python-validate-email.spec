# Created by pyp2rpm-3.3.2
%global pypi_name validate-email

Name:           python-%{pypi_name}
Version:        1.3
Release:        6
Summary:        Validate_email verify if an email address is valid and really exists
Group:          Development/Python
License:        LGPL
URL:            https://github.com/syrusakbary/validate_email
Source0:        https://files.pythonhosted.org/packages/source/v/%{pypi_name}/validate_email-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python%{pyver}dist(setuptools)
%rename 	python3-validate-email = %{version}-%{release}

%description
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
%py_build

%install
%py_install


%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/validate_email.py
%{python3_sitelib}/validate_email-%{version}-py*.*.egg-info
