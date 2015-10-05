#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	File
%define		pnam	Slurper
%include	/usr/lib/rpm/macros.perl
Summary:	File::Slurper - A simple, sane and efficient module to slurp a file
Name:		perl-File-Slurper
Version:	0.008
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6e4f8ab76e38dc3f3fec6a0f575bf132
URL:		http://search.cpan.org/dist/File-Slurper/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides functions for fast and correct slurping and
spewing. All functions are optionally exported.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/File/Slurper.pm
%{_mandir}/man3/File::Slurper.3pm*
