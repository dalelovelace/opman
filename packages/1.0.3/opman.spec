Summary: Remote management framework
Name: opman
Version: 1.0.3
Release: 1%{?dist}
License: GPLv3
Group: Applications/System
Source0: %{name}-%{version}.tar.gz
Source1: %{name}-%{version}.tar.gz.asc
Source2: %{name}-%{version}.tar.gz.md5
Source3: %{name}-%{version}.tar.gz.sha1

URL: http://www.daleandkim.com/opman/
Requires: perl
#BuildRequires: tar
#Requires(post): 
#Requires(preun): 
#Requires(postun): 
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Iterates through a pool of hosts, ssh'es to each of those and performs an
action on each. This is, obviously, much more useful if you have setup ssh
keys to each of these hosts ahead of time to prevent having to type your
password for each!

GPG Key at http://www.daleandkim.com/opman/RPM-GPG-KEY-EAN
%prep 
%setup -q 


%build

%install
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/opman/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8/

install -m 755 usr/bin/opman $RPM_BUILD_ROOT%{_bindir}
install -m 644 etc/opman/* $RPM_BUILD_ROOT%{_sysconfdir}/opman/
pod2man usr/bin/opman | %{__gzip} > $RPM_BUILD_ROOT%{_mandir}/man8/opman.8.gz

%clean
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/opman/
%{_bindir}/opman
%{_mandir}/man8/opman.8.gz

%doc docs/*

%config %{_sysconfdir}/opman/example.conf
%config(noreplace) %{_sysconfdir}/opman/opman.conf

%changelog
* Mon Oct 22 2012 Dale Lovelace <dlovelace@expedia.com> 1.0.3
- Up to 1.0.3
* Sat Oct 13 2012 Dale Lovelace <dlovelace@expedia.com> 1.0.0
- First RPM

