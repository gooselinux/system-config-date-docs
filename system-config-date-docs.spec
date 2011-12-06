# Command line configurables

%if 0%{?fedora}%{?rhel} == 0 || 0%{?fedora} >= 8 || 0%{?rhel} >= 6
%bcond_without rarian_compat
%else
%bcond_with rarian_compat
%endif

Summary: Documentation for setting the system date and time
Name: system-config-date-docs
Version: 1.0.9
Release: 1%{?dist}
URL: https://fedorahosted.org/%{name}
License: GPLv2+
Group: Documentation
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Source0: http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: gnome-doc-utils
BuildRequires: docbook-dtds
%if %{with rarian_compat}
BuildRequires: rarian-compat
%else
BuildRequires: scrollkeeper
%endif

# Until version 1.9.34, system-config-date contained online documentation.
# From version 1.9.35 on, online documentation is split off into its own
# package system-config-date-docs. The following ensures that updating from
# earlier versions gives you both the main package and documentation.
Obsoletes: system-config-date < 1.9.35
Requires: system-config-date >= 1.9.35
%if %{with rarian_compat}
Requires: rarian-compat
%else
Requires(post): scrollkeeper >= 0:0.3.4
Requires(postun): scrollkeeper >= 0:0.3.4
%endif
Requires: yelp

%description
This package contains the online documentation for system-config-date, with
which you can configure date, time and the use of timeservers on your system.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/scrollkeeper-update -q || :

%postun
%{_bindir}/scrollkeeper-update -q || :

%files
%defattr(-,root,root,-)
%doc COPYING
%doc %{_datadir}/omf/system-config-date
%doc %{_datadir}/gnome/help/system-config-date

%changelog
* Tue Mar 23 2010 Nils Philippsen <nils@redhat.com> - 1.0.9-1
- version 1.0.9

* Mon Sep 28 2009 Nils Philippsen <nils@redhat.com> - 1.0.8-1
- pick up new translations

* Wed Aug 26 2009 Nils Philippsen <nils@redhat.com>
- explain obsoleting old versions

* Wed Jun 10 2009 Nils Philippsen <nils@redhat.com>
- document keyboard navigation (#251822)

* Thu May 28 2009 Nils Philippsen <nils@redhat.com>
- use simplified source URL

* Tue Apr 14 2009 Nils Philippsen <nils@redhat.com> - 1.0.7-1
- add sr@latin structure (#495591)
- pick up updated translations

* Wed Apr 08 2009 Nils Philippsen <nils@redhat.com> - 1.0.6-1
- pull in updated translations

* Thu Dec 18 2008 Nils Philippsen <nils@redhat.com> - 1.0.5-1
- use non-colored rarian-compat requirement

* Wed Dec 17 2008 Nils Philippsen <nils@redhat.com>
- add yelp dependency

* Mon Dec 08 2008 Nils Philippsen <nils@redhat.com> - 1.0.4-1
- remove unnecessary "Conflicts: system-config-date < 1.9.35"

* Thu Nov 27 2008 Nils Philippsen <nils@redhat.com>
- replace "%%bcond_with scrollkeeper" with "%%bcond_with rarian_compat"

* Thu Nov 27 2008 Nils Philippsen <nils@redhat.com> - 1.0.3-1
- add source URL

* Wed Nov 26 2008 Nils Philippsen <nils@redhat.com>
- separate documentation from system-config-date
- remove stuff not related to documentation
