%define upstream_name    Data-TreeDumper
%define upstream_version 0.40

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Data::TreeDumper::OO\\)'
%else
%define _requires_exceptions perl(Data::TreeDumper::OO)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Improved replacement for Data::Dumper
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::ISA)
BuildRequires:	perl(Check::ISA)
BuildRequires:	perl(Devel::Size)
BuildRequires:	perl(Sort::Naturally)
BuildRequires:	perl(Term::Size)
BuildRequires:	perl(Text::Wrap)
BuildArch:	noarch

%description
Data::Dumper and other modules do a great job of dumping data structures. Their
output, however, often takes more brain power to understand than the data
itself. When dumping large amounts of data, the output can be overwhelming and
it can be difficult to see the relationship between each piece of the dumped
data.

Data::TreeDumper also dumps data in a tree-like fashion but hopefully in a
format more easily understood.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Data

%changelog
* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.400.0-1mdv2011.0
+ Revision: 677324
- update to new version 0.40

* Fri Jan 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.370.0-1mdv2011.0
+ Revision: 494930
- update to 0.37

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.350.0-1mdv2010.0
+ Revision: 403088
- rebuild using %%perl_convert_version

* Fri Nov 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2009.1
+ Revision: 300779
- new version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.33-3mdv2009.0
+ Revision: 268411
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-2mdv2009.0
+ Revision: 213661
- fix excessive dependencies

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2009.0
+ Revision: 213632
- import perl-Data-TreeDumper


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2009.0
- first mdv release
