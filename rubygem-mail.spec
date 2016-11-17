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

# Explicitly require runtime subpackage, as long as older scl-utils do not generate it
Requires: %{?scl_prefix}runtime

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
%{gem_instdir}/MIT-LICENSE

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

* Mon Jan 19 2015 Josef Stribny <jstribny@redhat.com> - 2.5.4-2
- Rebuilt for ror41

* Wed Oct 16 2013 Josef Stribny <jstribny@redhat.com> - 2.5.4-1
- Update to mail 2.5.4

* Wed Jun 19 2013 Josef Stribny <jstribny@redhat.com> - 2.4.4-5
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Wed Jun 12 2013 Josef Stribny <jstribny@redhat.com> - 2.4.4-4
- Patch encoding for Ruby 1.9.3
  Resolves: rhbz#973650

* Tue Jul 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.4-3
- Exclude the cached gem.

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.4-2
- Specfile cleanup

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.4-1
- Rebuilt for scl.
- Updated to 2.4.4.

* Tue Jan 31 2012 Vít Ondruch <vondruch@redhat.com> - 2.3.0-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 04 2011  <Minnikhanov@gmail.com> - 2.3.0-1
- Updated mail to latest upstream release (v.2.3.0 2011-04-27)
- Test excluded. May be need Zentest >= 4.4.0 and rubygem(rcov).

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011  <Minnikhanov@gmail.com> - 2.2.15-2
- Fix Comment 18 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=665560#c18 
- Remove create Gemfile.lock at prep-section.

* Sat Jan 29 2011  <Minnikhanov@gmail.com> - 2.2.15-1
- Updated mail to latest upstream release (v.2.2.15 2011-01-25)

* Thu Jan 27 2011  <Minnikhanov@gmail.com> - 2.2.14-5
- Fix Comment 14 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=665560#c14 

* Mon Jan 24 2011  <Minnikhanov@gmail.com> - 2.2.14-4
- Fix Comment 12 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=665560#c12 

* Sun Jan 23 2011  <Minnikhanov@gmail.com> - 2.2.14-3
- 'BuildRequires:%{?scl:%scl_prefix}' correct wrong tag 'BuildRequires(check):'. 

* Sat Jan 22 2011  <Minnikhanov@gmail.com> - 2.2.14-2
- Fix Comment 6 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=665560#c6 

* Thu Jan 13 2011  <Minnikhanov@gmail.com> - 2.2.14-1
- Updated mail to latest upstream release

* Fri Dec 24 2010  <Minnikhanov@gmail.com> - 2.2.13-1
- Initial package
