%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from mail-2.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mail

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.6.3
Release: 4%{?dist}
Summary: Mail provides a nice Ruby DSL for making, sending and reading emails
Group: Development/Languages
License: MIT
URL: https://github.com/mikel/mail
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/mikel/mail.git && cd mail && git checkout 2.6.3
# tar czvf mail-2.6.3-specs.tgz spec/
Source1: %{gem_name}-%{version}-specs.tgz

Requires:      %{?scl_prefix_ruby}ruby(release)
Requires:      %{?scl_prefix_ruby}ruby(rubygems)
Requires:      %{?scl_prefix}rubygem(mime-types) >= 1.16
Requires:      %{?scl_prefix}rubygem(mime-types) < 3
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix}rubygem(mime-types) >= 1.16
BuildRequires: %{?scl_prefix}rubygem(mime-types) < 3
BuildRequires: %{?scl_prefix}rubygem(rspec)
BuildArch:     noarch
Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A really Ruby Mail handler.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}


%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
tar xzvf %{SOURCE1}
%{?scl:scl enable %{scl} - << \EOF}
rspec spec
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/MIT-LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/Dependencies.txt
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/TODO.rdoc
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile

%changelog
* Thu Feb 25 2016 Pavel Valena <pvalena@redhat.com> - 2.6.3-4
- Update to 2.6.3

