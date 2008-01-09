#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Object
%define	pnam	Declare
Summary:	Object::Declare - Declarative object constructor
#Summary(pl):	
Name:		perl-Object-Declare
Version:	0.22
Release:	1
License:	MIT
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AU/AUDREYT/Object-Declare-0.22.tar.gz
# Source0-md5:	9607cd7b485bd7e01c3286f1dd8df187
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Sub::Override)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exports one function, declare, for building named
objects with a declarative syntax, similar to how Jifty::DBI::Schema
defines its columns.

In list context, declare returns a list of name/object pairs in the
order of declaration (allowing duplicates), suitable for putting into a hash.
In scalar context, declare returns a hash reference.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Object/*.pm
#%%{perl_vendorlib}/Object/Declare
%{_mandir}/man3/*
