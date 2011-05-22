%define upstream_name    Data-TreeDumper
%define upstream_version 0.40

%define _requires_exceptions perl(Data::TreeDumper::OO)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Improved replacement for Data::Dumper
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::ISA)
BuildRequires: perl(Check::ISA)
BuildRequires: perl(Devel::Size)
BuildRequires: perl(Sort::Naturally)
BuildRequires: perl(Term::Size)
BuildRequires: perl(Text::Wrap)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/Data
