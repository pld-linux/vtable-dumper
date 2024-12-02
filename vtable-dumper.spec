Summary:	Tool to list content of virtual tables in a C++ shared library
Name:		vtable-dumper
Version:	1.2
Release:	1
License:	LGPL v2.1+
Group:		Development/Tools
Source0:	https://github.com/lvc/vtable-dumper/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1b1e2bc09b0fe63abf01e1ad2526c40d
URL:		https://github.com/lvc/vtable-dumper
BuildRequires:	elfutils-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vtable-Dumper - a tool to list content of virtual tables in a C++
shared library.

The tool is intended for developers of software libraries and
maintainers of Linux distributions who are interested in ensuring
backward binary compatibility.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D vtable-dumper $RPM_BUILD_ROOT%{_bindir}/vtable-dumper

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/vtable-dumper
