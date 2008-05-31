%define module   Data-TreeDumper
%define version  0.33
%define release  %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Improved replacement for Data::Dumper
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Data/%{module}-%{version}.tar.gz
BuildRequires: perl(Class::ISA)
BuildRequires: perl(Devel::Size)
BuildRequires: perl(Sort::Naturally)
BuildRequires: perl(Term::Size)
BuildRequires: perl(Text::Wrap)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Data::Dumper and other modules do a great job of dumping data structures. Their
output, however, often takes more brain power to understand than the data
itself. When dumping large amounts of data, the output can be overwhelming and
it can be difficult to see the relationship between each piece of the dumped
data.

Data::TreeDumper also dumps data in a tree-like fashion but hopefully in a
format more easily understood.

%prep
%setup -q -n %{module}-%{version} 

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
%perl_vendorlib/auto/Data

