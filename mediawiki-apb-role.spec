%if 0%{?copr}
%define build_timestamp .%(date +"%Y%m%d%H%M%%S")
%else
%define build_timestamp %{nil}
%endif

Name: 		mediawiki-apb-role
Version:	1.3.0
Release:	1%{build_timestamp}%{?dist}
Summary:	Ansible Playbook for Mediawiki APB

License:	ASL 2.0
URL:		https://github.com/ansibleplaybookbundle/mediawiki-apb
Source0:	https://github.com/ansibleplaybookbundle/Mediawiki-apb/archive/%{name}-%{version}.tar.gz
BuildArch:  noarch

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}
%if !0%{?copr}
patch -p1 < downstream.patch
%endif

%install
mkdir -p %{buildroot}/opt/apb/ %{buildroot}/opt/ansible/roles/mediawiki-apb
mv playbooks %{buildroot}/opt/apb/actions
mv defaults tasks templates vars %{buildroot}/opt/ansible/roles/mediawiki-apb

%files
%doc
/opt/apb/actions
/opt/ansible/roles

%changelog
* Mon Jun 04 2018 David Zager <david.j.zager@gmail.com> 1.2.8-1
- fix deprovision when username and password match (#35) (jmontleo@redhat.com)

* Wed May 30 2018 David Zager <david.j.zager@gmail.com> 1.2.7-1
- Bug 1583543 - Use route host in openshift (#34) (dzager@redhat.com)

* Thu May 24 2018 David Zager <david.j.zager@gmail.com> 1.2.6-1
- Include vars for ansible version >= 2.6 (#33) (dzager@redhat.com)
- Force the deployment name to be mediawiki for ci (#32) (rhallise@redhat.com)

* Thu May 17 2018 David Zager <david.j.zager@gmail.com> 1.2.5-1
- Bug 1570603: Make mediawiki-apb (de)provision idempotent
  (david.j.zager@gmail.com)

* Wed May 02 2018 Jason Montleon <jmontleo@redhat.com> 1.2.4-1
- Update downstream.patch (jmontleo@redhat.com)

* Wed Apr 25 2018 Jason Montleon <jmontleo@redhat.com> 1.2.3-1
- Update to remove version specific names (jmontleo@redhat.com)

* Thu Apr 19 2018 David Zager <david.j.zager@gmail.com> 1.2.2-1
- Bug 1563641 - Specify PV Size (#28) (dzager@redhat.com)

* Mon Apr 09 2018 David Zager <david.j.zager@gmail.com> 1.2.1-1
- Bump version for 3.10 (david.j.zager@gmail.com)

* Thu Feb 15 2018 David Zager <david.j.zager@gmail.com> 1.1.7-1
- Bug 154260 - Use Recreate instead of Rolling Strategy (jmontleo@redhat.com)

* Thu Feb 08 2018 Jason Montleon <jmontleo@redhat.com> 1.1.6-1
- add downstream patch with conditional for easier builds (jmontleo@redhat.com)

* Wed Feb 07 2018 David Zager <david.j.zager@gmail.com> 1.1.5-1
- Bug 1537955 - Add parameter validation task (#23) (ernelson@redhat.com)
- Bug 1540866 - Use k8s as default cluster (david.j.zager@gmail.com)
- Added retries for webpage status verification (psturc@redhat.com)

* Fri Jan 19 2018 David Zager <david.j.zager@gmail.com> 1.1.4-1
- Revert erroneous change to image name (jmontleo@redhat.com)

* Tue Jan 16 2018 David Zager <david.j.zager@gmail.com> 1.1.3-1
- Use the proper mediawiki image name (rhallise@redhat.com)
- Few fixes after the update rebase (rhallise@redhat.com)
- Kubernetes playbooks for mediawiki (rhallise@redhat.com)

* Mon Jan 08 2018 David Zager <david.j.zager@gmail.com> 1.1.2-1
- Update tito releasers (david.j.zager@gmail.com)
- Bug 1472226 - Add pattern regex for UI validation (cchase@redhat.com)
- Use the proper git name ansibleplaybookbundle/rhscl-postgresql-apb
  (rhallise@redhat.com)

* Mon Dec 04 2017 Jason Montleon <jmontleo@redhat.com> 1.1.1-1
- updates for repo and container name change (jmontleo@redhat.com)
- Use the proper git name ansibleplaybookbundle/rhscl-postgresql-apb
  (rhallise@redhat.com)
- Add README with travis status (rhallise@redhat.com)
- bump release (jmontleo@redhat.com)
- Bug 1508994 - Hide password with display_type: password (cchase@redhat.com)
- Match the serviceinstance name to the deployment (rhallise@redhat.com)
- Add a log gathering script to the end of the job (rhallise@redhat.com)
- Update config.yaml to get 3.7 framework changes (rhallise@redhat.com)
- Fix templates to work with 3.7 (rhallise@redhat.com)
- Use the ansible-service-broker script to setup the gate (rhallise@redhat.com)
- Remove comments in config.yaml (rhallise@redhat.com)
- Add an empty go file so travis doesn't complain when setting up go
  (rhallise@redhat.com)
- Add CI to the mediawiki apb (rhallise@redhat.com)

* Mon Oct 23 2017 Jason Montleon <jmontleo@redhat.com> 1.0.7-1
- Bug 1495503 - Wait for deployment controller to scale down before deleting rc
  (dymurray@redhat.com)

* Tue Oct 10 2017 Jason Montleon <jmontleo@redhat.com> 1.0.6-1
- Bug 1500364 - Update role with correct images (david.j.zager@gmail.com)

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
