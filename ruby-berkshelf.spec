# TODO
# - bash completions: berkshelf-complete.sh

%define	pkgname	berkshelf
Summary:	Manages a Cookbook's, or an Application's, Cookbook dependencies
Name:		ruby-%{pkgname}
Version:	2.0.8
Release:	0.1
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	f44c874ab5d2abd769c93fa6d84c96ab
URL:		http://berkshelf.com/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
Requires:	ruby-activesupport < 3.3
Requires:	ruby-activesupport >= 3.2.0
Requires:	ruby-addressable < 2.4
Requires:	ruby-addressable >= 2.3.4
Requires:	ruby-buff-shell_out < 1
Requires:	ruby-buff-shell_out >= 0.1
Requires:	ruby-celluloid >= 0.14.0
Requires:	ruby-chozo >= 0.6.1
Requires:	ruby-faraday >= 0.8.5
Requires:	ruby-hashie >= 2.0.2
Requires:	ruby-minitar < 0.6
Requires:	ruby-minitar >= 0.5.4
Requires:	ruby-rbzip2 < 0.3
Requires:	ruby-rbzip2 >= 0.2.0
Requires:	ruby-retryable < 1.4
Requires:	ruby-retryable >= 1.3.3
Requires:	ruby-ridley < 1.3
Requires:	ruby-ridley >= 1.2.1
Requires:	ruby-rubygems >= 1.8.0
Requires:	ruby-solve >= 0.5.0
Requires:	ruby-thor < 0.19
Requires:	ruby-thor >= 0.18.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manages a Cookbook's, or an Application's, Cookbook dependencies.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md PLUGINS.md CHANGELOG.md LICENSE
%attr(755,root,root) %{_bindir}/berks
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
