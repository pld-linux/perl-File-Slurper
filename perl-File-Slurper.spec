#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	File
%define		pnam	Slurper
Summary:	File::Slurper - A simple, sane and efficient module to slurp a file
Summary(pl.UTF-8):	File::Slurper - prosty, rozsądny, wydajny moduł do wciągania pliku
Name:		perl-File-Slurper
Version:	0.009
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b4ffcb66095aebbcd6df03de7befda13
URL:		http://search.cpan.org/dist/File-Slurper/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-Warnings
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides functions for fast and correct slurping and
spewing. All functions are optionally exported.

%description -l pl.UTF-8
Ten moduł udostępnia funkcje do szybkiego i poprawnego wciągania i
wypluwania. Wszystkie funkcje są eksportowane opcjonalnie.

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
%doc Changes README
%{perl_vendorlib}/File/Slurper.pm
%{_mandir}/man3/File::Slurper.3pm*
