%define	pkgname	berkshelf
Summary:	Manages a Cookbook's, or an Application's, Cookbook dependencies
Name:		ruby-%{pkgname}
Version:	1.4.0
Release:	0.1
License:	Distributable
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	18f3049da4bb12dd90b9f51e58b7f416
URL:		http://berkshelf.com
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	ruby-activesupport >= 3.2.0
Requires:	ruby-addressable
Requires:	ruby-aruba
Requires:	ruby-cane
Requires:	ruby-celluloid >= 0.13.0
Requires:	ruby-chozo >= 0.6.1
Requires:	ruby-faraday >= 0.8.5
Requires:	ruby-hashie >= 2.0.2
Requires:	ruby-json >= 1.5.0
Requires:	ruby-json_spec
Requires:	ruby-minitar
Requires:	ruby-mixlib-config < 2
Requires:	ruby-mixlib-config => 1.1
Requires:	ruby-mixlib-shellout < 2
Requires:	ruby-mixlib-shellout => 1.1
Requires:	ruby-multi_json < 2
Requires:	ruby-multi_json => 1.5
Requires:	ruby-rake >= 0.9.2.2
Requires:	ruby-retryable
Requires:	ruby-ridley < 0.10
Requires:	ruby-ridley => 0.9.0
Requires:	ruby-rspec
Requires:	ruby-simplecov
Requires:	ruby-solve >= 0.4.2
Requires:	ruby-spork
Requires:	ruby-thor
Requires:	ruby-thor < 0.19
Requires:	ruby-thor => 0.18.0
Requires:	ruby-vcr < 2.5
Requires:	ruby-vcr => 2.4.0
Requires:	ruby-webmock
Requires:	ruby-yajl-ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manages a Cookbook's, or an Application's, Cookbook dependencies

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
%attr(755,root,root) %{_bindir}/berks
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}

# addons to thor
%{ruby_vendorlibdir}/thor/monkies.rb
%{ruby_vendorlibdir}/thor/monkies
