%define abiquo_basedir /opt/abiquo

Name:     abiquo-api-community
Version: 1.7
Release:  3%{?dist}%{?buildstamp}
Summary:  Abiquo API Component
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  api.war
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-server-community
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package contains the community api component.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/api
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
/usr/bin/unzip -d $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/api/ %{SOURCE0}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
#%doc %{_docdir}/%{name}/README
%{abiquo_basedir}/tomcat/webapps/api

%changelog
* Mon Feb 14 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3
- updated release string

* Mon Feb 07 2011 Sergio Rubio <rubiojr@frameos.org> - 1.7-2
- rebuilt

* Wed Feb 02 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-1
- Initial Release
