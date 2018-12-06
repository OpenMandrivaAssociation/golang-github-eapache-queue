# http://github.com/eapache/queue
%global goipath         github.com/eapache/queue
Version:                1.1.0

%global common_description %{expand:
A fast Golang queue using a ring-buffer, based on the version suggested by 
Dariusz Górecki. Using this instead of other, simpler, queue implementations 
(slice+append or linked list) provides substantial memory and time benefits, 
and fewer GC pauses.

The queue implemented here is as fast as it is in part because it is not 
thread-safe.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Fast golang queue using ring-buffer
# Detected licences
# - MIT/X11 (BSD like) at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .


%install
%goinstall glide.lock glide.yaml


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Mon Oct 29 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Release 1.1.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.0.2-0.10.20150606gitded5959
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.9.gitded5959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.2-0.8.20150606gitded5959
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.2-0.7.20150606gitded5959
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.6.gitded5959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.5.gitded5959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.4.gitded5959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.3.gitded5959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.2.gitded5959
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu Apr 14 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.gitded5959
- First package for Fedora
  resolves: #1327254
