# http://github.com/coreos/go-systemd
%global goipath         github.com/coreos/go-systemd
Version:                18

%gometa 

Name:           golang-github-coreos-go-systemd
Release:        1%{?dist}
Summary:        Go bindings to systemd socket activation, journal and D-BUS APIs
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: systemd-devel

BuildRequires: golang(github.com/godbus/dbus)
BuildRequires: golang(github.com/coreos/pkg/dlopen)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall examples glide.lock glide.yaml

%check
%gochecks -d dbus -d login1 -d machine1 -d sdjournal -d journal

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Wed Nov 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 18-1
- Release 18

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 10-11
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 10-9
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 10-8
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Jan Chaloupka <jchaloup@redhat.com> - 10-4
- Bump to upstream 48702e0da86bd25e76cfef347e2adeb434a0d0a6
  related: #1248722

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 10-2
- Polish the spec file
  related: #1248722

* Wed Aug 03 2016 jchaloup <jchaloup@redhat.com> - 10-1
- Bump to upstream d6c05a1dcbb5ac02b7653da4d99e5db340c20778
  related: #1248722

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-4
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 jchaloup <jchaloup@redhat.com> - 4-1
- Bump to upstream b4a58d95188dd092ae20072bac14cece0e67c388
  related: #1248722

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 3-3
- Update to spec-2.1
  related: #1248722

* Fri Sep 11 2015 jchaloup <jchaloup@redhat.com> - 3-2
- Bump to upstream cea488b4e6855fee89b6c22a811e3c5baca861b6
  related: #1248722

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 3-1
- Bump to upstream be94bc700879ae8217780e9d141789a2defa302b
  related: #1248722

* Thu Jul 30 2015 jchaloup <jchaloup@redhat.com> - 2-8
- Update spec file to spec-2.0
  resolves: #1248722

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 jchaloup <jchaloup@redhat.com> - 2-6
- Bump to upstream 7a81740665de3d730bf98811f6b2ae5746e42a32
  The last commit containing unchanged StartTransientUnit method (libcontainer)
  and still providing daemon package (fleet).
  related: #1165690

* Tue Mar 31 2015 jchaloup <jchaloup@redhat.com> - 2-5
- Bump to upstream fe2137a286b607d0023a8356cdc22a38098246b8
  related: #1165690

* Mon Mar 30 2015 jchaloup <jchaloup@redhat.com> - 2-4
- Bump to upstream 2d21675230a81a503f4363f4aa3490af06d52bb8
  related: #1165690

* Mon Jan 19 2015 jchaloup <jchaloup@redhat.com> - 2-3
- Adding missing Provides and removing superfluous Provides
  related: #1165690

* Wed Nov 19 2014 jchaloup <jchaloup@redhat.com> - 2-2
- Update to a606a1e936df81b70d85448221c7b1c6d8a74ef1 commit
  resolves: #1165688
- remove gopath and add golang >= 1.2.1-3
- add Requires on github.com/godbus/dbus

* Mon Jun 09 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2-1
- upstream version bump to v2
- change in NVR format since numbered versions are available

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git8514b9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Bobby Powers <bobbypowers@gmail.com> 0-0.4.git8514b9f
- update to latest upstream

* Fri Oct 18 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.3.git68bc612
- double quotes removed from provides

* Mon Oct 14 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.2.git68bc612
- provides golang("github.com/coreos/go-systemd")
- defattr removed

* Sat Oct 12 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.git68bc612
- Initial fedora package

