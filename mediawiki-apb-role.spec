%if 0%{?copr}
%define build_timestamp .%(date +"%Y%m%d%H%M%%S")
%else
%define build_timestamp %{nil}
%endif

Name: 		mediawiki-apb-role
Version:	1.0.5
Release:	1%{build_timestamp}%{?dist}
Summary:	Ansible Playbook for Mediawiki APB

License:	ASL 2.0
URL:		https://github.com/ansibleplaybookbundle/Mediawiki123-APB
Source0:	https://github.com/ansibleplaybookbundle/Mediawiki123-APB/archive/%{name}-%{version}.tar.gz
BuildArch:  	noarch

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}/opt/apb/ %{buildroot}/opt/ansible/
mv playbooks %{buildroot}/opt/apb/actions
mv roles %{buildroot}/opt/ansible/roles

%files
%doc
/opt/apb/actions
/opt/ansible/roles

%changelog
* Thu Oct 05 2017 Jason Montleon <jmontleo@redhat.com> 1.0.5-1
- Add update playbook (jmontleo@redhat.com)
- Bug 1498571 - Remove image from APB (david.j.zager@gmail.com)

* Wed Oct 04 2017 Jason Montleon <jmontleo@redhat.com> 1.0.4-1
- Bug 1498185 - Move version label onto APB spec (dymurray@redhat.com)
- Fix nightly dockerfile metadata (jmontleo@redhat.com)
- Update source urls for mediawiki apb rpm (david.j.zager@gmail.com)
- Bumped APB spec version to 1.0 (dymurray@redhat.com)
- Updated APB to include proper providerDisplayName metadata
  (dymurray@redhat.com)
- Updated APB to include proper dependencies (dymurray@redhat.com)

* Tue Sep 19 2017 Jason Montleon <jmontleo@redhat.com> 1.0.3-1
- new package built with tito

* Fri Aug 18 2017 Jason Montleon <jmontleo@redhat.com> 1.0.2-1
- new package built with tito

* Fri Jul 07 2017 Jason Montleon <jmontleo@redhat.com> 1.0.1-1
- 1468199 Change Mediawiki PVC to ReadWriteOnce

* Tue Jun 06 2017 Jason Montleon <jmontleo@redhat.com> 1.0.0-1
- Initial Build
