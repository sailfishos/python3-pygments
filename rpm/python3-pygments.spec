Name:       python3-pygments
Summary:    Generic syntax highlighter written in Python
Version:    2.6.1
Release:    1
License:    BSD
URL:        https://github.com/sailfishos/python3-pygments
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Pygments is a generic syntax highlighter written in Python that supports
over 500 languages and text formats, for use in code hosting, forums,
wikis or other applications that need to prettify source code.

%package -n pygmentize
Summary:    Command line tool for pygments
Requires:   python3-pygments = %{version}-%{release}

%description -n pygmentize
Command line tools for pygments.

%prep
%setup -q -n %{name}-%{version}/pygments

%build
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/pygments
%{python3_sitelib}/Pygments-*.egg-info

%files -n pygmentize
%defattr(-,root,root,-)
%{_bindir}/pygmentize
